from __future__ import annotations

import json
import random
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path

from .quality import (
    normalize_translation_source,
    protect_azure_text,
    protect_plain_commands,
    read_glossary,
    restore_azure_text,
    restore_plain_commands,
)


@dataclass(frozen=True)
class TranslationConfig:
    provider: str
    api_key: str
    region: str = "global"
    endpoint: str = ""
    azure_chars_per_minute: int = 30_000
    batch_characters: int = 8_000
    batch_items: int = 50
    glossary_path: str = ""
    azure_category: str = ""
    deepl_context_characters: int = 8_000


GAME_CONTEXT = (
    "Ar tonelico: Melody of Elemia is a fantasy science-fiction role-playing game. "
    "Its story follows Lyner Barsett and the Reyvateils Aurica, Misha, and Shurelia "
    "in the tower world of Sol Ciel. The following material is surrounding dialogue "
    "from the same in-game event scene."
)


def _request(url: str, body: dict | list, headers: dict[str, str], retries: int = 7):
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    for attempt in range(retries):
        request = urllib.request.Request(url, data=data, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt + 1 == retries:
                detail = exc.read().decode("utf-8", errors="replace")
                raise RuntimeError(f"HTTP {exc.code}: {detail[:500]}") from exc
            retry_after = exc.headers.get("Retry-After")
            delay = float(retry_after) if retry_after and retry_after.isdigit() else min(60, 2 ** attempt + random.random())
            time.sleep(delay)
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt + 1 == retries:
                raise RuntimeError(str(exc)) from exc
            time.sleep(min(60, 2 ** attempt + random.random()))


def translate_batch(
    config: TranslationConfig,
    texts: list[str],
    azure_html: bool = False,
    context: str = "",
) -> list[str]:
    if config.provider.casefold() == "azure":
        endpoint = (config.endpoint or "https://api.cognitive.microsofttranslator.com").rstrip("/")
        if not endpoint.casefold().endswith("/translate"):
            endpoint += "/translate"
        query = {"api-version": "3.0", "from": "en", "to": "pt-br"}
        if azure_html:
            query["textType"] = "html"
        if config.azure_category:
            query["category"] = config.azure_category
            query["allowFallback"] = "true"
        url = endpoint + "?" + urllib.parse.urlencode(query)
        headers = {"Content-Type": "application/json", "Ocp-Apim-Subscription-Key": config.api_key}
        if config.region and config.region != "global":
            headers["Ocp-Apim-Subscription-Region"] = config.region
        result = _request(url, [{"Text": text} for text in texts], headers)
        return [item["translations"][0]["text"] for item in result]
    free = config.api_key.endswith(":fx")
    endpoint = config.endpoint or ("https://api-free.deepl.com" if free else "https://api.deepl.com")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"DeepL-Auth-Key {config.api_key}",
    }
    payload = {
        "text": texts,
        "source_lang": "EN",
        "target_lang": "PT-BR",
        "preserve_formatting": True,
        "split_sentences": "nonewlines",
        "show_billed_characters": True,
    }
    if context:
        payload["context"] = context
    if len(json.dumps(payload, ensure_ascii=False).encode("utf-8")) >= 128 * 1024:
        raise ValueError("O lote DeepL excede o limite de 128 KiB incluindo o contexto")
    result = _request(endpoint.rstrip("/") + "/v2/translate", payload, headers)
    return [item["text"] for item in result["translations"]]


def pending_batches(db, config: TranslationConfig):
    rows = db.execute(
        "SELECT id,event_file,entry_index,speaker_id,original FROM dialogues "
        "WHERE automatic='' AND translation='' AND locked=0 "
        "AND translation_track='dialogue' ORDER BY event_file,entry_index"
    ).fetchall()
    batch = []
    chars = 0
    event_file = None
    for row in rows:
        source_length = len(normalize_translation_source(row["original"]))
        changes_event = (
            config.provider.casefold() == "deepl"
            and event_file is not None
            and row["event_file"] != event_file
        )
        if batch and (changes_event or len(batch) >= config.batch_items or chars + source_length > config.batch_characters):
            yield batch
            batch, chars = [], 0
        event_file = row["event_file"]
        batch.append(row)
        chars += source_length
    if batch:
        yield batch


