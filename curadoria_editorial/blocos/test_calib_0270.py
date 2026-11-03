import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

calib_0270 = {
    26642: ("Vocês são pai e filho,CRnão dá pra viver em pé de guerra.", "Misha aconselhando Lyner sobre a relação familiar com Leard."),
    26643: ("Vai continuar com essa birraCRpor quantos anos mais?", "Misha confrontando a imaturidade de Lyner com firmeza afetuosa."),
    26644: ("Falar é fácil, mas...", "Lyner na defensiva sobre o conflito geracional com o pai."),
    26645: ("Dá dor de cabeçaCRolhar pra vocês.", "Misha expressando o cansaço de presenciar as brigas dos dois."),
    26646: ("Não tem jeito! A culpa é dele,CRo meu pai é quem tá errado!", "Lyner teimoso jogando a responsabilidade no comandante Leard."),
    26647: ("Só porque discordo, ele quer mandar...CRÉ um pai cabeça-dura demais!", "Lyner reclamando da rigidez autoritária de Leard."),
    26648: ("Ah... Vai demorarCRpra fazer as pazes.", "Misha exalando desalento sem recorrer a rubricas teatrais."),
    26649: ("Mas já vi que pai e filhoCRsão iguaizinhos.", "Misha apontando com ironia fina a semelhança de temperamento entre os dois."),
    26650: ("Iguais?", "Lyner ofendido e chocado com a comparação."),
    26651: ("Hehehe... Só vocês doisCRque não enxergam isso.", "Misha rindo da cegueira mútua de pai e filho."),
    26652: ("Platina mudou bastante, né?", "Misha mudando de assunto e observando a arquitetura da cidade alta."),
    26653: ("Tá bem diferenteCRde quando eu morava aqui.", "Misha comparando a Platina atual com a de sua infância."),
    26654: ("Acha? Desde que nasci,CRnão vi mudar quase nada.", "Lyner manifestando sua falta de percepção urbana."),
    26655: ("Você é tão esquecidoCRque nem nota as mudanças!", "Misha implicando com a memória curta de Lyner."),
    26656: ("Qual é a sua, hein?", "Lyner protestando comicamente contra a alfinetada."),
    26657: ("Ué, lembrou do passado?CREntão lembrou de mim também, né?", "Misha usando a deixa com astúcia para cobrar lembranças românticas."),
    26658: ("Foi mal...", "Lyner sem graça admitindo a falha."),
    26659: ("Mas antes não tinhaCRloja de departamentos lá.", "Misha destacando a nova construção urbana no local de memórias sem rubrica teatral."),
    26660: ("Disso você lembra, né?", "Misha testando um ponto de referência clássico de Platina."),
    26661: ("...Não, aquilo sempre esteve lá!", "Lyner teimoso insistindo em sua falsa lembrança."),
    26662: ("O quê? Ali era sóCRum terreno baldio antes!", "Misha corrigindo o fato histórico sobre o terreno baldio."),
    26663: ("Quê?! Mentira!", "Lyner em choque com o fato histórico revelado."),
    26664: ("Ai, ai... deixa pra lá.CRFiquei tão chocada que até cansei...", "Misha exalando cansaço natural sem rubrica teatral."),
    26665: ("Falando nisso, ainda não vimosCRtoda a Crônica Crescente, né?", "Misha introduzindo com curiosidade a Crônica Crescente (Crescent Chronicle)."),
}

max_map = {
    26642: 120, 26643: 120, 26644: 64, 26645: 80, 26646: 152, 26647: 152,
    26648: 80, 26649: 104, 26650: 16, 26651: 112, 26652: 64, 26653: 104,
    26654: 120, 26655: 128, 26656: 64, 26657: 136, 26658: 24, 26659: 104,
    26660: 56, 26661: 96, 26662: 104, 26663: 32, 26664: 136, 26665: 136
}

all_ok = True
for tid, (txt, rat) in calib_0270.items():
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
    print("=== 0270 100% PERFEITO ===")
