# -*- coding: utf-8 -*-
import json
import datetime

glossario_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json"
with open(glossario_path, "r", encoding="utf-8") as f:
    g = json.load(f)

# Update last_scene_handoff
handoff_008 = {
    "status": "COMPLETED",
    "block_id": "BLK_EVD_008",
    "axis_id": "AXIS_3",
    "id_range": "1888-2114",
    "completed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "dramatic_context": (
        "Bloco narrativo de história e eventos BLK_EVD_008 (IDs 1888 a 2114, 23 arquivos Event/*.evd). "
        "Consagra momentos decisivos da narrativa: a criação da Ocarina da Hama revelando os segredos de infância em Platina; "
        "a obtenção do Fragmento de Yuteria e restauração de mecanismos com energia condutora e Magia Verde com Krusche; "
        "a confecção afetiva do Sorvete Natural (Natural Ice) por Misha; a conversa nostálgica com Lorde Flute em Em Pheyna sobre Jack; "
        "a travessia guiada por Aurica e Ayatane no Corredor Musical; o clímax dramático da Mudança de Paradigma Nível 8 de Misha "
        "rebelando-se contra seu cativeiro sagrado e tecendo a temível Magia Vermelha [Sopro Demoníaco]; a conversa íntima comovente "
        "de Aurica e Lyner sobre Don Leon e a memória das ruínas de Skuwat; a autenticação biométrica do Espectro FFT com versos "
        "em Hymmnos ancestral abrindo as Comportas A4 e A7; a infiltração em Tenba revelando a dura realidade das Reyvateils escravizadas; "
        "o arrependimento afetuoso de Claire; o encontro com os aventureiros Eizel e Ruwen rumo ao Planalto Oriental; a aula técnica "
        "de Shurelia no Altar dos Apóstolos sobre o Plug Sinfônico e a artéria condutora da Torre com a clássica incompreensão de Lyner; "
        "o tutorial tático do Campo de Ambiente nível 3; o reforço de sintonia de Magia da Canção de Aurica; e a revelação triunfal "
        "da nau Chronicle Key na mente de Misha tecendo a lendária Magia Azul [Poção das Fadas]."
    ),
    "emotional_state": "Soberania dramatúrgica absoluta, conformidade estrita aos 12 Critérios Canônicos, zero rubricas, blindagem integral de tags de controle e versos sagrados em Hymmnos.",
    "active_hooks": [
        "Conclusão integral do bloco BLK_EVD_008 (IDs 1888 a 2114).",
        "Avanço da Cosmosfera de Misha para o Nível 8 com o despertar do Sopro Demoníaco.",
        "Promessa de Lyner de forjar o Don Leon de pelúcia com a receita da irmã Claire para confortar a Aurica do mundo real."
    ]
}

g["last_scene_handoff"] = handoff_008

# Ensure terms are complete
new_terms_to_add = {
    "Demon Breath": {
        "pt": "Sopro Demoníaco",
        "category": "Magia da Canção / Vermelha",
        "note": "Magia Vermelha de dano colossal tecida por Misha no Nível 8 de sua Cosmosfera (JP デモンブレス)."
    },
    "Fairy Potion": {
        "pt": "Poção das Fadas",
        "category": "Magia da Canção / Azul",
        "note": "Magia Azul curativa e de suporte tecida por Misha a bordo do navio Chronicle Key (JP 桃源金丹)."
    },
    "Skuwat Village": {
        "pt": "Vilarejo de Skuwat",
        "category": "Localização / Lore",
        "note": "Aldeia natal de Aurica, devastada pela catástrofe viral e guardiã de suas memórias de infância com Don Leon (JP スクワート村)."
    },
    "Eastern Plateau": {
        "pt": "Planalto Oriental",
        "category": "Geografia / Cenário",
        "note": "Região vasta explorada por aventureiros como Ruwen e alquimistas como Eizel (JP 東の台地)."
    }
}

for k, v in new_terms_to_add.items():
    if k not in g["terms"]:
        g["terms"][k] = v
        print(f"Added term to glossary: {k} -> {v['pt']}")

with open(glossario_path, "w", encoding="utf-8") as f:
    json.dump(g, f, ensure_ascii=False, indent=2)

print("Glossario mestre atualizado com sucesso!")
