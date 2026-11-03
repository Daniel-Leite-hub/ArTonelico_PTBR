"""Extração do Dossiê Ativo da Cena (Scene Spotlight) para Curadoria Editorial
Cruza o bloco decupado no scene_breakdown_ledger.json com o glossario_mestre.json
e extrai falas com contexto read-only e Tríade de Idiomas (JP Soberano + EN Crítico -> PT-BR).
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
CURADORIA_DIR = BASE_DIR / "curadoria_editorial"
LEDGER_PATH = CURADORIA_DIR / "scene_breakdown_ledger.json"
GLOSSARIO_PATH = CURADORIA_DIR / "glossario_mestre.json"
CONFIG_PATH = CURADORIA_DIR / "curadoria_config.json"
BLOCOS_DIR = CURADORIA_DIR / "blocos"

# Mapeamento canônico de speaker_id para nome
SPEAKER_NAMES = {
    1: "Lyner",
    2: "Aurica",
    3: "Misha",
    4: "Jack",
    5: "Krusche",
    6: "Radolf",
    7: "Ayatane",
    8: "Claire",
    9: "Shurelia",
    10: "Leard",
    12: "Vendedora de Doces (Porto Gaivota)",
    13: "Bourd / Guarda da Porta A5",
    14: "Operador de Portão",
    15: "Atendente do Dive Shop",
    16: "Bispo Falss",
    17: "Oficial da Igreja",
    18: "Soldado / Sentinela",
    19: "Hama",
    20: "Tastiella",
    48: "Pombad",
    50: "Sistema / Caixa Narrativa / Tutorial",
    53: "Don Leon (Donsuke)",
    54: "Moradora do Mundo Inferior",
    55: "Guarda / Viajante",
    70: "Cientista / Pesquisador",
    91: "Atendente de Loja",
    113: "Criança da Igreja",
    118: "Cidadão de Karff",
    119: "Esposa de Karff",
    123: "Jovem de Karff",
    128: "Reyvateil da Cosmosfera",
    129: "Amiga de Infância da Cosmosfera",
    130: "Espírito da Flor",
    132: "Lyner (Voz Interior / Memória na Cosmosfera)",
    133: "Estudante da Cosmosfera",
    147: "Guia da Cosmosfera"
}


def get_speaker_name(speaker_id: int) -> str:
    return SPEAKER_NAMES.get(speaker_id, f"Personagem [{speaker_id}]" if speaker_id > 0 else "Sistema / Narração")


def build_spotlight(block_id: str) -> dict:
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)
    with open(GLOSSARIO_PATH, "r", encoding="utf-8") as f:
        glossario = json.load(f)
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)

    # Localizar bloco
    block_info = next((b for b in ledger["blocks"] if b["block_id"] == block_id), None)
    if not block_info:
        raise ValueError(f"Bloco {block_id} não encontrado no ledger!")

    db_path = Path(config["database_path"])
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    # 1. Extrair Lead-in Context (10-15 falas anteriores read-only)
    lead_in = []
    if block_info.get("lead_in_range"):
        l_start, l_end = block_info["lead_in_range"]
        c.execute("""
            SELECT id, event_file, speaker_id, original, original_jp, automatic, reviewed
            FROM dialogues
            WHERE id BETWEEN ? AND ?
            ORDER BY id
        """, (l_start, l_end))
        for r in c.fetchall():
            lead_in.append({
                "id": r["id"],
                "event_file": r["event_file"],
                "speaker": get_speaker_name(r["speaker_id"]),
                "speaker_id": r["speaker_id"],
                "original_jp": r["original_jp"] or "",
                "original_en": r["original"],
                "text_ptbr": r["reviewed"] or r["automatic"] or ""
            })

    # 2. Extrair Falas do Bloco
    b_start = block_info["id_start"]
    b_end = block_info["id_end"]
    c.execute("""
        SELECT id, event_file, speaker_id, original, original_jp, automatic, reviewed, review_status
        FROM dialogues
        WHERE id BETWEEN ? AND ?
        ORDER BY id
    """, (b_start, b_end))
    dialogues = []
    block_speakers = set()
    block_full_text = []

    for r in c.fetchall():
        spk_name = get_speaker_name(r["speaker_id"])
        block_speakers.add((r["speaker_id"], spk_name))
        
        orig_en = r["original"]
        orig_jp = r["original_jp"] or ""
        pt_curr = r["reviewed"] or r["automatic"] or ""
        
        dialogues.append({
            "id": r["id"],
            "event_file": r["event_file"],
            "speaker_id": r["speaker_id"],
            "speaker": spk_name,
            "original_jp": orig_jp,
            "original_en": orig_en,
            "current_ptbr": pt_curr,
            "review_status": r["review_status"]
        })
        block_full_text.append(orig_en)
        if orig_jp:
            block_full_text.append(orig_jp)

    conn.close()

    full_text_blob = " ".join(block_full_text).lower()

    # 3. Varredura do Glossário Mestre para Matched Terms
    matched_terms = {}
    for term, data in glossario.get("terms", {}).items():
        # Busca por termos em inglês ou português no texto
        pt_val = data.get("pt") or data.get("term_pt") or data.get("term_ptbr") or ""
        if term.lower() in full_text_blob or pt_val.lower() in full_text_blob:
            matched_terms[term] = data

    # 4. Elenco Ativo em Cena (Active Cast)
    active_cast = {}
    for spk_id, spk_name in block_speakers:
        # Se temos ficha no glossário
        for char_key, char_data in glossario.get("characters", {}).items():
            if char_data.get("id") == spk_id or char_key.lower() in spk_name.lower():
                active_cast[char_key] = char_data

    spotlight = {
        "block_id": block_id,
        "axis_id": block_info["axis_id"],
        "axis_name": block_info["axis_name"],
        "category": block_info["category"],
        "line_count": len(dialogues),
        "id_range": [b_start, b_end],
        "scene_handoff_received": glossario.get("last_scene_handoff", {}),
        "active_cast": active_cast,
        "matched_terms": matched_terms,
        "lead_in_context_read_only": lead_in,
        "dialogues": dialogues
    }

    output_path = BLOCOS_DIR / f"{block_id}_input.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(spotlight, f, ensure_ascii=False, indent=2)

    print(f"Spotlight gerado com sucesso: {output_path}")
    print(f"  Falas no bloco: {len(dialogues)} (IDs {b_start}..{b_end})")
    print(f"  Falas de lead-in: {len(lead_in)}")
    print(f"  Personagens em cena: {len(active_cast)}")
    print(f"  Termos casados do glossário: {len(matched_terms)}")
    return spotlight


def main():
    parser = argparse.ArgumentParser(description="Extrai Dossiê Ativo da Cena (Scene Spotlight) para Curadoria.")
    parser.add_argument("block_id", help="ID do bloco (ex.: BLK_SYS_001 ou BLK_EVD_001)")
    args = parser.parse_args()
    build_spotlight(args.block_id)


if __name__ == "__main__":
    main()
