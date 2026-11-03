import json
import sys
import datetime

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_012_input.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_012_output.json"

with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_map = {d["id"]: d for d in input_data["dialogues"]}

batches = [
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch1_012.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch2_012.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch3_012.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch4_012.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch5_012.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch6_012.json"
]

all_curated = []
for b_path in batches:
    with open(b_path, "r", encoding="utf-8") as f:
        all_curated.extend(json.load(f))

print(f"Loaded {len(all_curated)} curated items.")
assert len(all_curated) == 296, f"Expected 296 items, got {len(all_curated)}"

dialogues_output = []
lines_rewritten = 0
lines_approved_as_is = 0

for item in all_curated:
    d_id = item["id"]
    orig = input_map[d_id]
    curated_text = item["curated_ptbr"]
    verdict = item["verdict"]
    rationale = item["rationale"]
    
    if verdict == "rewritten":
        lines_rewritten += 1
        status_val = "rewritten"
    else:
        lines_approved_as_is += 1
        status_val = "approved_as_is"
        
    d_obj = {
        "id": d_id,
        "event_file": orig["event_file"],
        "speaker": orig["speaker"],
        "original_jp": orig["original_jp"],
        "original_en": orig["original_en"],
        "current_ptbr": orig["current_ptbr"],
        "curated_ptbr": curated_text,
        "verdict": verdict,
        "rationale": rationale,
        "speaker_id": orig.get("speaker_id", 0),
        "review_status": "approved",
        "change_type": "curadoria_editorial_profunda",
        "status": status_val,
        "texto_ptbr_anterior": orig["current_ptbr"],
        "texto_ptbr_curado": curated_text,
        "justificativa": rationale,
        "revised_ptbr": curated_text,
        "notes_or_justification": rationale
    }
    dialogues_output.append(d_obj)

