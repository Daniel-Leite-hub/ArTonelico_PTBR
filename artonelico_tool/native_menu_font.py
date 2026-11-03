from __future__ import annotations

import struct

from .portuguese_font import ACCENT_TO_ALIAS, PORTUGUESE_GLYPHS


class NativeMenuText(str):
    """Menu text whose Portuguese glyphs use reserved two-byte SJIS codes."""


class ResetMenuText(str):
    """Menu text that restores the native font after every PT-BR alias."""


class NativePrintfText(NativeMenuText):
    """Scoped native menu format with an ASCII runtime substitution token."""
    ascii_format_tokens = ('%s', '%d')


NATIVE_MENU_CODES = {
    character: bytes((0xE0, 0x40 + index))
    for index, character in enumerate(PORTUGUESE_GLYPHS)
}

# The selected-item visual object obtains its name at this one call site.
# Intercept only this display pointer; persistent game data stays command-free.
HOOK_SITE_VA = 0x317130
HOOK_SITE_OFFSET = HOOK_SITE_VA - 0x100000 + 0x1000
ORIGINAL_ITEM_NAME_VA = 0x2D8C88

# INVALID CAVE: contains SDK messages followed by the live jump table used at
# 0x33fc70. Kept only for forensic reproduction; generation is blocked below.
CAVE_OFFSET = 0x97BE30
CAVE_VA = CAVE_OFFSET - 0x1000 + 0x100000
VISUAL_BUFFER_SIZE = 0x100


def native_menu_text(value: str) -> NativeMenuText:
    return NativeMenuText(value)


def reset_menu_text(value: str) -> ResetMenuText:
    return ResetMenuText(value)


def encode_native_menu_character(character: str) -> bytes | None:
    return NATIVE_MENU_CODES.get(character)


def _i(op: int, rs: int, rt: int, immediate: int) -> int:
    return (op << 26) | (rs << 21) | (rt << 16) | (immediate & 0xFFFF)


def _r(rs: int, rt: int, rd: int, function: int) -> int:
    return (rs << 21) | (rt << 16) | (rd << 11) | function


def _jal(address: int) -> int:
    return (3 << 26) | ((address >> 2) & 0x03FFFFFF)


