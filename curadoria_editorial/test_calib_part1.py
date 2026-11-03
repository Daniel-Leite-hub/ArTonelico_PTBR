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
caps = {row[0]: row[1] for row in c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 32421 AND 32516").fetchall()}
orig_ens = {row[0]: row[1] for row in c.execute("SELECT id, original FROM dialogues WHERE id BETWEEN 32421 AND 32516").fetchall()}
conn.close()

PART1 = {
    32421: "Chamam isso de traje de banquete, né?",
    32422: "É, só serve para essas ocasiões mesmo,CRmas tem uma defesa excelente.",
    32423: "Mesmo assim, acho bem estranhoCRusar isso no dia a dia.",
    32424: "Armadura Bushido.CRVocê sabe o que significa Bushido?",
    32425: "Já ouvi falar, mas não sou guerreira,CRentão não sei os detalhes...",
    32426: "Nem eu sei direito, mas isso aquiCRnão tem nada de Bushido.",
    32427: "...É só impressão minha, mas pareceCRum traje de \"Gerente Abastado\".",
    32428: "É isso!CREsse nome é perfeito!",
    32429: "E então? Me esforcei bastante.",
    32430: "Que trabalho minucioso.CRDeve ter dado um trabalhão.",
    32431: "Mas valeu a pena.CRTenho certeza de que será muito útil!",
    32432: "Além de aumentar o MP,CRtem vários outros efeitos.",
    32433: "Obrigada.CRQuero usar logo...",
    32434: "Que coroa enorme.CROu melhor... não é grande demais?",
    32435: "Pode ser um pouco pesada,CRmas tem um efeito formidável!",
    32436: "Parece uma abóbora... Mas se vocêCRquer que eu use, vou tentar...",
    32437: "Anel Grathnode pronto!CRAcelera o tempo de canto das canções!",
    32438: "O elemento base é o Grathnode...CREntendi a lógica por trás.",
    32439: "Usa a halação do canto para amplificarCRa fônica sutil, e com uma latênciaCRde nanossegundos...",
    32440: "...Enfim, é como se a Reyvateil tivesseCRduas bocas. Por isso parece que cantaCRcom o dobro de velocidade.",
    32441: "F-Ficou bem fácil de entender...CRmas também bem assustador...",
    32442: "Anel Parameno pronto!CRIsso corta o gasto de força mentalCRpela metade!",
    32443: "Usou Parameno, um ingrediente valioso.CRConduz a fônica do ar via halação eCRfunde-a ao corpo da Reyvateil, certo?",
    32444: "...Hã? Do que está falando?",
    32445: "Deixa para lá. Já vi queCRseu Grathmeld é puro instinto.",
    32446: "Lágrima Estelar pronta!",
    32447: "Que belo colar.CRAdoraria usá-lo...",
    32448: "Disse algo errado?",
    32449: "A-Ah, não! Não é isso...",
    32450: "É que... não sei se diria o mesmoCRse soubesse os ingredientes...",
    32451: "Hein?! O que quer dizer com isso?!",
    32452: "...Por que sinto uma aura assustadoraCRsaindo desse anel?",
    32453: "Pudera! Misturei Presa SupremaCRao Amuleto do Desamor.",
    32454: "Mas afinal, quem foi que inventouCResse \"Amuleto do Desamor\"?",
    32455: "S-Sei lá... Não fui eu que inventei.CRAlgum artesão deve ter varado noitesCRremoendo mágoas...",
    32456: "...\"Anel da Vingança\"CRnão seria bem melhor?",
    32457: "Aí vão achar que é um item amaldiçoado...",
    32458: "Quem diria que eu criariaCRuma Touca de Banho...",
    32459: "Touca de Banho?",
    32460: "Hã? Shurelia, você não sabeCRo que é Touca de Banho?!",
    32461: "Mas agora já entendi.CRÉ um chapéu usado no banho, certo?",
    32462: "Mas com essa touca a cabeça parece careca...CRE nem protege da luz do sol...",
    32463: "N-Não é para proteger do sol! É para lavarCRo cabelo. Aliás, em banheiros geralmenteCRnem bate sol...",
    32464: "E por que fez disso um acessório?",
    32465: "Pegou no ponto fraco...CREssa finta me pegou de jeito...",
    32466: "Lyner... sabe para que isso serveCRou fez sem pensar?",
    32467: "Ué? Bem, isso nos une maisCRe fortalece nossos laços...",
    32468: "Isso se amarra no dedo mindinho...CRMas não funciona sozinho. É preciso amarrarCRo mesmo fio no mindinho de duas pessoas...",
    32469: "É mesmo? Que complexo...CREntão amarro com o Radolf ou alguém.",
    32470: "N-Não faça isso!CRÉ perigoso demais!",
    32471: "Uau! Que susto!CRÉ algo tão perigoso assim...?",
    32472: "N-Não... é que você me fazCRpensar besteira...",
    32473: "É um item bem esquisito...",
    32474: "Um Cristal de Ardel, certo?",
    32475: "Sim.",
    32476: "Não foi difícil de criar? É bem delicadoCRtrabalhar para aumentar a pureza dele...",
    32477: "Ué? Não achei tão difícil assim.",
    32478: "...É mesmo? Não faz sentido...CRBem, vindo de você, deve ter feitoCRtudo sem nem perceber...",
    32479: "Mas afinal, o Ardel serve para algo sozinho?CRDeveria ser só um condutor de fônicaCRunidirecional...",
    32480: "Diz aqui... que ampliaCRa resistência a tudo...",
    32481: "S-Sério...?CRNão deve ser engano...?",
    32482: "Ou será que isso nem éCRCristal de Ardel de verdade?",
    32483: "N-Não me culpe! Eu também nãoCRentendo nada do que estou fazendo...",
    32484: "Esse é o problema! Se um venenoCRviesse com rótulo de remédio,CRvocê preparava e tomava sem pestanejar.",
    32485: "...Não posso negar.",
    32486: "Pronto! O Modar Febril, uma peçaCRfeita para engatar golpes críticos!",
    32487: "Você criou algo impressionante.",
    32488: "Que nada...",
    32489: "Não foi um elogio... Se usar isso,CRvocê vai ficar exausto, sabia?",
    32490: "Isso só mascara a fadiga. Parisa os nervosCRmusculares e injeta microcorrentesCRpara forçar o corpo...",
    32491: "Entendi que tem certas teorias no mundoCRque é bem melhor nem saber...",
    32492: "Anel Branco concluído!CRIsto impede o sono!",
    32493: "Um anel de Grathnode baseado em halação.CRPara você, aposto que é mais útil para passarCRa noite em claro do que em combate.",
    32494: "Boa ideia... Espera aí!CRPor que eu passaria a noite acordado?!",
    32495: "Ué? Porque você tem que virar noitesCRproduzindo itens úteis pra nós...",
    32496: "Logo eu...",
    32497: "Anel Verde! Equipando isso,CRveneno nenhum faz efeito.",
    32498: "Um anel de Grathnode que usa halação.CRO Grathnode serve para tanta coisa...",
    32499: "O que é essa tal halação?",
    32500: "As ondas do cristal GrathnodeCRconseguem penetrar o corpo humano.",
    32501: "Assim, o espectro do cristal se somaCRao espectro do corpo, como se uma novaCRcapacidade tivesse despertado em você.",
    32502: "Entendi. Então, nesse caso, ganha-seCRuma imunidade temporária a venenos.",
    32503: "S-Sim... exatamente. Que milagre vocêCRentender algo de primeira.",
    32504: "Lady Shurelia... não fica dando essasCRexplicações difíceis de propósitoCRsó para me ver confuso...?",
    32505: "C-Claro que não!",
    32506: "Cesto Aéreo concluído!",
    32507: "Está fumegando!CRPrecisa apagar logo!",
    32508: "Não apague! Essa fumaça protegeCRo corpo de qualquer anomalia.",
    32509: "Entendi... Um item vaporizadoCRque aproveita a halação...",
    32510: "Isso requer um nível altíssimo.CRFez um ótimo trabalho ao conseguir...",
    32511: "Claro!",
    32512: "...E o que era halação mesmo?",
    32513: "Sabia que ia perguntar... Halação éCRa técnica de sobrepor um espectro especialCRao espectro interno do corpo.",
    32514: "Com isso, um dom extra se acopla às suasCRaptidões natas, como se um novo poderCRtivesse acabado de despertar.",
    32515: "Bem que você podia despertarCRa vontade de estudar mais.",
    32516: "Lâmpada do Sol pronta!CREquipar ela dá um salto no HP!"
}

overflows = 0
gate_errors = 0
for did, text in sorted(PART1.items()):
    cap = caps[did]
    sz = encoded_size(text)
    if sz > cap:
        overflows += 1
        print(f"OVERFLOW {did}: {sz}B > {cap}B (+{sz - cap}B) -> {text}")
    errs = validate_line(did, orig_ens[did], text)
    if errs:
        gate_errors += 1
        print(f"GATE ERR {did}: {errs} -> {text}")

print(f"Part 1 result: {overflows} overflows, {gate_errors} gate errors.")
