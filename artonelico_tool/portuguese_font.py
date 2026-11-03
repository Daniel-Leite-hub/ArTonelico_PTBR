from __future__ import annotations

import struct
import unicodedata
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont


PORTUGUESE_GLYPHS = "áàâãéêíóôõúüçÁÀÂÃÉÊÍÓÔÕÚÜÇªº"
# Aliases are assigned by advance width, not alphabetically.  The #1 renderer
# uses each source glyph's atlas width as its horizontal advance; the old
# A-Z mapping therefore made variants of the same vowel visibly uneven (most
# notably í using the 17 px G slot).  These slots keep lowercase families at
# 13-15 px, capitals at 16-18 px, and both í/Í at 6 px.
GLYPH_ALIASES = "JFLSYZIBETUX*ACGHDP!KNORVQ<>"
ACCENT_TO_ALIAS = dict(zip(PORTUGUESE_GLYPHS, GLYPH_ALIASES, strict=True))

# The #1 font descriptor in SLUS_214.45 points at texture FO_HGGBP.  Its UV
# bounds are inclusive, while PIL rectangles are exclusive, hence the +1 on
# the right/bottom coordinates below.  Using the visually estimated bounds
# clips Q-Z and shifts their accents by two pixels.
_FIRST_ROW = (
    (0, 16), (17, 31), (32, 48), (49, 64), (65, 79), (80, 93),
    (94, 110), (111, 127), (128, 133), (134, 146), (147, 163),
    (164, 177), (178, 196), (197, 213), (214, 230), (231, 246),
)
_SECOND_ROW = (
    (0, 17), (18, 33), (34, 47), (48, 62), (63, 77),
    (78, 93), (94, 114), (115, 129), (130, 143), (144, 157),
)
GLYPH_RECTS = {
    **{
        chr(ord("A") + index): (bounds[0], 44, bounds[1] + 1, 66)
        for index, bounds in enumerate(_FIRST_ROW)
    },
    **{
        chr(ord("Q") + index): (bounds[0], 66, bounds[1] + 1, 88)
        for index, bounds in enumerate(_SECOND_ROW)
    },
    "@": (180, 22, 201, 44),
    "*": (201, 22, 212, 44),
    "!": (64, 22, 70, 44),
    "<": (141, 22, 151, 44),
    ">": (152, 22, 162, 44),
}


def encode_portuguese_character(character: str) -> bytes | None:
    alias = ACCENT_TO_ALIAS.get(character)
    return alias.encode("ascii") if alias else None


def has_portuguese_glyphs(text: str) -> bool:
    return any(character in ACCENT_TO_ALIAS for character in text)


def _font(size: int) -> ImageFont.FreeTypeFont:
    candidates = (
        Path(r"C:\Windows\Fonts\arial.ttf"),
        Path(r"C:\Windows\Fonts\segoeui.ttf"),
    )
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default(size=size)


def _vertical_origin(
    draw: ImageDraw.ImageDraw,
    character: str,
    font: ImageFont.ImageFont,
    bounds: tuple[int, int, int, int],
    cell_height: int,
) -> int:
    """Align an accented glyph to the baseline of its unaccented letter.

    Centering every complete glyph independently makes the body of a, e and
    other accented lowercase letters sit lower than the game's ordinary Latin
    glyphs.  Use the base letter's vertical box instead, then clamp only when
    needed to keep an accent or cedilla inside the atlas cell.
    """
    base_character = unicodedata.normalize("NFD", character)[0]
    # The source atlas uses one common baseline for lowercase letters and one
    # for capitals.  A shared reference prevents tall letters such as i/I from
    # being centered lower merely because their dot/ascender changes the box.
    reference_character = "a" if base_character.islower() else "A"
    base_bounds = draw.textbbox((0, 0), reference_character, font=font)
    base_height = base_bounds[3] - base_bounds[1]
    origin = (cell_height - base_height) // 2 - base_bounds[1]
    minimum = -bounds[1]
    maximum = cell_height - bounds[3]
    return min(max(origin, minimum), maximum)


