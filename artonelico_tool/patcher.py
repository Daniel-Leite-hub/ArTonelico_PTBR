from __future__ import annotations

import hashlib
import json
import shutil
import sqlite3
import struct
import tempfile
import unicodedata
from pathlib import Path

from .evd import build, encode_game_text, parse, validate_runtime_layout
from .executable_text import EXECUTABLE_TEXT_PREFIX, executable_slot_capacity
from .iso import SECTOR, find, read_entry
from .lzr import compress, decompress
from .native_menu_font import (
    NativeMenuText,
    NativePrintfText,
    native_menu_text,
    reset_menu_text,
)
from .portuguese_font import has_portuguese_glyphs, patch_tm2
from .native_bitmap_font import patch_native_menu_font
from .project import get_meta, select_final_text
from .rpk import read_index
from .relocation import plan_rpk, move_iso_file_record
from .string_relocation import plan_string_moves, apply_string_moves
from .text_arena import arena_layout, install_arena


# All EVDs, including the prologue, use the sequential loader at 0x196EC8.
# Its NEXT-word padding rule is implemented in evd.py. Keeping original text
# lengths only masked that format bug; it is not a runtime requirement.

# These executable banks are rendered as selectable menu rows.  The #1 font
# escape works in dialogue boxes, but the inventory/menu code later reuses the
# same bytes as data and crashes when it encounters that escape.  Keep the
# accented editorial text in SQLite and transliterate only the binary payload
# for these renderers until a native two-byte menu-font mapping is available.
MENU_RENDERER_GROUPS = frozenset({"SLUS/TEXT/0339", "SLUS/TEXT/0341"})

# These exact original executable formats contain raw ASCII substitutions.
# Verified against work/SLUS_214.45; ordinary narrative percent signs must
# retain the normal full-width game encoding.
ASCII_RUNTIME_FORMATS = frozenset({
    'Use [%s]', 'Obtained %d Cole.', 'Obtained %s [%s].',
    'Obtained [%s].', 'Obtained item: [%s]',
})


def effective_event_capacity(event_file: str, original_size: int, slot_capacity: int) -> int:
    return slot_capacity


def remove_accents(text: str) -> str:
    text = text.replace("ç", "c").replace("Ç", "C")
    return "".join(char for char in unicodedata.normalize("NFKD", text) if not unicodedata.combining(char))


def encode_fixed_slot(value: str, capacity: int) -> bytes:
    encoded = encode_game_text(value)
    if len(encoded) > capacity:
        raise ValueError(f"o texto usa {len(encoded)} bytes; limite fixo de {capacity} bytes")
    return encoded + b"\0" * (capacity - len(encoded))


def selected_replacements(
    db: sqlite3.Connection, event_file: str, accent_mode: str
) -> tuple[dict[int, str], dict[str, int], dict[int, str]]:
    rows = db.execute(
        "SELECT * FROM dialogues WHERE event_file=? ORDER BY entry_index",
        (event_file,),
    ).fetchall()
    replacements = {}
    counts = {"reviewed": 0, "automatic": 0, "original": 0}
    sources = {}
    for row in rows:
        value, source = select_final_text(row)
        counts[source] += 1
        sources[row["entry_index"]] = source
        if source == "original":
            continue
        if accent_mode == "transliterate":
            value = remove_accents(value)
        elif accent_mode == "native-menu-font" and (
            row["translation_track"] == "localization"
            or event_file in MENU_RENDERER_GROUPS
        ):
            value = native_menu_text(value)
        elif accent_mode == "menu-font-reset" and (
            row["translation_track"] == "localization"
            or event_file in MENU_RENDERER_GROUPS
        ):
            value = reset_menu_text(value)
        elif accent_mode == "portuguese-font" and (
            row["translation_track"] == "localization"
            or event_file in MENU_RENDERER_GROUPS
        ):
            value = remove_accents(value)
        if accent_mode == 'native-menu-font' and event_file.startswith(EXECUTABLE_TEXT_PREFIX) and row['original'] in ASCII_RUNTIME_FORMATS:
            if row['original'] == 'Use [%s]':
                value = value.replace('Usar [', 'Use [', 1)
            value = NativePrintfText(value)
        replacements[row["entry_index"]] = value
    return replacements, counts, sources