def hook_payload() -> bytes:
    labels: dict[str, int] = {}
    code: list[tuple[str | None, int | tuple[int, int, int, str]]] = []

    def emit(word: int, label: str | None = None) -> None:
        if label:
            labels[label] = len(code)
        code.append((None, word))

    def branch(op: int, rs: int, rt: int, target: str, label: str | None = None) -> None:
        if label:
            labels[label] = len(code)
        code.append(("branch", (op, rs, rt, target)))

    # t0=source, t1=scan/destination, t2=byte, t3=trail/index,
    # t4=flag, t5=alias, t6=table, t7=end, t8=original, t9=buffer.
    emit(_i(0x09, 29, 29, -0x20))
    emit(_i(0x2B, 29, 31, 0x1C))
    emit(_jal(ORIGINAL_ITEM_NAME_VA))
    emit(0)
    emit(_r(2, 0, 8, 0x21))
    emit(_r(2, 0, 24, 0x21))
    emit(_r(8, 0, 9, 0x21))
    emit(_i(0x24, 9, 10, 0), label="scan")
    branch(0x04, 10, 0, "finish_original")
    emit(0)
    emit(_i(0x09, 0, 11, 0xE0))
    branch(0x05, 10, 11, "scan_one")
    emit(0)
    emit(_i(0x24, 9, 11, 1))
    emit(_i(0x09, 11, 11, -0x40))
    emit(_i(0x0B, 11, 12, len(PORTUGUESE_GLYPHS)))
    branch(0x05, 12, 0, "transform")
    emit(0)
    emit(_i(0x09, 9, 9, 1), label="scan_one")
    branch(0x04, 0, 0, "scan")
    emit(0)

    buffer_lui = len(code)
    emit(0, label="transform")
    buffer_add = len(code)
    emit(0)
    emit(_r(15, 0, 25, 0x21))
    emit(_r(25, 0, 9, 0x21))
    emit(_i(0x09, 15, 15, VISUAL_BUFFER_SIZE - 1))
    table_lui = len(code)
    emit(0)
    table_add = len(code)
    emit(0)

    emit(_i(0x24, 8, 10, 0), label="copy")
    branch(0x04, 10, 0, "finish_buffer")
    emit(0)
    emit(_i(0x09, 0, 11, 0xE0))
    branch(0x05, 10, 11, "copy_one")
    emit(0)
    emit(_i(0x24, 8, 11, 1))
    emit(_i(0x09, 11, 11, -0x40))
    emit(_i(0x0B, 11, 12, len(PORTUGUESE_GLYPHS)))
    branch(0x04, 12, 0, "copy_one")
    emit(0)
    emit(_i(0x09, 15, 12, -5))
    emit(_r(12, 9, 12, 0x2B))
    branch(0x05, 12, 0, "finish_original")
    emit(0)
    emit(_r(14, 11, 12, 0x21))
    emit(_i(0x24, 12, 13, 0))
    for offset, character in enumerate("#1"):
        emit(_i(0x09, 0, 10, ord(character)))
        emit(_i(0x28, 9, 10, offset))
    emit(_i(0x28, 9, 13, 2))
    for offset, character in ((3, "#"), (4, "0")):
        emit(_i(0x09, 0, 10, ord(character)))
        emit(_i(0x28, 9, 10, offset))
    emit(_i(0x09, 8, 8, 2))
    emit(_i(0x09, 9, 9, 5))
    branch(0x04, 0, 0, "copy")
    emit(0)

    emit(_r(9, 15, 12, 0x2B), label="copy_one")
    branch(0x04, 12, 0, "finish_original")
    emit(0)
    emit(_i(0x28, 9, 10, 0))
    emit(_i(0x09, 8, 8, 1))
    emit(_i(0x09, 9, 9, 1))
    branch(0x04, 0, 0, "copy")
    emit(0)

    emit(_i(0x28, 9, 0, 0), label="finish_buffer")
    emit(_r(25, 0, 2, 0x21))
    branch(0x04, 0, 0, "finish")
    emit(0)
    emit(_r(24, 0, 2, 0x21), label="finish_original")
    emit(_i(0x23, 29, 31, 0x1C), label="finish")
    emit(_i(0x09, 29, 29, 0x20))
    emit(_r(31, 0, 0, 0x08))
    emit(0)

    words: list[int] = []
    for index, (kind, value) in enumerate(code):
        if kind is None:
            words.append(value)  # type: ignore[arg-type]
        else:
            op, rs, rt, target = value  # type: ignore[misc]
            words.append(_i(op, rs, rt, labels[target] - (index + 1)))

    aliases = bytes(ord(ACCENT_TO_ALIAS[c]) for c in PORTUGUESE_GLYPHS)
    table_va = CAVE_VA + len(words) * 4
    buffer_va = (table_va + len(aliases) + 15) & ~15

    def address_pair(address: int, register: int) -> tuple[int, int]:
        return (
            _i(0x0F, 0, register, (address + 0x8000) >> 16),
            _i(0x09, register, register, address & 0xFFFF),
        )

    words[table_lui], words[table_add] = address_pair(table_va, 14)
    words[buffer_lui], words[buffer_add] = address_pair(buffer_va, 15)
    machine = b"".join(struct.pack("<I", word) for word in words)
    padding = b"\0" * (buffer_va - (CAVE_VA + len(machine) + len(aliases)))
    return machine + aliases + padding + b"\0" * VISUAL_BUFFER_SIZE


def patch_native_menu_hook(executable: bytearray) -> None:
    # Both earlier payloads destroyed live data. A mapped RWX segment does not
    # make its contents disposable. Do not generate another broken experiment.
    raise ValueError(
        "Modo experimental de acentos em menus bloqueado: o endereço 0x97BE30 "
        "contém dados ativos e a tabela de funções em 0x97C030. "
        "Use o modo padrão até validar uma extensão de fonte sem sobrescrita."
    )
