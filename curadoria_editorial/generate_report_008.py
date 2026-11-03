# -*- coding: utf-8 -*-
import json
import datetime

report = {
    "block_id": "BLK_EVD_008",
    "completed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "total_dialogues": 227,
    "lines_rewritten": 221,
    "lines_approved_as_is": 6,
    "new_terms_added": 4,
    "hard_gate_errors": 0,
    "lint_warnings": 0,
    "scene_handoff": {
        "status": "COMPLETED",
        "block_id": "BLK_EVD_008",
        "axis_id": "AXIS_3",
        "id_range": "1888-2114",
        "completed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "dramatic_context": (
            "Bloco narrativo de história e eventos BLK_EVD_008 (IDs 1888 a 2114, 23 arquivos de eventos Event/*.evd). "
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
    },
    "highlights": [
        "Restauração e blindagem dos encantamentos sagrados em Hymmnos ancestral declamados por Lyner (#0Ma paks ga exec guol A4 al noes.) e Ayatane (#0Ma num ra exec guol A7 al noes.), que estavam apagados na tradução preliminar.",
        "Correção da grave inversão de sentido no diálogo de Misha e a Guardiã na Mudança de Paradigma (ID 1950), onde 'Não saia ainda!' foi corrigido para 'Não faça isso! Se você entrar aí, nem imagino o que pode acontecer!'.",
        "Erradicação do termo 'Gelo Natural', restaurando 'Sorvete Natural' (大自然アイス) e a terminologia culinária correta da síntese de Grathmeld.",
        "Lapidação da revelação existencial de Misha na nave 'Chronicle Key', alinhando a melodia ao canto sagrado e eliminando ecos e cacófatos sonoros.",
        "Adaptação poética do pedido de Aurica para restaurar o Don Leon de pelúcia deixado nas ruínas de Skuwat."
    ]
}

report_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_008_report.json"
with open(report_path, "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print("Report saved successfully!")
