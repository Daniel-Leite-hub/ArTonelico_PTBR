import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0302 = {
    27410: 192, 27411: 144, 27412: 232, 27413: 256, 27414: 64, 27415: 112,
    27416: 168, 27417: 120, 27418: 64, 27419: 120, 27420: 96, 27421: 88,
    27422: 104, 27423: 184, 27424: 80, 27425: 184, 27426: 216, 27427: 32,
    27428: 80, 27429: 272, 27430: 16, 27431: 216, 27432: 128, 27433: 144
}

calib_0302 = {
    27410: ("É mesmo!? Mas é tão refrescante! E coisas geladas são raras em Horus.", "Lyner defendendo a sobremesa gelada em Horus. (143B <= 192B)"),
    27411: ("Pensando bem, é verdade...CRAqui não é frio como em Platina.", "Shurelia comparando o clima de Horus com Platina com CR. (124B <= 144B)"),
    27412: ("Mas a senhora também gosta de raspadinha, né? Foi inesperado, mas me fez sentir mais perto de você.", "Lyner confessando proximidade afetiva. (202B <= 232B)"),
    27413: ("G-Gostar eu gosto, mas não como sempre! Só apontei a discrepância com os dados da Primeira Era...", "Shurelia se justificando na defensiva com dados da Primeira Era. (198B <= 256B)"),
    27414: ("A senhora sabe cozinhar.", "Lyner surpreso com o dom culinário. (49B <= 64B)"),
    27415: ("Hã? Falando do Arroz de CoelhoCRque fiz outro dia?", "Shurelia referenciando o Usarice com CR. (102B <= 112B)"),
    27416: ("Será que conta como culinária?CREu só moldei o arrozCRem forma de coelho...", "Shurelia modesta e tímida com CRs. (154B <= 168B)"),
    27417: ("Faria sucesso com crianças.CRSabe fazer mais coisas?", "Lyner sugerindo o apelo infantil e instigando mais dotes com CR. (106B <= 120B)"),
    27418: ("C-Claro que faço de tudo!", "Shurelia orgulhosa prometendo versatilidade. (52B <= 64B)"),
    27419: ("Tipo cortar maçã em formatoCRde coelhinho.", "Shurelia dando outro exemplo temático de coelho com CR. (85B <= 120B)"),
    27420: ("Coelho de novo? A senhoraCRgosta mesmo, né?", "Lyner apontando a obsessão por coelhos com CR. (88B <= 96B)"),
    27421: ("Ué... Não é fofo?CRCoelhinhos...", "Shurelia defendendo os coelhinhos com meiguice e CR. (68B <= 88B)"),
    27422: ("Só não sabia que eraCRtão louca por coelhos...", "Lyner achando graça na mania dela com CR. (96B <= 104B)"),
    27423: ("A senhora levou um baita tomboCRao lançar a magia outro dia.CRTudo bem?", "Lyner preocupado com a queda cômica dela com CRs. (144B <= 184B)"),
    27424: ("A-Aquilo... foi só excessoCRde impulso.", "Shurelia tentando disfarçar a falta de jeito com CR. (80B <= 80B)"),
    27425: ("É? Mas caiu de cara no chão,CRpareceu doer bastante...", "Lyner insistindo na dor evidente do tombo com CR. (111B <= 184B)"),
    27426: ("L-Lyner!? Pra onde estava olhando na batalha!? Foque no inimigo!", "Shurelia mortificada exigindo foco tático. (129B <= 216B)"),
    27427: ("Ai, d-desculpe!", "Lyner pedindo desculpas constrangido. (31B <= 32B)"),
    27428: ("Mas tenho que cuidarCRda parceira, né?", "Lyner justificando a atenção protetora com CR. (78B <= 80B)"),
    27429: ("Isso é diferente de ficar olhando meu tombo do começo ao fim! Se tem tempo pra isso, ataque o inimigo...", "Shurelia reclamando do constrangimento de ser observada caindo. (211B <= 272B)"),
    27430: ("Ou...", "Shurelia hesitando antes de cobrar ajuda. (11B <= 16B)"),
    27431: ("Em vez de só olhar, podia ter ajudado! Pode ter esquecido sem a armadura, mas eu sou sua...!", "Shurelia deixando escapar sua expectativa de ser amparada. (186B <= 216B)"),
    27432: ("Tem razão. Se cair de novo,CReu vou lá te acudir.", "Lyner prometendo socorrê-la no próximo tombo com CR. (101B <= 128B)"),
    27433: ("...N-Não precisa mais. É vergonhoso,CReu me levanto sozinha...", "Shurelia tímida e orgulhosa recusando com CR. (127B <= 144B)")
}

if __name__ == "__main__":
    all_ok = True
    for tid, (txt, rat) in calib_0302.items():
        maxb = max_map_0302[tid]
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
        print("=== 0302 100% PERFEITO ===")
