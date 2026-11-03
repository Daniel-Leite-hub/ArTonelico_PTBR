"""Aplicador Transacional de Bloco Curado para o Banco do Projeto SQLite (.atproj)
Aplica validação Fail-Fast (curadoria_validate), cria backup de segurança,
persiste linhas revisadas/aprovadas, atualiza o Glossário Mestre e o Scene Breakdown Ledger.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from curadoria_validate import validate_batch

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
CURADORIA_DIR = BASE_DIR / "curadoria_editorial"
LEDGER_PATH = CURADORIA_DIR / "scene_breakdown_ledger.json"
GLOSSARIO_PATH = CURADORIA_DIR / "glossario_mestre.json"
CONFIG_PATH = CURADORIA_DIR / "curadoria_config.json"
BLOCOS_DIR = CURADORIA_DIR / "blocos"
BACKUPS_DIR = BASE_DIR / "backups" / "curadoria"
BACKUPS_DIR.mkdir(parents=True, exist_ok=True)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def apply_block(output_path: Path) -> dict:
    with open(output_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    block_id = data.get("block_id")
    if not block_id:
        raise ValueError("Bloco sem 'block_id' identificado!")

    # 1. Hard Gate Determinístico (Validação Fail-Fast)
    is_valid, errors = validate_batch(data)
    if not is_valid:
        error_summary = []
        for d_id, err_list in sorted(errors.items())[:10]:
            error_summary.append(f"ID {d_id}: " + "; ".join(err_list))
        raise ValueError(f"FALHA NO HARD GATE TÉCNICO ({len(errors)} erros):\n" + "\n".join(error_summary))

    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)
    db_path = Path(config["database_path"])

    # 2. Backup de Segurança Transacional
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = BACKUPS_DIR / f"ArTonelico_backup_pre_{block_id}_{timestamp}.atproj"
    source_db = sqlite3.connect(db_path)
    backup_db = sqlite3.connect(backup_file)
    try:
        source_db.backup(backup_db)
    finally:
        backup_db.close()
        source_db.close()
    print(f"[1/5] Backup de segurança criado: {backup_file.name}")

    # 3. Transação no SQLite
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    now_iso = datetime.now(timezone.utc).isoformat()
    lines_rewritten = 0
    lines_approved_as_is = 0

    dialogues = data.get("dialogues") or data.get("curated_lines", [])
    if not dialogues:
        print("[ERRO] Nenhuma fala encontrada em 'dialogues' ou 'curated_lines'. Abortando aplicação.")
        conn.close()
        return

    for d in dialogues:
        d_id = d["id"]
        curated_text = d.get("curated_ptbr") or d.get("texto_ptbr_curado") or d.get("current_ptbr") or ""
        
        # Puxar texto existente no banco
        c.execute("SELECT automatic, reviewed FROM dialogues WHERE id = ?", (d_id,))
        row = c.fetchone()
        if not row:
            continue
        old_auto, old_rev = row[0], row[1]
        
        digest = sha256_text(curated_text)
        
        if curated_text != (old_rev or old_auto):
            # Linha lapidada / reescrita
            c.execute("""
                UPDATE dialogues
                SET reviewed = ?,
                    automatic = ?,
                    review_status = 'approved',
                    review_origin = 'curadoria_editorial',
                    reviewed_at = ?,
                    reviewed_hash = ?
                WHERE id = ?
            """, (curated_text, curated_text, now_iso, digest, d_id))
            lines_rewritten += 1
        else:
            # Linha aprovada como excelente
            c.execute("""
                UPDATE dialogues
                SET reviewed = ?,
                    review_status = 'approved',
                    review_origin = 'curadoria_editorial',
                    reviewed_at = ?,
                    reviewed_hash = ?
                WHERE id = ?
            """, (curated_text, now_iso, digest, d_id))
            lines_approved_as_is += 1

    conn.commit()
    conn.close()
    print(f"[2/5] Banco atualizado: {lines_rewritten} linhas reescritas, {lines_approved_as_is} linhas aprovadas (Total: {len(dialogues)}).")

    # 4. Atualizar Glossário Mestre no Disco
    with open(GLOSSARIO_PATH, "r", encoding="utf-8") as f:
        glossario = json.load(f)

    # Inserir novos termos descobertos
    new_terms_added = 0
    raw_new_terms = data.get("new_terms", {})
    if isinstance(raw_new_terms, dict):
        for term, term_data in raw_new_terms.items():
            if term not in glossario.get("terms", {}):
                glossario.setdefault("terms", {})[term] = term_data
                new_terms_added += 1
    elif isinstance(raw_new_terms, list):
        for t in raw_new_terms:
            if isinstance(t, dict):
                term_key = t.get("term_en") or t.get("term_jp") or t.get("term_ptbr")
                if term_key and term_key not in glossario.get("terms", {}):
                    glossario.setdefault("terms", {})[term_key] = {
                        "pt": t.get("term_ptbr") or t.get("term_pt") or t.get("pt") or "",
                        "category": t.get("category", "Geral"),
                        "note": t.get("rationale") or t.get("note") or ""
                    }
                    new_terms_added += 1

    # Atualizar matriz de tratamento
    for char_key, updates in data.get("updated_address_matrix", {}).items():
        if char_key in glossario.get("characters", {}):
            glossario["characters"][char_key].setdefault("address_matrix", {}).update(updates)

    # Gravar Scene Handoff
    new_handoff = data.get("scene_handoff_final") or data.get("scene_handoff")
    if new_handoff:
        glossario["last_scene_handoff"] = new_handoff

    with open(GLOSSARIO_PATH, "w", encoding="utf-8") as f:
        json.dump(glossario, f, ensure_ascii=False, indent=2)
    print(f"[3/5] Glossário Mestre atualizado ({new_terms_added} novos termos; Scene Handoff gravado).")

    # 5. Atualizar Scene Breakdown Ledger
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    for b in ledger["blocks"]:
        if b["block_id"] == block_id:
            b["status"] = "concluido"
            b["completed_at"] = now_iso
            b["lines_rewritten"] = lines_rewritten
            b["lines_approved_as_is"] = lines_approved_as_is

    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, ensure_ascii=False, indent=2)
    print(f"[4/5] Scene Breakdown Ledger atualizado: {block_id} marcado como 'concluido'.")

    # 6. Relatório Executivo do Bloco
    report = {
        "block_id": block_id,
        "completed_at": now_iso,
        "backup_created": str(backup_file),
        "total_dialogues": len(dialogues),
        "lines_rewritten": lines_rewritten,
        "lines_approved_as_is": lines_approved_as_is,
        "new_terms_added": new_terms_added,
        "scene_handoff": new_handoff,
        "highlights": data.get("highlights", [])
    }
    report_file = BLOCOS_DIR / f"{block_id}_report.json"
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(f"[5/5] Relatório executivo gravado: {report_file.name}")

    return report


def main():
    parser = argparse.ArgumentParser(description="Aplica bloco de curadoria no banco SQLite e atualiza o projeto.")
    parser.add_argument("output_path", help="Caminho do arquivo JSON de saída curado (ex.: BLK_SYS_001_output.json)")
    args = parser.parse_args()

    path = Path(args.output_path)
    if not path.exists():
        print(f"Erro: Arquivo {path} não encontrado.")
        return

    report = apply_block(path)
    print(f"\n[SUCESSO] Bloco {report['block_id']} aplicado com total integridade e segurança!")


if __name__ == "__main__":
    main()
