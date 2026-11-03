from __future__ import annotations

import csv
import html
import re
from html.parser import HTMLParser
from pathlib import Path


DEFAULT_GLOSSARY = (
    ("Ar tonelico", "Ar tonelico"),
    ("Lyner", "Lyner"),
    ("Aurica", "Aurica"),
    ("Misha", "Misha"),
    ("Shurelia", "Shurelia"),
    ("Reyvateil", "Reyvateil"),
    ("Grathnode", "Grathnode"),
    ("Tenba", "Tenba"),
)

GAME_COMMAND_PATTERN = re.compile(
    r"#[01][A-Za-z0-9_./-]*|0x[0-9A-Fa-f]+|\\[A-Za-z][A-Za-z0-9]*|%[A-Za-z0-9]+"
)

VISUAL_LINE_CONTINUATION_PATTERN = re.compile(
    r"[ \t]*\\[ \t]*(?:\r\n?|\n|\u2028|\u2029)[ \t]*"
)
LINE_BREAK_PATTERN = re.compile(r"[ \t]*(?:\r\n?|\n|\u2028|\u2029)[ \t]*")
HORIZONTAL_WHITESPACE_PATTERN = re.compile(r"[ \t\f\v]+")


def normalize_translation_source(text: str) -> str:
    """Join visual game lines before sending a complete sentence to an API.

    Some extracted scripts mark a visual continuation with a literal backslash
    immediately before the physical line break.  Both that form and ordinary
    physical line breaks are layout, not paragraph boundaries.  Literal game
    commands such as ``\\n`` contain no physical newline and remain untouched.
    """
    text = VISUAL_LINE_CONTINUATION_PATTERN.sub(" ", text)
    text = LINE_BREAK_PATTERN.sub(" ", text)
    return HORIZONTAL_WHITESPACE_PATTERN.sub(" ", text).strip()


def ensure_default_glossary(project_path: Path) -> Path:
    path = project_path.with_suffix(".glossario.csv")
    if not path.exists():
        with path.open("w", encoding="utf-8-sig", newline="") as stream:
            writer = csv.writer(stream)
            writer.writerow(("original", "traducao"))
            writer.writerows(DEFAULT_GLOSSARY)
    return path


def read_glossary(path: Path | None) -> list[tuple[str, str]]:
    if path is None:
        return []
    if not path.is_file():
        raise ValueError(f"Glossário não encontrado: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != ["original", "traducao"]:
            raise ValueError("O glossário deve ter exatamente as colunas original,traducao")
        entries: list[tuple[str, str]] = []
        seen: set[str] = set()
        for line, row in enumerate(reader, 2):
            source = row["original"].strip()
            target = row["traducao"].strip()
            if not source and not target:
                continue
            if not source or not target:
                raise ValueError(f"Glossário incompleto na linha {line}")
            folded = source.casefold()
            if folded in seen:
                raise ValueError(f"Termo duplicado no glossário: {source}")
            seen.add(folded)
            entries.append((source, target))
    return entries


def protect_plain_commands(text: str) -> tuple[str, list[tuple[str, str]]]:
    protected: list[tuple[str, str]] = []

    def replace(match: re.Match[str]) -> str:
        token = f"ZXQCMD{len(protected):04d}QXZ"
        protected.append((token, match.group(0)))
        return token

    return GAME_COMMAND_PATTERN.sub(replace, text), protected


def restore_plain_commands(text: str, protected: list[tuple[str, str]]) -> str:
    for token, command in protected:
        if text.count(token) != 1:
            raise ValueError(f"A API alterou o marcador protegido {token}")
        text = text.replace(token, command)
    return text


def protect_azure_text(text: str, glossary: list[tuple[str, str]]) -> tuple[str, list[str]]:
    candidates: list[tuple[int, int, int, str, str]] = []
    masked = list(text)
    for match in GAME_COMMAND_PATTERN.finditer(text):
        candidates.append((match.start(), match.end(), 0, "command", match.group(0)))
        masked[match.start():match.end()] = " " * (match.end() - match.start())
    searchable = "".join(masked)
    for source, target in sorted(glossary, key=lambda item: len(item[0]), reverse=True):
        pattern = re.escape(source)
        if source[0].isalnum():
            pattern = rf"(?<![A-Za-z]){pattern}"
        if source[-1].isalnum():
            pattern = rf"{pattern}(?![A-Za-z])"
        for match in re.finditer(pattern, searchable, flags=re.IGNORECASE):
            candidates.append((match.start(), match.end(), 1, "glossary", target))

    selected: list[tuple[int, int, str, str]] = []
    occupied_until = -1
    for start, end, priority, kind, value in sorted(
        candidates, key=lambda item: (item[0], item[2], -(item[1] - item[0]))
    ):
        if start < occupied_until:
            continue
        selected.append((start, end, kind, value))
        occupied_until = end

    output = ["<div>"]
    protected: list[str] = []
    position = 0
    for start, end, kind, value in selected:
        output.append(html.escape(text[position:start]))
        source = text[start:end]
        if kind == "command":
            number = len(protected)
            protected.append(source)
            output.append(
                f'<span class="notranslate" data-at-tag="{number}">{html.escape(source)}</span>'
            )
        else:
            output.append(
                f'<mstrans:dictionary translation="{html.escape(value, quote=True)}">'
                f'{html.escape(source)}</mstrans:dictionary>'
            )
        position = end
    output.append(html.escape(text[position:]))
    output.append("</div>")
    return "".join(output), protected


class _AzureTextExtractor(HTMLParser):
    def __init__(self, protected: list[str]):
        super().__init__(convert_charrefs=True)
        self.protected = protected
        self.output: list[str] = []
        self.seen: list[int] = []
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag.casefold() == "span" and "notranslate" in (attributes.get("class") or "").split():
            try:
                number = int(attributes.get("data-at-tag", ""))
                value = self.protected[number]
            except (ValueError, IndexError) as exc:
                raise ValueError("A API Azure alterou um comando protegido") from exc
            self.output.append(value)
            self.seen.append(number)
            self.skip_depth = 1
        elif self.skip_depth:
            self.skip_depth += 1
        elif tag.casefold() == "br":
            self.output.append("\n")

    def handle_endtag(self, _tag: str) -> None:
        if self.skip_depth:
            self.skip_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self.skip_depth:
            self.output.append(data)


def restore_azure_text(text: str, protected: list[str]) -> str:
    parser = _AzureTextExtractor(protected)
    parser.feed(text)
    parser.close()
    if sorted(parser.seen) != list(range(len(protected))):
        raise ValueError("A API Azure removeu ou duplicou um comando protegido")
    return "".join(parser.output)
