import json
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")

# 1. Atualizar scene_breakdown_ledger.json
ledger_path = BASE_DIR / "curadoria_editorial" / "scene_breakdown_ledger.json"
with open(ledger_path, "r", encoding="utf-8") as f:
    ledger = json.load(f)

for b in ledger.get("blocks", []):
    if b.get("block_id") == "BLK_SYS_018":
        b["status"] = "concluido"
        b["completed_at"] = datetime.now(timezone.utc).isoformat()
        b["lines_rewritten"] = 258
        b["lines_approved_as_is"] = 30
        break

with open(ledger_path, "w", encoding="utf-8") as f:
    json.dump(ledger, f, ensure_ascii=False, indent=2)

print("[OK] scene_breakdown_ledger.json atualizado com sucesso!")

# 2. Atualizar glossario_mestre.json
glossary_path = BASE_DIR / "curadoria_editorial" / "glossario_mestre.json"
with open(glossary_path, "r", encoding="utf-8") as f:
    glossary = json.load(f)

terms = glossary.get("terms", {})

new_terms_dict = {
    "Tranquility": {
        "pt": "Tranquilidade",
        "gender": "feminino",
        "number": "singular",
        "category": "Item / Suporte",
        "note": "トランキリティ. Remédio calmante / item tático consumível de Grathmeld usado em combate para restaurar e estabilizar o canto das Reyvateils."
    },
    "Natural Ice": {
        "pt": "Sorvete Natural",
        "gender": "masculino",
        "number": "singular",
        "category": "Grathmeld / Culinária",
        "note": "大自然アイス. Item culinário refrescante criado por Misha via síntese Grathmeld."
    },
    "Capri Soda": {
        "pt": "Soda Capri",
        "gender": "feminino",
        "number": "singular",
        "category": "Grathmeld / Culinária",
        "note": "カプリソーダ. Bebida gaseificada criada por Misha via síntese Grathmeld, cujo sabor é elogiado apesar dos ingredientes peculiares."
    },
    "First Era": {
        "pt": "Primeira Era",
        "gender": "feminino",
        "number": "singular",
        "category": "Lore / Cronologia",
        "note": "第一紀. A era primordial da civilização de Sol Ciel antes da Primeira Calamidade, quando Shurelia convivia com sua figura paterna / criador."
    },
    "Second Era": {
        "pt": "Segunda Era",
        "gender": "feminino",
        "number": "singular",
        "category": "Lore / Cronologia",
        "note": "第二紀. A era de reconstrução pós-primeira catástrofe com companheiros valorosos, encerrada pela traição humana e pela Grande Calamidade (Second Disaster)."
    },
    "Third Era": {
        "pt": "Terceira Era",
        "gender": "feminino",
        "number": "singular",
        "category": "Lore / Cronologia",
        "note": "第三紀. A era atual de isolamento de Sol Ciel, na qual Shurelia viveu centenas de anos em reclusão burocrática e solidão absoluta na Torre."
    }
}

for k, v in new_terms_dict.items():
    if k not in terms:
        terms[k] = v

glossary["terms"] = terms

handoff_final = {
    "last_scene_id": "BLK_SYS_018",
    "last_line_id": 25513,
    "location_and_situation": "Núcleo Sistêmico Parte 18 (SLUS/TEXT/0211 a 0222: Tópicos de acampamento com Aurica sobre massagem e cristais Grathnode em 0211-0213; Tópicos de acampamento com Misha sobre itens de batalha como Tranquilidade e receitas de Grathmeld como Sorvete Natural e Soda Capri em 0213-0217; Tópicos com Shurelia sobre parcerias táticas, bico aristocrático ao cair em combate e seu despertar em 0217-0221; e o Ponto Culminante da Confissão da Solidão de Shurelia em 0222 sob a luz da noite) concluído com 100% de maestria editorial e ZERO estouros de buffer.",
    "emotional_state": "Intimidade, Cuidado Mútuo, Comédia Gastronômica, Soberania Solene e Confissão Romântica / Aurica tímida oferecendo massagem, Misha brincalhona defendendo seus pratos exóticos de Grathmeld e exigindo proteção no canto, Shurelia cobrando postura com bico régio e, no clímax noturno, despindo séculos de solidão e traumas das Três Eras de Sol Ciel para chorar e pedir a proximidade de Lyner como amiga e algo a mais.",
    "active_hooks": [
        "Conclusão integral do bloco BLK_SYS_018. Seguir para o próximo bloco temático BLK_SYS_019 conforme o Scene Breakdown Ledger."
    ]
}

glossary["last_scene_handoff"] = handoff_final

with open(glossary_path, "w", encoding="utf-8") as f:
    json.dump(glossary, f, ensure_ascii=False, indent=2)

print("[OK] glossario_mestre.json atualizado com sucesso com novos termos e handoff!")
