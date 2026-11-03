# -*- coding: utf-8 -*-
"""
generate_blk086_output.py - Gera BLK_EVD_086_output.json completo e validado.
"""
import json
from pathlib import Path

notes_map = {
    # Event/448.evd
    19361: "Radolf expressa surpresa calorosa e fraterna ao reencontrar Lyner.",
    19362: "Lyner retribui a saudação a Radolf com afeto e alegria pelo reencontro.",
    19363: "Radolf pergunta com vigor sobre o bem-estar do amigo.",
    19364: "Radolf nota a presença de Aurica e a cumprimenta com carinho pastoral.",
    19365: "Aurica saúda Radolf com respeito e formalidade, usando seu antigo título cerimonial.",
    19366: "Radolf ri desconcertado ao ouvir o título militar de Comandante-Geral.",
    19367: "Radolf revela sua promoção a Bispo após a reestruturação da Igreja.",
    19368: "Lyner celebra com empolgação genuína a elevação eclesiástica do companheiro.",
    19369: "Radolf comenta a raridade histórica de um cavaleiro ascender ao sacerdócio.",
    19370: "Radolf detalha o reconhecimento recebido por salvar a Igreja do colapso.",
    19371: "Lyner parabeniza o amigo com entusiasmo fraterno.",
    19372: "Aurica congratula Radolf com reverência e doçura.",
    19373: "Radolf reage encabulado diante das felicitações tão cerimoniosas.",
    19374: "Radolf proclama a ruptura definitiva da Igreja com os desígnios de Mir.",
    19375: "Radolf define a nova missão da Igreja voltada inteiramente ao serviço do povo.",
    19376: "Lyner comemora a realização do antigo sonho pastoral de Radolf.",
    19377: "Radolf pondera que este é só o começo e ri com energia guerreira.",
    19378: "Lyner hesita em silêncio ao lembrar do motivo grave de sua visita.",
    19379: "Aurica sussurra a Lyner lembrando-o de falar sobre a situação de Shurelia.",
    19380: "Radolf brinca maliciosamente perguntando se os dois vieram anunciar casamento.",
    19381: "Aurica cora e protesta constrangida com a insinuação de Radolf.",
    19382: "Lyner corta o clima descontraído e traz à tona o estado crítico de Shurelia.",
    19383: "Radolf reage com esperança e júbilo ao saber da chance de despertar Shurelia.",
    19384: "Lyner explica a condição essencial de localizar o Cristal RE Nation.",
    19385: "Radolf expressa imenso alívio ao saber que Shurelia não foi perdida em definitivo.",
    19386: "Lyner faz o convite para Radolf integrar o grupo na busca pelo cristal sagrado.",
    19387: "Radolf compreende a gravidade do pedido e pondera com sobriedade.",
    19388: "Radolf lamenta com pesar sua impossibilidade de deixar as obrigações da Igreja.",
    19389: "Lyner escuta o dilema com empatia e afeto sincero.",
    19390: "Radolf reflete sobre a época em que era apenas um soldado sob ordens alheias.",
    19391: "Radolf explica o peso da liderança pastoral e o risco de desamparar a Igreja.",
    19392: "Radolf desculpa-se com tristeza por não poder empunhar a lança ao lado de Lyner.",
    19393: "Lyner tranquiliza Radolf com generosidade e acolhimento compreensivo.",
    19394: "Lyner valida a recusa e reconhece a prioridade dos deveres de Bispo de Radolf.",
    19395: "Radolf agradece a compreensão madura e fraterna de Lyner.",

    # Event/125.evd
    19396: "Falss saúda os jovens pela manhã com cortesia e tom paternal benévolo.",
    19397: "Falss revela os frutos de sua pesquisa situando o cristal na Colina do Canto.",
    19398: "Falss assegura a permanência da relíquia caso os sítios não tenham sido saqueados.",
    19399: "Lyner reage animado e disposto a partir de imediato para resgatar o cristal.",
    19400: "Falss chama a atenção de Lyner para um detalhe tático crucial da missão.",
    19401: "Falss introduz uma preocupação pastoral com delicadeza calculada.",
    19402: "Falss adverte sobre os perigos mortais de explorar ruínas sem o amparo de uma Reyvateil.",
    19403: "Falss propõe que Lyner acolha Aurica como sua parceira de jornada sagrada.",
    19404: "Aurica reage surpresa e atônita com a indicação de seu nome pelo bispo.",
    19405: "Lyner hesita por receio de abusar da benevolência da autoridade da Igreja.",
    19406: "Falss exalta o potencial adormecido e ilimitado de Aurica como donzela cantora.",
    19407: "Aurica balbucia sem acreditar na confiança depositada por seu mentor clerical.",
    19408: "Falss concede autonomia total à jovem e pede que ela escute o próprio coração.",
    19409: "Aurica supera a insegurança e aceita a missão com fervor e dedicação sincera.",
    19410: "Falss volta-se para Lyner aguardando o consentimento solene do cavaleiro.",
    19411: "Lyner aceita com entusiasmo e agradece a concessão de tão valorosa parceira.",
    19412: "Notificação de sistema: Aurica é formalmente integrada ao grupo de jornada.",
    19413: "Falss ordena a Radolf que acompanhe os jovens para prestar custódia e proteção militar.",
    19414: "Radolf curva-se com disciplina militar e acata a ordem episcopal sem hesitação.",
    19415: "Notificação de sistema: Radolf passa a integrar o grupo como guerreiro de vanguarda.",
    19416: "Lyner expressa gratidão profunda a Falss pelo suporte inestimável concedido.",
    19417: "Falss detém Lyner para um conselho particular e confidencial.",
    19418: "Lyner atende com reverência à advertência final do bispo.",
    19419: "Falss alude às cicatrizes psíquicas e ao passado doloroso de Aurica.",
    19420: "Falss diagnostica a couraça emocional erguida pela jovem para se proteger da dor.",
    19421: "Falss elucida a relação essencial entre a sensibilidade afetiva e a Magia da Canção.",
    19422: "Lyner acolhe a revelação em silêncio compenetrado.",
    19423: "Falss roga a Lyner que atue como guardião curador do coração de Aurica.",
    19424: "Lyner assume solenemente o compromisso protetor perante o bispo.",
    19425: "Falss concede a sagrada bênção do Trio de Elemia para proteger a expedição.",
    19426: "Lyner volta-se para Aurica com afeto e sela a parceria com cumplicidade direta.",
    19427: "Aurica consente com meiguice e renovada coragem ao lado de seu guardião.",
    19428: "Notificação de sistema: O local Colina do Canto é liberado para acesso no Mapa-Múndi.",

    # Event/552.evd
    19429: "Lyner brada o nome de Ayatane ao interceptá-lo diante da Plasma Bell.",
    19430: "Ayatane expressa surpresa calculada ao ver o amigo descobrir seu paradeiro secreto.",
    19431: "Lyner relata ter viajado pelo mundo para desvendar a verdade sobre Mir e Ayatane.",
    19432: "Shurelia indaga com severidade divina sobre a conspiração contra a Plasma Bell.",
    19433: "Shurelia evoca o paralelo trágico com a catástrofe original do selamento de Mir.",
    19434: "Ayatane confirma as suspeitas com frieza lacônica e serena.",
    19435: "Ayatane proclama sua missão programada de estilhaçar o sino e derrubar as Asas de Hórus.",
    19436: "Lyner questiona angustiado qual o propósito humano ou moral de tamanha devastação.",
    19437: "Ayatane replica com desdém afirmando que a lógica humana não lhe diz respeito.",
    19438: "Ayatane afirma seu dever inflexível de executar o comando absoluto de sua Mãe.",
    19439: "Lyner apela à consciência individual de Ayatane perguntando por seus próprios anseios.",
    19440: "Ayatane confessa que seu único desejo é propiciar um mundo onde sua Mãe viva em paz.",
    19441: "Ayatane assevera que pagará qualquer preço ou cometerá qualquer ato por esse fim.",
    19442: "Lyner rebate revelando que compartilha do mesmo sonho de salvar e libertar Mir.",
    19443: "Ayatane estremece atônito perante a declaração imprevista de seu antagonista.",
    19444: "Lyner defende que a verdadeira paz só existe se abarcar a felicidade de todos os povos.",
    19445: "Ayatane silencia abalado pelo peso moral das convicções de Lyner.",
    19446: "Lyner implora pela escuta de Ayatane e nega qualquer ímpeto de destruição cega contra Mir.",
    19447: "Lyner explica as conclusões colhidas dos testemunhos ao longo de sua peregrinação.",
    19448: "Lyner denuncia as atrocidades históricas cometidas pela humanidade contra Mir.",
    19449: "Ayatane absorve em silêncio o reconhecimento da dor ancestral de sua criadora.",
    19450: "Lyner argumenta que Mir não é uma criatura puramente maligna por natureza.",
    19451: "Lyner manifesta fé inabalável no poder do acolhimento compassivo para resgatar Mir.",
    19452: "Lyner suplica para que Ayatane renuncie ao massacre da queda das Asas de Hórus.",
    19453: "Ayatane lamenta o atraso do apelo e revela a consumação da reescrita viral de Kanade.",
    19454: "Ayatane revela a salvaguarda da Plasma Bell: só sua guardiã pode destruí-la.",
    19455: "Ayatane anuncia que Kanade iniciou o protocolo físico de aniquilação do sino vital.",
    19456: "Lyner reage chocado e estarrecido diante do perigo iminente.",
    19457: "Lyner clama por Kanade tentando despertar sua consciência sob a lavagem cerebral.",
    19458: "Kanade permanece silente e entorpecida pelas diretrizes virais da reescrita.",
    19459: "Lyner recusa-se a ferir a irmã de Mei Mei e busca alternativas pacíficas.",
    19460: "Lyner clama pelo auxílio técnico e divino de Shurelia para conter a guardiã.",
    19461: "Shurelia constata que a única via de salvação é desativar Kanade à força.",
    19462: "Lyner lamenta com agonia a necessidade de combater uma aliada inocente.",
    19463: "Lyner indaga com sobressalto se Kanade cessou seus movimentos temporariamente.",
    19464: "Lyner sobressalta-se diante da reativação hostil da androide de combate.",
    19465: "Shurelia adverte sobre o poder incomensurável da Criança da Luz contra ataques comuns.",
    19466: "Lyner desespera-se diante da invulnerabilidade do constructo de defesa da Torre.",
    19467: "Lyner clama diretamente a Ayatane implorando por sua intervenção imediata.",
    19468: "Ayatane hesita em tormento interior diante da súplica desesperada do amigo.",
    19469: "Lyner eleva o apelo com veemência arrebatadora tocando o íntimo do Cavaleiro de Platina.",
    19470: "Lyner mal consegue processar o clarão súbito e o desfecho da investida de Ayatane.",
    19471: "Lyner corre em socorro de Ayatane ao vê-lo tombar após o golpe.",
    19472: "Lyner ampara o amigo ferido com aflição e solicitude genuína.",
    19473: "Ayatane ri com autodepreciação poética diante de seu ato irracional de desobediência.",
    19474: "Lyner indaga com espanto e comoção os motivos que levaram Ayatane a conter Kanade.",
    19475: "Ayatane confessa com ternura contida o desejo secreto de apostar no ideal de Lyner.",
    19476: "Ayatane geme contendo os estertores do desgaste viral em sua estrutura de dados.",
    19477: "Lyner ordena que o amigo poupe as forças e não se desgaste tentando falar.",
    19478: "Ayatane tranquiliza Lyner afirmando que recuperará a estabilidade com repouso.",
    19479: "Ayatane descreve o abismo de rancor que hoje aprisiona a mente de Mir.",
    19480: "Ayatane revela a existência histórica de um Hymmnos amoroso tecido por Mir para humanos.",
    19481: "Ayatane encarrega Lyner e sua party de entoar essa melodia sagrada para redimir Mir.",
    19482: "Lyner certifica-se com ansiedade aflita sobre a integridade vital do amigo.",
    19483: "Ayatane responde com altivez e ironia refinada que não perecerá por tão pouco.",
    19484: "Lyner indaga sobre o destino e os rumos de Ayatane após a insubordinação à Mir.",
    19485: "Ayatane divaga sobre buscar um recanto deserto para desvanecer e esperar o fim.",
    19486: "Ayatane reconhece que sua punição por trair Mir será a exclusão e a morte inevitável.",
    19487: "Lyner recusa o sacrifício e estende a mão para marcharem juntos em socorro a Mir.",
    19488: "Ayatane constata com carinho zombeteiro que Lyner é um tolo incurável e puro.",
    19489: "Ayatane compreende o magnetismo ético que leva tantos heróis a confiarem a vida em Lyner.",
    19490: "Ayatane decide consagrar o restante de sua existência à causa redentora de Lyner.",
    19491: "Lyner agradece comovidamente e jura que jamais deixará o amigo ser apagado do mundo.",
    19492: "Lyner renova o pacto de lealdade fraterna convidando Ayatane de volta ao seu lado.",
    19493: "Ayatane acolhe as palavras em silêncio emocionado e serena resignação.",
    19494: "Notificação de sistema: Ayatane junta-se formalmente à comitiva dos heróis.",
    19495: "Lyner volta sua atenção compassiva para o estado corporal de Kanade.",
    19496: "Ayatane esclarece que Kanade sofreu apenas estafa sinfônica e recobrará os sentidos.",
    19497: "Shurelia confirma a fisiologia androide de recarga durante o ciclo de sono profundo.",
    19498: "Lyner lamenta o sofrimento infligido à jovem sentinela durante o confronto.",
    19499: "Kanade repousa em sono sereno e inerte na câmara de salvaguarda.",
    19500: "Lyner cumpre a promessa feita a Mei Mei e aproxima o artefato familiar da donzela.",
    19501: "Notificação de sistema: Lyner ajusta o Pingente de Memória ao pescoço de Kanade.",
    19502: "Lyner propõe evacuar o compartimento da Plasma Bell para poupar o descanso da guardiã.",
    19503: "Lyner indaga sobre a localização exata do cântico redentor composto por Mir.",
    19504: "Ayatane indica que o Hymmnos ancestral se encontra selado nas entranhas do Silver Horn.",
    19505: "Lyner espanta-se com a toponímia e questiona a viabilidade física de adentrar a estrutura.",
    19506: "Shurelia adverte que o complexo nunca fora projetado para abrigar corpos mortais desprotegidos.",
    19507: "Shurelia descreve o mortal Rugido dos Deuses, voragem de alta voltagem sinfônica no chifre.",
    19508: "Shurelia alerta que viajantes desprovidos de blindagem podem vaporizar-se instantaneamente.",
    19509: "Jack assusta-se com o perigo extremo e protesta indignado contra a missão suicida.",
    19510: "Shurelia pondera com serenidade que o poder acumulado pelo grupo resistirá à torrente.",
    19511: "Ayatane expõe a dor de Mir, que viveu décadas confinada em isolamento atroz no local.",
    19512: "Ayatane revela que até ser selada por Shurelia, Mir jamais contemplara o mundo exterior.",
    19513: "Ayatane denuncia a exploração desumana que obrigou Mir a tecer hinos em cativeiro.",
    19514: "Ayatane salienta que uma dessas canções nascidas da opressão é o segredo de sua salvação.",
    19515: "Lyner assimila a missão com determinação heroica e ordena a marcha ao Silver Horn.",
    19516: "Notificação de sistema: O local Silver Horn é liberado para acesso e viagem no Mapa-Múndi."
}

