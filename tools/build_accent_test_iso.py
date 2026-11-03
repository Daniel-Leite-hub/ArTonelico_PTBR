from __future__ import annotations

import shutil
import sqlite3
import struct
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from artonelico_tool.evd import EvdFile, parse
from artonelico_tool.iso import SECTOR, find, read_entry
from artonelico_tool.lzr import compress, decompress
from artonelico_tool.rpk import read_index


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "testes pt br" / "teste.atproj"
OUTPUT = ROOT / "testes pt br" / "Ar tonelico - PTBR teste acentos.iso"
TARGETS = {"Event/107.evd": 5, "Event/108.evd": 0}

# In the #1 Latin font, these rarely used symbols become Portuguese glyphs.
ACCENT_CODES = {"é": "%", "ã": "@", "ó": "<", "ç": ">", "º": "*"}
GLYPH_RECTS = {
    "%": (86, 22, 107, 44),
    "@": (180, 22, 201, 44),
    "<": (141, 22, 151, 44),
    ">": (152, 22, 162, 44),
    "*": (201, 22, 212, 44),
}


def encode_test_text(text: str) -> bytes:
    unsupported = sorted({char for char in text if ord(char) > 0x7F and char not in ACCENT_CODES})
    if unsupported:
        raise ValueError(f"Caracteres ainda não mapeados para o teste: {unsupported}")
    encoded = "".join(ACCENT_CODES.get(char, char) for char in text)
    return b"#1" + encoded.encode("ascii") + b"\0"


def build_evd_raw(evd: EvdFile, replacements: dict[int, bytes]) -> bytes:
    output = bytearray(struct.pack("<I", len(evd.dialogues)))
    for row in evd.dialogues:
        changed = row.index in replacements
        raw = replacements[row.index] if changed else row.raw
        output.extend(struct.pack("<IIIIII", row.position, row.name_id, row.portrait_id, row.text_id, row.portrait_type, len(raw)))
        output.extend(raw)
        output.extend(b"\0" * ((-len(raw)) % 4) if changed else row.padding)
        output.extend(row.extra)
    output.extend(evd.trailer)
    return bytes(output)


