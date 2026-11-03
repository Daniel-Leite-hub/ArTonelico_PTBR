import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.insert(0, str(BASE_DIR))
from artonelico_tool.project import encoded_size

tests = {
    27820: (32, ['Sério?CREntão...', 'É mesmo?CREntão...', 'Sério? Então...', 'Mesmo?... Então...']),
    27821: (24, ['Ah... sim.', 'Sim...', 'Ah, sim.', 'Ah... vem.']),
    27825: (64, ['A senhora temCRdias ruins?', 'Também temCRdias ruins?', 'A senhora temCRmágoas?']),
    27829: (96, ['Se notasse, cuidaria melhor da senhora...', 'Se eu notasse, cuidaria melhor de ti...', 'Se soubesse, cuidaria melhor...']),
    27834: (56, ['...CRConte comigo.', '...Se for só isso, conte comigo.', '...Se for isso, conte comigo.']),
    27836: (72, ['Hoje fiz um lanche para você.', 'Fiz um lanche para você hoje.', 'Preparei um lanche noturno hoje.']),
    27844: (80, ['Perdão...CRComerei. Por favor.', 'Desculpe...CREu como. Por favor.', 'Perdão... Eu como. Por favor.']),
    27846: (64, ['Dá para comer. Não tá tão ruim.', 'Dá para comer.', 'Nem é tão ruim. Dá pra comer.', 'Não tá tão ruim. Dá pra comer.']),
    27850: (152, ['No Mergulho era tão fácil...CRNão creio mais num programa desses!', 'No Mergulho era tão fácil...CRNão confio mais nesse programa!']),
    27857: (208, ['Se houvesse chance, queria provar essa vida ao menos uma vez. Mas sei que não deve ser fácil.', 'Se pudesse, queria provar essa vida ao menos uma vez. Sei que não é tão fácil assim.']),
    27858: (176, ['No Cais Flutuante,CRvi gente com loja aberta atéCRnum lugar daqueles.', 'No Cais Flutuante,CRvi gente com tendas abertasCRnum lugar daqueles.']),
    27864: (144, ['Temos que aguentar.CRSó achamos isso porque nossa situação é especial.', 'Temos que aguentar isso.CRSó achamos isso porque somos especiais.']),
    27865: (24, ['Especial?', 'Especiais?']),
    27869: (16, ['Pode ser.', 'Talvez.']),
    27875: (112, ['...Se encolhesse agora,CRviraria um moleque brigão.', '...Se encolhesse,CRviraria um pestinha brigão.']),
    27882: (40, ['...Bem... sim...', '...B-bem... sim...', '...B-bem... é...']),
    27890: (80, ['Pareço adulta ou criança?', 'Minha aparência: adulta ou criança?', 'Minha silhueta é adulta ou infantil?']),
    27892: (48, ['Fiquei no meio-termo.', '...Fiquei no meio.', '...Fiquei no meio-termo.']),
    27920: (24, ['Gafanhotos?', '...Gafanhotos?', '...Gafanhotos...']),
    27922: (80, ['Kyu! Kyu kyu!CR(Coma! Me coma!)', 'Kyu! Kyu kyu!CR(Me coma!)', 'Kyu kyu!CR(Me coma! Me coma!)', 'Kyu kyu!CR(Coma! Coma!)']),
    27966: (120, ['Mesmo lendo, não entendo nada. É difícil demais.', 'Mesmo lendo tudo, não entendo. É difícil demais.']),
    28000: (32, ['Hã?!CRE-é que...', 'Hã?!CRÉ...']),
    28012: (104, ['Sim... Naquela época,CRminha idade era de três dígitos.', 'Sim... Na época,CRminha idade era de três dígitos.']),
    28022: (112, ['E eles cultivando a terra na calma... Quem são eles?!', 'E eles lá, cultivando em paz... Quem são eles?!']),
    28024: (112, ['Nunca pensei que usaríamos o A.B.R. nós mesmos.', 'Nunca imaginei usar o A.B.R. nós mesmos.']),
    28028: (168, ['O A.B.R. é guardião da Torre. Ele só estava infectado por vírus.', 'O A.B.R. é guardião da Torre. Estava apenas infectado por vírus.']),
    28030: (72, ['A-ah, é!...CREra isso mesmo! Ahaha!', 'Ah, é!...CREra isso mesmo! Ahaha!']),
    28032: (32, ['Lyner é meu...', 'Lyner é meu... ', 'O Lyner é...']),
    28034: (24, ['...Não, nada.', '...Nada.', '...Não foi nada.']),
    28035: (96, ['Lutar usando Apóstolos de Mir...CRé meio estranho.', 'Lutar com Apóstolos de Mir...CRé estranho, né?']),
    28036: (112, ['Vamos enfrentar a Mir, e usar os apóstolos dela...', 'Lutaremos contra Mir, e usar os apóstolos dela...']),
    28051: (56, ['O Mundo Inferior é tão quente!', 'Como o Mundo Inferior é quente!']),
    28062: (32, ['Já disse que não!', 'Disse que não!', 'Já falei que não!']),
    28067: (40, ['Você não faz diário?', 'Você não anota?', 'Não tem diário?']),
    28104: (88, ['Nem morta! Aquele lugar só traz dor!!', 'Nem morta! Só traz memórias horríveis!', 'Nem pensar! Só traz memórias horríveis!'])
}

for did, (limit, var_list) in tests.items():
    print(f"=== ID {did} (limite {limit}B) ===")
    for v in var_list:
        sz = encoded_size(v)
        ok = "OK" if sz <= limit else f"EXCESSO (+{sz - limit})"
        print(f"  {sz}B [{ok}]: {v}")
