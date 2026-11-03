from __future__ import annotations

import struct
import sys
from pathlib import Path

from PIL import Image


def decode(path: Path) -> Image.Image:
    data = path.read_bytes()
    if data[:4] != b"TIM2":
        raise ValueError(path)
    base = 16
    total, clut_size, image_size = struct.unpack_from("<III", data, base)
    header_size, colors = struct.unpack_from("<HH", data, base + 12)
    image_type = data[base + 19]
    width, height = struct.unpack_from("<HH", data, base + 20)
    pixels = data[base + header_size : base + header_size + image_size]
    clut = data[base + header_size + image_size : base + header_size + image_size + clut_size]
    palette = []
    for i in range(colors):
        r, g, b, a = clut[i * 4 : i * 4 + 4]
        palette.append((r, g, b, min(255, a * 2)))
    indices = []
    if image_type == 4:
        for byte in pixels:
            indices.extend((byte & 0xF, byte >> 4))
    elif image_type == 5:
        # PS2 8-bit indexed textures store the middle CLUT blocks swapped.
        palette = [
            palette[(i & 0xE7) | ((i & 0x08) << 1) | ((i & 0x10) >> 1)]
            for i in range(256)
        ]
        indices.extend(pixels)
    else:
        raise ValueError(f"Unsupported TIM2 image type {image_type}")
    image = Image.new("RGBA", (width, height))
    image.putdata([palette[i] for i in indices[: width * height]])
    return image


for name in sys.argv[1:]:
    path = Path(name)
    output = path.with_suffix(".png")
    decode(path).save(output)
    print(output)