def patch_latin_font(raw_tm2: bytes) -> tuple[bytes, Image.Image]:
    data = bytearray(raw_tm2)
    base = 16
    _, clut_size, image_size = struct.unpack_from("<III", data, base)
    header_size, colors = struct.unpack_from("<HH", data, base + 12)
    image_type = data[base + 19]
    width, height = struct.unpack_from("<HH", data, base + 20)
    if image_type != 4 or colors != 16:
        raise ValueError("FO_HGGBP.tm2 não é uma textura TIM2 4-bit esperada")
    pixel_offset = base + header_size
    clut_offset = pixel_offset + image_size
    packed = data[pixel_offset : pixel_offset + image_size]
    indices: list[int] = []
    for byte in packed:
        indices.extend((byte & 0xF, byte >> 4))
    indices = indices[: width * height]
    alphas = [min(255, data[clut_offset + i * 4 + 3] * 2) for i in range(16)]
    transparent = min(range(16), key=lambda i: alphas[i])

    font_path = Path(r"C:\Windows\Fonts\arial.ttf")
    font = ImageFont.truetype(str(font_path), 21)
    for accented, symbol in ACCENT_CODES.items():
        x0, y0, x1, y1 = GLYPH_RECTS[symbol]
        for y in range(y0, y1):
            indices[y * width + x0 : y * width + x1] = [transparent] * (x1 - x0)
        mask = Image.new("L", (x1 - x0, y1 - y0), 0)
        draw = ImageDraw.Draw(mask)
        bbox = draw.textbbox((0, 0), accented, font=font)
        glyph_width, glyph_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        draw.text(
            ((mask.width - glyph_width) // 2 - bbox[0], (mask.height - glyph_height) // 2 - bbox[1]),
            accented,
            font=font,
            fill=255,
        )
        for y in range(mask.height):
            for x in range(mask.width):
                alpha = mask.getpixel((x, y))
                if alpha:
                    index = min(range(16), key=lambda i: abs(alphas[i] - alpha))
                    indices[(y0 + y) * width + x0 + x] = index

    for i in range(0, len(indices), 2):
        data[pixel_offset + i // 2] = indices[i] | (indices[i + 1] << 4)

    palette = []
    for i in range(16):
        r, g, b, a = data[clut_offset + i * 4 : clut_offset + i * 4 + 4]
        palette.append((r, g, b, min(255, a * 2)))
    preview = Image.new("RGBA", (width, height))
    preview.putdata([palette[i] for i in indices])
    return bytes(data), preview


def main() -> None:
    db = sqlite3.connect(PROJECT)
    db.row_factory = sqlite3.Row
    rows = db.execute(
        "SELECT event_file,entry_index,reviewed FROM dialogues "
        "WHERE reviewed<>'' ORDER BY event_file,entry_index"
    ).fetchall()
    selected = {(row["event_file"], row["entry_index"]): row["reviewed"] for row in rows}
    expected = {(name, index) for name, index in TARGETS.items()}
    if set(selected) != expected:
        raise ValueError(f"O projeto deve conter somente as duas revisões de teste; encontrei {sorted(selected)}")
    source_iso = Path(db.execute("SELECT value FROM meta WHERE key='iso_path'").fetchone()[0].strip('"'))
    db.close()

    executable_entry = find(source_iso, "SLUS_214.45")
    rpk_entry = find(source_iso, "RPK.BIN")
    executable = bytearray(read_entry(source_iso, executable_entry))
    with tempfile.NamedTemporaryFile(suffix=".elf", delete=False) as temporary:
        temporary.write(executable)
        executable_path = Path(temporary.name)
    try:
        entries = read_index(executable_path, rpk_entry.size)
    finally:
        executable_path.unlink(missing_ok=True)
    by_name = {entry.name: entry for entry in entries}

    rpk_changes: list[tuple[int, bytes, int]] = []
    with source_iso.open("rb") as source:
        for event_name, row_index in TARGETS.items():
            entry = by_name[event_name]
            source.seek(rpk_entry.extent * SECTOR + entry.offset)
            evd = parse(source.read(entry.size))
            text = selected[(event_name, row_index)]
            rebuilt = build_evd_raw(evd, {row_index: encode_test_text(text)})
            entry_position = entries.index(entry)
            capacity = (entries[entry_position + 1].sector - entry.sector) * SECTOR
            if len(rebuilt) > capacity:
                raise ValueError(f"{event_name} excede a capacidade de {capacity} bytes")
            struct.pack_into("<I", executable, entry.table_offset + 8, len(rebuilt))
            rpk_changes.append((entry.offset, rebuilt, capacity))

        font_entry = by_name["fpack/font.fp"]
        source.seek(rpk_entry.extent * SECTOR + font_entry.offset)
        font_pack = bytearray(source.read(font_entry.size))
        child_offset, child_capacity = 12 * SECTOR, 3 * SECTOR
        original_size = struct.unpack_from("<I", executable, 0x3010A8)[0]
        patched_tm2, preview = patch_latin_font(decompress(font_pack[child_offset : child_offset + original_size]))
        packed_font = compress(patched_tm2)
        if len(packed_font) > child_capacity:
            raise ValueError(f"Fonte recomprimida tem {len(packed_font)} bytes; limite {child_capacity}")
        font_pack[child_offset : child_offset + child_capacity] = packed_font + b"\0" * (child_capacity - len(packed_font))
        struct.pack_into("<I", executable, 0x3010A8, len(packed_font))
        rpk_changes.append((font_entry.offset, bytes(font_pack), font_entry.size))
        preview_bg = Image.new("RGBA", preview.size, (24, 24, 24, 255))
        preview_bg.alpha_composite(preview)
        preview_bg.resize((preview.width * 4, preview.height * 4), Image.Resampling.NEAREST).convert("RGB").save(
            OUTPUT.with_suffix(".font-preview.png")
        )

    shutil.copyfile(source_iso, OUTPUT)
    with OUTPUT.open("r+b") as target:
        for offset, payload, capacity in rpk_changes:
            target.seek(rpk_entry.extent * SECTOR + offset)
            target.write(payload)
            if len(payload) < capacity:
                target.write(b"\0" * (capacity - len(payload)))
        target.seek(executable_entry.extent * SECTOR)
        target.write(executable)
    print(OUTPUT)
    print(f"Fonte LZR: {len(packed_font)} / {child_capacity} bytes")
    print("Dialogos modificados: Event/107.evd:5, Event/108.evd:0")


if __name__ == "__main__":
    main()
