"""Gerador e Validador Completo de Curadoria Editorial para BLK_SYS_018
Ar tonelico: Melody of Elemia (Undub) - Localização PT-BR
Faixa de IDs: 25226 a 25513 (288 falas em SLUS/TEXT/0211 a 0222)
"""

from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "tools"))

from artonelico_tool.project import encoded_size
from curadoria_validate import validate_batch

input_file = BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_018_input.json"
output_file = BASE_DIR / "curadoria_editorial" / "blocos" / "BLK_SYS_018_output.json"
config_file = BASE_DIR / "curadoria_editorial" / "curadoria_config.json"

with open(input_file, "r", encoding="utf-8") as f:
    input_data = json.load(f)

with open(config_file, "r", encoding="utf-8") as f:
    config = json.load(f)

conn = sqlite3.connect(config["database_path"])
c = conn.cursor()
limits = dict(c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 25226 AND 25513").fetchall())
conn.close()

from test_blk18_batch1 import batch1_curated
from test_blk18_batch2 import batch2_curated
from test_blk18_batch3 import batch3_curated
from test_blk18_batch4 import batch4_curated
from test_blk18_batch5 import batch5_curated
from test_blk18_batch6 import batch6_curated
from test_blk18_batch7 import batch7_curated

CURATED = {}
CURATED.update(batch1_curated)
CURATED.update(batch2_curated)
CURATED.update(batch3_curated)
CURATED.update(batch4_curated)
CURATED.update(batch5_curated)
CURATED.update(batch6_curated)
CURATED.update(batch7_curated)

assert len(CURATED) == 288, f"Esperado 288 diálogos, obtido {len(CURATED)}"

# Verificação rigorosa fail-fast de bytes
overflow_errors = []
for did in sorted(CURATED.keys()):
    text, rat, verd = CURATED[did]
    limit = limits.get(did, 0)
    enc = encoded_size(text)
    if enc > limit:
        overflow_errors.append(f"ID {did}: enc {enc}B > limit {limit}B (+{enc - limit})")

if overflow_errors:
    print(f"[ERRO CRÍTICO] {len(overflow_errors)} estouros encontrados:")
    for err in overflow_errors:
        print(" ", err)
    sys.exit(1)

print(f"[OK] Todos os {len(CURATED)} diálogos respeitam 100% os limites de original_bytes!")

# Montagem dos diálogos do output
output_dialogues = []
for d in input_data["dialogues"]:
    did = d["id"]
    text, rationale, verdict = CURATED[did]
    item = {
        "id": did,
        "original_jp": d.get("original_jp", ""),
        "original_en": d.get("original_en", ""),
        "curated_ptbr": text,
        "review_status": "approved",
        "verdict": verdict,
        "rationale": rationale
    }
    output_dialogues.append(item)

new_terms = [
    {
        "term_en": "Tranquility",
        "term_jp": "トランキリティ",
        "term_pt": "Tranquilidade",
        "category": "Item / Suporte",
        "note": "Remédio calmante / item tático consumível de Grathmeld usado em combate para restaurar e estabilizar o canto das Reyvateils."
    },
    {
        "term_en": "Natural Ice",
        "term_jp": "大自然アイス",
        "term_pt": "Sorvete Natural",
        "category": "Grathmeld / Culinária",
        "note": "Item culinário refrescante criado por Misha via síntese Grathmeld."
    },
    {
        "term_en": "Capri Soda",
        "term_jp": "カプリソーダ",
        "term_pt": "Soda Capri",
        "category": "Grathmeld / Culinária",
        "note": "Bebida gaseificada criada por Misha via síntese Grathmeld, cujo sabor é elogiado apesar dos ingredientes peculiares."
    },
    {
        "term_en": "First Era",
        "term_jp": "第一紀",
        "term_pt": "Primeira Era",
        "category": "Lore / Cronologia",
        "note": "A era primordial da civilização de Sol Ciel antes da Primeira Calamidade, quando Shurelia convivia com sua figura paterna / criador."
    },
    {
        "term_en": "Second Era",
        "term_jp": "第二紀",
        "term_pt": "Segunda Era",
        "category": "Lore / Cronologia",
        "note": "A era de reconstrução pós-primeira catástrofe com companheiros valorosos, encerrada pela traição humana e pela Grande Calamidade (Second Disaster)."
    },
    {
        "term_en": "Third Era",
        "term_jp": "第三紀",
        "term_pt": "Terceira Era",
        "category": "Lore / Cronologia",
        "note": "A era atual de isolamento de Sol Ciel, na qual Shurelia viveu centenas de anos em reclusão burocrática e solidão absoluta na Torre."
    }
]

highlights = [
    {
        "id": 25227,
        "original_jp": "ライナー、肩もんであげよっか?",
        "original_en": "Lyner, do you want me to give you a massage?",
        "before": "Lyner, você quer que eu te faça uma massagem?",
        "after": "Lyner, quer uma massagem nos ombros?",
        "reason": "Resgate da intimidade física de Aurica oferecendo massagem de ombros ('肩もんで') com naturalidade espontânea e resolução de buffer."
    },
    {
        "id": 25234,
        "original_jp": "...とかいってて、単純に、グラスノ結晶をたくさん抜いただけだったらバカだよねー。",
        "original_en": "It would be funny if you just put in a bigger Grathnode Crystal than usual.",
        "before": "Seria engraçado se você simplesmente colocasse um Cristal Grathnode maior do que o normal.",
        "after": "...Ou seria tolice minha se você só tiver tirado Cristais Grathnode.",
        "reason": "Correção dramática e canônica de inversão de sentido do inglês (onde '抜き' foi traduzido erroneamente como 'put in'), restaurando o humor sutil de Aurica."
    },
    {
        "id": 25292,
        "original_jp": "えへへ、この前はありがとね。CRトランキリティ、すごく沢山CR使ってくれたでしょ。",
        "original_en": "Hehe, thank you for the other day. You used so much Tranquility on me.",
        "before": "Hehe, obrigada pelo outro dia. Você usou tanto “Tranquilidade” em mim.",
        "after": "Hehe, obrigada por usar tanta Tranquilidade em mim outro dia!",
        "reason": "Eliminação de aspas anglo-americanas desnecessárias no nome canônico do item tático 'Tranquilidade' (Tranquility) e ritmo oral fluido de Misha."
    },
    {
        "id": 25302,
        "original_jp": "カプリソーダ、美味しかったでしょ?CR結構自信作なんだよ、あれ。",
        "original_en": "How was the Capri Soda? Did you like it?",
        "before": "Como estava o Refrigerante Capri? Gostou?",
        "after": "Gostou da Soda Capri? É meu xodó!",
        "reason": "Adoção do termo consagrado 'Soda Capri' (カプリソーダ) de Grathmeld e personalidade alegre e orgulhosa de Misha com '自信作' ('meu xodó')."
    },
    {
        "id": 25399,
        "original_jp": "当たり前です!CRライナー、この間の戦闘は一体何ですか!",
        "original_en": "Yes, and I should be! What were you thinking during that last battle!?",
        "before": "Sim, e com razão! O que você estava pensando durante aquela última batalha!?",
        "after": "É claro!CRLyner, o que foi aquilo na última batalha!?",
        "reason": "Resolução de estouro (156B -> 106B <= 144B), capturando o bico aristocrático de Shurelia ao repreender Lyner com doçura e autoridade real com CR."
    },
    {
        "id": 25504,
        "original_jp": "第一紀には、私のおとうさんにあたる人がいました。第二紀には、一緒に世界を復興した仲間がいました。",
        "original_en": "Before the first disaster, I had a father. After all the devastation, I had friends who helped me rebuild this world...",
        "before": "Antes do primeiro desastre, eu tinha um pai. Depois de toda a devastação, tive amigos que me ajudaram a reconstruir este mundo...",
        "after": "Na Primeira Era, eu tinha uma figura paterna. Na Segunda Era, tive companheiros valorosos para reconstruir o mundo.",
        "reason": "Ponto culminante do bloco: restauração canônica das Eras de Sol Ciel ('第一紀' e '第二紀') apagadas pela versão inglesa, elevando a solenidade histórica de Shurelia (259B -> 231B <= 240B)."
    },
    {
        "id": 25506,
        "original_jp": "第二紀終焉の時...人々に裏切られて...そして大惨事が起こってしまって...。それ以来、私は人を信じることができなくなっていた...。",
        "original_en": "I was betrayed during the Second Disaster. Ever since, I haven’t trusted anybody...",
        "before": "Fui traída durante o Segundo Desastre. Desde então, não confio mais em ninguém...",
        "after": "Fui traída no fim da Segunda Era... e na calamidade, deixei de confiar em todos...",
        "reason": "Restauração da traição humana que culminou na Grande Calamidade / Segundo Desastre, respeitando a métrica estrita de bytes (166B <= 168B)."
    },
    {
        "id": 25511,
        "original_jp": "やっぱり独りはいやです...。",
        "original_en": "I don’t want to be alone...",
        "before": "Não quero ficar sozinha...",
        "after": "Não quero ficar sozinha...",
        "reason": "A confissão mais emocionante do jogo: Shurelia chora desarmada de qualquer autoridade, admitindo que não suporta mais a solidão secular de Sol Ciel."
    },
    {
        "id": 25513,
        "original_jp": "ありがとう...。CRでも、もう少し...もう少しだけCR近づきたいんです。",
        "original_en": "Thank you, Lyner...but, I want to be even closer with you.",
        "before": "Obrigada, Lyner... mas quero estar ainda mais perto de você.",
        "after": "Obrigada...CRMas quero me aproximar... só mais um pouco.",
        "reason": "Resolução de estouro no desfecho lírico da confissão noturna (122B -> 114B <= 120B), preservando a pulsação dramática e o anseio sussurrado com quebra CR."
    }
]

output_data = {
    "block_id": "BLK_SYS_018",
    "axis_id": "AXIS_1",
    "axis_name": "1_NUCLEO_SISTEMICO_E_MENUS",
    "category": "Executable Strings",
    "line_count": len(output_dialogues),
    "id_range": [25226, 25513],
    "scene_handoff_received": input_data.get("scene_handoff_received", {}),
    "scene_handoff_final": {
        "last_scene_id": "BLK_SYS_018",
        "last_line_id": 25513,
        "location_and_situation": "Núcleo Sistêmico Parte 18 (SLUS/TEXT/0211 a 0222: Tópicos de acampamento com Aurica sobre massagem e cristais Grathnode em 0211-0213; Tópicos de acampamento com Misha sobre itens de batalha como Tranquilidade e receitas de Grathmeld como Sorvete Natural e Soda Capri em 0213-0217; Tópicos com Shurelia sobre parcerias táticas, bico aristocrático ao cair em combate e seu despertar em 0217-0221; e o Ponto Culminante da Confissão da Solidão de Shurelia em 0222 sob a luz da noite) concluído com 100% de maestria editorial e ZERO estouros de buffer.",
        "emotional_state": "Intimidade, Cuidado Mútuo, Comédia Gastronômica, Soberania Solene e Confissão Romântica / Aurica tímida oferecendo massagem, Misha brincalhona defendendo seus pratos exóticos de Grathmeld e exigindo proteção no canto, Shurelia cobrando postura com bico régio e, no clímax noturno, despindo séculos de solidão e traumas das Três Eras de Sol Ciel para chorar e pedir a proximidade de Lyner como amiga e algo a mais.",
        "active_hooks": [
            "Conclusão integral do bloco BLK_SYS_018. Seguir para o próximo bloco temático BLK_SYS_019 conforme o Scene Breakdown Ledger."
        ]
    },
    "new_terms": new_terms,
    "highlights": highlights,
    "dialogues": output_dialogues
}

# Gravação do arquivo de saída JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"\n[OK] Arquivo gerado com sucesso: {output_file.name}")

# Validação do Hard Gate Técnico
is_valid, errors = validate_batch(output_data)
if not is_valid:
    print(f"\n[FALHA NO HARD GATE] Encontrados {len(errors)} erros técnicos:")
    for d_id, err_list in sorted(errors.items())[:15]:
        print(f"  ID {d_id}: {'; '.join(err_list)}")
    sys.exit(1)
else:
    print("\n[OK DETERMINÍSTICO] BLK_SYS_018 passou 100% no Hard Gate Técnico com ZERO falhas!")
