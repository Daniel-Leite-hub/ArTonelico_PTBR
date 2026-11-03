import sys
sys.path.append(r'G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao')
import artonelico_tool.project as proj

test_strings = [
    # 22917-22939
    (22917, 72, "[Equipamento]CRConcede HP +150."),
    (22918, 24, "Super HP+"),
    (22919, 72, "[Equipamento]CRConcede HP +250."),
    (22920, 40, "Chip de Reforço"),
    (22921, 72, "[Equipamento]CRConcede HP +500."),
    (22922, 32, "Stamina Plus"),
    (22923, 72, "[Equipamento]CRConcede HP +750."),
    (22924, 32, "Life Booster"),
    (22925, 72, "[Equipamento]CRConcede HP +1250."),
    (22926, 24, "Leve MP+"),
    (22927, 64, "[Equipamento]CRConcede MP +50."),
    (22928, 32, "Médio MP+"),
    (22929, 72, "[Equipamento]CRConcede MP +100."),
    (22930, 24, "Alto MP+"),
    (22931, 72, "[Equipamento]CRConcede MP +150."),
    (22932, 24, "Super MP+"),
    (22933, 72, "[Equipamento]CRConcede MP +250."),
    (22934, 24, "Mega Memory"),
    (22935, 72, "[Equipamento]CRConcede MP +500."),
    (22936, 24, "Giga Memory"),
    (22937, 72, "[Equipamento]CRConcede MP +750."),
    (22938, 24, "Tera Memory"),
    (22939, 72, "[Equipamento]CRConcede MP +1250."),
    
    # Attack progression (22940-22949)
    (22940, 32, "Leve Ataque+"),
    (22941, 96, "[Equipamento]CREleva levemente o ataque."),
    (22942, 32, "Médio Ataque+"),
    (22943, 88, "[Equipamento]CREleva um pouco o ataque."),
    (22944, 24, "Alto Ataque+"),
    (22945, 96, "[Equipamento]CREleva bem o ataque."),
    (22946, 24, "Super Ataque+"),
    (22947, 88, "[Equipamento]CREleva bastante o ataque."),
    (22948, 40, "Técnica de Mestre"),
    (22949, 96, "[Equipamento]CREleva enormemente o ataque."),
]

for d_id, limit, text in test_strings:
    size = proj.encoded_size(text)
    status = "OK" if size <= limit else f"FAIL (+{size - limit}B)"
    print(f"{d_id}: limit={limit}B, size={size}B [{status}] -> '{text}'")
