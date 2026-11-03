import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "tools"))

from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line
import json, sqlite3

cfg = json.load(open(BASE_DIR / "curadoria_editorial/curadoria_config.json", "r", encoding="utf-8"))
conn = sqlite3.connect(cfg["database_path"])
c = conn.cursor()
caps = {row[0]: row[1] for row in c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 32613 AND 32708").fetchall()}
orig_ens = {row[0]: row[1] for row in c.execute("SELECT id, original FROM dialogues WHERE id BETWEEN 32613 AND 32708").fetchall()}
conn.close()

PART3 = {
    32613: "Ramcluster concluído!",
    32614: "Inseriu a Bússola Gravard?",
    32615: "Claro! Senão seria impossívelCRcontrolar o voo.",
    32616: "Mas estou bem surpresa... Você conseguiuCRcriar o motor daquela aeronave selada.",
    32617: "Na época em que o Juramento de ElemiaCRera rigoroso, isso seria impossível.",
    32618: "O Flute teria nos atacado cem vezesCRenquanto a gente tentava montar isso.",
    32619: "Até mais... Teria explodidoCRa cidade inteira conosco.",
    32620: "Núcleo de Partilha pronto!",
    32621: "O compressor fônico da aeronave...",
    32622: "Sabia que este núcleo gera, num instante,CRpressão fônica que nem a Torre suportaria?",
    32623: "...E aguenta tanta força?",
    32624: "É a única utilidade dele.CRNão tem outro efeito e, na verdade,CRa aeronave voa mesmo sem isso.",
    32625: "Depois de todo o trabalho que tive,CRnão dá para ouvir isso numa boa.",
    32626: "Fazer ocarina é tão difícil...CROu será que qualquer instrumento é?",
    32627: "Provável. Deve ter sido bem difícilCRacertar a posição dos furos, né?",
    32628: "Pois é. Se não seguir a receita à risca,CRo tom da nota pode desafinar...",
    32629: "E os materiais deram trabalho: quebreiCRuma espada e usei Canção Enlatada...",
    32630: "Usou tanta coisa... Uma pilha de materiaisCRque nem deveria caber numa peça tão pequena.",
    32631: "Deu tanto trabalho que devia se chamarCR\"Superocarina\"...",
    32632: "Ela só funciona como ocarina normal,CRentão seria exagero.",
    32633: "Tripolar?! Lyner, por queCRfez um dispositivo tripolar?!",
    32634: "P-Por quê?... Era a única receitaCRque eu tinha...",
    32635: "...Céus! O que você foi inventar?!",
    32636: "D-Desculpe... Mas é tão perigoso?",
    32637: "N-Não é isso... é que...",
    32638: "Meu protótipo, o gene Master Spectrum,CRfoi cultivado numa câmara com essaCRmesma tecnologia...",
    32639: "Entendi... Era como o seu berço.",
    32640: "...É...",
    32641: "Mas por que reagiu em pânico,CRcomo se fosse algo proibido...?",
    32642: "É que... fico sem jeito...",
    32643: "Consegui!CRFoi bem trabalhoso forjar isso...",
    32644: "Um forno de fusão com calor superiorCRao da Caixa de Fogo de Kant!",
    32645: "Lyner... se tombar isso aceso, aconteceráCRuma tragédia. Tome muito cuidado!",
    32646: "...O que aconteceria?",
    32647: "Vai derreter o solo, perfurar o continenteCRe afundar abaixo do Mar de Nuvens.",
    32648: "Chegaria a esse ponto!?",
    32649: "Até eu me surpreendo por ter conseguidoCRcriar uma coisa dessas...",
    32650: "Lyner, seu tarado!",
    32651: "Não estou entendendo nada...",
    32652: "Não fique criando as fibras nervosasCRque correm pelo meu corpo...",
    32653: "Seus nervos usam isso?",
    32654: "...É... usam.",
    32655: "Nossa, isso fica dentro de você...",
    32656: "Kyaaa!CRNão me encare desse jeito!",
    32657: "Eu sintetizei, mas afinal...CRO que significa D3?",
    32658: "São as iniciais deCR\"Drooly Doopy Doom\".",
    32659: "...Sério?",
    32660: "...Brincadeira.CRPor que não percebeu?",
    32661: "Hum, bem... Achei que talvez houvesseCRuma chance de ser verdade...",
    32662: "Na verdade, é a Célula Di-Dron Dinoxina.CRUma variante quimicamente alterada da D2,CRa Célula Dron Dinoxina.",
    32663: "\"Drooly Doopy Doom\"CRestá ótimo! Sim!",
    32664: "Puxa vida... Você anda meio estranhoCRultimamente, Lyner...",
    32665: "Acho que quem está estranha é você...CRMas o que tem de errado nisso?",
    32666: "Por que fica forjando partesCRdo meu próprio corpo?",
    32667: "Isto faz parte do seu corpo...?",
    32668: "Sim... E de uma parteCRmuito importante...",
    32669: "P-Parte importante...",
    32670: "...É o equivalente ao cérebro!CRNão vá pensar besteira, ouviu?CREstá me ouvindo?",
    32671: "Hã?! C-Claro! Imagina! Hahaha!",
    32672: "Divisor FFT pronto!",
    32673: "É impressionante ter criado isto,CRmas tenha cautela extrema ao usar.",
    32674: "Na receita dizia que era parte de algoCRterrível. É por causa disso?",
    32675: "Exatamente. Pode se tornar algo terrível,CRdependendo de como você decidir usá-lo.",
    32676: "Chame de \"Perigo Extremo\" para queCRtodos saibam que não se deve brincar.",
    32677: "Até eu fiquei com medo de tocar...",
    32678: "Aposto 100 Leafs que você criouCRsem nem saber o que era.",
    32679: "Não entro numa aposta perdida dessas!CRÉ óbvio que não faço ideia do que é.",
    32680: "Imaginei.",
    32681: "O Quantizador alinha o fluxo e a direçãoCRdos componentes fônicos, mantendo estáveisCRa vazão e a pressão por unidade de tempo.",
    32682: "Saquei!",
    32683: "...E serve para quê?",
    32684: "Você não deveria perguntar isso!",
    32685: "\"Plugue Fônico\"... Já ouvi esse nomeCRem algum lugar. O que era mesmo?",
    32686: "Dica 1: Kyle Clancy.",
    32687: "Dica 2: Cópia da ELMA.",
    32688: "...Hum...",
    32689: "Dica 3: Onde levei o LeardCRquando o sequestrei...",
    32690: "Ah, é o Altar dos Apóstolos!",
    32691: "Tinha que lembrar logo por essa dica...?",
    32692: "Tanto este item quanto o Altar usamCRplugues de faísca. Conduzem a fônicaCRpelo ar e geram uma pressão brutal.",
    32693: "É tipo uma arma de choque?",
    32694: "É parecido, mas quem usar vai presoCRpor assassinato na hora.",
    32695: "Disco Grathnode DH pronto!",
    32696: "Foi difícil de forjar, não foi?CROs ingredientes são muito raros.",
    32697: "Melhor do que fazer coisa boba.CRSe for fácil demais, perco o interesse.",
    32698: "Sinal de que pegou gosto pelo Grathmeld.CR...Mas nada de criar perigos por aí!",
    32699: "Não vou fazer nada perigoso.",
    32700: "Pode não ter notado, mas este discoCRjá é perigoso por si só.",
    32701: "Hã?! Isto aqui?",
    32702: "Você não sabe de nada mesmo... É idênticoCRaos Discos de Grathnode flutuandoCRno céu de Platina.",
    32703: "Sabe que a Primeira Era acabouCRquando eles se estilhaçaram, né?",
    32704: "C-Claro que sei! Então se issoCRse partir, teremos um problemão...",
    32705: "Causará um Grathnode Inferiorzinho.",
    32706: "Pensando bem, \"Grathnode Inferior Petit\"CRsoa mais bonitinho...",
    32707: "Tanto faz o nome...",
    32708: "Faltam itens para criar %s..."
}

overflows = 0
gate_errors = 0
for did, text in sorted(PART3.items()):
    cap = caps[did]
    sz = encoded_size(text)
    if sz > cap:
        overflows += 1
        print(f"OVERFLOW {did}: {sz}B > {cap}B (+{sz - cap}B) -> {text}")
    errs = validate_line(did, orig_ens[did], text)
    if errs:
        gate_errors += 1
        print(f"GATE ERR {did}: {errs} -> {text}")

print(f"Part 3 result: {overflows} overflows, {gate_errors} gate errors.")
