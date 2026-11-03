from __future__ import annotations


def translation_track(event_file: str, entry_index: int) -> str:
    """Route known executable banks without mistaking short dialogue for UI."""
    if not event_file.startswith("SLUS/TEXT/"):
        return "dialogue"
    offset = entry_index
    if 0x869000 <= offset < 0x86D000 or offset in {0x928138, 0x92B4C8}:
        return "dialogue"
    if (
        0x7C0000 <= offset < 0x800000
        or 0x807EB8 <= offset < 0x807ED0
        or 0x81EBB0 <= offset < 0x869000
        or 0x86D000 <= offset < 0x86D418
        or 0x8E2C00 <= offset < 0x8E3000
        or 0x900000 <= offset < 0x932810
        or 0x936980 <= offset < 0x936A80
        or 0x938000 <= offset < 0x939000
        or 0x977528 <= offset < 0x977F48
        or 0x98F000 <= offset < 0x9A0000
    ):
        return "localization"
    return "dialogue"
