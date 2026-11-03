from pathlib import Path
import sys
import struct

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from PIL import Image


data = Path("work/fonts/FO_HGGBP.tm2").read_bytes()
base = 16
_, _, image_size = struct.unpack_from("<III", data, base)
header_size = struct.unpack_from("<H", data, base + 12)[0]
width, height = struct.unpack_from("<HH", data, base + 20)
pixel_offset = base + header_size
clut_offset = pixel_offset + image_size
pixels = []
for value in data[pixel_offset : pixel_offset + image_size]:
    pixels.extend((value & 0xF, value >> 4))
alphas = [min(255, data[clut_offset + index * 4 + 3] * 2) for index in range(16)]
preview = Image.new("L", (width, height))
preview.putdata([alphas[index] for index in pixels[: width * height]])
for y0, y1 in ((0, 22), (22, 44), (44, 66), (66, 88), (88, 110)):
    points = {
        (x, y)
        for y in range(y0, y1)
        for x in range(preview.width)
        if preview.getpixel((x, y)) > 32
    }
    boxes = []
    while points:
        seed = points.pop()
        stack = [seed]
        component = [seed]
        while stack:
            x, y = stack.pop()
            for neighbor in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if neighbor in points:
                    points.remove(neighbor)
                    stack.append(neighbor)
                    component.append(neighbor)
        if len(component) > 2:
            boxes.append(
                (
                    min(x for x, _ in component),
                    min(y for _, y in component),
                    max(x for x, _ in component),
                    max(y for _, y in component),
                    len(component),
                )
            )
    print((y0, y1), sorted(boxes))