scene_handoff = {
    "resumo_dramatico": (
        "O bloco narrativo BLK_EVD_012 (IDs 2874 a 3169, abrangendo 29 arquivos de eventos Event/*.evd) "
        "descortina momentos de enorme densidade emocional, revelações de passado, humor lírico e avanços cruciais na jornada: "
        "1. No acampamento noturno a caminho de Nemo (Event/42.evd), Jack propõe descansar antes de continuar a marcha. "
        "Em conversa sincera ao redor da fogueira, Jack agradece a Lyner pela ajuda e pergunta sobre seus objetivos; "
        "Lyner revela ser um Cavaleiro de Elemia vindo do Mundo Superior em busca do Cristal Hymmnos Purger. "
        "Lyner mostra o pingente e Jack, retribuindo a dívida de honra pelo prato de comida e teto, promete ajudá-lo na busca. "
        "A sós na escuridão, Jack murmura com nostalgia que fazia anos que não ouvia falar em Cristais Hymmnos e promete resgatar Misha ('Misha... aguenta firme'); "
        "2. Na estalagem (Event/22.evd), Lyner descobre que o Grathmeld é indispensável ao cotidiano do Mundo Inferior e que todas as pousadas disponibilizam oficinas de síntese em seus menus; "
        "3. Nas ruínas do vilarejo de Stonehenge (Event/386.evd), Aurica visita a casa destruída de sua amiga de infância Claire, cujo pai era o prefeito, revelando que Claire foi sua única amiga quando Aurica não conseguia falar com ninguém; "
        "4. O excêntrico Mestre Pochoma (Event/25.evd) zomba da ideia de que aeronaves precisem de oficinas convencionais, ensinando que tralhas mecânicas se consertam com Grathmeld; "
        "5. Fuga tensa de Lyner de um dragão (Event/639.evd); "
        "6. A busca aflita por Aurica desaparecida na cidade (Event/320.evd), onde Misha estava prestes a partir para a Placa Hexagonal até Claire avisar em pânico que Aurica foi vista na floresta indo em direção aos escombros da Placa Hexagonal; "
        "7. A decolagem triunfal da aeronave lendária Gungnir (Event/522.evd), fruto da colaboração entre Tenba, Platina e a Tribo Teru, permitindo romper a Blastline e acessar o Ninho do Dragão no mapa-múndi; "
        "8. A descoberta do Cartão de Receita 'Tranquilidade' nas Asas de Horus (Event/79.evd), item vital que restaura o MP das Reyvateils e evita que a Magia da Canção entre em combustão explosiva fora de controle, fortalecendo a Barra de Burst; "
        "9. Lyner e Krusche escapando de armadilha mecânica ativada (Event/852.evd); "
        "10. Radolf lamentando a tragédia na Catedral após a tempestade (Event/371.evd); "
        "11. O desafio etílico na Cosmosfera (Event/627.evd), onde Jack se oferece para disputar com o Espírito da Flor ('gosto mais de um trago do que de comer'), galanteia a rival, mas capota no sono após roncos épicos, falhando em superar a campeã; "
        "12. A apreensão de Don Leon nas camadas inferiores da mente de Aurica (Event/746.evd), alertando Lyner de que o abismo ignoto além do vulcão é incontrolável e pode aniquilar o próprio ego; "
        "13. O enigma do baú selado (Event/466.evd) com a nota de 02/07/3770; "
        "14. A comoção dos refugiados da tempestade na estalagem de Karff (Event/300.evd) e a indignação de Radolf com a falta de amparo humanitário da Igreja; "
        "15. O tutorial de carga e disparo de Magia da Canção (Event/56.evd); "
        "16. A conversa madura entre Misha e Lyner sobre o verdadeiro significado de 'proteger' alguém (Event/319.evd), ensinando que resguardar a alma de Aurica vai muito além de aparar lâminas inimigas; "
        "17. O comovente diálogo da ocarina de infância (Event/973.evd), onde Misha confessa aos prantos que quebrou a ocarina Hama quando Bourd a sequestrou, e Lyner promete confeccionar uma nova com todo o seu amor, recebendo o Cartão de Receita [Ocarina]; "
        "18. A visita à cela onde se reencontraram (Event/254.evd), com as fantasias matrimoniais de Misha sobre 'a primeira obra em conjunto do casal'; "
        "19. A admiração de Krusche na profundeza da Torre (Event/241.evd); "
        "20. A garotinha agradecendo com Fruta Seca (Event/861.evd); "
        "21. A confissão íntima de Krusche sobre seu ex-namorado Luke (Event/163.evd), o mais brilhante mecânico de seu time que voou até o topo da Torre e nunca mais voltou, mantendo viva a chama de que os sonhos alimentam as grandes invenções; "
        "22. O convite de Shurelia para a simulação virtual (Event/783.evd); "
        "23. O prólogo marcial de Lyner e Ayatane com a Senhora Shurelia no Plugue Sinfônico (Event/0.evd), instruindo os aprendizes de cavaleiro a nunca serem imprudentes; "
        "24. A visita ao memorial cenotáfio (Event/500.evd), onde Shurelia revela que Mir derrubou o continente flutuante no vazio pelo imenso ódio que guardava da humanidade, matando incontáveis vidas; "
        "25. O fortalecimento mágico da persona Raina na simulação colegial (Event/824.evd) após a sintonização com o Chifre Prateado; "
        "26. A comovente transição de patamar psíquico (Event/725.evd), onde Aurica, apavorada por ter tentado matar a mana Claire em seu delírio, pede que Lyner segure a sua mão durante a Mudança de Paradigma, enquanto Don Leon profere uma lição magistral sobre como o subconsciente opera em direção diametralmente oposta aos desejos conscientes da alma; "
        "27. E o acionamento cerimonial do Anteparo A2 na Torre (Event/838.evd), onde Lyner tem seu espectro FFT validado e recita em língua Hymmnos: '#0Ma paks ga exec guol A2 al noes.' para liberação das comportas."
    ),
    "decisoes_terminologicas": {
        "Hymn Crystal (ヒュムネクリスタル)": "[Cristal Hymmnos] (padronização canônica sagrada, banindo o decalque 'Cristal do Hino')",
        "Purger (パージャ)": "[Purger] (Cristal Hymmnos ancestral primordial buscado por Lyner)",
        "Gungnir (グングニル)": "aeronave [Gungnir] (obra conjunta de Tenba, Platina e Tribo Teru capaz de romper a Blastline)",
        "Dragon's Nest (竜の巣 - Ryu no Su)": "[Ninho do Dragão] (toponímia canônica do mapa-múndi)",
        "Tranquility (トランキリティ)": "item [Tranquilidade] (essência alquímica restauradora de MP para Reyvateils)",
        "Burst Gauge (バーストゲージ)": "[Barra de Burst] (indicador de carga de potência da Magia da Canção)",
        "Invert Hook (インバートフック)": "[Gancho Invertido] (ferramenta especial de escalada desenvolvida por Lyner e Luke)",
        "Luke (ルーク)": "Luke (ex-namorado de Krusche e piloto visionário desaparecido no topo da Torre)",
        "Symphonic Plug (導力プラグ)": "[Plugue Sinfônico] (instalação vital de condução de energia na Torre)",
        "Memorial Cenotaph (慰霊碑 - Ireihi)": "[memorial em homenagem aos mortos] (cenotáfio dedicado às vítimas da queda do continente provocada por Mir)",
        "Floating Continent (浮遊大陸)": "[continente flutuante] (massa de terra celestial derrubada por Mir, corrigindo o disparate 'the wing' da NISA)",
        "Silver Horn (シルヴァホルン)": "[Chifre Prateado] (instalação ancestral de ressonância da Torre)",
        "Raina Harase (頼奈 / 原瀬頼奈)": "Raina / Raina Harase (identidade feminina simulada de Lyner no minigame colegial de Shurelia)",
        "Paradigm Shift (パラダイムシフト)": "[Mudança de Paradigma] (rito de transição e amadurecimento entre níveis da Cosmosfera)",
        "Don Leon (どんすけ / ドンスケ)": "Don Leon (guardião samurai da mente de Aurica com dicção arcaica '拙者 / 貴様')",
        "A2 Dividing Gate (A2隔壁)": "[Anteparo A2] (comporta militar de contenção e segurança da Torre)",
        "Hymmnos Control Key (#0Ma paks...)": "#0Ma paks ga exec guol A2 al noes. (frase de controle ancestral com tag de sistema #0 mantida)"
    },
    "alertas_para_proximo_bloco": (
        "1. A travessia pelo Anteparo A2 (Event/838.evd) e a navegação pela Gungnir rumo ao Ninho do Dragão (Event/522.evd) abrem os níveis centrais e superiores da Torre: atentar para termos técnicos de propulsão e arquitetura de Elemia. "
        "2. Na Cosmosfera de Aurica, a Mudança de Paradigma realizada de mãos dadas (Event/725.evd) aprofundará o contato com os traumas do massacre de Stonehenge e a infecção pelo vírus de Mir: manter a sensibilidade dramática ao contraste entre o terror de Aurica e o apoio incondicional de Lyner. "
        "3. Na Cosmosfera de Misha, a restauração da ocarina Hama (Event/973.evd) e as feridas do sequestro por Bourd exigirão fidelidade ao vínculo de infância e à persona Hama. "
        "4. Manter o tom solene e nobre de Don Leon, a postura de liderança cerimonial de Shurelia e a lealdade fraternal de Jack em relação a Lyner e Misha."
    )
}

