import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0266 = {
    26546: ("Como assim?CRRolou algo ruim, afinal?!", "Misha apavorada achando que Lyner descobriu algum segredo proibido."),
    26547: ("Não é isso...CRÉ que... como eu posso explicar...?", "Lyner hesitando e buscando as palavras certas para descrever a Cosmosfera."),
    26548: ("Deixa pra lá, não fala!CRTô ficando com medo de saber...", "Misha tapando os ouvidos e recuando por constrangimento."),
    26549: ("Ah, é? Ufa, que alívio...", "Lyner respirando aliviado por não precisar tocar em assuntos embaraçosos."),
    26550: ("...Só responde:", "Misha insistindo na pergunta essencial."),
    26551: ("Quer voltar na minha Cosmosfera?", "Misha querendo saber se Lyner voltará a mergulhar nela."),
    26552: ("...Claro que quero.", "Lyner respondendo com firmeza e afeto incondicional."),
    26553: ("É...? Então tá tudo bem!", "Misha comemorando aliviada a confirmação do vínculo."),
    26554: ("Lyner, também curte garotinhasCRcomo o Jack?", "Misha provocando Lyner sobre preferências românticas."),
    26555: ("Q-que pergunta do nada...CRE o do Jack foi puro engano!", "Lyner desmentindo a acusação cômica sobre Jack."),
    26556: ("Ele disse que preferiaCRmulheres elegantes e com curvas...", "Lyner lembrando a declaração original de Jack sobre mulheres maduras."),
    26557: ("Ah, o Jack não importa.CRSó usei ele pra puxar assunto,CResquece ele.", "Misha descartando o assunto de Jack para focar no que realmente quer saber."),
    26558: ("...É-é mesmo?", "Lyner sem reação diante do descaramento de Misha."),
    26559: ("E aí? Prefere baixinhasCRou mulheres cheias de curvas?", "Misha exigindo que Lyner escolha entre os dois biotipos."),
    26560: ("Calma aí!CRSó tem essas duas opções?!", "Lyner protestando comicamente contra o dilema forçado."),
    26561: ("Só duas!CRFala com franqueza.", "Misha encurralando Lyner com firmeza fofa."),
    26562: ("...Pra mim tanto faz.CRDesde que seja bonitinha.", "Lyner optando pela resposta diplomática e sincera."),
    26563: ("Que indeciso!CRResponde de uma vez!", "Misha indignada com a resposta em cima do muro."),
    26564: ("Me dá um tempo...", "Lyner pedindo arrego diante da sabatina íntima."),
    26565: ("Misha, já entendi que vocêCRestudou de tudo nessa vida.", "Lyner reconhecendo a versatilidade acadêmica de Misha."),
    26566: ("Mas não entendo como você sabeCRarrombar até fechaduras...", "Lyner intrigado com as habilidades de arrombamento de Misha."),
    26567: ("Ué, não é super prático?", "Misha defendendo a utilidade pragmática do furto e da gazua."),
    26568: ("É prático, mas... ainda acho meio bizarroCRvocê saber arrombar trancas...", "Lyner mantendo o choque moral diante da malandragem de Misha."),
    26569: ("É para emergências!CRMuito útil na hora de dar no pé.", "Misha justificando suas habilidades de fuga nas ruas do Beco Vagalume."),
}

max_map = {
    26546: 88, 26547: 120, 26548: 128, 26549: 72, 26550: 40, 26551: 88,
    26552: 40, 26553: 64, 26554: 96, 26555: 112, 26556: 120, 26557: 192,
    26558: 32, 26559: 136, 26560: 96, 26561: 64, 26562: 152, 26563: 120,
    26564: 48, 26565: 144, 26566: 128, 26567: 80, 26568: 152, 26569: 152
}

all_ok = True
for tid, (txt, rat) in calib_0266.items():
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
    print("=== 0266 100% PERFEITO ===")
