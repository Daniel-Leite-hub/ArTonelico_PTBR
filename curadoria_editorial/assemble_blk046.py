# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

cur_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(cur_dir))

from seg1_046 import segment1
from seg2_046 import segment2
from seg3_046 import segment3
from seg4_046 import segment4

all_segments = segment1 + segment2 + segment3 + segment4

print(f"Total curated lines assembled: {len(all_segments)}")

input_path = cur_dir / "blocos" / "BLK_EVD_046_input.json"
with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_dialogues = input_data["dialogues"]
print(f"Total input lines: {len(input_dialogues)}")

assert len(all_segments) == len(input_dialogues), f"Mismatch: {len(all_segments)} vs {len(input_dialogues)}"

output_dialogues = []
for cur, inp in zip(all_segments, input_dialogues):
    assert cur["id"] == inp["id"], f"ID mismatch: {cur['id']} vs {inp['id']}"
    
    text = cur["curated_ptbr"]
    notes = cur["curation_notes"]
    orig_en = inp.get("original_en", cur.get("original_en", ""))
    
    d_out = {
        "id": cur["id"],
        "original_en": orig_en,
        "custom_text": text,
        "pt_curated": text,
        "curated_ptbr": text,
        "review_status": "approved",
        "notes": notes,
        "curation_notes": notes
    }
    output_dialogues.append(d_out)

scene_handoff_final = {
    "resumo_dramatico": "O bloco BLK_EVD_046 articula quatro sequências capitais e contrastantes de profunda carga dramática e comédia de costumes: primeiro, no santuário do Rinkernator, Aurica entoa seu canto harmônico enquanto Misha na distante Crônica Crescente inicia o hino sagrado de selamento (agradecendo a Lyner pela breve liberdade vivida). Shurelia desperta sobressaltada, alertando em pânico que Mir ainda está viva e que reativar a Torre trará de volta a ameaça viral. Lyner revela que a acordou ciente de tudo, recusando-se a aceitar que a guardiã que mais amou o mundo termine esquecida num martírio eterno enquanto os outros vivem em paz egoísta; questiona a lógica de sacrifício que obriga Misha a se tornar sacrifício humano (人柱) e proclama seu juramento de encontrar um caminho onde todos sejam felizes. Shurelia, profundamente comovida com a maturidade do cavaleiro, oferece todo o seu apoio. Enquanto Jack e Aurica planejam checar Misha, na Crônica Crescente Ayatane se infiltra recitando suavemente a canção de ninar dos deuses, confrontando Misha com serenidade enigmática. Em seguida, Shurelia ingressa formalmente no grupo de combate (#0Wee i ga flip... enter ARTONELICO) e revive-se a cena solene do prólogo em Platina, na qual ela concede a Lyner o Broche Hymmnos com os diagramas do Purger e autoriza em caráter emergencial o uso da aeronave sagrada rumo às Asas de Horus. Mais adiante, em conversa noturna no acampamento, Shurelia pede a Lyner uma Instalação: ela confessa que a única pessoa que já a instalou foi seu criador ('pai') milênios atrás antes do Grathnode Inferia, explicando que embora a Instalação seja dolorosa, o amor do parceiro a transforma em felicidade sublime; revela timidamente sua Porta de Instalação no quadril/lombar (acima do bumbum), deixando Lyner ruborizado, e após o ritual bem-sucedido elogia a extrema delicadeza do rapaz adquirida na prática com Aurica e Misha. Por fim, diante de uma porta ancestral trancada na Torre, Lyner reconhece a arquitetura de Platina abaixo da Blastline enquanto Krusche faz Grathmeld; Misha e Krusche tentam hackear o circuito e se desentendem comicamente sobre a didática da 'irmãzona' e a escolha do fio preto vs. verde, apostando refeições do Combo Dokkoi no Beco Vagalume. O fio verde destrava o acesso e a porta abre, desencadeando uma cobrança cômica colossal de dívidas culinárias (58 Combos Dokkoi, 118 Balas de Gato e 21 Megamilks contra 87 Combos Dokkoi, 59 Raspadinhas de Gelo, 9 Peixes Secos ao Mirin e 2 Megamilks), deixando Lyner estarrecido antecipando o sofrimento financeiro que o aguarda.",
    "decisoes_terminologicas": {
        "Senhora Shurelia": "シュレリア様 (tratamento reverente constante de Lyner e dos Cavaleiros)",
        "Sacrifício humano / Pilar vivo": "人柱 (hitobashira - sacrifício vivo imposto a Misha para conter Mir)",
        "Canção de ninar dos deuses": "神の子守唄 (estrofe lírica entoada por Ayatane ao confrontar Misha)",
        "Broche Hymmnos": "ヒュムネブローチ (artefato sagrado de Shurelia contendo o mapa tridimensional do Purger)",
        "Asas de Horus": "ホルスの翼 (Wings of Horus / região do Mundo Inferior)",
        "Purger": "パージャ (Cristal Hymmnos sagrado de purificação)",
        "Blastline": "ブラストライン (a barreira de plasma entre Mundo Inferior e Mundo Superior)",
        "Apóstolos de Elemia": "エレミアの使徒 (os cavaleiros de guarda sagrada de Platina)",
        "Porta de Instalação": "インストールポイント (conector biológico dérmico lombar das Reyvateils)",
        "Combo Dokkoi": "ドッコイ定食 (refeição substancial tradicional em Sol Ciel)",
        "Beco Vagalume": "ほたる横丁 (distrito comercial do Mundo Inferior)",
        "Balas de Gato": "猫飴 (Nekocandy / guloseima doce tradicional do Beco Vagalume)",
        "Raspadinhas de Gelo": "かち割り氷 (gelo raspado servido nas feiras e barracas)",
        "Peixes Secos ao Mirin": "みりん干し (iguaria salgada e curada de Sol Ciel)",
        "Megamilk": "メガミルク (bebida láctea energizante consumida em grandes porções)"
    },
    "alertas_para_proximo_bloco": "Com Shurelia acordada e integrada ao grupo com o poder do Purger e as aeronaves liberadas, e com Ayatane agindo misteriosamente junto a Misha na Crônica Crescente, o grupo segue adiante na exploração dos níveis intermediários da Torre e desvendamento das maquinações de Bourd e Ayatane."
}