output_data = {
    "block_id": "BLK_EVD_012",
    "axis_id": "AXIS_3",
    "axis_name": "HISTÓRIA E EVENTOS",
    "category": "HISTÓRIA E EVENTOS",
    "total_lines": len(dialogues_output),
    "line_count": len(dialogues_output),
    "lines_rewritten": lines_rewritten,
    "lines_approved_as_is": lines_approved_as_is,
    "id_range": [dialogues_output[0]["id"], dialogues_output[-1]["id"]],
    "curator_notes": (
        "Curadoria editorial profunda em duas passagens de 100% das 296 falas de BLK_EVD_012 (IDs 2874 a 3169). "
        "Auditoria integral contra a Tríade de Idiomas (JP SLPS-732.49 soberano; EN SLUS-214.45 suporte; PT-BR viva). "
        "Destaques: resgate da autêntica fala de Jack sobre ser um 'especialista em combate' (ID 2886) e gostar de beber mais do que de comer (ID 2997); "
        "correção do erro crasso de tradução em ID 2905 ('翌朝' pretérito em vez de 'Tomorrow morning' futuro); "
        "correção dramática em ID 2940 (sentido original restaurado para a partida de Misha à Placa Hexagonal); "
        "correção do disparate 'the wing' da NISA em ID 3132, restabelecendo o 'continente flutuante' derrubado por Mir; "
        "correção de concordância de gênero com Krusche em ID 2990 ('você tem razão') e ID 3096 ('Obrigada'), e da menina em ID 3084 ('Muito obrigada'); "
        "correção crítica de número em ID 3119 (Lady Shurelia falando no plural com Lyner e Ayatane); "
        "restauração da identidade canônica de Raina na simulação colegial (ID 3134); "
        "restauração da psicologia da Cosmosfera destruída pela NISA em ID 3157 (Don Leon alertando para o colapso irreversível do ego); "
        "preservação estrita das vocalizações sem rubricas (ronco etílico em ID 3003, rugido em ID 2933); "
        "e blindagem total da frase ancestral em Hymmnos com tag #0 em ID 3167 ('#0Ma paks ga exec guol A2 al noes.')."
    ),
    "curated_lines": dialogues_output,
    "dialogues": dialogues_output,
    "scene_handoff": scene_handoff
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"BLK_EVD_012_output.json generated successfully with {len(dialogues_output)} dialogues.")
print(f"Lines rewritten: {lines_rewritten}, lines approved as-is: {lines_approved_as_is}.")
