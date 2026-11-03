from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass


EXECUTABLE_TEXT_PREFIX = "SLUS/TEXT/"


def executable_slot_capacity(executable: bytes, offset: int, encoded_length: int) -> int:
    """Include only the zero padding immediately following an executable string.

    The bank aligns neighboring strings and leaves up to a few zero bytes after
    their terminators.  Using that padding does not move the next string or any
    pointer.  Stop at the first nonzero byte and reject implausibly large gaps,
    which may be reserved data rather than alignment.
    """
    end = offset + encoded_length
    limit = min(len(executable), end + 15)
    while end < limit and executable[end] == 0:
        end += 1
    return end - offset


@dataclass(frozen=True)
class ExecutableText:
    offset: int
    encoded_length: int
    text: str
    group: int
    locked: bool

    @property
    def event_file(self) -> str:
        return f"{EXECUTABLE_TEXT_PREFIX}{self.group:04d}"


def _is_technical_identifier(text: str) -> bool:
    if text.startswith("#"):
        return True
    if len(text) > 40 and text.startswith("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        return True
    return bool(
        len(text) >= 6
        and not any(character.isspace() for character in text)
        and re.fullmatch(r"[A-Z][A-Z0-9_./:+-]*", text)
    )


def extract_executable_texts(executable: bytes) -> tuple[ExecutableText, ...]:
    """Find null-terminated full-width English strings embedded in the ELF.

    The English executable contains a second text bank outside the RPK/EVD
    archive.  Its printable characters are mainly CP932 full-width ASCII.
    Strings are kept in-place, so ``encoded_length`` includes the terminator
    and is also the maximum safe replacement size.
    """
    found: list[tuple[int, int, str, bool]] = []
    for match in re.finditer(rb"[^\x00]{4,}\x00", executable):
        raw = match.group()[:-1]
        try:
            decoded = raw.decode("cp932")
        except UnicodeDecodeError:
            continue
        if len(decoded) < 2:
            continue
        full_width = sum(
            character == "\u3000" or 0xFF01 <= ord(character) <= 0xFF5E
            for character in decoded
        )
        if full_width / len(decoded) < 0.65:
            continue
        text = unicodedata.normalize("NFKC", decoded)
        if not all(character.isprintable() for character in text):
            continue
        if not any(character.isalpha() for character in text):
            continue
        found.append(
            (match.start(), len(raw) + 1, text, _is_technical_identifier(text))
        )

    output: list[ExecutableText] = []
    group = 0
    previous_end: int | None = None
    group_items = 0
    for offset, encoded_length, text, locked in found:
        if previous_end is not None and (
            offset - previous_end > 0x80 or group_items >= 24
        ):
            group += 1
            group_items = 0
        output.append(
            ExecutableText(
                offset,
                executable_slot_capacity(executable, offset, encoded_length),
                text,
                group,
                locked,
            )
        )
        previous_end = offset + encoded_length
        group_items += 1
    return tuple(output)
