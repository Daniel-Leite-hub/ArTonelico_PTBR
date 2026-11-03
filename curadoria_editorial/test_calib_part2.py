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
caps = {row[0]: row[1] for row in c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 32517 AND 32612").fetchall()}
orig_ens = {row[0]: row[1] for row in c.execute("SELECT id, original FROM dialogues WHERE id BETWEEN 32517 AND 32612").fetchall()}
conn.close()

PART2 = {
    32517: "É para equipar e acender a luz?",
    32518: "Ah, isso é perigoso! Afinal é o sol,CRé tão claro que prejudica a visão.",
    32519: "E ainda dá para chamar de lâmpada?CRChamar de lâmpada se não pode acenderCRé muito esquisito.",
    32520: "É que brilha demais! Só de carregarCRjá dá um bom efeito, então que mal tem?",
    32521: "Vidro de Fótons. É usado como espelhoCRno Corredor Musical.",
    32522: "Também serve para muitas outras coisas.CRÉ um excelente material para sintetizar.",
    32523: "É mesmo? Eu costumo usar apenasCRcomo espelho comum, mas é bem útil.",
    32524: "...Usar só como espelho comumCRme parece um desperdício.",
    32525: "Não entorta, não quebra nem amassa!CRO parafuso invencível: Parafuso Elétrico!",
    32526: "Não dá para cortar com espadaCRnem destruir com magia?",
    32527: "Impossível! A lâmina da espada quebraCRe você só vai cansar de gastar magia.",
    32528: "Entendo... Em tese, mesmo que o mundoCRexploda, este parafuso manterá a forma.",
    32529: "Hahaha, é bem por aí mesmo.",
    32530: "Reciclagem péssima.CRNada ecológico.",
    32531: "Opa! Não esperava uma alfinetadaCRdessas...",
    32532: "Além do mais, se é indestrutível,CRcomo conseguiu forjar e moldar isso?",
    32533: "Me rendo!CRDá uma folga, por favor...",
    32534: "Bússola Gravard pronta!CRTambém serve de controle para o Ramcluster.",
    32535: "A Bússola Gravard é imune a interferênciasCRou magnetismo. Ela aponta para as coordenadasCRabsolutas deste mundo.",
    32536: "No passado, era usada em mediçõesCRe vinha de fábrica nos navegadores.",
    32537: "Navi...? Coelho?",
    32538: "Esse é o Rabi.CRPiada bem forçada.",
    32539: "Droga, errei...",
    32540: "Mas... um coelhinho comCRBússola Gravard... até que eu queria...",
    32541: "Foi gostar disso?",
    32542: "Caixa de Fogo de Kant pronta!CRTodo fumante sonharia em ter uma!",
    32543: "Fumar faz mal à saúde.",
    32544: "Eu não fumo! Mas se precisarmosCRde fogo, acende na mesma hora.",
    32545: "Na verdade, se você pensar bem,CRum cigarrinho viraria cinza na hora.",
    32546: "Com esses ingredientes, em tese o calorCRchega a 800 graus, capaz de derreterCRaté metal.",
    32547: "Que coisa mais assustadora...",
    32548: "Mas é você quem fica criandoCRessas coisas assustadoras.",
    32549: "Fazer mero pó de polimentoCRjá perdeu toda a graça.",
    32550: "Mas ele é indispensávelCRpara o Grathmeld.",
    32551: "Serve como ingredienteCRpara inúmeras coisas.",
    32552: "...É verdade. Também ajuda bastanteCRna hora de forjar armas.",
    32553: "Harmonizador.CRÉ essencial ao criar amplificadores.",
    32554: "Uma pergunta para você, Lyner:CRO que esse amplificador amplifica?",
    32555: "Opa! É... poder mágico?",
    32556: "Bzzz! Errado!CRA resposta certa é \"fônica\"!",
    32557: "É, é isso! É a mesma coisa.CRSó muda o jeito de falar...",
    32558: "Muitos alunos tinham a mesma queixa.CRAí eu apontava outros erros e a notaCRdeles caía ainda mais.",
    32559: "Q-Que exemplo específico foi esse...?",
    32560: "A vida não é moleza.CRDecore bem: é \"fônica\".",
    32561: "Ímã Flanmelt pronto!",
    32562: "Parece um ímã vulgar, mas dá um trabalhoCRdanado de criar e quase não compensa!",
    32563: "Essa introdução foi bem comprida...",
    32564: "Mas é famoso! O Ímã Flanmelt foi criadoCRna Primeira Era pelo Professor Flanmelt.",
    32565: "Envolve Cristal de Ardel entre GrathnodeCRe Parameno. Em tese, tem efeito idênticoCRà Torre Ar tonelico, mas...",
    32566: "Fugia tanto da teoria da época que zombavamCRdele, chamando de \"Flanmelt Lapidador\".",
    32567: "Sua eficácia só foi reconhecida poucoCRantes do colapso da Primeira Era...",
    32568: "Se tivessem notado isso antes,CRa história teria sido bem diferente.",
    32569: "...Por exemplo, como?",
    32570: "Ué, por exemplo... ImagineCRAr tonelico na palma da mão.",
    32571: "Quer dizer que... só de eu ter conseguidoCRfazer isso já é algo incrível?!",
    32572: "Sem dúvida alguma. Dominou o GrathmeldCRa um nível admirável. Merece meu respeito.",
    32573: "Ah, não é para tanto... Hahaha!",
    32574: "Mas tem uma coisa estranha: eu não useiCRGrathnode, Parameno nem Cristal de ArdelCRquando fiz isso.",
    32575: "Lyner... isso é falsificação pura!CREstou decepcionada com você.",
    32576: "E-Eu só segui o cartão da receita!CRNão precisa ficar tão decepcionada...",
    32577: "Isto é Yuteria, certo?CRTransformou em um fio?",
    32578: "Na verdade, é uma corda.CRServe para instrumentos de corda.",
    32579: "Para instrumentos? A Yuteria serveCRpara esse tipo de coisa?",
    32580: "É muito resistente. Pode ser útil pra fazerCRoutras coisas além de instrumentos.",
    32581: "...Que fedor!CRIsso é Suco de Nyo? Guts?",
    32582: "Nem pense em beber.CRÉ fertilizante de petrárvores.",
    32583: "Petrárvores? As de Em Pheyna?",
    32584: "Leva Cogumelo-Trovão, então se beberCRvai passar muito mal.",
    32585: "...Eu não ia beber! Mas devia amenizarCRo fedor de Nyo? Guts.",
    32586: "Impressão minha ou ouvi um estrondoCRenorme enquanto você sintetizava?",
    32587: "Detonei uma bomba daquelas!CRSó assim para dar certo.",
    32588: "E foi assim que fez esse algodão...",
    32589: "Pois é! Nada mais revigorante do queCRcriar um item assim!",
    32590: "O povo da Terceira Era é ousado demais.CRDesde que comecei a viajar com você,CRvivo me surpreendendo.",
    32591: "...Este é o revestimento externo usadoCRnos andares superiores de Ar tonelico...",
    32592: "Usam em aeronaves e tambémCRpara forjar armas.",
    32593: "É mesmo? Usam para tanta coisa...",
    32594: "É bem resistente.CRServe para quase tudo.",
    32595: "Pano Remendado pronto!",
    32596: "...Isso é algo para se comemorar?CRNão é só um trapo velho?",
    32597: "Ele é muito útil!CRVocê ainda vai se surpreender.",
    32598: "Olha... não use isso nas minhas roupas.CRDispenso esse tipo de surpresa.",
    32599: "Um... bicho de pelúcia?",
    32600: "Sim! Parece mais costuraCRdo que Grathmeld.",
    32601: "É um manto de tigre bem fofo.",
    32602: "O nome dele é Don Leon.CRVocê não vai trocar, né...?",
    32603: "É tão fofinho... Queria um...CRNão, esquece.",
    32604: "Peça flutuante: Nadadeira!",
    32605: "Usam em aeronaves, mas é raroCRver apenas essa peça avulsa.",
    32606: "Sabe a teoria de sustentação da Nadadeira?CREla amplifica a sutil flutuação inerenteCRà pedra cantora.",
    32607: "Ao cruzar a fônica em planos ortogonais,CRa pedra gera empuxo vertical. Quanto maiorCRo vetor, mais intensa a força...",
    32608: "Ao girar em alta velocidade, o vetor que cortaCRa fônica cresce, aumentando a sustentação.",
    32609: "Tinha toda essa teoria por trás?!",
    32610: "...Achou que era mágica?",
    32611: "Achei que voava que nem frisbee...",
    32612: "Que mente fascinante a sua..."
}

overflows = 0
gate_errors = 0
for did, text in sorted(PART2.items()):
    cap = caps[did]
    sz = encoded_size(text)
    if sz > cap:
        overflows += 1
        print(f"OVERFLOW {did}: {sz}B > {cap}B (+{sz - cap}B) -> {text}")
    errs = validate_line(did, orig_ens[did], text)
    if errs:
        gate_errors += 1
        print(f"GATE ERR {did}: {errs} -> {text}")

print(f"Part 2 result: {overflows} overflows, {gate_errors} gate errors.")
