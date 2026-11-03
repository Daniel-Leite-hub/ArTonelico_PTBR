import json

glossary_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_017_output.json"

with open(glossary_path, "r", encoding="utf-8") as f:
    glossary = json.load(f)

with open(output_path, "r", encoding="utf-8") as f:
    out_data = json.load(f)

# Update last_scene_handoff
glossary["last_scene_handoff"] = out_data["scene_handoff"]

# Add or update new terms
new_terms = {
    "Yuteria String": {
        "pt": "Corda Yuteria",
        "gender": "feminino",
        "number": "singular",
        "category": "Item / Síntese Grathmeld",
        "note": "Fio condutor de extrema finura e tenacidade inquebrável usado para instrumentos musicais e amarrações sintetizado via Grathmeld (JP ユーテリア弦)."
    },
    "Fragment of Yuteria": {
        "pt": "Fragmento de Yuteria",
        "gender": "masculino",
        "number": "singular",
        "category": "Item de Síntese / Material",
        "note": "Fragmento metálico e acústico extraído da carcaça do Guardião para forja de cordas de alaúde (JP ユーテリア破片)."
    },
    "Altar of Apostles": {
        "pt": "Altar dos Apóstolos",
        "gender": "masculino",
        "number": "singular",
        "category": "Localização / Lore da Igreja",
        "note": "Santuário sagrado e tenebroso reivindicado por Falss como epicentro de sua guerra santa (JP 使徒の祭壇)."
    },
    "Hymn Crystal Linker": {
        "pt": "Cristal Hymmnos Linker",
        "gender": "masculino",
        "number": "singular",
        "category": "Item / Lore",
        "note": "Cristal Hymmnos catalisador sagrado de conexão e sintonia procurado pela Igreja e disputado por Falss (JP ヒュムネクリスタル「リンカ」)."
    },
    "A7 Dividing Wall": {
        "pt": "Comporta A7 / Barreira A7",
        "gender": "feminino",
        "number": "singular",
        "category": "Estrutura / Tecnologia da Torre",
        "note": "Bloqueio e comporta de contenção hermética de alta segurança da Torre (JP A7隔壁ゲート)."
    },
    "FFT Spectrum": {
        "pt": "Espectro FFT",
        "gender": "masculino",
        "number": "singular",
        "category": "Tecnologia / Autenticação Fônica",
        "note": "Protocolo fônico de autenticação por transformada rápida de Fourier para reconhecimento de cavaleiros (JP FFTスペクトラム認証)."
    },
    "Symphonic Plug": {
        "pt": "Plugue Sinfônico / Conector Sinfônico",
        "gender": "masculino",
        "number": "singular",
        "category": "Tecnologia / Condutor de Energia",
        "note": "Terminal condutor de energia harmônica e fônica da Torre acionado por Ayatane (JP 導力プラグ)."
    },
    "Kanade": {
        "pt": "Kanade",
        "gender": "feminino",
        "number": "singular",
        "category": "Personagem / Androide",
        "note": "Terceira androide de manutenção da Torre (Criança da Luz), guardiã dos Sinos de Plasma e combatente apaixonada por artes marciais (JP カナデ)."
    },
    "Mai": {
        "pt": "Mai",
        "gender": "feminino",
        "number": "singular",
        "category": "Personagem / Androide",
        "note": "Segunda androide de manutenção e irmã mais velha de Kanade, guardiã do Sino de Plasma da Asa Direita de Hórus, sacrificada na Guerra das Reyvateils (JP マイ)."
    },
    "Right Wing of Horus": {
        "pt": "Asa Direita de Hórus",
        "gender": "feminino",
        "number": "singular",
        "category": "Toponímia / Estrutura da Torre",
        "note": "Setor monumental da superestrutura da Torre onde se localizava o sino estabilizador de gravidade gêmeo guardado por Mai (JP ホルス右翼)."
    },
    "Angel Shura": {
        "pt": "Anjo Shura",
        "gender": "masculino",
        "number": "singular",
        "category": "Cosmosfera / Magia Azul",
        "note": "Entidade onírica que rege a inovação e o poder na Cosmosfera de Misha, convertida na Magia Azul Anjo Shura (JP 修羅天)."
    },
    "Moon Mansion": {
        "pt": "Mansão da Lua",
        "gender": "feminino",
        "number": "singular",
        "category": "Cosmosfera / Localização",
        "note": "Edifício solene de retiro e penitência interior na mente de Misha (JP 月ノ館)."
    },
    "Hare no Hi": {
        "pt": "Dia Festivo / Grande Dia",
        "gender": "masculino",
        "number": "singular",
        "category": "Cultura / Ritual",
        "note": "O grande dia solene de celebração espiritual e rito de passagem na mente da Reyvateil (JP 晴れの日)."
    },
    "Dondoko Bowl": {
        "pt": "Tigela Dondoko",
        "gender": "feminino",
        "number": "singular",
        "category": "Culinária / Item",
        "note": "Prato tradicional farto muito apreciado na Torre (JP どんどこ丼)."
    },
    "Phebes Salad": {
        "pt": "Salada de Phebes",
        "gender": "feminino",
        "number": "singular",
        "category": "Culinária / Item",
        "note": "Salada fresca típica preparada com vegetais locais (JP フェベスサラダ)."
    },
    "Lando": {
        "pt": "Lando",
        "gender": "masculino",
        "number": "singular",
        "category": "Culinária / Sobremesa",
        "note": "Sobremesa doce e refrescante muito popular em Sol Ciel (JP ランドー)."
    }
}

terms = glossary.setdefault("terms", {})
for k, v in new_terms.items():
    terms[k] = v

with open(glossary_path, "w", encoding="utf-8") as f:
    json.dump(glossary, f, indent=2, ensure_ascii=False)

print(f"Master glossary updated successfully with {len(new_terms)} terms and last_scene_handoff.")