def build_deepl_context(db, batch, max_characters: int = 8_000) -> str:
    if not batch or max_characters <= 0:
        return ""
    event_files = {row["event_file"] for row in batch}
    if len(event_files) != 1:
        raise ValueError("O contexto DeepL não pode misturar eventos diferentes")
    event_file = next(iter(event_files))
    scene = db.execute(
        "SELECT entry_index,speaker_id,original FROM dialogues "
        "WHERE event_file=? ORDER BY entry_index",
        (event_file,),
    ).fetchall()
    lines = [GAME_CONTEXT, f"Scene resource: {event_file}", "Surrounding scene dialogue:"]
    for row in scene:
        text = normalize_translation_source(row["original"])
        if text and not text.lstrip().startswith("#"):
            lines.append(f"[{row['entry_index']}] Speaker {row['speaker_id']}: {text}")
    context = "\n".join(lines)
    if len(context) <= max_characters:
        return context
    # Preserve the game description and both ends of an oversized scene.
    prefix = "\n".join(lines[:3]) + "\n"
    remaining = max(0, max_characters - len(prefix) - len("\n[… scene omitted …]\n"))
    first = remaining // 2
    last = remaining - first
    body = "\n".join(lines[3:])
    tail = body[-last:] if last else ""
    return prefix + body[:first] + "\n[… scene omitted …]\n" + tail


def run_queue(db, config: TranslationConfig, progress=None, should_stop=None) -> int:
    completed = 0
    glossary = read_glossary(Path(config.glossary_path)) if config.glossary_path else []
    for batch in pending_batches(db, config):
        if should_stop and should_stop():
            break
        started = time.monotonic()
        # Keep the database original unchanged, but remove visual wrapping from
        # the API input so the service translates each dialogue as one context.
        originals = [normalize_translation_source(row["original"]) for row in batch]
        if config.provider.casefold() == "azure":
            prepared_and_tokens = [protect_azure_text(text, glossary) for text in originals]
            translated = translate_batch(
                config, [item[0] for item in prepared_and_tokens], azure_html=True
            )
            translated = [
                restore_azure_text(text, item[1])
                for text, item in zip(translated, prepared_and_tokens, strict=True)
            ]
        else:
            prepared_and_tokens = [protect_plain_commands(text) for text in originals]
            context = build_deepl_context(db, batch, config.deepl_context_characters)
            translated = translate_batch(
                config, [item[0] for item in prepared_and_tokens], context=context
            )
            translated = [
                restore_plain_commands(text, item[1])
                for text, item in zip(translated, prepared_and_tokens, strict=True)
            ]
        for row, text in zip(batch, translated, strict=True):
            from .project import encoded_size
            size = encoded_size(text)
            original_size = db.execute("SELECT original_bytes FROM dialogues WHERE id=?", (row["id"],)).fetchone()[0]
            error = "" if size is not None else "Caractere não suportado pela codificação do jogo"
            db.execute(
                "UPDATE dialogues SET automatic=?,translation=?,translated_bytes=?,size_ok=?,provider=?,error=? "
                "WHERE id=?",
                (text, text, size or 0, int(size is not None and size <= original_size),
                 config.provider, error, row["id"]),
            )
        db.commit()  # Persistent resume point after every successful request.
        completed += len(batch)
        if progress:
            progress(completed, len(batch))
        if config.provider.casefold() == "azure":
            required = sum(len(text) for text in originals) * 60 / max(1, config.azure_chars_per_minute)
            time.sleep(max(0, required - (time.monotonic() - started)))
        else:
            time.sleep(max(0, 0.25 - (time.monotonic() - started)))
    return completed