def patch_tm2(raw_tm2: bytes) -> tuple[bytes, Image.Image]:
    data = bytearray(raw_tm2)
    base = 16
    _, _, image_size = struct.unpack_from("<III", data, base)
    header_size, colors = struct.unpack_from("<HH", data, base + 12)
    image_type = data[base + 19]
    width, height = struct.unpack_from("<HH", data, base + 20)
    if image_type != 4 or colors != 16 or (width, height) != (256, 128):
        raise ValueError("FO_HGGBP.tm2 não é a textura TIM2 PSMT4 esperada")
    pixel_offset = base + header_size
    clut_offset = pixel_offset + image_size
    pixels: list[int] = []
    for value in data[pixel_offset : pixel_offset + image_size]:
        pixels.extend((value & 0xF, value >> 4))
    pixels = pixels[: width * height]
    alphas = [min(255, data[clut_offset + index * 4 + 3] * 2) for index in range(16)]
    transparent = min(range(16), key=lambda index: alphas[index])
    regular = _font(21)
    capital_body = _font(19)
    ordinal = _font(16)

    for character, alias in ACCENT_TO_ALIAS.items():
        x0, y0, x1, y1 = GLYPH_RECTS[alias]
        for y in range(y0, y1):
            pixels[y * width + x0 : y * width + x1] = [transparent] * (x1 - x0)
        mask = Image.new("L", (x1 - x0, y1 - y0), 0)
        draw = ImageDraw.Draw(mask)
        selected_font = ordinal if character in "ªº" else regular
        bounds = draw.textbbox((0, 0), character, font=selected_font)
        glyph_width = bounds[2] - bounds[0]
        glyph_height = bounds[3] - bounds[1]
        if character in "ªº":
            vertical_origin = (mask.height - glyph_height) // 2 - bounds[1]
            draw.text(
                ((mask.width - glyph_width) // 2 - bounds[0], vertical_origin),
                character,
                font=selected_font,
                fill=255,
            )
        elif character in "ÁÀÂÃÉÊÍÓÔÕÚÜ":
            # Compose capital and diacritic separately.  Centering the complete
            # accented glyph forced its body two pixels below the lowercase
            # baseline.  Keep the original accent at the top of the cell, but
            # draw the base capital with its last pixel on row 15, the same
            # baseline used by the ordinary text rendered alongside it.
            accent_origin = _vertical_origin(
                draw, character, selected_font, bounds, mask.height
            )
            accented = Image.new("L", mask.size, 0)
            accented_draw = ImageDraw.Draw(accented)
            accented_x = (mask.width - glyph_width) // 2 - bounds[0]
            accented_draw.text(
                (accented_x, accent_origin), character, font=selected_font, fill=255
            )

            base_character = unicodedata.normalize("NFD", character)[0]
            accent_base_bounds = draw.textbbox(
                (0, 0), base_character, font=selected_font
            )
            accent_base_width = accent_base_bounds[2] - accent_base_bounds[0]
            accent_base_x = (
                (mask.width - accent_base_width) // 2 - accent_base_bounds[0]
            )
            base_at_accent = Image.new("L", mask.size, 0)
            ImageDraw.Draw(base_at_accent).text(
                (accent_base_x, accent_origin),
                base_character,
                font=selected_font,
                fill=255,
            )
            accent_difference = ImageChops.subtract(accented, base_at_accent)
            accent_bottom = max(
                0, min(mask.height, accent_origin + accent_base_bounds[1])
            )
            accent_only = Image.new("L", mask.size, 0)
            if accent_bottom:
                accent_only.paste(
                    accent_difference.crop((0, 0, mask.width, accent_bottom)), (0, 0)
                )

            # A slightly shorter capital body reserves two clear atlas rows
            # for the diacritic while keeping the same row-15 baseline.  At
            # size 21 the O/E body began on row 1 and swallowed most of the
            # accent after composition.
            base_bounds = draw.textbbox((0, 0), base_character, font=capital_body)
            base_width = base_bounds[2] - base_bounds[0]
            base_x = (mask.width - base_width) // 2 - base_bounds[0]
            capital_origin = 15 - (base_bounds[3] - 1)
            draw.text(
                (base_x, capital_origin),
                base_character,
                font=capital_body,
                fill=255,
            )
            mask.paste(ImageChops.lighter(mask, accent_only))
        else:
            vertical_origin = _vertical_origin(
                draw, character, selected_font, bounds, mask.height
            )
            draw.text(
                ((mask.width - glyph_width) // 2 - bounds[0], vertical_origin),
                character,
                font=selected_font,
                fill=255,
            )
        for y in range(mask.height):
            for x in range(mask.width):
                alpha = mask.getpixel((x, y))
                if alpha:
                    palette_index = min(range(16), key=lambda index: abs(alphas[index] - alpha))
                    pixels[(y0 + y) * width + x0 + x] = palette_index

    for index in range(0, len(pixels), 2):
        data[pixel_offset + index // 2] = pixels[index] | (pixels[index + 1] << 4)

    palette = []
    for index in range(16):
        red, green, blue, alpha = data[clut_offset + index * 4 : clut_offset + index * 4 + 4]
        palette.append((red, green, blue, min(255, alpha * 2)))
    preview = Image.new("RGBA", (width, height))
    preview.putdata([palette[index] for index in pixels])
    return bytes(data), preview
