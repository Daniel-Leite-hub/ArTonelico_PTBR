import json

glossary_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_015_output.json"

with open(glossary_path, "r", encoding="utf-8") as f:
    glossary = json.load(f)

with open(output_path, "r", encoding="utf-8") as f:
    out_data = json.load(f)

# Update last_scene_handoff
glossary["last_scene_handoff"] = out_data["scene_handoff"]

# Add new terms
new_terms = {
    "Binary Field": {
        "pt": "Campo Binário",
        "gender": "masculino",
        "number": "singular",
        "category": "Cosmosphere / Tecnologia",
        "note": "Dimensão de fônica e dados da Torre habitada por Shurelia e vírus além da porta mental das Reyvateils (JP バイナリ野)."
    },
    "A1 Dividing Gate": {
        "pt": "Anteparo A1",
        "gender": "masculino",
        "number": "singular",
        "category": "Militar / Torre",
        "note": "Porta de alta segurança de contenção da Torre operada por Espectro FFT e Hymmnos (JP A1隔壁)."
    },
    "Topology Ribbon": {
        "pt": "Fita de Topologia",
        "gender": "feminino",
        "number": "singular",
        "category": "Acessório / Síntese",
        "note": "Acessório criado por Shurelia que aprimora o poder de Reyvateils e a velocidade de Burst (JP トポロジーリボン)."
    },
    "Donsuke": {
        "pt": "Donsuke",
        "gender": "masculino",
        "number": "singular",
        "category": "Cosmosphere / Personagem",
        "note": "Persona cômica de samurai incorporada por Aurica na Cosmosfera em alusão ao guardião Don Leon (JP どんすけ)."
    },
    "Foul Mouth": {
        "pt": "Língua Insuportável",
        "gender": "feminino",
        "number": "singular",
        "category": "Item / Crossover",
        "note": "Item de busca de Atelier Marie obtido na Academia de Salburg com o arrogante Kreis (JP 憎たらしい舌)."
    },
    "Heritage of Super Civilization?": {
        "pt": "SínC: Herança da Supercivilização?",
        "gender": "feminino",
        "number": "singular",
        "category": "Cartão de Receita",
        "note": "Cartão de Receita para a síntese do Gancho Invertido entregue por Krusche (JP 合C:?超文明の遺産?)."
    }
}

for k, v in new_terms.items():
    if k not in glossary["terms"]:
        glossary["terms"][k] = v
        print(f"Added term: {k} -> {v['pt']}")

with open(glossary_path, "w", encoding="utf-8") as f:
    json.dump(glossary, f, ensure_ascii=False, indent=2)

print("Glossário Mestre atualizado com sucesso!")
