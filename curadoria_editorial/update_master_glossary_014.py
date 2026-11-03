# -*- coding: utf-8 -*-
"""
Atualização do Glossário Mestre e registro de handoff do bloco BLK_EVD_014.
Ar tonelico: Melody of Elemia (Undub) - PS2
"""

import json
import datetime
import os
import shutil

glossario_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json"
backup_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json.bak_014"

if os.path.exists(glossario_path):
    shutil.copy2(glossario_path, backup_path)
    print(f"Backup created at {backup_path}")

with open(glossario_path, "r", encoding="utf-8") as f:
    g = json.load(f)

# 1. Update last_scene_handoff
handoff_014 = {
    "status": "COMPLETED",
    "block_id": "BLK_EVD_014",
    "axis_id": "AXIS_3",
    "id_range": "3464-3750",
    "completed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "dramatic_context": (
        "Bloco narrativo de história e eventos BLK_EVD_014 (IDs 3464 a 3750, abrangendo 29 arquivos Event/*.evd). "
        "Consolida revelações cruciais, momentos de alta voltagem emocional, humor e a revelação definitiva do complô do Bispo Falss: "
        "1. No combate de treinamento contra o autômato marcial (Event/567.evd), a máquina registra dados para evoluir e oferece um prêmio fabuloso após 5 vitórias; "
        "2. Lyner, Radolf e Jack debatem a arriscada escalada da Torre e o perigo iminente representado pela hostil Tribo Teru (Event/140.evd); "
        "3. No portão de alta segurança da Torre (Event/841.evd), o sistema realiza a autenticação por Espectro FFT de Lyner Barsett e abre o Anteparo A2 através da invocação ancestral sagrada em Hymmnos (#0Ma paks ga exec guol A2 al noes.); "
        "4. O reencontro efusivo de Lyner com conhecidos na cidade (Event/664.evd), que celebram suas conquistas e perguntam pelo paradeiro de Misha; "
        "5. Na Cosmosfera de Aurica (Event/765.evd), Lyner presencia uma fadinha alada roubar o vestido cerimonial branco de Aurica; logo em seguida, Aurica sai do banho revigorada, e Lyner, em pânico gaguejado para não parecer pervertido, descobre que ela nem suspeitou e fica radiante com sua presença nos níveis profundos, convidando-o para acompanhá-la no ritual sagrado antes de descobrirem o roubo do vestido; "
        "6. A aula de síntese Grathmeld do ancião Pombad (Event/23.evd), que ensina os fundamentos com um Healy C, Pedra Azul e Cristal Grathnode (botão IM00), tomando cômica e descaradamente o frasco recém-sintetizado para si próprio com estalos de satisfação ('Glub, glub... Aaaah!'); "
        "7. A interação rural em Sol Ciel (Event/862.evd), onde uma vaca dócil é ordenhada para obtenção de Megamilk; "
        "8. Pistas sobre a fraca emissão de energia condutiva pelo artefato Power Sourcer nas conversas com moradores e com o atendente do Dive Shop (Event/333.evd, Event/337.evd); "
        "9. O motim em Em Pheyna e o avanço dos Cavaleiros da Igreja (Event/283.evd), onde sentinelas Teru chamam Jack por seu nome nativo 'Harmonica' e relatam o ataque dos 'cavaleiros brancos' sob o pretexto de Guerra Santa contra os pagãos heréticos; Jack desmascara a farsa apontando que a Igreja conspira para reviver Mir e por isso sequestrou Misha; Misha ressurge imponente em sua forma adulta restaurada, proclamando que a Chronicle Key vive em seu coração, mas Flute revela que a Matriarca Tastiella está presa na Crônica Crescente (Crescent Chronicle), liberando a localização no Mapa-Múndi; "
        "10. O hilário crossover de Atelier Elie na mente de Aurica (Event/679.evd), onde Eisel e Lyner convencem o preguiçoso e arrogante cavaleiro Douglas a escoltá-los até o Planalto Oriental através de chantagem emocional envolvendo os sentimentos dele por Elfir (Elie); "
        "11. A criação do letal e adorável 'Coelho Mecânico' (Mecha Bunny) por Shurelia (Event/882.evd), uma bomba devastadora disfarçada de bichinho de pelúcia que chacoalha fazendo 'Usa-usa♪', gerando perplexidade cômica em Lyner pela função inútil e pelo orgulho ferido ao ser salvo por algo tão fofo; "
        "12. A colisão dramática de Lyner com Don Leon (Event/698.evd), onde o guardião samurai recusa-se com fúria épica a revelar o sagrado Código Hymmnos de Aurica a um 'patife insolente', exigindo que Lyner abra seu coração e alcance ao menos o Nível 3 da Cosmosfera; "
        "13. A quest da flor cósmica na mente de Misha (Event/690.evd e Event/693.evd), onde Lyner rega uma plantinha misteriosa trazida do armazém com 1.000 DP, transformando-a num tronco colossal que desperta como entidade consciente e se oferece como oferenda de poder, tecendo a Magia Vermelha Flor; "
        "14. A chegada ao deslumbrante Jardim dos Prismas (Prism Garden, Event/394.evd) e a descoberta da antiga passagem de fuga secreta no Beco Vagalume por Misha (Event/92.evd); "
        "15. O operador técnico do Terceiro Reator (Event/960.evd) que aciona os condutores de fônica para alternar o tamanho de Misha entre menina e mulher adulta; "
        "16. A visita tímida de Lyner aos aposentos de Shurelia (Event/781.evd) e os preparativos na Catedral para a instalação da canção Re-Nation em Aurica (Event/474.evd); "
        "17. O choque estarrecedor de Ayatane, Radolf e Lyner ao encontrarem a sede da Igreja de Elemia completamente deserta (Event/350.evd), percebendo que o Bispo Falss e todo o clero conspirador evacuaram o local após armarem uma emboscada; "
        "18. A tentativa de contato de Krusche sobre o Projeto Shoga (aeronave Gungnir) na sede da Tenba (Event/516.evd), constatando que a presidente Ayano partiu em expedição pela Torre; "
        "19. As memórias fragmentadas e tímidas de Lyner em um encontro colegial com Togasaki na Cosmosfera (Event/795.evd); "
        "20. E a confissão psicopática no diário secreto de Falss ('Nova Autobiografia de Kyle, Volume 6', Event/464.evd), que desmascara seu ódio profundo por Platina (que o baniu), seu nojo por Radolf e pelas esmolas dadas à 'plebe ignorante', a aquisição do Cristal Hymmnos Linker para sacrificar Aurica ('uma sonhadora fracassada fácil de manipular'), o plano de soterrar Radolf e os Apóstolos de Elemia vivos na Colina Cantante através de traidores infiltrados na sua tropa, o plano para assassinar o trapalhão Bourd e o anúncio de que a farsa do Trio de Elemia acabou, saudando o alvorecer da tirânica Era de Mir."
    ),
    "decisoes_terminologicas": {
        "A2 Dividing Gate (A2隔壁)": "Anteparo A2 (nomenclatura militar canônica de contenção da Torre, aberta via Espectro FFT e invocação em Hymmnos)",
        "#0Ma paks ga exec guol A2 al noes.": "código sagrado original em Hymmnos com tag #0 restaurado",
        "FFT Spectrum (FFTスペクトラム認証)": "Espectro FFT (sistema de autenticação de fônica da Torre)",
        "Harmonica (アルモニカ)": "Harmonica (nome Teru / sacerdotal de Jack em Em Pheyna)",
        "Star Singer (星詠 - Hoshiyomi)": "Cantora das Estrelas (título sagrado de Misha em Sol Ciel)",
        "Chronicle Key (クロニクルキー)": "Chronicle Key (canção sagrada mística gravada no coração de Misha para conter Mir)",
        "Rectory / Great Sanctuary (大本願)": "Santuário Principal (sede espiritual da Tribo Teru em Em Pheyna)",
        "Crescent Chronicle (クレセントクロニクル)": "Crônica Crescente (estrutura/navio lendário ancestral dos Teru)",
        "Mecha Bunny (めかうさぎ / めかうさ)": "Coelho Mecânico (bomba explosiva com formato de coelho concebida por Shurelia com o som característico “Usa-usa♪”)",
        "Recipe Card Synthesis C: Mecha Bunny (合C:めかうさ)": "Síntese C: Coelho Mecânico",
        "Sigsal Castle (シグザール城)": "Castelo de Sigsal (sede dos cavaleiros no crossover de Atelier Elie)",
        "Eastern Lands / Plateau (東の台地)": "Planalto Oriental (topônimo canônico de Atelier Elie)",
        "Prism Garden (プリズムガーデン)": "Jardim dos Prismas (área mística da Torre)",
        "Red Magic [Flower] (赤魔法【華】)": "Magia Vermelha Flor (feitiço de ataque tecido na mente de Misha)",
        "New Biography of Kyle Vol. 6 (新・カイエル自伝6巻)": "“Nova Autobiografia de Kyle, Volume 6” (segundo tomo confidencial do diário do Bispo Falss)",
        "Hymn Crystal Linker (ヒュムネクリスタル「リンカ」)": "Cristal Hymmnos Linker (cristal catalisador para a ligação fônica)",
        "Project Shoga (プロジェクト『翔雅』)": "Projeto Shoga (projeto técnico de dirigível liderado por Krusche)"
    },
    "alertas_para_proximo_bloco": (
        "1. A conspiração de Falss atinge o ponto de ignição: os Cavaleiros da Igreja iniciaram a suposta 'Guerra Santa', o clero desertou de suas sedes e traidores dentro da unidade de Radolf receberam ordens para soterrá-lo junto com os Apóstolos nas profundezas da Colina Cantante. "
        "2. Misha restaurou sua forma física adulta e a canção Chronicle Key vive em seu coração, mas a Matriarca Tastiella está inacessível na Crônica Crescente (Crescent Chronicle). "
        "3. Aurica se prepara para o ritual no Nível 3 da Cosmosfera, onde seu vestido cerimonial roubado pela fadinha alada precisará ser recuperado e Don Leon exigirá convicção de Lyner antes de revelar o Código Hymmnos. "
        "4. Preservação contínua de tokens procedurais, versos sagrados em Hymmnos (#0...) e vigilância extrema contra quebras órfãs de linha."
    )
}

