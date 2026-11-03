import sys
from pathlib import Path

path = Path('Ferramentas_Traducao/curadoria_editorial/blocos/generate_curated_blk_sys_037.py')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Load calibrated fixes from calib_blk37
import calib_blk37

# Also add the final 10 refined fixes
calib_blk37.CALIBRATED_FIXES[30717] = (
    "Por dentro é só remédio comum, né?CRPodíamos chamar só de \"Remédio\"...",
    "Aurica sugerindo de forma simples e direta chamar o item apenas de 'Remédio' (148B/152B)."
)
calib_blk37.CALIBRATED_FIXES[30725] = (
    "...Como os ingredientes viraramCRessa coisa é um mistério, né?",
    "Aurica perplexa com a transmutação inusitada dos componentes originais (128B/136B)."
)
calib_blk37.CALIBRATED_FIXES[30727] = (
    "Pois é. Vão achar que a gente vaiCRfazer uma festa ou coisa assim.",
    "Lyner concordando que o artefato parece um adereço festivo (135B/136B)."
)
calib_blk37.CALIBRATED_FIXES[30739] = (
    "Brincadeira! Pensei em quem odeia amargoCRe fiz no sabor Miolo Nyo?.",
    "Lyner revelando o sabor especial para quem detesta o gosto amargo (137B/144B)."
)
calib_blk37.CALIBRATED_FIXES[30772] = (
    "Espiral de mosquito...CREm forma de porquinho!",
    "Aurica apontando o formato tradicional de porquinho fumegante (93B/104B)."
)
calib_blk37.CALIBRATED_FIXES[30775] = (
    "Ai... Pior que não posso rebater...",
    "Lyner admitindo que não tem como rebater a lógica irrefutável de Aurica (72B/88B)."
)
calib_blk37.CALIBRATED_FIXES[30791] = (
    "Lança no alvo: a mira caiCRe os golpes erram!",
    "Lyner resumindo a mecânica de evasão garantida contra ataques rivais (92B/96B)."
)
calib_blk37.CALIBRATED_FIXES[30867] = (
    "(...Escolhi a pessoa errada.)",
    "Lyner se arrependendo amargamente de ter consultado Aurica (59B/64B)."
)
calib_blk37.CALIBRATED_FIXES[30870] = (
    "Não achei que ia falarCRna lata desse jeito...",
    "Lyner desconcertado com a franqueza desinibida da Reyvateil (94B/104B)."
)
calib_blk37.CALIBRATED_FIXES[30928] = (
    "...Só não fala esse nomeCRna frente dos outros!",
    "Lyner implorando para que ela guarde segredo sobre a alcunha vergonhosa (97B/104B)."
)

# In generate_curated_blk_sys_037.py, we can inject an update to CURATION_DATA right before validation loop!
marker = "# Validation loop"
patch = "\n# Apply all calibrated fixes\nimport calib_blk37\nCURATION_DATA.update(calib_blk37.CALIBRATED_FIXES)\n\n"

if "calib_blk37.CALIBRATED_FIXES" not in text:
    new_text = text.replace(marker, patch + marker)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully patched generate_curated_blk_sys_037.py with calibrated fixes!")
else:
    print("Already patched.")