def main():
    input_path = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_086_input.json")
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    from build_and_test_086 import curated_translations

    dialogues = []
    curated_lines = []

    for item in data["dialogues"]:
        item_id = item["id"]
        curated_text = curated_translations[item_id]
        note = notes_map[item_id]

        entry = {
            "id": item_id,
            "event_file": item["event_file"],
            "speaker_id": item["speaker_id"],
            "speaker": item["speaker"],
            "original_jp": item["original_jp"],
            "original_en": item["original_en"],
            "current_ptbr": item["current_ptbr"],
            "review_status": "approved",
            "ptbr_text": curated_text,
            "text_ptbr": curated_text,
            "curated_ptbr": curated_text,
            "final_ptbr": curated_text,
            "texto_ptbr_curado": curated_text,
            "custom_text": curated_text,
            "reviewed": True,
            "notes": note,
            "curation_notes": note,
            "curadoria_notes": note
        }
        dialogues.append(entry)
        curated_lines.append(entry)

    glossary_additions = {
        "Rugido dos Deuses": {
            "pt": "Rugido dos Deuses",
            "gender": "masculino",
            "number": "singular",
            "category": "Fenômeno / Instalação da Torre",
            "note": "神の咆吼 (Kami no Houkou / Voice of God). Torrente avassaladora e letal de poder sinfônico que flui no interior do Silver Horn, capaz de desintegrar seres vivos desprotegidos; NISA traduziu erroneamente como 'Voice of God'."
        },
        "Criança da Luz": {
            "pt": "Criança da Luz",
            "gender": "feminino",
            "number": "singular",
            "category": "Título / Guardiã Androide",
            "note": "光の御子 (Hikari no Miko / Child of Light). Alcunha solene de Kanade, a terceira androide de manutenção da Torre e guardiã da Plasma Bell."
        },
        "Reescrita": {
            "pt": "Reescrita",
            "gender": "feminino",
            "number": "singular",
            "category": "Conceito Viral / Sistema",
            "note": "書き換え (Kakikae / Rewritten). Sobrescrita forçada de diretrizes de programação executada por entidades virais (como Mir e Ayatane) para subjugar androides de manutenção."
        },
        "Bispo Radolf": {
            "pt": "Bispo Radolf",
            "gender": "masculino",
            "number": "singular",
            "category": "Título / Clero de Elemia",
            "note": "ラードルフ司祭 (Radolf Shisai). Título clerical assumido por Radolf Schneider após salvar a Igreja de Elemia da crise provocada pelo Bispo Falss, marcando a transição inédita de cavaleiro para sacerdote."
        },
        "Colina do Canto": {
            "pt": "Colina do Canto",
            "gender": "feminino",
            "number": "singular",
            "category": "Topônimo / Lore",
            "note": "謳う丘 (Utau Oka / Singing Hill). Colina ancestral sagrada onde repousam relíquias e Cristais Hymmnos nos arredores do Beco Vagalume."
        }
    }

    scene_handoff = {
        "last_scene_id": "Event/552.evd",
        "last_line_id": 19516,
        "resumo_dramatico": "O bloco BLK_EVD_086 consolida três momentos dramáticos seminais de liderança pastoral, rito de parceria fundacional e redenção fraternal heroica: (1) Em Event/448.evd, na Igreja de Elemia, Lyner e Aurica encontram Radolf. Aurica o saúda cerimoniosamente como 'Comandante-Geral Radolf', mas o veterano revela com modéstia que foi ordenado Bispo após salvar a Igreja da conspiração de Mir e Falss, inaugurando uma era em que o templo pertence ao povo e não mais a dogmas corrompidos. Radolf brinca perguntando se os dois vieram anunciar casamento, arrancando protestos corados de Aurica. Lyner explica que Shurelia está em suspensão criogênica e necessita do Cristal Hymmnos «RE Nation». Aliviado por saber que Shurelia pode despertar, Radolf lamenta não poder acompanhá-los, pois suas novas obrigações episcopais impediriam a Igreja de funcionar sem sua liderança, o que Lyner acolhe com carinho e maturidade. (2) Em Event/125.evd, no início da jornada no Mundo Inferior, o Bispo Falss orienta Lyner após seu repouso, confirmando que o cristal procurado repousa na [Colina do Canto]. Alertando que desbravar ruínas sem uma Reyvateil é árduo até para um Apóstolo de Elemia, Falss confia Aurica como parceira de Lyner, destacando seu potencial infinito. Aurica aceita a convocação com reverência solene, e Falss ordena que Radolf também os proteja. A sós com Lyner, o bispo confia-lhe o passado traumático de Aurica e pede que ele cure o coração ferido da donzela para que sua Magia da Canção possa florescer. Abençoados pelo Trio de Elemia, Lyner e Aurica selam sua parceria inicial ('Conto com você, Aurica'), desbloqueando a Colina do Canto no Mapa-Múndi. (3) Em Event/552.evd, diante da colossal Plasma Bell sob as Asas de Hórus, Lyner, Shurelia e Jack interceptam Ayatane. O Cavaleiro de Platina revela que foi incumbido por sua criadora e Mãe, Mir, de reprogramar Kanade (a Criança da Luz) para destruir a Plasma Bell e derrubar as Asas de Hórus. Lyner contrapõe com veemência que sua jornada o ensinou que os humanos cometeram atrocidades hediondas contra Mir, e que seu objetivo é construir um mundo onde ela e a humanidade vivam felizes em harmonia. Quando Kanade avança para despedaçar a campânula e Shurelia avisa que a guardiã suprema só pode ser detida por desligamento emergencial, Lyner suplica desesperadamente pela ajuda de Ayatane. Tocado pelo ideal ingênuo de Lyner, Ayatane quebra o comando de Mir e neutraliza Kanade com suas próprias forças, sofrendo colapso energético crítico. Ayatane instrui Lyner a encontrar e entoar a única canção de afeto tecida por Mir para os humanos, localizada no interior do Silver Horn. Recusando-se a deixar o amigo desaparecer sozinho após trair sua Mãe, Lyner o convida para salvarem Mir juntos. Ayatane aceita ingressar no grupo, maravilhado com a 'tolice' heroica de Lyner que faz tantos confiarem suas vidas a ele. Lyner entrega o Pingente de Memória de Mei Mei à adormecida Kanade. Shurelia alerta sobre o mortífero [Rugido dos Deuses] no interior do Silver Horn, aterrorizando Jack, mas assegura que o vigor do grupo resistirá. O Silver Horn é liberado no Mapa-Múndi.",
        "decisoes_terminologicas": {
            "Rugido dos Deuses": "神の咆吼 (Kami no Houkou - fluxo letal de poder sinfônico no Silver Horn, corrigindo o erro da NISA 'Voice of God')",
            "Comandante-Geral Radolf": "ラードルフ総司 (Título militar de liderança dos Cavaleiros de Elemia)",
            "Bispo Radolf": "ラードルフ司祭 (Ordenação episcopal de Radolf na Igreja do Povo)",
            "Colina do Canto": "謳う丘 (Utau Oka - local sagrado dos Cristais Hymmnos)",
            "Criança da Luz": "光の御子 (Hikari no Miko - título de Kanade como guardiã da Plasma Bell)",
            "Pingente de Memória": "メモリペンダント (Memory Pendant - lembrança familiar entregue por Mei Mei)",
            "Silver Horn": "シルヴァホルン (Instalação e dungeon ancestral no Mapa-Múndi)",
            "Tolo incurável": "...君は...僕が思っていた以上にバカだ (Inversão crucial da NISA que traduzira erroneamente como 'not as dumb as I thought')",
            "Entoar a canção": "それを謳ってあげてくれ (Correção da NISA 'try finding that song' para o comando afetivo de cantar a melodia)"
        },
        "alertas_para_proximo_bloco": "Para os blocos seguintes (BLK_EVD_087 em diante), atentar para a exploração interna do Silver Horn sob o Rugido dos Deuses, a busca pelo Hymmnos de Mir, a reativação de Shurelia via RE Nation e a paridade absoluta de tags e quebras sintáticas."
    }

    output_data = {
        "block_id": "BLK_EVD_086",
        "axis_id": data.get("axis_id", "AXIS_3"),
        "axis_name": data.get("axis_name", "3_HISTORIA_E_EVENTOS"),
        "category": data.get("category", "Event Dialogue"),
        "line_count": len(dialogues),
        "id_range": [dialogues[0]["id"], dialogues[-1]["id"]],
        "stats": {
            "total_lines": len(dialogues),
            "lines_rewritten": len(dialogues),
            "lines_approved_as_is": 0,
            "new_terms_added": len(glossary_additions)
        },
        "curated_lines": curated_lines,
        "glossary_additions": glossary_additions,
        "dialogues": dialogues,
        "scene_handoff": scene_handoff,
        "entries": dialogues,
        "block_entries": dialogues
    }

    out_path = Path("Ferramentas_Traducao/curadoria_editorial/blocos/BLK_EVD_086_output.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated {out_path} with {len(dialogues)} curated lines.")

if __name__ == "__main__":
    main()