g["last_scene_handoff"] = handoff_014

# 2. Add / update terms safely
terms = g.setdefault("terms", {})

new_terms = {
    "Mecha Bunny": {
        "pt": "Coelho Mecânico",
        "gender": "masculino",
        "number": "singular",
        "category": "Item / Grathmeld",
        "note": "Bomba explosiva com formato de coelho concebida por Shurelia com o som característico “Usa-usa♪” (JP めかうさぎ / めかうさ)."
    },
    "Sigsal Castle": {
        "pt": "Castelo de Sigsal",
        "gender": "masculino",
        "number": "singular",
        "category": "Topônimo / Crossover",
        "note": "Castelo real da capital no crossover do mundo de Atelier Elie na Cosmosfera de Aurica (JP シグザール城)."
    },
    "Eastern Lands / Plateau": {
        "pt": "Planalto Oriental",
        "gender": "masculino",
        "number": "singular",
        "category": "Topônimo / Crossover",
        "note": "Área montanhosa distante no mundo de Atelier Elie para onde Eisel e Douglas viajam (JP 東の台地)."
    },
    "Red Magic [Flower]": {
        "pt": "Magia Vermelha Flor",
        "gender": "feminino",
        "number": "singular",
        "category": "Magia da Canção / Vermelha",
        "note": "Feitiço ofensivo de Magia Vermelha tecido na mente de Misha após o crescimento pleno da flor cósmica (JP 赤魔法【華】)."
    },
    "Great Sanctuary / Rectory": {
        "pt": "Santuário Principal",
        "gender": "masculino",
        "number": "singular",
        "category": "Topônimo / Tribo Teru",
        "note": "Santuário e sede espiritual central da Tribo Teru em Em Pheyna (JP 大本願)."
    },
    "Project Shoga": {
        "pt": "Projeto Shoga",
        "gender": "masculino",
        "number": "singular",
        "category": "Tecnologia / Aeronáutica",
        "note": "Projeto de engenharia de dirigível liderado por Krusche na corporação Tenba para construir a aeronave Gungnir (JP プロジェクト『翔雅』)."
    },
    "Hymn Crystal Linker": {
        "pt": "Cristal Hymmnos Linker",
        "gender": "masculino",
        "number": "singular",
        "category": "Item / Lore",
        "note": "Cristal Hymmnos catalisador obtido pela Igreja e cobiçado por Falss para realizar a conexão forçada com Aurica (JP ヒュムネクリスタル「リンカ」)."
    }
}

for k, v in new_terms.items():
    if k not in terms:
        terms[k] = v
        print(f"Added term: {k} -> {v['pt']}")
    else:
        terms[k].update(v)
        print(f"Updated term: {k} -> {terms[k]['pt']}")

with open(glossario_path, "w", encoding="utf-8") as f:
    json.dump(g, f, indent=2, ensure_ascii=False)

print("Glossario Mestre updated successfully with BLK_EVD_014 handoff.")
