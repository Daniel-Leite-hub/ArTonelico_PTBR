import sys
sys.path.insert(0, 'Ferramentas_Traducao')
sys.path.insert(0, 'Ferramentas_Traducao/curadoria_editorial/blocos')
import generate_curated_blk_sys_037 as gen
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

test10 = {
    30717: ("Por dentro é só remédio comum, né?CRPodíamos chamar só de \"Remédio\"...", 152),
    30725: ("...Como os ingredientes viraramCRessa coisa é um mistério, né?", 136),
    30727: ("Pois é. Vão achar que a gente vaiCRfazer uma festa ou coisa assim.", 136),
    30739: ("Brincadeira! Pensei em quem odeia amargoCRe fiz no sabor Miolo Nyo?.", 144),
    30772: ("Espiral de mosquito...CREm forma de porquinho!", 104),
    30775: ("Pior que você não tá errada,CRnem tenho o que dizer.", 88),
    30791: ("Lança no alvo: a mira caiCRe os golpes erram!", 96),
    30867: ("(...Escolhi a pessoa errada.)", 64),
    30870: ("Não achei que ia falarCRna lata desse jeito...", 104),
    30928: ("...Só não fala esse nomeCRna frente dos outros!", 104)
}

for did, (text, max_b) in test10.items():
    sz = encoded_size(text)
    flag = "OK" if sz <= max_b else "FAIL"
    print(f"{did}: {sz}/{max_b}B -> {flag} | {text}")
