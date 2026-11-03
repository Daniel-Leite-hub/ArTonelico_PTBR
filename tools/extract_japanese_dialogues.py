"""Extract original Japanese dialogues and executable strings from the Japanese PS2 ISO and add to project database."""
from __future__ import annotations

import argparse
import datetime
import re
import shutil
import sqlite3
import struct
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from artonelico_tool import evd, rpk
from artonelico_tool.iso import SECTOR, find, list_files, read_entry


def find_japanese_iso(candidates: list[Path]) -> Path | None:
    for path in candidates:
        if path.is_file() and "japan" in path.name.lower() and path.suffix.lower() == ".iso":
            return path
    return None


def find_us_iso(candidates: list[Path]) -> Path | None:
    for path in candidates:
        if (
            path.is_file()
            and "japan" not in path.name.lower()
            and "elemia" in path.name.lower()
            and path.suffix.lower() == ".iso"
        ):
            return path
    return None


def us_va_to_off(va: int) -> int | None:
    if 0x003E8980 <= va < 0x00878ED8:
        return va - 0x003E8980 + 3053952
    if 0x00879400 <= va < 0x00A8DD30:
        return va - 0x00879400 + 7840768
    if 0x00A8DD80 <= va < 0x00A91858:
        return va - 0x00A8DD80 + 10022272
    return None


def us_off_to_va(off: int) -> int | None:
    if 3053952 <= off < 7839528:
        return off - 3053952 + 0x003E8980
    if 7840768 <= off < 10022160:
        return off - 7840768 + 0x00879400
    if 10022272 <= off < 10037336:
        return off - 10022272 + 0x00A8DD80
    return None


def jp_va_to_off(va: int) -> int | None:
    if 0x003E7700 <= va < 0x008FC118:
        return va - 0x003E7700 + 3049216
    if 0x008FC580 <= va < 0x00A76440:
        return va - 0x008FC580 + 8377728
    if 0x00A76580 <= va < 0x00A7A0B8:
        return va - 0x00A76580 + 9926016
    return None


def read_cstr(elf: bytes, off: int) -> str:
    end = elf.find(b"\x00", off)
    if end == -1:
        end = off + 512
    return evd.decode_game_text(elf[off:end])


def split_jp_by_us_pages(full_jp: str, u_texts: list[str]) -> list[str]:
    n = len(u_texts)
    if n == 1:
        return [full_jp]
    tokens = [t for t in re.split(r"(?<=。)|(?=CR)", full_jp) if t]
    if len(tokens) < n:
        return [full_jp] * n
    u_lens = [max(1, len(t)) for t in u_texts]
    total_u = sum(u_lens)
    total_j = len(full_jp)
    targets = []
    acc = 0
    for l in u_lens[:-1]:
        acc += l
        targets.append(total_j * acc / total_u)
    splits = [0]
    cum_lens = []
    c = 0
    for t in tokens:
        c += len(t)
        cum_lens.append(c)
    for k, target in enumerate(targets):
        min_idx = splits[-1] + 1
        max_idx = len(tokens) - (n - 1 - k)
        best_idx = min(
            range(min_idx, max_idx + 1), key=lambda i: abs(cum_lens[i - 1] - target)
        )
        splits.append(best_idx)
    splits.append(len(tokens))
    res = []
    for a, b in zip(splits[:-1], splits[1:]):
        chunk = "".join(tokens[a:b])
        if chunk.startswith("CR"):
            chunk = chunk[2:]
        res.append(chunk)
    return res


