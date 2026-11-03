# -*- coding: utf-8 -*-
"""Calibração e redação editorial de Chunk 6 (IDs 31509 a 31556)."""
import json, sqlite3, sys
sys.path.insert(0, 'Ferramentas_Traducao')
sys.path.insert(0, 'Ferramentas_Traducao/tools')
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

conn = sqlite3.connect('Ferramentas_Traducao/ArTonelico_PTBR.atproj')
c = conn.cursor()

with open('Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_039_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

dialogues = {d['id']: d for d in data['dialogues']}

CHUNK_6 = {
    31509: ("Por quê?", "Pergunta ingênua de Lyner eliminando o estouro de +3B (17B/24B)."),
    31510: ("I-isso não é coisa pra eu falar!CRPense por conta própria!", "Timidez envergonhada de Aurica eliminando o estouro de +28B (118B/144B)."),
    31511: ("...O que ela tá pensando?", "Lyner desconfiado com o subtexto (48B/56B)."),
    31512: ("Dúvida sincera: isso é feitoCRcom a solução negra, né?", "Pergunta prática de Aurica sobre os ingredientes (118B/168B)."),
    31513: ("Claro. E o resto é cristal Grathnode.", "Lyner detalhando os componentes (82B/96B)."),
    31514: ("Ou seja: o frasco é de GrathnodeCRe dentro tem solução negra?", "Aurica deduzindo a estrutura do artefato eliminando o estouro de +7B (124B/184B)."),
    31515: ("Então não dava só pra jogar a soluçãoCRnum frasco comum e atirar?", "Questionamento cômico de Aurica eliminando o estouro de +26B (114B/136B)."),
    31516: ("Mudar o visual é bem melhor!CRAlém de parecer mais forte.", "Lyner defendendo a estética bélica (129B/160B)."),
    31517: ("Aparência importa, admito.CREntão vamos dar um nome à altura.", "Aurica concordando com o capricho estético eliminando o estouro de +10B (124B/168B)."),
    31518: ("“Paralzy Pot”.CRFofo, não?", "Batismo meigo do pote paralisante (52B/80B)."),
    31519: ("Ai, isso dá um medo...", "Receio espontâneo diante do projétil eliminando o estouro de +2B (48B/56B)."),
    31520: ("Ele reage à canção e avança com tudo.CRDá medo mesmo.", "Lyner explicando o disparo acústico eliminando o estouro de +24B (108B/152B)."),
    31521: ("Dá medo na cabeça, mas no estômagoCRouvi dizer que dói demais!", "Aurica comentando o impacto brutal no plexo solar (122B/232B)."),
    31522: ("Nocaute na certa!CRQuem passou por isso me contou.", "Relato direto de Aurica eliminando o estouro de +44B (86B/176B)."),
    31523: ("...Eu ficaria tão em choqueCRque nem cantava mais.", "Lyner empatizando com a dor eliminando o estouro de +19B (89B/104B)."),
    31524: ("Dá pra criar até flauta?CRSó a cor que me incomoda...", "Aurica surpresa com a flauta eliminando o estouro de +4B (96B/144B)."),
    31525: ("Não é flauta comum.CRUm toque e o inimigo morre!", "Aviso sombrio de Lyner eliminando o estouro de +25B (89B/168B)."),
    31526: ("...Você criou algo bem tenebroso.", "Aurica chocada com a arma mortal (74B/88B)."),
    31527: ("Também acho.CRDevia virar armeiro de vez...", "Lyner refletindo sobre o talento bélico eliminando o estouro de +9B (89B/168B)."),
    31528: ("Boa ideia! Já que faz até estaCR“Flauta do Demônio”...", "Aurica batizando a flauta macabra (95B/152B)."),
    31529: ("O Raio de Transe cura muito MP,CRmas parece meio vazio.", "Aurica avaliando a frieza mecânica do item eliminando o estouro de +17B (112B/144B)."),
    31530: ("Costume com a Tranquilidade?", "Indagação de Lyner eliminando o estouro de +10B (64B/80B)."),
    31531: ("Pode ser, mas parece uma recargaCRtão mecânica...", "Aurica expressando o incômodo com a falta de afeto (86B/112B)."),
    31532: ("Uma recarga sem vida e sem gosto.CRNão consigo gostar disso...", "Desdém de Aurica pela impessoalidade tecnológica (122B/160B)."),
    31533: ("Um nome bonito ameniza isso:CRque tal “Curador Cósmico”?", "Batismo acolhedor de Aurica (108B/160B)."),
    31534: ("Amplificador de Reflexão Mudo!CRO Harmogauge vai disparar!", "Apresentação técnica por Lyner eliminando o estouro de +31B (114B/152B)."),
    31535: ("Olhando assim, ninguém dizCRque é algo tão incrível.", "Aurica admirada com a discrição do artefato (92B/120B)."),
    31536: ("Eu mesmo fiz, mas nem seiCRcomo funciona o mecanismo.", "Lyner admitindo a surpresa com a própria criação (118B/160B)."),
    31537: ("Se analisar, dá pra entender.CRÉ um Grathmeld bem avançado!", "Aurica valorizando a alta alquimia eliminando o estouro de +15B (124B/200B)."),
    31538: ("Merece um nome estiloso:CRque tal “Excellen Harmo”?", "Batismo harmônico de Aurica eliminando o estouro de +34B (96B/160B)."),
    31539: ("Pronto! Não é algo que eu queiraCRusar direto, mas tá feito.", "Lyner concluindo o item de emergência eliminando o estouro de +13B (118B/168B)."),
    31540: ("Mas ter isso dá um alívio.CRPrevenir nunca é demais.", "Aurica apreciando a segurança eliminando o estouro de +6B (102B/176B)."),
    31541: ("Entendo a parte do luto,CRmas o que significa “alegria”?", "Dúvida de Lyner sobre a inscrição da fórmula (114B/152B)."),
    31542: ("Se estiver sofrendo,CRuse isto e se alegre!", "Aurica decifrando o lema curativo eliminando o estouro de +14B (77B/120B)."),
    31543: ("Entendi! Vai se chamarCR“Millennium Heal”. É de luxo!", "Batismo soberbo de Aurica eliminando o estouro de +11B (110B/128B)."),
    31544: ("Núcleo Restaurador pronto!", "Apresentação do remédio por Lyner eliminando o estouro de +25B (62B/88B)."),
    31545: ("Item de cura nunca é demais.CRDá pra usar até na batalha.", "Aurica elogiando a utilidade eliminando o estouro de +1B (108B/152B)."),
    31546: ("Pior que não dá pra usar em combate.", "Aviso desapontado de Lyner eliminando o estouro de +12B (82B/128B)."),
    31547: ("É complexo demais. Se tentar na luta,CRa gente é derrotado na hora!", "Lyner alertando sobre o risco tático eliminando o estouro de +25B (134B/184B)."),
    31548: ("Não é pra se gabar disso!CRDevia ter feito outro item, então.", "Bronca cômica de Aurica eliminando o estouro de +28B (124B/176B)."),
    31549: ("E eu tão animada...CRQue decepção.", "Frustração de Aurica com a restrição de uso eliminando o estouro de +7B (70B/88B)."),
    31550: ("Mas serve onde não dá pra acampar...", "Lyner tentando justificar a utilidade do núcleo eliminando o estouro de +7B (92B/128B)."),
    31551: ("Deu um trabalhão pra criar...CRMas o que é isso afinal?", "Aurica encarando a forma esquisita da bomba (112B/144B)."),
    31552: ("Ah... Ar tonelico?", "Lyner hesitante diante da criação (43B/48B)."),
    31553: ("...Por que a dúvida?", "Estranhamento de Aurica eliminando o estouro de +11B (44B/56B)."),
    31554: ("Nem eu entendi direito...CRSó sei que na receita dizia “perigo”.", "Lyner confessando o mistério eliminando o estouro de +3B (114B/152B)."),
    31555: ("Essa bola bizarraCRé tão perigosa assim?", "Dúvida atônita de Aurica eliminando o estouro de +39B (78B/88B)."),
    31556: ("Sei que é uma bomba,CRmas fora isso não sei de nada...", "Lyner admitindo o limite do conhecimento bélico (109B/136B).")
}

overflows = 0
validation_errors = 0

for d_id, (txt, note) in sorted(CHUNK_6.items()):
    c.execute('SELECT original_bytes FROM dialogues WHERE id = ?', (d_id,))
    ob = c.fetchone()[0]
    sz = encoded_size(txt)
    diff = sz - ob
    orig_en = dialogues[d_id]['original_en']
    errs = validate_line(d_id, orig_en, txt)
    if diff > 0:
        print(f"ERRO DE ESTOURO ID 31509 + {d_id}: Cap {ob}B | Sz {sz}B (+{diff}B) | {txt}")
        overflows += 1
    if errs:
        print(f"ERRO DE VALIDAÇÃO ID {d_id}: {errs} | {txt}")
        validation_errors += 1

print(f"\n--- Resultado Chunk 6 ---")
print(f"Total de falas: {len(CHUNK_6)}")
print(f"Estouros de buffer: {overflows}")
print(f"Erros de validação: {validation_errors}")
if overflows == 0 and validation_errors == 0:
    print("[PERFEITO] Chunk 6 aprovado 100%!")