def fit_event_to_capacity(evd, replacements: dict[int, str], sources: dict[int, str], capacity: int):
    fitted = dict(replacements)
    rebuilt = build(evd, fitted)
    if len(rebuilt) <= capacity:
        return rebuilt, fitted, []
    candidates = []
    for entry_index, value in fitted.items():
        if sources.get(entry_index) != "automatic":
            continue
        saving = len(encode_game_text(value)) - len(evd.dialogues[entry_index].raw)
        if saving > 0:
            candidates.append((saving, entry_index))
    fallbacks = []
    for _saving, entry_index in sorted(candidates, reverse=True):
        fitted.pop(entry_index)
        fallbacks.append(entry_index)
        rebuilt = build(evd, fitted)
        if len(rebuilt) <= capacity:
            return rebuilt, fitted, sorted(fallbacks)
    raise ValueError(
        f"{len(rebuilt)} bytes excedem a área disponível de {capacity} bytes mesmo após "
        "retornar traduções automáticas expansivas ao texto original. Reduza uma revisão aprovada."
    )


def fit_event_to_record_layout(
    evd, replacements: dict[int, str], sources: dict[int, str], exact_size: int
):
    """Replace text without moving or resizing any EVD record.

    Legacy diagnostic helper, not used by the production ISO builder.
    Keep each original length field and payload slot intact, zero-filling
    the unused tail after a shorter translated C string.
    """
    fitted = dict(replacements)
    fallbacks: list[int] = []
    encoded_values: dict[int, bytes] = {}
    for entry_index, value in replacements.items():
        encoded = encode_game_text(value)
        available = len(evd.dialogues[entry_index].raw)
        if len(encoded) <= available:
            encoded_values[entry_index] = encoded
            continue
        if sources.get(entry_index) == "automatic":
            fitted.pop(entry_index)
            fallbacks.append(entry_index)
            continue
        raise ValueError(
            f"a revisão da fala {entry_index} usa {len(encoded)} bytes, mas seu registro "
            f"fixo possui {available} bytes. Encurte o texto revisado."
        )

    output = bytearray(struct.pack("<I", len(evd.dialogues)))
    for row in evd.dialogues:
        output.extend(
            struct.pack(
                "<IIIIII",
                row.position,
                row.name_id,
                row.portrait_id,
                row.text_id,
                row.portrait_type,
                row.encoded_length,
            )
        )
        if row.index in fitted:
            encoded = encoded_values[row.index]
            output.extend(encoded)
            output.extend(b"\0" * (len(row.raw) - len(encoded)))
        else:
            output.extend(row.raw)
        output.extend(row.padding)
        output.extend(row.extra)
    output.extend(evd.trailer)
    rebuilt = bytes(output)
    if len(rebuilt) != exact_size:
        raise ValueError(
            f"falha ao preservar todos os registros internos: {len(rebuilt)} != {exact_size} bytes"
        )
    return rebuilt, fitted, sorted(fallbacks)


