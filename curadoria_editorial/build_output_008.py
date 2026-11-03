# -*- coding: utf-8 -*-
import json
import os

from test_batch1 import batch1
from test_batch2 import batch2
from test_batch3 import batch3
from test_batch4 import batch4

curated_lines = batch1 + batch2 + batch3 + batch4

output_data = {
    "block_id": "BLK_EVD_008",
    "axis_id": "AXIS_3",
    "axis_name": "HISTÓRIA E EVENTOS",
    "total_lines": len(curated_lines),
    "lines_rewritten": sum(1 for x in curated_lines if x["status"] == "rewritten"),
    "lines_approved_as_is": sum(1 for x in curated_lines if x["status"] == "approved_as_is"),
    "curated_lines": curated_lines,
    "scene_handoff": {
        "resumo_dramatico": (
            "O bloco BLK_EVD_008 (IDs 1888 a 2114, 23 arquivos de eventos Event/*.evd) aprofunda e consolida momentos dramáticos e sistêmicos capitais de Ar tonelico: Melody of Elemia: "
            "1. A revelação e criação da Ocarina da Hama na Cosmosfera de Misha (Event/669.evd e Event/948.evd), amarrando a infância de Lyner e Misha em Platina à gênese de sua Guardiã da Mente; "
            "2. A conquista do Fragmento de Yuteria com Krusche e a ativação de mecanismos com poder sinfônico e Magia Verde (Event/128.evd, Event/113.evd, Event/247.evd); "
            "3. O hilário e afetuoso evento culinário do Sorvete Natural (Natural Ice) com Misha surpreendendo Lyner com seus dotes gastronômicos (Event/876.evd); "
            "4. O reencontro solene em Em Pheyna com o líder da Tribo Teru, Lorde Flute, revelando o passado e a preocupação com o mercenário Jack (Event/450.evd, Event/451.evd); "
            "5. O avanço e cumplicidade de Aurica e Ayatane no Corredor Musical (Event/304.evd); "
            "6. O clímax dramático e existencial da Mudança de Paradigma para o Nível 8 na Cosmosfera de Misha (Event/654.evd), onde Misha se rebela contra o fardo de cantar eternamente enclausurada 'naquela sala' para carregar o destino do mundo, decide superar sua faceta rígida e tece a temível Magia Vermelha [Sopro Demoníaco] (デモンブレス); "
            "7. A comovente cena na Cosmosfera de Aurica após o salvamento de Don Leon (Event/749.evd), onde Aurica mostra sua vulnerabilidade, pede a Lyner para entalhar/costurar um novo Don Leon de pelúcia repleto de carinho e revela a dor de ter deixado seu mascote original nas ruínas do Vilarejo de Skuwat; "
            "8. O solene protocolo de segurança FFT Spectrum nas Comportas Divisórias A4 e A7 com os versos sagrados em Hymmnos ancestral declamados por Lyner e Ayatane (Event/843.evd, Event/430.evd); "
            "9. A infiltração nas instalações de Tenba onde Misha arromba uma tranca giratória e expõe a desumana realidade das Reyvateils sem direitos humanos no Submundo, enquanto flerta intimamente com Lyner (Event/76.evd); "
            "10. O arrependimento afetuoso de Claire em Firefly Alley por ter brigado com Aurica (Event/316.evd); "
            "11. O encontro cômico de crossover com Eizel e Ruwen contratado como escolta rumo ao Planalto Oriental (Event/681.evd); "
            "12. A explicação técnico-tecnológica de Lady Shurelia no Altar dos Apóstolos revelando o Plug Sinfônico como a grande artéria de transmissão de energia da Torre e ninho dos vírus de Mir, culminando na incompreensão cômica de Lyner e na terna resignação da deusa (Event/499.evd); "
            "13. O treinamento tático de combate de Misha ensinando a elevar o Campo de Ambiente até o nível 3 (Event/103.evd); "
            "14. A percepção sensorial à distância de Shurelia sentindo o sinal de Lyner vivo (Event/110.evd); "
            "15. O ritual de Grathmeld com Aurica ampliando as utilizações de Magia da Canção após sintonizar com a Torre (Event/770.evd); "
            "16. E a revelação sublime na Cosmosfera de Misha a bordo do navio 'Chronicle Key', a personificação de sua vida e de sua canção para salvar o mundo, recebendo a Poção das Fadas (桃源金丹 / Fairy Potion) e tecendo a lendária Magia Azul (Event/695.evd)."
        ),
        "decisoes_terminologicas": {
            "Natural Ice (大自然アイス)": "Sorvete Natural (alinhado ao Glossário Mestre; erradicação do errôneo 'Gelo Natural')",
            "Fragment of Yuteria (ユーテリア破片)": "[Fragmento de Yuteria] (item com colchetes de inventário)",
            "Chief Flute (フラウト様)": "Lorde Flute (título canônico do líder da Tribo Teru no Portão Pheyna)",
            "Apostle's Altar / Symphonic Reactor (使徒の祭壇 / 導力プラグ)": "Altar dos Apóstolos / Plug Sinfônico (instalação de alta voltagem e transmissão da Torre)",
            "Musical Corridor (彩音回廊)": "Corredor Musical (calabouço de ondas fônicas)",
            "Demon Breath (デモンブレス)": "Sopro Demoníaco (Magia Vermelha de Misha no Nível 8; substituição do vulgar 'Bafo do Demônio')",
            "Fairy Potion (桃源金丹)": "Poção das Fadas (Magia Azul canônica ligada ao navio mental Chronicle Key)",
            "Chronicle Key (クロニクルキー)": "Chronicle Key (preservado como nome sagrado do Hino e da nau mental)",
            "Skuwat Village (スクワート村)": "Vilarejo de Skuwat (localidade destruída do passado de Aurica)",
            "Dividing Gate (隔壁)": "Comporta A4 / Comporta A7 (padronizado com a Comporta A9 do Bloco 7)",
            "FFT Spectrum (FFTスペクトラム認証)": "Autenticação do Espectro FFT (reconhecimento biométrico harmônico)",
            "Hymmnos Chants (#0Ma paks ga exec guol A4 al noes. / #0Ma num ra exec guol A7 al noes.)": "Preservação absoluta com tag '#0' blindada",
            "Ambience Field (アンビエンスフィールド)": "Campo de Ambiente (mecânica de combate)",
            "Eastern Lands (東の台地)": "Planalto Oriental (localidade clássica de Atelier/Ar tonelico)"
        },
        "alertas_para_proximo_bloco": (
            "1. Cuidado com falas do sistema que contêm marcadores de áudio/evento '#0' seguidos de Hymmnos: esses comandos ativam efeitos sonoros e dublagem de encantamento no motor do jogo e jamais podem ser omitidos ou alterados. "
            "2. Manter a paridade terminológica de 'Plug Sinfônico' (導力プラグ) e 'Comportas' (A1 a A9). "
            "3. Acompanhar a evolução dos arcos de Misha e Aurica nas fases avançadas de suas Cosmosferas (Nível 8 e 9), mantendo o contraste entre a maturidade trágica da missão de cantar e o amor protetor por Lyner. "
            "4. Blindar tokens dinâmicos de síntese e magia como [○○○] e ○."
        )
    }
}

output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_008_output.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"File saved successfully to: {output_path}")
print(f"Total lines: {output_data['total_lines']}")
print(f"Lines rewritten: {output_data['lines_rewritten']}")
print(f"Lines approved as is: {output_data['lines_approved_as_is']}")
