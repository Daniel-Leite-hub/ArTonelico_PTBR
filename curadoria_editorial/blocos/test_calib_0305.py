import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0305 = {
    27482: 224, 27483: 56, 27484: 216, 27485: 152, 27486: 96, 27487: 40,
    27488: 56, 27489: 32, 27490: 40, 27491: 80, 27492: 48, 27493: 112,
    27494: 72, 27495: 104, 27496: 176, 27497: 168, 27498: 128, 27499: 64,
    27500: 144, 27501: 120, 27502: 32, 27503: 16, 27504: 120, 27505: 56
}

calib_0305 = {
    27482: ("I-Isso é assunto meu!CRÉ invasão de privacidade! E não se faz essa pergunta a uma superior!", "Shurelia indignada com a curiosidade dele com CRs. (187B <= 224B)"),
    27483: ("T-Tem razão! Desculpe...", "Lyner acatando com receio. (50B <= 56B)"),
    27484: ("Brinco com a Mei Mei e a ELMA-chan. A de verdade, não o vírus, a minha Guardiã pessoal, sabe?", "Shurelia confessando suas brincadeiras secretas com Mei Mei e ELMA. (190B <= 216B)"),
    27485: ("Não conte pra ninguém!CRSó contei porque você insistiu!", "Shurelia ordenando segredo absoluto com CR. (115B <= 152B)"),
    27486: ("Lyner... Ultimamente andoCRmeio estranha...", "Shurelia iniciando confissão íntima com CR. (87B <= 96B)"),
    27487: ("Hã? Por quê?", "Lyner surpreso e atento. (27B <= 40B)"),
    27488: ("...Não quero voltar...", "Shurelia confessando a aversão ao isolamento. (46B <= 56B)"),
    27489: ("...Pra onde?", "Lyner perguntando o destino com delicadeza. (25B <= 32B)"),
    27490: ("Ao Rinkernator...", "Shurelia nomeando seu cárcere solitário no topo da torre. (35B <= 40B)"),
    27491: ("Por que vai ficar só de novo?", "Lyner compreendendo a raiz da angústia dela. (60B <= 80B)"),
    27492: ("...É... Talvez seja...", "Shurelia confirmando com vulnerabilidade comovente. (46B <= 48B)"),
    27493: ("Onde quer que a senhora vá,CReu vou junto.", "Lyner jurando lealdade incondicional de cavaleiro com CR. (86B <= 112B)"),
    27494: ("Sou seu cavaleiro!CRClaro que vou.", "Lyner reafirmando sua vocação protetora com CR. (69B <= 72B)"),
    27495: ("...Obrigada, Lyner...CRMe sinto tão feliz agora...", "Shurelia tocada às lágrimas com CR. (102B <= 104B)"),
    27496: ("Só de ouvir alguém me dizer isso, sinto que não estou mais sozinha.", "Shurelia expressando o fim do abandono cósmico. (138B <= 176B)"),
    27497: ("Passei centenas de anos esperandoCRalguém como você aparecer...", "Shurelia revelando séculos de solidão romântica com CR. (129B <= 168B)"),
    27498: ("Eu sempre a admirei tanto,CRfico muito feliz em ouvir isso.", "Lyner retribuindo o afeto com CR. (119B <= 128B)"),
    27499: ("Hehe... Que bom para nós dois.", "Shurelia sorrindo com ternura genuína. (62B <= 64B)"),
    27500: ("...Mas lá é tão frio. Já ficaCRalém da atmosfera...", "Shurelia lembrando o rigor gélido do Rinkernator com CR. (108B <= 144B)"),
    27501: ("É... Ficar lá pra sempreCRseria meio difícil...", "Lyner fraquejando diante do frio extremo com CR. (98B <= 120B)"),
    27502: ("Mentiroso!", "Shurelia revoltada com a quebra de promessa cômica. (21B <= 32B)"),
    27503: ("Poxa...", "Lyner cabisbaixo com o recuo. (15B <= 16B)"),
    27504: ("Lyner, vi uma [Ar tonelico?]CRna sua bolsa.", "Shurelia avistando o item perigoso com colchetes e CR. (87B <= 120B)"),
    27505: ("Uau... A senhora viu?", "Lyner surpreso por ter sido flagrado. (43B <= 56B)")
}

if __name__ == "__main__":
    all_ok = True
    for tid, (txt, rat) in calib_0305.items():
        maxb = max_map_0305[tid]
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
        print("=== 0305 100% PERFEITO ===")
