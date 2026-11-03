"""Validador Técnico Determinístico (Hard Gate Fail-Fast) para Curadoria Editorial
Implementa as 7 Travas Técnicas de Integridade Canônica conforme curadoria-editorial-game-localization v4.1.0.
Verifica tags, variáveis, quebras de linha, fraturas sintáticas, rubricas proibidas e balanceamento.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


# Padrões de tags e variáveis comuns em Ar tonelico
RE_TAG_BRACKETS = re.compile(r"\[[0-9A-Fa-f]{4}\]")
RE_TAG_AT = re.compile(r"＠[0-9A-Fa-f]{6}#[0-9A-Fa-f]{2}")
RE_VARIABLES = re.compile(r"(%[sSdD]|%[0-9]+[sSdD]|{[0-9]+}|{[a-zA-Z0-9_]+})")
RE_IMAGE_TAGS = re.compile(r"IM[0-9]{2}")

# Rubricas proibidas (decalques teatrais)
FORBIDDEN_STAGE_DIRECTIONS = [
    re.compile(r"\*suspiro\*", re.IGNORECASE),
    re.compile(r"\(suspira\)", re.IGNORECASE),
    re.compile(r"\*risos?\*", re.IGNORECASE),
    re.compile(r"\(risos?\)", re.IGNORECASE),
    re.compile(r"\*sorriso\*", re.IGNORECASE),
    re.compile(r"\(sorri\)", re.IGNORECASE),
    re.compile(r"\*gasp\*", re.IGNORECASE),
    re.compile(r"\*sigh\*", re.IGNORECASE),
    re.compile(r"\*chuckle\*", re.IGNORECASE),
    re.compile(r"\*groan\*", re.IGNORECASE)
]

# Fraturas sintáticas em quebras de linha (\n)
FRACTURE_ARTICLES = re.compile(r"\b(o|a|os|as|um|uma|uns|umas)\s*\n", re.IGNORECASE)
FRACTURE_PREPOSITIONS = re.compile(r"\b(de|da|do|das|dos|em|na|no|nas|nos|por|com|sob|sobre)\s*\n", re.IGNORECASE)
FRACTURE_ORPHAN_PUNCTUATION = re.compile(r"\n\s*[,.:;?!]")


def validate_line(dialogue_id: int, original_en: str, translation_pt: str) -> list[str]:
    errors = []

    # 1. Rubricas teatrais proibidas
    for pattern in FORBIDDEN_STAGE_DIRECTIONS:
        if pattern.search(translation_pt):
            errors.append(f"Rubrica teatral proibida detectada: '{pattern.pattern}'")

    # 2. Paridade de variáveis
    orig_vars = sorted(RE_VARIABLES.findall(original_en))
    trans_vars = sorted(RE_VARIABLES.findall(translation_pt))
    if orig_vars != trans_vars:
        errors.append(f"Divergência de variáveis: original={orig_vars} vs tradução={trans_vars}")

    # 3. Paridade de tags especiais [00XX] e ＠
    orig_brackets = sorted(RE_TAG_BRACKETS.findall(original_en))
    trans_brackets = sorted(RE_TAG_BRACKETS.findall(translation_pt))
    if orig_brackets != trans_brackets:
        errors.append(f"Divergência de tags [00XX]: original={orig_brackets} vs tradução={trans_brackets}")

    orig_ats = sorted(RE_TAG_AT.findall(original_en))
    trans_ats = sorted(RE_TAG_AT.findall(translation_pt))
    if orig_ats != trans_ats:
        errors.append(f"Divergência de marcadores ＠: original={orig_ats} vs tradução={trans_ats}")

    # Paridade de tags de botão/imagem (IM00, IM01, etc.)
    orig_im = sorted(RE_IMAGE_TAGS.findall(original_en))
    trans_im = sorted(RE_IMAGE_TAGS.findall(translation_pt))
    if orig_im != trans_im:
        errors.append(f"Divergência de tags IM##: original={orig_im} vs tradução={trans_im}")

    # 4. Proibição de quebras de linha (\n ou \r) no motor do PS2
    if "\n" in translation_pt or "\r" in translation_pt:
        errors.append("Quebra de linha (\\n ou \\r) proibida no motor do PS2 (use texto corrido com espaços)")

    # 5. Balanceamento de aspas e parênteses
    # Aspas duplas normais
    if translation_pt.count('"') % 2 != 0:
        errors.append("Aspas duplas retas (\") desbalanceadas (número ímpar)")
    # Parênteses
    if translation_pt.count('(') != translation_pt.count(')'):
        errors.append("Parênteses () desbalanceados")
    # Colchetes
    if translation_pt.count('[') != translation_pt.count(']'):
        errors.append("Colchetes [] desbalanceados")

    return errors


def validate_batch(batch_data: dict) -> tuple[bool, dict[int, list[str]]]:
    all_errors = {}
    dialogues = batch_data.get("dialogues") or batch_data.get("curated_lines", [])
    if not dialogues:
        return False, {-1: ["Bloco não contém falas para validação (dialogues/curated_lines vazios ou ausentes)"]}

    for d in dialogues:
        d_id = d.get("id")
        orig_en = d.get("original_en", "")
        # Usa o texto curado final proposto ou current_ptbr / texto_ptbr_curado
        trans_pt = d.get("curated_ptbr") or d.get("texto_ptbr_curado") or d.get("current_ptbr") or ""
        
        errs = validate_line(d_id, orig_en, trans_pt)
        if errs:
            all_errors[d_id] = errs

    is_valid = len(all_errors) == 0
    return is_valid, all_errors


def main():
    parser = argparse.ArgumentParser(description="Valida integridade técnica de bloco de curadoria.")
    parser.add_argument("file_path", help="Caminho do arquivo JSON do bloco (input ou output)")
    args = parser.parse_args()

    path = Path(args.file_path)
    if not path.exists():
        print(f"Erro: Arquivo {path} não existe.")
        return

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    is_valid, errors = validate_batch(data)
    if is_valid:
        print(f"[OK] Bloco {data.get('block_id', path.stem)} passou 100% no Hard Gate Técnico!")
    else:
        print(f"[FALHA] Bloco {data.get('block_id', path.stem)} contém {len(errors)} falhas técnicas:")
        for d_id, err_list in sorted(errors.items())[:15]:
            print(f"  ID {d_id}:")
            for err in err_list:
                print(f"    - {err}")
        if len(errors) > 15:
            print(f"  ... e mais {len(errors) - 15} erros omitidos.")


if __name__ == "__main__":
    main()
