# -*- coding: utf-8 -*-
"""Atualiza o glossario_mestre.json com as decisões canônicas do bloco BLK_EVD_062."""

import json
from pathlib import Path

GLOSSARY_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json")

with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
    glossary = json.load(f)

new_terms = {
    "Fire Shot": {
        "pt": "Tiro Ígneo",
        "gender": "masculino",
        "number": "singular",
        "category": "Magia Verde / Cosmosphere",
        "note": "Primeira Magia Verde de campo tecida na mente de Aurica sob forma de uma pequena esfera falante (JP 火炎弾)."
    },
    "Water God": {
        "pt": "Gota Divina",
        "gender": "feminino",
        "number": "singular",
        "category": "Magia Vermelha / Cosmosphere",
        "note": "Magia Vermelha ofensiva elemental aquática tecida na Cosmosfera de Misha (JP 雫神)."
    },
    "Neo Temple of Elemia": {
        "pt": "Neo-Templo de Elemia",
        "gender": "masculino",
        "number": "singular",
        "category": "Topônimo / Templo Sagrado",
        "note": "O mais monumental santuário histórico consagrado ao culto de Elemia e às suas Deusas ancestrais (JP ネオ・エレミア神殿)."
    },
    "War of the Reyvateils": {
        "pt": "Guerra das Reyvateils",
        "gender": "feminino",
        "number": "singular",
        "category": "História / Conflito Ancestral",
        "note": "Guerra civil histórica deflagrada por Mir contra a humanidade que destruiu metade do mundo e dizimou 70% da população (JP レーヴァテイル戦争)."
    }
}

for term, data in new_terms.items():
    glossary["terms"][term] = data

# Atualização de handoff
glossary["last_scene_handoff"] = {
    "last_scene_id": "Event/538.evd",
    "last_line_id": 14550,
    "resumo_dramatico": "O bloco BLK_EVD_062 articula quatro frentes dramáticas e psicológicas cruciais: (1) Na Cosmosfera de Aurica (Event/703.evd), Lyner acolhe o pavor e o complexo de inferioridade de Aurica, cujo vilarejo mental é consumido pelo Demônio do Fogo. Vencendo o medo da zombaria, Aurica tece sua primeira Magia Verde, o tagarela e cômico Tiro Ígneo. Don Leon entra em pânico ao descobrir que o bloqueio mágico de anos de Aurica foi finalmente rompido. (2) Na Cosmosfera de Misha (Event/640.evd), Lyner é encurralado por um dragão e confrontado pela faceta possessiva de Misha, que expressa seu amor ferido através da dor e do veneno da toxina. Lyner é salvo pela consciência da alma livre de Misha no Stonehenge, tecendo a Magia Vermelha Gota Divina. A Moradora do Mundo Inferior alerta para os perigos do inconsciente profundo, onde as atitudes se invertem mas a raiz emocional é idêntica. (3) No mundo real (Event/238.evd), após uma tarde de brincadeiras com Krusche e Lyner, Misha abre seu coração, confessando seu medo e desabafo por não querer cantar e carregar o fardo eterno de Cantora das Estrelas, antes de reafirmar sua decisão heroica pelo mundo. Jack une-se ao grupo trazendo a pista de uma passagem pelo Silvaplate até as imediações do Beco Vagalume. (4) No Neo-Templo de Elemia (Event/538.evd), Shurelia revela a Lyner e Radolf a trágica crônica de Mir: consagrada no passado como divindade pelo povo mas abusada e subjugada em segredo pelos homens, Mir desenvolveu senciência própria e deflagrou a Guerra das Reyvateils, aniquilando 70% da humanidade e cimentando seu ódio genocida.",
    "decisoes_terminologicas": {
        "Tiro Ígneo": "火炎弾 (Primeira Magia Verde tecida por Aurica, dotada de voz e personalidade)",
        "Gota Divina": "雫神 (Magia Vermelha de Misha gerada no Stonehenge)",
        "Cantora das Estrelas": "星詠 (Título e missão sagrada de Misha como sacrificada no selo de Mir)",
        "Neo-Templo de Elemia": "ネオ・エレミア神殿 (O maior templo consagrado ao culto ancestral de Elemia)",
        "Guerra das Reyvateils": "レーヴァテイル戦争 (Conflito que destruiu metade do mundo e 70% da população)"
    },
    "alertas_para_proximo_bloco": "Com a adesão de Jack e a rota pelo Silvaplate aberta em direção ao Beco Vagalume, somadas às revelações ancestrais de Shurelia sobre as origens da Guerra das Reyvateils e a psique profunda de Misha em ebulição, a trama avança para a exploração da passagem secreta da Torre e a intensificação dos conflitos com a Tenba e a facção de Falss."
}

with open(GLOSSARY_PATH, "w", encoding="utf-8") as f:
    json.dump(glossary, f, ensure_ascii=False, indent=2)

print("glossario_mestre.json atualizado com sucesso para BLK_EVD_062.")