def build_slus_to_slps_map(
    us_elf: bytes, jp_elf: bytes, target_offsets: list[int]
) -> dict[int, str]:
    target_set = set(target_offsets)
    va_to_us_off: dict[int, int] = {}
    for off in target_offsets:
        va = us_off_to_va(off)
        if va is not None:
            va_to_us_off[va] = off

    mapped: dict[int, list[str]] = {}

    def add_mapping(us_off: int, jp_text: str) -> None:
        if not jp_text:
            return
        lst = mapped.setdefault(us_off, [])
        if jp_text not in lst:
            lst.append(jp_text)

    # 0. World Terminology multi-page articles (7404144..7409984, 80-byte structs)
    for base in range(7404144, 7409984, 80):
        u_title_va = struct.unpack_from("<I", us_elf, base)[0]
        j_title_va = struct.unpack_from("<I", jp_elf, base + 537008)[0]
        if u_title_va in va_to_us_off:
            j_title_off = jp_va_to_off(j_title_va)
            if j_title_off is not None:
                add_mapping(va_to_us_off[u_title_va], read_cstr(jp_elf, j_title_off))
        u_pages: list[tuple[int, str]] = []
        j_pages: list[str] = []
        for k in range(1, 10):
            uv = struct.unpack_from("<I", us_elf, base + k * 8)[0]
            jv = struct.unpack_from("<I", jp_elf, base + 537008 + k * 8)[0]
            if uv and uv in va_to_us_off:
                u_off = va_to_us_off[uv]
                u_pages.append((u_off, read_cstr(us_elf, u_off)))
            if jv:
                j_off = jp_va_to_off(jv)
                if j_off is not None:
                    j_pages.append(read_cstr(jp_elf, j_off))
        if u_pages and j_pages:
            if len(u_pages) == len(j_pages):
                for (u_off, _), j_txt in zip(u_pages, j_pages):
                    add_mapping(u_off, j_txt)
            else:
                full_jp = "".join(j_pages)
                parts = split_jp_by_us_pages(full_jp, [ut for _, ut in u_pages])
                for (u_off, _), j_txt in zip(u_pages, parts):
                    add_mapping(u_off, j_txt)

    # 1. Tier 1: Main .data struct & pointer tables (5650000..7600000)
    for us_pos in range(5650000, 7600000, 4):
        if 7404144 <= us_pos < 7409984:
            continue
        uv = struct.unpack_from("<I", us_elf, us_pos)[0]
        us_off = va_to_us_off.get(uv)
        if us_off is None:
            continue
        delta = 537008 if (6400000 <= us_pos < 7410288) else 536992
        jp_pos = us_pos + delta
        jv = struct.unpack_from("<I", jp_elf, jp_pos)[0]
        if jv == uv and us_pos < 5705000:
            # Packed 16-bit integer pair in 5694000..5700000, not a relocated pointer
            continue
        if not (0x008FC580 <= jv < 0x00A7A0B8):
            continue
        jp_off = jp_va_to_off(jv)
        if jp_off is not None:
            add_mapping(us_off, read_cstr(jp_elf, jp_off))

    # 2. Tier 2: UI Block 8170440..8172736 (SLUS/TEXT/0001..0004)
    jp_ui_strings: dict[int, str] = {}
    pos = 8707416
    while pos <= 8708728:
        if jp_elf[pos] == 0:
            pos += 1
            continue
        end = jp_elf.find(b"\x00", pos)
        jp_ui_strings[pos] = evd.decode_game_text(jp_elf[pos:end])
        pos = (end + 4) & ~3
    jp_ui_list = list(jp_ui_strings.items())

    us_ui_offs = sorted(o for o in target_offsets if 8170440 <= o <= 8172736)
    for i in range(56):
        add_mapping(us_ui_offs[i], jp_ui_list[i][1])
    jp_57_69 = [txt for off, txt in jp_ui_list[57:70] if off != 8708216]
    for u_off, j_txt in zip(us_ui_offs[56:68], jp_57_69):
        add_mapping(u_off, j_txt)
    add_mapping(8172048, jp_ui_strings[8707480])
    add_mapping(8172072, jp_ui_strings[8708344])
    add_mapping(8172112, jp_ui_strings[8708360])
    add_mapping(8172128, jp_ui_strings[8708376])
    us_rest = [o for o in us_ui_offs if o >= 8172152]
    jp_skip = {8708464, 8708512, 8708528, 8708608, 8708624, 8708648, 8708696, 8708712}
    jp_rest = [txt for off, txt in jp_ui_list if off >= 8708384 and off not in jp_skip]
    for u_off, j_txt in zip(us_rest, jp_rest):
        add_mapping(u_off, j_txt)

    # 3. Tier 3: .text LUI + ADDIU instruction references & pointer tables
    va_plus2_to_us_off = {us_off_to_va(9634630) + 2: 9634630}

    def mask_inst(w: int) -> int:
        op = w >> 26
        if op in (2, 3):
            return op << 26
        if op == 15:
            return w & 0xFFFF0000
        if op in (8, 9, 12, 13, 14, 32, 33, 35, 36, 37, 40, 41, 43):
            return w & 0xFFFF0000
        return w

    us_text_end = 3023200
    jp_text_end = 3018400

    us_words = struct.unpack_from(f"<{us_text_end // 4}I", us_elf, 0)
    jp_words = struct.unpack_from(f"<{jp_text_end // 4}I", jp_elf, 0)
    us_masked = [mask_inst(w) for w in us_words]
    jp_masked = [mask_inst(w) for w in jp_words]

    def match_lui_addiu_in_jp(l_idx: int, a_idx: int) -> int | None:
        rt = (us_words[l_idx] >> 16) & 0x1F
        add_op_rs_rt = us_words[a_idx] >> 16
        best_score = -1
        best_va = None
        start_j = max(1024, l_idx - 2000)
        end_j = min(len(jp_words) - 32, l_idx + 500)
        for j_l in range(start_j, end_j):
            jw = jp_words[j_l]
            if (jw >> 26) != 15 or ((jw >> 16) & 0x1F) != rt:
                continue
            j_a = j_l + (a_idx - l_idx)
            if j_a >= len(jp_words) or (jp_words[j_a] >> 16) != add_op_rs_rt:
                continue
            score = 0
            for k in range(-16, 17):
                if 1024 <= l_idx + k < len(us_masked) and 1024 <= j_l + k < len(jp_masked):
                    if us_masked[l_idx + k] == jp_masked[j_l + k]:
                        score += 1
            if score > best_score:
                best_score = score
                hi = jw & 0xFFFF
                lo = jp_words[j_a] & 0xFFFF
                if lo >= 0x8000:
                    lo -= 0x10000
                best_va = (hi << 16) + lo
        if best_score >= 15:
            return best_va
        return None

    reg_lui: dict[int, tuple[int, int]] = {}
    ptr_table_matches: list[tuple[int, int]] = []
    for idx in range(1024, len(us_words)):
        w = us_words[idx]
        op = w >> 26
        if op == 15:
            rt = (w >> 16) & 0x1F
            reg_lui[rt] = (idx, w & 0xFFFF)
        elif op == 9:
            rs = (w >> 21) & 0x1F
            rt = (w >> 16) & 0x1F
            if rs in reg_lui:
                l_idx, hi = reg_lui[rs]
                if idx - l_idx <= 16:
                    lo = w & 0xFFFF
                    if lo >= 0x8000:
                        lo -= 0x10000
                    va = (hi << 16) + lo
                    if va in va_to_us_off:
                        us_off = va_to_us_off[va]
                        if us_off not in mapped:
                            j_va = match_lui_addiu_in_jp(l_idx, idx)
                            if j_va is not None:
                                j_off = jp_va_to_off(j_va)
                                if j_off is not None:
                                    add_mapping(us_off, read_cstr(jp_elf, j_off))
                    elif va in va_plus2_to_us_off:
                        us_off = va_plus2_to_us_off[va]
                        if us_off not in mapped:
                            j_va = match_lui_addiu_in_jp(l_idx, idx)
                            if j_va is not None:
                                j_off = jp_va_to_off(j_va - 2)
                                if j_off is not None:
                                    add_mapping(us_off, read_cstr(jp_elf, j_off))
                    elif 0x00879400 <= va < 0x00A91858:
                        t_off = us_va_to_off(va)
                        if t_off is not None and t_off % 4 == 0:
                            first_ptr = struct.unpack_from("<I", us_elf, t_off)[0]
                            if first_ptr in va_to_us_off:
                                j_va = match_lui_addiu_in_jp(l_idx, idx)
                                if j_va is not None:
                                    j_t_off = jp_va_to_off(j_va)
                                    if j_t_off is not None:
                                        ptr_table_matches.append((t_off, j_t_off))
            if rt in reg_lui and rt != rs:
                del reg_lui[rt]

    for u_t_off, j_t_off in ptr_table_matches:
        if u_t_off == 10032976:
            continue
        for k in range(64):
            if u_t_off + k * 4 >= len(us_elf) or j_t_off + k * 4 >= len(jp_elf):
                break
            u_ptr = struct.unpack_from("<I", us_elf, u_t_off + k * 4)[0]
            j_ptr = struct.unpack_from("<I", jp_elf, j_t_off + k * 4)[0]
            if u_ptr not in va_to_us_off:
                break
            j_s_off = jp_va_to_off(j_ptr)
            if j_s_off is None:
                break
            u_s_off = va_to_us_off[u_ptr]
            if u_s_off not in mapped:
                add_mapping(u_s_off, read_cstr(jp_elf, j_s_off))

    # 4. Exact verified counterparts for remaining sandwiched .rodata / .sdata / .data strings
    explicit_jp_offsets = {
        3204728: 3199992,   # 0123456789... character table
        9339456: 9507000,   # What is it? -> なんだろう?
        9510560: 8707936,   # Use Effect -> 使用効果
        9598256: 9658120,   # How to Play -> 遊び方
        9598288: 9658136,   # World Terminology -> 世界用語辞典
        9598592: 9663648,   # Lazy -> 一文字ずつ
        9634680: 9680864,   # Cosmosphere -> コスモスフィア
        9634704: 9680880,   # Costume -> コスチューム
        9634720: 9680896,   # Magic Reference -> 魔法図鑑
        9645632: 9937184,   # Sell -> 売る
        9651824: 9693512,   # Dive -> ダイブ
        9651840: 9693520,   # Recrystallize -> グラスノ再結晶化
        9662184: 9699560,   # What is it? -> なんだろう?
        9666944: 9704304,   # Total Price -> 合計金額
        9666968: 9704320,   # Total DP -> 合計DP
        9666992: 9937944,   # Leaf -> リーフ
        9672064: 9707688,   # Change Equipment -> 装備変更
        9672104: 9707704,   # Enhancements -> パワード
        9926408: 9832728,   # Grathnode Crystal -> グラスノ結晶
        10025496: 9929192,  # BGM -> BGM
        10025504: 9929200,  # SSE -> SSE
        10032984: 9663632,  # Bam -> いっぺんに
        10033000: 9936760,  # OFF -> OFF
        10033008: 9936768,  # ON -> ON
        10033560: 9937392,  # No -> いいえ
        10034120: 9937952,  # DP -> DP
    }
    for u_off, j_off in explicit_jp_offsets.items():
        if u_off in target_set and u_off not in mapped:
            add_mapping(u_off, read_cstr(jp_elf, j_off))

    # 5. US-exclusive voice language options (English / Japanese)
    for u_off, jp_label in ((8172136, "英語"), (9598552, "英語"), (9598568, "日本語")):
        if u_off in target_set and u_off not in mapped:
            add_mapping(u_off, jp_label)

    return {u_off: " / ".join(txts) for u_off, txts in mapped.items()}


