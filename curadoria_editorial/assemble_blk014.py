import json
import sys
import datetime

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_014_input.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_014_output.json"

with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_map = {d["id"]: d for d in input_data["dialogues"]}

batches = [
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch1_014.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch2_014.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch3_014.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch4_014.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch5_014.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch6_014.json"
]

all_curated = []
for b_path in batches:
    with open(b_path, "r", encoding="utf-8") as f:
        all_curated.extend(json.load(f))

print(f"Loaded {len(all_curated)} curated items.")
assert len(all_curated) == 287, f"Expected 287 items, got {len(all_curated)}"

dialogues_output = []
lines_rewritten = 0
lines_approved_as_is = 0

for item in all_curated:
    d_id = item["id"]
    orig = input_map[d_id]
    curated_text = item["curated_ptbr"]
    verdict = item["verdict"]
    rationale = item["rationale"]
    
    if verdict == "rewritten":
        lines_rewritten += 1
        status_val = "rewritten"
    else:
        lines_approved_as_is += 1
        status_val = "approved_as_is"
        
    d_obj = {
        "id": d_id,
        "event_file": orig["event_file"],
        "speaker": orig["speaker"],
        "original_jp": orig["original_jp"],
        "original_en": orig["original_en"],
        "current_ptbr": orig["current_ptbr"],
        "curated_ptbr": curated_text,
        "verdict": verdict,
        "rationale": rationale,
        "speaker_id": orig.get("speaker_id", 0),
        "review_status": "approved",
        "change_type": "curadoria_editorial_profunda",
        "status": status_val,
        "texto_ptbr_anterior": orig["current_ptbr"],
        "texto_ptbr_curado": curated_text,
        "justificativa": rationale,
        "revised_ptbr": curated_text,
        "notes_or_justification": rationale
    }
    dialogues_output.append(d_obj)

scene_handoff = {
    "resumo_dramatico": (
        "O bloco narrativo BLK_EVD_014 (IDs 3464 a 3750, abrangendo 29 arquivos de eventos Event/*.evd) "
        "consolida revelações cruciais, momentos de alta voltagem emocional, humor e a revelação definitiva do complô do Bispo Falss: "
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

output_data = {
    "block_id": "BLK_EVD_014",
    "axis_id": "AXIS_3",
    "axis_name": "HISTÓRIA E EVENTOS",
    "category": input_data.get("category", "HISTÓRIA E EVENTOS"),
    "total_lines": len(dialogues_output),
    "lines_rewritten": lines_rewritten,
    "lines_approved_as_is": lines_approved_as_is,
    "dialogues": dialogues_output,
    "scene_handoff": scene_handoff
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"\nAssembly Complete!")
print(f"Total lines: {len(dialogues_output)}")
print(f"Rewritten: {lines_rewritten}")
print(f"Approved as is: {lines_approved_as_is}")
print(f"Saved to: {output_path}")
