from __future__ import annotations

import csv
import json
from pathlib import Path

from .portuguese_font import ACCENT_TO_ALIAS
from .project import get_meta, save_text, text_digest


CSV_COLUMNS = (
    "arquivo", "id", "ingles", "resposta_automatica", "traducao_em_edicao",
    "situacao", "texto_final", "estado_revisao", "origem_revisao", "revisado_em",
    "hash_revisado", "bytes_original", "bytes_atual", "provedor", "erro",
)


def _status(row) -> str:
    if row["locked"]:
        return "protegido"
    if not (row["automatic"].strip() or row["translation"].strip() or row["reviewed"].strip()):
        return "pendente"
    if row["error"]:
        return "erro"
    if not row["size_ok"]:
        return "acima_dos_bytes"
    return "certo"


def export_project_reports(db, project_path: Path, output_dir: Path) -> dict[str, Path | int]:
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = list(db.execute("SELECT * FROM dialogues ORDER BY id"))
    csv_path = output_dir / "Traducao_PTBR.csv"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow({
                "arquivo": row["event_file"], "id": row["entry_index"], "ingles": row["original"],
                "resposta_automatica": row["automatic"], "traducao_em_edicao": row["translation"],
                "situacao": _status(row), "texto_final": row["reviewed"],
                "estado_revisao": row["review_status"], "origem_revisao": row["review_origin"],
                "revisado_em": row["reviewed_at"], "hash_revisado": row["reviewed_hash"],
                "bytes_original": row["original_bytes"], "bytes_atual": row["translated_bytes"],
                "provedor": row["provider"], "erro": row["error"],
            })

    reviewed = []
    review_drafts = []
    oversized = []
    for row in rows:
        record = {
            "arquivo": row["event_file"], "id": row["entry_index"], "ingles": row["original"],
            "resposta_automatica": row["automatic"], "traducao_em_edicao": row["translation"],
            "texto_final": row["reviewed"], "estado_revisao": row["review_status"],
            "origem_revisao": row["review_origin"], "revisado_em": row["reviewed_at"],
            "bytes_original": row["original_bytes"], "bytes_atual": row["translated_bytes"],
            "situacao": _status(row), "erro": row["error"],
        }
        if row["reviewed"].strip() and row["review_status"] == "approved":
            reviewed.append(record)
        elif row["reviewed"].strip():
            review_drafts.append(record)
        if not row["size_ok"] and not row["error"] and (row["automatic"].strip() or row["translation"].strip() or row["reviewed"].strip()):
            oversized.append({**record, "excesso": row["translated_bytes"] - row["original_bytes"]})

    review_path = output_dir / "relatorio_revisao.json"
    review_path.write_text(json.dumps(reviewed, ensure_ascii=False, indent=2), encoding="utf-8")
    drafts_path = output_dir / "relatorio_revisoes_pendentes.json"
    drafts_path.write_text(json.dumps(review_drafts, ensure_ascii=False, indent=2), encoding="utf-8")
    oversized_path = output_dir / "relatorio_bytes_excedentes.json"
    oversized_path.write_text(json.dumps(oversized, ensure_ascii=False, indent=2), encoding="utf-8")
    font_path = output_dir / "manifesto_fonte_portugues.json"
    font_path.write_text(json.dumps({
        "formato": 1,
        "jogo": "Ar tonelico: Melody of Elemia (SLUS-214.45)",
        "metodo": "aliases ASCII no atlas FO_HGGBP ativados por marcadores locais #1",
        "mapeamento": {character: alias for character, alias in ACCENT_TO_ALIAS.items()},
        "projeto": str(project_path.resolve()),
        "iso_tamanho": get_meta(db, "iso_size"),
        "executavel_sha256": get_meta(db, "executable_sha256"),
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    return {
        "csv": csv_path, "review": review_path, "review_drafts": drafts_path,
        "oversized": oversized_path,
        "font": font_path, "rows": len(rows), "reviewed": len(reviewed),
        "review_drafts_count": len(review_drafts),
        "oversized_count": len(oversized),
    }


def import_project_csv(db, csv_path: Path) -> dict[str, int]:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        required = {"arquivo", "id", "traducao_em_edicao", "texto_final"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError(
                "CSV incompatível: faltam arquivo, id, traducao_em_edicao ou texto_final"
            )
        incoming = list(reader)

    prepared = []
    for line_number, item in enumerate(incoming, 2):
        try:
            entry_index = int(item["id"])
        except (TypeError, ValueError) as exc:
            raise ValueError(f"ID inválido na linha {line_number}") from exc
        row = db.execute(
            "SELECT id FROM dialogues WHERE event_file=? AND entry_index=?",
            (item["arquivo"], entry_index),
        ).fetchone()
        if row is None:
            raise ValueError(
                f"Entrada desconhecida na linha {line_number}: {item['arquivo']}:{entry_index}"
            )
        prepared.append((row["id"], item))

    approved = 0
    drafts = 0
    for row_id, item in prepared:
        translation = item.get("traducao_em_edicao", "")
        reviewed = item.get("texto_final", "")
        save_text(db, row_id, translation, reviewed, commit=False)
        wants_approved = item.get("estado_revisao", "") == "approved"
        supplied_hash = item.get("hash_revisado", "")
        if reviewed.strip() and wants_approved and supplied_hash == text_digest(reviewed):
            db.execute(
                "UPDATE dialogues SET review_status='approved',review_origin=?,reviewed_at=?,"
                "reviewed_hash=? WHERE id=?",
                ("importado", item.get("revisado_em", ""), supplied_hash, row_id),
            )
            approved += 1
        elif reviewed.strip():
            drafts += 1
    db.commit()
    return {"updated": len(prepared), "approved": approved, "drafts": drafts}
