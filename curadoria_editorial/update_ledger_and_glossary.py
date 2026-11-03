import json
from datetime import datetime, timezone

# 1. Atualizar scene_breakdown_ledger.json
ledger_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\scene_breakdown_ledger.json"
with open(ledger_path, "r", encoding="utf-8") as f:
    ledger = json.load(f)

for b in ledger.get("blocks", []):
    if b.get("block_id") == "BLK_SYS_015":
        b["status"] = "concluido"
        b["completed_at"] = datetime.now(timezone.utc).isoformat()
        b["lines_rewritten"] = 181
        b["lines_approved_as_is"] = 118
        break

with open(ledger_path, "w", encoding="utf-8") as f:
    json.dump(ledger, f, ensure_ascii=False, indent=2)

print("[OK] scene_breakdown_ledger.json atualizado com sucesso!")

# 2. Atualizar glossario_mestre.json
glossary_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json"
with open(glossary_path, "r", encoding="utf-8") as f:
    glossary = json.load(f)

terms = glossary.get("terms", {})

if "Mind Guardian" not in terms:
    terms["Mind Guardian"] = {
        "pt": "Guardião da Mente",
        "gender": "masculino",
        "number": "singular",
        "category": "Cosmosphere / Lore",
        "note": "Entidade gerada pelo subconsciente da Reyvateil para zelar por seus traumas e memórias na Cosmosfera (em Aurica, encarnado como Don Leon, seu bichinho de pelúcia da infância)."
    }

if "Neko-go" not in terms:
    terms["Neko-go"] = {
        "pt": "miauês / língua dos gatos",
        "gender": "masculino",
        "number": "singular",
        "category": "Cultura Pop / Traço de Personagem",
        "note": "ねこ語. Habilidade excêntrica e carinhosa de Aurica, fanática por felinos a ponto de miar e conversar com gatos nas estalagens."
    }

if "Menkui" not in terms:
    terms["Menkui"] = {
        "pt": "gostar de galãs / só querer homens bonitos",
        "gender": "neutro",
        "number": "singular",
        "category": "Expressão Idiomática / Comédia",
        "note": "面食い. Atração exclusiva por beleza facial masculina. Don Leon alega isso como piada/defesa para afastar Lyner de Aurica."
    }

glossary["terms"] = terms

with open(glossary_path, "w", encoding="utf-8") as f:
    json.dump(glossary, f, ensure_ascii=False, indent=2)

print("[OK] glossario_mestre.json atualizado com sucesso!")