output_data = {
    "block_id": "BLK_EVD_046",
    "axis_id": input_data.get("axis_id", "AXIS_3"),
    "axis_name": input_data.get("axis_name", "3_HISTORIA_E_EVENTOS"),
    "category": input_data.get("category", "Event Dialogue"),
    "line_count": len(output_dialogues),
    "dialogues": output_dialogues,
    "scene_handoff": scene_handoff_final,
    "scene_handoff_final": scene_handoff_final,
    "new_terms": {
        "Hymn Brooch": {
            "pt": "Broche Hymmnos",
            "category": "Item / Lore",
            "note": "ヒュムネブローチ. Artefato sagrado concedido por Shurelia com dados tridimensionais do Purger."
        },
        "Kitty Candy": {
            "pt": "Bala de Gato / Doce de Gato",
            "category": "Culinária / Item",
            "note": "猫飴. Guloseima tradicional em formato de gatinho vendida nas barracas do Beco Vagalume."
        },
        "Shaved Ice": {
            "pt": "Raspadinha de Gelo",
            "category": "Culinária / Bebida",
            "note": "かち割り氷. Gelo picado/raspado tradicional servido como sobremesa refrescante nas feiras."
        },
        "Dried Fish": {
            "pt": "Peixe Seco ao Mirin",
            "category": "Culinária / Alimento",
            "note": "みりん干し. Petisco salgado e curado com molho mirin consumido em mercados de Sol Ciel."
        }
    },
    "highlights": [
        "Despertar de Shurelia no Rinkernator: restauração da carga dramática original do japonês no discurso de Lyner ('血のにじむような想いで' e recusa à injustiça do sacrifício perpétuo '人柱').",
        "Aparição poética de Ayatane na Crônica Crescente: restauração da estrofe lírica '«Entoa, doce melodia... Eu sou o acalanto dos deuses...»' (奏でよ優しき調べ 私は神の子守唄...) suprimida pela tradução em inglês.",
        "Preservação integral do comando sagrado Hymmnos '#0Wee i ga flip 0x1011001101 enter ARTONELICO' e retrospectiva da outorga do [Broche Hymmnos] com o mapa do [Purger].",
        "Conversa noturna e Instalação de Shurelia: revelação comovente de seu passado milenar com seu criador ('pai'), explicação da transcendência espiritual sobre a dor física e cômico embaraço de Lyner com a localização da Porta de Instalação no quadril/bumbum.",
        "Hackeamento e duelo cômico de Krusche e Misha na porta trancada da Torre: deboche mútuo sobre a 'irmãzona', didática com a 'raiz de dois da resistência' e a disputa hilária de apostas culinárias no Beco Vagalume com Combos Dokkoi, Balas de Gato, Raspadinhas de Gelo e Peixes Secos ao Mirin."
    ]
}

output_path = cur_dir / "blocos" / "BLK_EVD_046_output.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {output_path} with {len(output_dialogues)} curated lines.")
