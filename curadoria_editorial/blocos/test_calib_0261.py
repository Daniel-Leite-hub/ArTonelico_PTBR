import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0261 = {
    26426: ("...Sério!?", "Lyner surpreso com o apetite literário voraz de Misha."),
    26427: ("Teve uma época que li sem parar.CRFoi até divertido.", "Misha relembrando seu período de intensa leitura."),
    26428: ("Mas não tinha nadaCRque desse vontade de reler.", "Misha expressando sua exigência literária."),
    26429: ("Ah, é...?", "Lyner impressionado e sem reação diante da dedicação de Misha."),
    26430: ("Larga a espada e vai lerCRum livro de vez em quando, Lyner.", "Misha aconselhando Lyner a cultivar o intelecto."),
    26431: ("Mesmo forte e bonitão,CRde que adianta ter a cabeça oca?", "Misha provocando Lyner carinhosamente com humor refinado."),
    26432: ("Quando tiver tempo... Mas e você,CRnão comprou um livro outro dia?", "Lyner desviando da cobrança e lembrando a compra suspeita de Misha."),
    26433: ("...S-sei lá?CRSerá...?", "Misha tentando desconversar disfarçadamente."),
    26434: ("Comprou sim!CRDe capa meio cor-de-rosa...", "Lyner detalhando o livro com capa reveladora."),
    26435: ("...Achei que ninguém tinha visto.", "Misha admitindo o constrangimento de ter sido flagrada."),
    26436: ("Claro que dava pra ver!CRA loja nem é grande assim.", "Lyner apontando o óbvio sobre as dimensões da loja."),
    26437: ("É verdade...CRComprei mesmo, mas...", "Misha se rendendo às evidências sem jeito."),
    26438: ("...Não me diga que é conteúdoCRque não dá pra falar?", "Lyner insinuando com malícia bem-humorada sobre a leitura de Misha."),
    26439: ("Lyner! Não vai me dizerCRque tá pensando bobagem?!", "Misha reagindo indignada à insinuação atrevida."),
    26440: ("N-não tô! Mas com essa vergonha toda,CReu pensei que, sei lá...", "Lyner se defendendo sem jeito diante do rubor de Misha."),
    26441: ("N-nada a ver!CRSe tá pensando isso,CRagora que não conto mesmo!", "Misha fazendo bico e se recusando a revelar o segredo do romance."),
    26442: ("Hahaha, tá bom.CRMas fiquei curioso.", "Lyner rindo e admitindo a curiosidade."),
    26443: ("...Mas nada de pensar besteira!", "Misha repreendendo Lyner com advertência dengosa."),
    26444: ("Lyner, você pegouCRuma roupa bem gracinha, né?", "Misha mudando de assunto e comentando o figurino Glamisole."),
    26445: ("Roupa gracinha?CRDo que cê tá falando?", "Lyner fingindo desentendimento sobre a vestimenta sensual."),
    26446: ("Toda fininha, decotadaCRe cheia de babados.", "Misha descrevendo com precisão a lingerie/traje Glamisole."),
    26447: ("...Ah!CRTá falando da Glamisole?!", "Lyner caindo na ficha sobre a vestimenta mencionada."),
    26448: ("Essa mesma!CRQue bom gosto você tem, hein?", "Misha ironizando o gosto ousado de Lyner."),
    26449: ("Roupas finas e bem decotadasCRsão o seu fraco, Lyner?", "Misha encurralando Lyner com pergunta atrevida sobre seus fetiches."),
}

max_map = {
    26426: 24, 26427: 112, 26428: 128, 26429: 24, 26430: 128, 26431: 152,
    26432: 160, 26433: 48, 26434: 144, 26435: 72, 26436: 136, 26437: 72,
    26438: 120, 26439: 104, 26440: 160, 26441: 136, 26442: 96, 26443: 72,
    26444: 104, 26445: 88, 26446: 96, 26447: 72, 26448: 120, 26449: 144
}

all_ok = True
for tid, (txt, rat) in calib_0261.items():
    maxb = max_map[tid]
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
    print("=== 0261 100% PERFEITO ===")