def build_iso(project_path: Path, output_iso: Path, accent_mode: str = "block", progress=None, relocate: bool = False, relocate_strings: bool = False, string_priority: tuple[int, ...] = (), expand_text_arena: bool = False) -> dict:
    from .movie_pack import load_movie_pack, apply_movie_pack
    db = sqlite3.connect(project_path)
    db.row_factory = sqlite3.Row
    source_iso = Path(get_meta(db, "iso_path"))
    if not source_iso.exists():
        raise FileNotFoundError(f"ISO original não encontrada: {source_iso}")
    movies = load_movie_pack(source_iso, project_path.parent / 'videos_ptbr')
    expected_iso_size = get_meta(db, "iso_size")
    if expected_iso_size is not None and source_iso.stat().st_size != expected_iso_size:
        raise ValueError("A ISO-base não corresponde ao tamanho registrado no projeto")
    total_count = db.execute("SELECT COUNT(*) FROM dialogues").fetchone()[0]
    executable_entry = find(source_iso, "SLUS_214.45")
    rpk_entry = find(source_iso, "RPK.BIN")
    executable = bytearray(read_entry(source_iso, executable_entry))
    original_executable = bytes(executable)
    arena_info = {}
    if expand_text_arena:
        relocate_strings = True
        arena_file_offset, _ = arena_layout(original_executable)
    string_moves = []
    string_blocked = {}
    string_manifest = []
    expected_executable_hash = get_meta(db, "executable_sha256")
    actual_executable_hash = hashlib.sha256(executable).hexdigest()
    if expected_executable_hash and actual_executable_hash != expected_executable_hash:
        raise ValueError("A ISO-base não corresponde ao executável registrado no projeto")
    with tempfile.NamedTemporaryFile(suffix=".elf", delete=False) as temp:
        temp.write(executable)
        temp_path = Path(temp.name)
    try:
        entries = read_index(temp_path, rpk_entry.size)
    finally:
        temp_path.unlink(missing_ok=True)
    event_entries = [entry for entry in entries if entry.name.casefold().endswith(".evd")]
    modifications: list[tuple[int, bytes, int]] = []
    verification: list[tuple[str, int, int, dict[int, str]]] = []
    event_references = {}
    selection_counts = {"reviewed": 0, "automatic": 0, "original": 0}
    capacity_fallbacks: list[dict[str, int | str]] = []
    executable_verification: list[tuple[int, int, str]] = []
    modified_events = 0
    needs_portuguese_font = False
    needs_native_menu_hook = False
    with source_iso.open("rb") as source:
        for number, entry in enumerate(event_entries, 1):
            replacements, event_counts, sources = selected_replacements(db, entry.name, accent_mode)
            for key in selection_counts:
                selection_counts[key] += event_counts[key]
            if not replacements:
                continue
            source.seek(rpk_entry.extent * SECTOR + entry.offset)
            evd = parse(source.read(entry.size))
            try:
                entry_index = entries.index(entry)
                next_sector = entries[entry_index + 1].sector if entry_index + 1 < len(entries) else rpk_entry.size // SECTOR
                slot_capacity = (next_sector - entry.sector) * SECTOR
                capacity = effective_event_capacity(entry.name, entry.size, slot_capacity)
                if relocate:
                    rebuilt = build(evd, replacements)
                    capacity = max(capacity, ((len(rebuilt)+SECTOR-1)//SECTOR)*SECTOR)
                    event_fallbacks = []
                else:
                    rebuilt, replacements, event_fallbacks = fit_event_to_capacity(
                        evd, replacements, sources, capacity
                    )
                validate_runtime_layout(rebuilt, evd)
                event_references[entry.name] = evd
            except UnicodeEncodeError as exc:
                raise ValueError(
                    f"{entry.name}: contém um caractere que não existe na fonte Shift-JIS nem "
                    "na biblioteca portuguesa. Revise aspas tipográficas, travessões ou outros símbolos."
                ) from exc
            except ValueError as exc:
                raise ValueError(f"{entry.name}: {exc}") from exc
            for dialogue_index in event_fallbacks:
                selection_counts["automatic"] -= 1
                selection_counts["original"] += 1
                row = db.execute(
                    "SELECT original,automatic,original_bytes FROM dialogues "
                    "WHERE event_file=? AND entry_index=?",
                    (entry.name, dialogue_index),
                ).fetchone()
                capacity_fallbacks.append({
                    "event_file": entry.name,
                    "entry_index": dialogue_index,
                    "original": row["original"],
                    "automatic": row["automatic"],
                    "original_bytes": row["original_bytes"],
                    "automatic_bytes": len(encode_game_text(row["automatic"])),
                    "reason": "sector_capacity",
                })
            needs_portuguese_font = needs_portuguese_font or any(
                has_portuguese_glyphs(value) for value in replacements.values()
            )
            needs_native_menu_hook = needs_native_menu_hook or any(
                isinstance(value, NativeMenuText) and has_portuguese_glyphs(value)
                for value in replacements.values()
            )
            struct.pack_into("<I", executable, entry.table_offset + 8, len(rebuilt))
            modifications.append((entry.offset, rebuilt, capacity))
            verification.append((entry.name, entry.offset, len(rebuilt), replacements))
            modified_events += 1
            if progress:
                progress(number, len(event_entries), entry.name)
        executable_groups = [
            row[0]
            for row in db.execute(
                "SELECT DISTINCT event_file FROM dialogues WHERE event_file LIKE ? "
                "ORDER BY event_file",
                (EXECUTABLE_TEXT_PREFIX + "%",),
            )
        ]
        if relocate_strings:
            outgoing = {}
            for group in executable_groups:
                chosen, _, _ = selected_replacements(db, group, accent_mode)
                outgoing.update({offset: encode_game_text(value) for offset, value in chosen.items()})
            string_moves, string_blocked = plan_string_moves(original_executable, outgoing, priority=string_priority,
                arena_offset=arena_file_offset if expand_text_arena else None)
        moved = {m.source: m for m in string_moves}
        for event_file in executable_groups:
            replacements, event_counts, sources = selected_replacements(
                db, event_file, accent_mode
            )
            for key in selection_counts:
                selection_counts[key] += event_counts[key]
            for offset, value in list(replacements.items()):
                row = db.execute(
                    "SELECT original,automatic,original_bytes FROM dialogues "
                    "WHERE event_file=? AND entry_index=?",
                    (event_file, offset),
                ).fetchone()
                encoded = encode_game_text(value)
                capacity = executable_slot_capacity(
                    executable, offset, row["original_bytes"]
                )
                if offset in moved:
                    executable_verification.append((moved[offset].destination, len(encoded), value))
                    continue
                if len(encoded) > capacity:
                    if sources.get(offset) != "automatic":
                        raise ValueError(
                            f"{event_file}:{offset:#x}: a revisão usa {len(encoded)} bytes, "
                            f"mas o espaço fixo possui {capacity}. Encurte o texto revisado."
                        )
                    replacements.pop(offset)
                    selection_counts["automatic"] -= 1
                    selection_counts["original"] += 1
                    capacity_fallbacks.append({
                        "event_file": event_file,
                        "entry_index": offset,
                        "original": row["original"],
                        "automatic": row["automatic"],
                        "original_bytes": capacity,
                        "automatic_bytes": len(encoded),
                        "reason": "executable_slot",
                        "relocation_block": string_blocked.get(offset, "not_requested"),
                    })
                    continue
                if offset < 0 or offset + capacity > len(executable):
                    raise ValueError(
                        f"{event_file}:{offset:#x}: posição fora do SLUS_214.45"
                    )
                executable[offset : offset + capacity] = encode_fixed_slot(
                    value, capacity
                )
                executable_verification.append((offset, capacity, value))
            needs_portuguese_font = needs_portuguese_font or any(
                has_portuguese_glyphs(value) for value in replacements.values()
            )
            needs_native_menu_hook = needs_native_menu_hook or any(
                isinstance(value, NativeMenuText) and has_portuguese_glyphs(value)
                for value in replacements.values()
            )
        if string_moves:
            if expand_text_arena:
                arena_info = install_arena(executable, original_executable, string_moves)
            string_manifest = apply_string_moves(executable,
                bytes(executable) if expand_text_arena else original_executable, string_moves)
            executable_verification = [
                (offset, len(encode_game_text(value)) if any(
                    offset <= m.destination < offset+capacity for m in string_moves
                ) else capacity, value)
                for offset, capacity, value in executable_verification
            ]
        if needs_native_menu_hook:
            catalog = [value.encode('cp932', errors='replace') for row in db.execute(
                "SELECT original, automatic, translation, reviewed FROM dialogues"
            ) for value in row if value]
            for row in db.execute("SELECT original, automatic, translation, reviewed FROM dialogues"):
                for value in row:
                    if value:
                        try:
                            catalog.append(encode_game_text(value))
                        except UnicodeEncodeError:
                            pass  # Raw CP932 collision scan above remains available.
            patch_native_menu_font(executable, catalog)
        if needs_portuguese_font:
            font_entry = next((entry for entry in entries if entry.name == "fpack/font.fp"), None)
            if font_entry is None:
                raise ValueError("O pacote fpack/font.fp não foi encontrado nesta ISO")
            source.seek(rpk_entry.extent * SECTOR + font_entry.offset)
            font_pack = bytearray(source.read(font_entry.size))
            child_offset = 12 * SECTOR
            child_capacity = 3 * SECTOR
            original_size = struct.unpack_from("<I", executable, 0x3010A8)[0]
            raw_font = decompress(font_pack[child_offset : child_offset + original_size])
            patched_font, _ = patch_tm2(raw_font)
            packed_font = compress(patched_font)
            if len(packed_font) > child_capacity:
                raise ValueError(
                    f"A fonte portuguesa recomprimida tem {len(packed_font)} bytes; limite {child_capacity}"
                )
            font_pack[child_offset : child_offset + child_capacity] = packed_font + b"\0" * (
                child_capacity - len(packed_font)
            )
            struct.pack_into("<I", executable, 0x3010A8, len(packed_font))
            modifications.append((font_entry.offset, bytes(font_pack), font_entry.size))
    db.close()
    if sum(selection_counts.values()) != total_count:
        raise ValueError("O catálogo do projeto não corresponde aos eventos da ISO-base")
    if output_iso.resolve() == source_iso.resolve():
        raise ValueError("Escolha outro nome; a ISO original nunca é sobrescrita")
    relocation_count = 0
    plans = []
    if relocate:
        plans, expanded_size = plan_rpk(entries, rpk_entry.size, modifications)
        offsets = {}
        for entry,new_offset,capacity,payload,old_capacity in plans:
            struct.pack_into('<I',executable,entry.table_offset+4,new_offset//SECTOR)
            offsets[entry.offset] = new_offset
            if new_offset != entry.offset: relocation_count += 1
        verification = [(name,offsets[offset],length,values) for name,offset,length,values in verification]
    shutil.copyfile(source_iso, output_iso)
    with output_iso.open("r+b") as target:
        rpk_base = rpk_entry.extent * SECTOR
        if relocate:
            target.seek(0,2)
            padding = (-target.tell()) % SECTOR
            target.write(b'\0'*padding)
            rpk_base = target.tell()
            with source_iso.open('rb') as source:
                for entry,new_offset,capacity,payload,old_capacity in plans:
                    if payload is None:
                        source.seek(rpk_entry.extent*SECTOR+entry.offset)
                        remaining=old_capacity
                        while remaining:
                            chunk=source.read(min(remaining,8*1024*1024))
                            if not chunk: raise ValueError('RPK original truncado')
                            target.write(chunk); remaining-=len(chunk)
                        target.write(b'\0'*(capacity-old_capacity))
                    else:
                        target.write(payload); target.write(b'\0'*(capacity-len(payload)))
        else:
            for offset, payload, capacity in modifications:
                target.seek(rpk_base + offset)
                target.write(payload)
                target.write(b"\0" * (capacity - len(payload)))
        if arena_info:
            target.seek(0,2)
            target.write(b'\0'*((-target.tell())%SECTOR))
            executable_base = target.tell()
        else:
            executable_base = executable_entry.extent * SECTOR
        target.seek(executable_base)
        target.write(executable)
        if arena_info:
            target.write(b'\0'*((-target.tell())%SECTOR))
    if relocate:
        move_iso_file_record(output_iso,rpk_entry,rpk_base//SECTOR,expanded_size)
        reopened_rpk = find(output_iso,'RPK.BIN')
        if reopened_rpk.extent*SECTOR != rpk_base or reopened_rpk.size != expanded_size:
            raise ValueError('Falha ao verificar realocação do arquivo RPK')
    if arena_info:
        move_iso_file_record(output_iso,executable_entry,executable_base//SECTOR,len(executable))
        reopened_entry=find(output_iso,'SLUS_214.45')
        if reopened_entry.extent*SECTOR!=executable_base or reopened_entry.size!=len(executable):
            raise ValueError('Falha ao reabrir executável expandido')
    verified_lines = 0
    with output_iso.open("rb") as rebuilt_iso:
        if relocate:
            with source_iso.open('rb') as source:
                for entry,new_offset,capacity,payload,old_capacity in plans:
                    rebuilt_iso.seek(rpk_base+new_offset)
                    if payload is not None:
                        if rebuilt_iso.read(len(payload)) != payload:
                            raise ValueError(f'Realocação inválida: {entry.name}')
                    else:
                        source.seek(rpk_entry.extent*SECTOR+entry.offset)
                        remaining=old_capacity
                        while remaining:
                            count=min(remaining,8*1024*1024)
                            if source.read(count)!=rebuilt_iso.read(count):
                                raise ValueError(f'Arquivo original alterado: {entry.name}')
                            remaining-=count
        for event_name, offset, length, replacements in verification:
            rebuilt_iso.seek(rpk_base + offset)
            event_payload = rebuilt_iso.read(length)
            validate_runtime_layout(event_payload, event_references[event_name])
            reopened = parse(event_payload)
            for entry_index, expected in replacements.items():
                actual = reopened.dialogues[entry_index].raw
                expected_encoded = encode_game_text(expected)
                matches = actual == expected_encoded
                if not matches:
                    raise ValueError(
                        f"Verificação da ISO falhou em {event_name}:{entry_index}: "
                        "o texto gravado não corresponde ao texto selecionado"
                    )
                verified_lines += 1
        rebuilt_iso.seek(executable_base)
        reopened_executable = rebuilt_iso.read(len(executable))
        if reopened_executable != bytes(executable):
            raise ValueError('Executável reaberto difere do reconstruído')
        for item in string_manifest:
            for pointer in item["pointers"]:
                if struct.unpack_from("<I", reopened_executable, pointer)[0] != item["destination_address"]:
                    raise ValueError("Falha na verificação do ponteiro de texto realocado")
        for offset, capacity, expected in executable_verification:
            expected_encoded = encode_game_text(expected)
            actual = reopened_executable[offset : offset + capacity]
            if not actual.startswith(expected_encoded) or any(
                actual[len(expected_encoded) :]
            ):
                raise ValueError(
                    f"Verificação da ISO falhou em SLUS_214.45:{offset:#x}"
                )
            verified_lines += 1
    if not relocate and not arena_info and output_iso.stat().st_size != source_iso.stat().st_size:
        raise ValueError("A ISO gerada não preservou o tamanho da imagem original")
    movie_results = apply_movie_pack(output_iso, movies)
    movie_report = output_iso.with_suffix('.movies.json')
    movie_report.write_text(json.dumps(movie_results, ensure_ascii=False, indent=2), encoding='utf-8')
    digest = hashlib.sha256()
    with output_iso.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    fallback_report = output_iso.with_suffix(".capacity_fallbacks.json")
    fallback_report.write_text(
        json.dumps(capacity_fallbacks, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    string_report = output_iso.with_suffix(".string_relocation.json")
    if relocate_strings:
        string_report.write_text(json.dumps({"experimental": True, "in_game_validated": False, "arena": arena_info,
            "moves": string_manifest, "blocked": string_blocked}, ensure_ascii=False, indent=2), encoding="utf-8")
    return {
        "events": modified_events,
        "lines": selection_counts["reviewed"] + selection_counts["automatic"],
        "output": str(output_iso),
        "accent_mode": accent_mode,
        "relocation_enabled": relocate,
        "relocated_files": relocation_count,
        "relocated_strings": len(string_manifest),
        "text_arena": arena_info,
        "string_relocation_report": str(string_report) if relocate_strings else None,
        "portuguese_font": needs_portuguese_font,
        "native_menu_font": needs_native_menu_hook,
        "verified_lines": verified_lines,
        "output_sha256": digest.hexdigest(),
        "movies_applied": len(movie_results),
        "movie_report": str(movie_report),
        "selection_counts": selection_counts,
        "capacity_fallbacks": capacity_fallbacks,
        "capacity_fallback_count": len(capacity_fallbacks),
        "capacity_fallback_report": str(fallback_report),
        "executable_texts": len(executable_verification),
    }