def extract_japanese_dialogues(
    jp_iso_path: Path,
    us_iso_path: Path | None = None,
    slus_rows: list[tuple[str, int]] | None = None,
) -> dict[tuple[str, int], str]:
    print(f"Lendo ISO japonesa: {jp_iso_path.name}")
    files = list_files(jp_iso_path)
    slps_entry = next((f for f in files if f.path.upper().startswith("SLPS_")), None)
    if not slps_entry:
        raise FileNotFoundError("Nao foi possivel encontrar o executavel SLPS na ISO japonesa")

    rpk_entry = next((f for f in files if f.path.upper() == "RPK.BIN"), None)
    if not rpk_entry:
        raise FileNotFoundError("Nao foi possivel encontrar RPK.BIN na ISO japonesa")

    jp_elf_bytes = read_entry(jp_iso_path, slps_entry)
    with tempfile.NamedTemporaryFile(suffix=".elf", delete=False) as tmp:
        tmp.write(jp_elf_bytes)
        tmp_elf_path = Path(tmp.name)

    try:
        rpk_entries = rpk.read_index(tmp_elf_path, rpk_entry.size)
    finally:
        tmp_elf_path.unlink(missing_ok=True)

    evd_entries = {e.name: e for e in rpk_entries if e.name.endswith(".evd")}
    print(f"Indice RPK carregado: {len(rpk_entries)} recursos, {len(evd_entries)} arquivos EVD.")

    extracted: dict[tuple[str, int], str] = {}
    with jp_iso_path.open("rb") as fp:
        rpk_base_offset = rpk_entry.extent * SECTOR
        for name, entry in sorted(evd_entries.items()):
            fp.seek(rpk_base_offset + entry.offset)
            raw = fp.read(entry.size)
            parsed = evd.parse(raw)
            for d in parsed.dialogues:
                extracted[(name, d.index)] = d.text

    print(f"Total de dialogos de eventos (EVD) em japones extraidos: {len(extracted)}")

    if us_iso_path is not None and slus_rows:
        print(f"Mapeando textos de sistema/menus (SLUS_214.45 <-> {slps_entry.path})...")
        us_elf_bytes = read_entry(us_iso_path, find(us_iso_path, "SLUS_214.45"))
        target_offsets = [off for _, off in slus_rows]
        slus_map = build_slus_to_slps_map(us_elf_bytes, jp_elf_bytes, target_offsets)
        slus_count = 0
        for event_file, off in slus_rows:
            jp_txt = slus_map.get(off)
            if jp_txt is not None:
                extracted[(event_file, off)] = jp_txt
                slus_count += 1
        print(f"Total de textos de sistema/menus (SLUS/TEXT) mapeados: {slus_count}/{len(slus_rows)}")

    print(f"Total geral de textos em japones prontos para gravacao: {len(extracted)}")
    return extracted


