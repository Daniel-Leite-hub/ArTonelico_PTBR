import json

glossary_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_016_output.json"

with open(glossary_path, "r", encoding="utf-8") as f:
    glossary = json.load(f)

with open(output_path, "r", encoding="utf-8") as f:
    out_data = json.load(f)

# Update last_scene_handoff
glossary["last_scene_handoff"] = out_data["scene_handoff"]

# Add or update new terms
new_terms = {
    "Tastiella": {
        "pt": "Tastiella",
        "gender": "feminino",
        "number": "singular",
        "category": "Personagem / Lore",
        "note": "Guardiã secular do repositório da Crônica Crescente e mentora espiritual que confia o futuro a Lyner (JP タスティエーラ)."
    },
    "Warm Sweater": {
        "pt": "Suéter Quentinho",
        "gender": "masculino",
        "number": "singular",
        "category": "Equipamento / Vestuário",
        "note": "Peça de vestuário tricotada por Aurica com grande valor defensivo e um coração espalhafatoso no peito (JP ほかほかセーター)."
    },
    "Ikaruga Mk.II": {
        "pt": "Ikaruga Modelo 2",
        "gender": "masculino",
        "number": "singular",
        "category": "Bélico / Tecnologia Tenba",
        "note": "Nova máquina de exploração avançada e mobilidade da Torre desenvolvida pela Tenba (JP イカルガ二号)."
    }
}

for k, v in new_terms.items():
    glossary["terms"][k] = v

with open(glossary_path, "w", encoding="utf-8") as f:
    json.dump(glossary, f, indent=2, ensure_ascii=False)

print(f"Glossary successfully updated with last_scene_handoff and {len(new_terms)} terms.")
