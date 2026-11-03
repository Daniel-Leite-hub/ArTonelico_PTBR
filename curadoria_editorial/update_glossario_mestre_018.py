# -*- coding: utf-8 -*-
import json

glossary_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_018_output.json"

with open(glossary_path, "r", encoding="utf-8") as f:
    glossary = json.load(f)

with open(output_path, "r", encoding="utf-8") as f:
    out_data = json.load(f)

glossary["last_scene_handoff"] = out_data["scene_handoff"]

new_terms = {
    "Team Mir": {
        "pt": "Facção Mir",
        "gender": "feminino",
        "number": "singular",
        "category": "Facção / Cosmosphere",
        "note": "Organização vilanesca liderada por Claire na paródia colegial da Cosmosfera de Shurelia (JP ミュール団)."
    },
    "Harmonics Power": {
        "pt": "Poder Harmônico",
        "gender": "masculino",
        "number": "singular",
        "category": "Energia / Cosmosphere",
        "note": "Energia vital psíquica e harmônica das alunas na Cosmosfera drenada pela vilã Claire (JP ハーモニクスパワー)."
    },
    "Goddess Tyria": {
        "pt": "Deusa Tyria",
        "gender": "feminino",
        "number": "singular",
        "category": "Divindade / Reyvateil Origin",
        "note": "A terceira Reyvateil Origin ancestral reverenciada como divindade na mitologia de Sol Ciel (JP ティリア神)."
    },
    "Dragon Heart": {
        "pt": "Coração de Dragão",
        "gender": "masculino",
        "number": "singular",
        "category": "Item / Colecionável",
        "note": "Item raro e precioso presenteado como mimo de cliente fiel na Fancy Shop de Platina (JP ドラゴンハート)."
    },
    "Talk Topics": {
        "pt": "Tópicos de Conversa",
        "gender": "masculino",
        "number": "plural",
        "category": "Sistema / Cosmosphere",
        "note": "Temas de conversa desbloqueados em viagens usados para aprofundar intimidade com as heroínas em pousadas e acampamentos (JP マター)."
    },
    "Supreme Commander Radolf": {
        "pt": "Comandante-Geral Radolf",
        "gender": "masculino",
        "number": "singular",
        "category": "Título / Militar",
        "note": "Título militar formal do Cardeal Radolf como líder dos Cavaleiros da Igreja (JP ラードルフ総司)."
    }
}

for term_k, term_v in new_terms.items():
    glossary["terms"][term_k] = term_v

with open(glossary_path, "w", encoding="utf-8") as f:
    json.dump(glossary, f, indent=2, ensure_ascii=False)

print(f"Updated {glossary_path} successfully with BLK_EVD_018 handoff and {len(new_terms)} terms.")