def update_database_with_japanese(
    project_path: Path,
    dialogues_jp: dict[tuple[str, int], str],
    backup: bool = True,
) -> int:
    if not project_path.is_file():
        raise FileNotFoundError(f"Projeto nao encontrado: {project_path}")

    con = sqlite3.connect(project_path)
    try:
        check = con.execute("PRAGMA quick_check").fetchone()[0]
        if check != "ok":
            raise ValueError(f"PRAGMA quick_check falhou no projeto original: {check}")
    finally:
        con.close()

    if backup:
        backup_dir = ROOT / "backups"
        backup_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{project_path.stem}_backup_antes_jp_{timestamp}{project_path.suffix}"
        backup_target = backup_dir / backup_name
        shutil.copy2(project_path, backup_target)
        print(f"Backup consistente criado em: {backup_target}")

    con = sqlite3.connect(project_path)
    con.row_factory = sqlite3.Row
    try:
        columns = [row["name"] for row in con.execute("PRAGMA table_info(dialogues)")]
        if "original_jp" not in columns:
            print("Adicionando coluna 'original_jp' na tabela 'dialogues'...")
            con.execute("ALTER TABLE dialogues ADD COLUMN original_jp TEXT")

        print("Atualizando registros com o texto original em japones...")
        params = [
            (jp_text, event_file, entry_index)
            for (event_file, entry_index), jp_text in dialogues_jp.items()
        ]
        cur = con.cursor()
        cur.executemany(
            "UPDATE dialogues SET original_jp=? WHERE event_file=? AND entry_index=?",
            params,
        )
        con.commit()

        check = con.execute("PRAGMA quick_check").fetchone()[0]
        if check != "ok":
            raise ValueError(f"PRAGMA quick_check falhou apos atualizacao: {check}")

        populated = con.execute(
            "SELECT count(*) FROM dialogues WHERE original_jp IS NOT NULL"
        ).fetchone()[0]
        evd_pop = con.execute(
            "SELECT count(*) FROM dialogues WHERE event_file LIKE 'Event/%' AND original_jp IS NOT NULL"
        ).fetchone()[0]
        slus_pop = con.execute(
            "SELECT count(*) FROM dialogues WHERE event_file LIKE 'SLUS/TEXT/%' AND original_jp IS NOT NULL"
        ).fetchone()[0]
        print(
            f"Concluido com sucesso: {populated} registros com original_jp preenchido "
            f"(Event: {evd_pop}, SLUS/TEXT: {slus_pop})."
        )
        return populated
    finally:
        con.close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--jp-iso",
        type=Path,
        default=None,
        help="Caminho para a ISO japonesa (se omitido, procura automaticamente no diretorio pai)",
    )
    parser.add_argument(
        "--us-iso",
        type=Path,
        default=None,
        help="Caminho para a ISO americana/undub (se omitido, procura automaticamente no diretorio pai)",
    )
    parser.add_argument(
        "--project",
        type=Path,
        default=ROOT / "release" / "ArTonelico_PTBR_adaptado_108_20260926.atproj",
        help="Caminho para o projeto .atproj a atualizar",
    )
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Nao criar backup antes de atualizar o banco",
    )
    args = parser.parse_args()

    candidates = list((ROOT.parent).glob("*.iso")) + list(ROOT.glob("*.iso"))
    jp_iso = args.jp_iso or find_japanese_iso(candidates)
    if not jp_iso:
        raise FileNotFoundError(
            "Nao foi possivel localizar automaticamente a ISO japonesa. Informe com --jp-iso <caminho>."
        )
    us_iso = args.us_iso or find_us_iso(candidates)

    con = sqlite3.connect(args.project)
    try:
        slus_rows = con.execute(
            "SELECT event_file, entry_index FROM dialogues WHERE event_file LIKE 'SLUS/TEXT/%' ORDER BY entry_index"
        ).fetchall()
    finally:
        con.close()

    print(f"ISO japonesa: {jp_iso}")
    if us_iso:
        print(f"ISO americana: {us_iso}")
    print(f"Projeto alvo: {args.project}")

    dialogues_jp = extract_japanese_dialogues(jp_iso, us_iso_path=us_iso, slus_rows=slus_rows)
    update_database_with_japanese(
        args.project, dialogues_jp, backup=not args.no_backup
    )


if __name__ == "__main__":
    main()
