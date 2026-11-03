import re

with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\test_refined_desc.py", "r", encoding="utf-8") as f:
    t_text = f.read()

# Extract REFINED_DESC dictionary from test_refined_desc.py
m = re.search(r"REFINED_DESC = \{(.*?)\}\n\nprint", t_text, re.DOTALL)
assert m, "REFINED_DESC not found"
refined_dict_str = m.group(1)

with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\generate_curated_blk_sys_003.py", "r", encoding="utf-8") as f:
    g_text = f.read()

# Fix 21000 in g_text
g_text = g_text.replace(
    '21000: ("RC: Anel Vistoso", "JP 合C:派手な指輪 (Receita de anel chamativo de luxo; 31B <= 32B)"),',
    '21000: ("RC: Anel de Luxo", "JP 合C:派手な指輪 (Receita de anel chamativo de luxo; 31B <= 32B)"),'
)

# Now update each description ID from 21022 to 21169
from test_refined_desc import REFINED_DESC
REFINED_DESC[21022] = "Animal parecido com uma castanha. A cabeça é pontuda, com a ponta rosa. É macio, por isso suas investidas não machucam muito."
REFINED_DESC[21100] = "Espadachim supremo, mestre na arte da espada. Aperfeiçoou todos os tipos de técnica."

from artonelico_tool.project import encoded_size

for d_id, desc in REFINED_DESC.items():
    sz = encoded_size(desc)
    pattern = rf'    {d_id}: \(".*?", "(.*?)"\),'
    replacement = f'    {d_id}: ("{desc}", "Descrição zoológica/bestiário refinada; {sz}B <= original_bytes"),'
    new_g_text, count = re.subn(pattern, replacement, g_text)
    if count == 1:
        g_text = new_g_text
    else:
        print(f"Could not replace ID {d_id} (count={count})")

with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\generate_curated_blk_sys_003.py", "w", encoding="utf-8") as f:
    f.write(g_text)

print("Updated generate_curated_blk_sys_003.py successfully.")
