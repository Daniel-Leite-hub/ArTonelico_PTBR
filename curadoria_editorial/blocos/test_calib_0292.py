import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0292 = {
    27170: 200, 27171: 128, 27172: 176, 27173: 112, 27174: 104, 27175: 192,
    27176: 224, 27177: 48, 27178: 168, 27179: 80, 27180: 208, 27181: 168,
    27182: 160, 27183: 192, 27184: 80, 27185: 216, 27186: 56, 27187: 128,
    27188: 112, 27189: 184, 27190: 24, 27191: 48, 27192: 112, 27193: 104
}

calib_0292 = {
    27170: ("Imagina! Mas o que você acha que iaCRacontecer se eu andasse grudadaCRem você assim todo dia?", "Misha rindo do escândalo de andar colada a Lyner em público com CRs. (189B <= 200B)"),
    27171: ("...Não sei bem, mas sinto queCRia sobrar feio pra mim.", "Lyner temendo represálias com CR. (106B <= 128B)"),
    27172: ("Viu só? Por isso fico tão felizCRde conversar a sós com você,CRsem ninguém por perto.", "Misha valorizando o refúgio a dois com CRs. (176B <= 176B)"),
    27173: ("É, mas... você não tá coladaCRdemais em mim, não?", "Lyner sentindo o calor do abraço com CR. (96B <= 112B)"),
    27174: ("Nem vem! É minha chanceCRde ter você só pra mim!", "Misha defendendo a exclusividade afetiva com CR. (100B <= 104B)"),
    27175: ("Você me deu a Hama, Lyner,CRmas nunca tocou uma música nelaCRnem me ouviu tocar, né?", "Misha puxando assunto sobre a ocarina Hama com termo canônico e CRs. (153B <= 192B)"),
    27176: ("Hã? É, bem lembrado.CRDepois de esculpir, eu só soprei,CRmas não foi bem uma música...", "Lyner lembrando a confecção artesanal de Hama com CRs. (161B <= 224B)"),
    27177: ("...Tava desafinada?", "Lyner perguntando com receio da afinação da ocarina. (41B <= 48B)"),
    27178: ("Que nada! Tanto a de agoraCRquanto a de antigamente ficaram perfeitas!", "Misha elogiando calorosamente o talento de Lyner com CR. (138B <= 168B)"),
    27179: ("Não precisa dessa caraCRpreocupada!", "Misha tranquilizando Lyner com afeto e CR. (72B <= 80B)"),
    27180: ("Ufa... que alívio.CRNão entendo nada de música, entãoCRjamais saberia tocar uma ocarina...", "Lyner aliviado por não ter desafinado a ocarina com CRs. (166B <= 208B)"),
    27181: ("...O mistério é por que você cismouCRde esculpir uma ocarina do nada?", "Misha intrigada com a inspiração original de infância com CR. (138B <= 168B)"),
    27182: ("Se esquentar, é pior.CREu devia gostar de ocarinaCRna época, só isso.", "Lyner desconversando com humor simples com CRs. (142B <= 160B)"),
    27183: ("Dizer 'devia' sobre você mesmo...CRBem, é bem a sua cara falar isso, Lyner.", "Misha rindo do jeito despreocupado de Lyner com CR. (150B <= 192B)"),
    27184: ("Ué? Isso foi uma ofensaCRdisfarçada?", "Lyner desconfiando do elogio irônico com CR. (68B <= 80B)"),
    27185: ("Se esquentar, é pior!CRBem, que tal eu tocar a Hama hojeCRdepois de tanto tempo?", "Misha propondo uma melodia com Hama com CRs. (149B <= 216B)"),
    27186: ("Você sabe tocar direito?", "Lyner perguntando com curiosidade genuína. (51B <= 56B)"),
    27187: ("Que grosseria! Eu treinei todo diaCRdesde que ganhei de você!", "Misha ofendida e orgulhosa de sua prática diária com CR. (116B <= 128B)"),
    27188: ("Típico de uma aluna exemplar.CREntão toca uma pra mim.", "Lyner elogiando a dedicação de Misha com CR. (106B <= 112B)"),
    27189: ("Sim... Ah, já sei!CREm agradecimento por ter feito ela,CRdeita a cabeça aqui rapidinho?", "Misha convidando Lyner para o colo hizamakura com CRs. (177B <= 184B)"),
    27190: ("Hã?! Eita!!", "Lyner puxado repentinamente para o colo de Misha. (21B <= 24B)"),
    27191: ("Gostou do meu colo?", "Misha oferecendo seu colo aconchegante com doçura. (39B <= 48B)"),
    27192: ("Foi meio bruto, forçadoCRe atrevido demais...", "Lyner sem ar no colo de Misha com CR. (81B <= 112B)"),
    27193: ("Não ouvi um único elogioCRnisso aí, sabia?", "Misha fazendo bico dengoso pela falta de elegância dele com CR. (79B <= 104B)")
}

all_ok = True
for tid, (txt, rat) in calib_0292.items():
    maxb = max_map_0292[tid]
    sz = encoded_size(txt)
    diff = sz - maxb
    if diff > 0:
        all_ok = False
        print(f"OVERFLOW ID {tid}: {sz}B > {maxb}B (+{diff}) -> {txt}")
    else:
        errs = validate_line(tid, "", txt)
        if errs:
            all_ok = False
            print(f"ERRO VALIDACAO ID {tid}: {errs} -> {txt}")
        else:
            print(f"OK ID {tid}: {sz}B <= {maxb}B")

if all_ok:
    print("=== 0292 100% PERFEITO ===")
