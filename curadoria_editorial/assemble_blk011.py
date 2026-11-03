import json
import sys

sys.path.insert(0, r"C:\Users\Daniel\.gemini\config\skills\curadoria-editorial-game-localization\scripts")
import validador_editorial

input_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_011_input.json"
output_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_011_output.json"

with open(input_path, "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_map = {d["id"]: d for d in input_data["dialogues"]}

batches = [
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch1_curated.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch2_curated.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch3_curated.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch4_curated.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch5_curated.json",
    r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\batch6_curated.json"
]

all_curated = []
for b_path in batches:
    with open(b_path, "r", encoding="utf-8") as f:
        all_curated.extend(json.load(f))

print(f"Loaded {len(all_curated)} curated items.")
assert len(all_curated) == 239, f"Expected 239 items, got {len(all_curated)}"

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
        "speaker_id": item.get("speaker_id", orig.get("speaker_id", 0)),
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
        "O bloco BLK_EVD_011 (IDs 2635 a 2873, abrangendo 23 arquivos de eventos Event/*.evd) descortina momentos de rica "
        "humanidade, humor, traumas psíquicos profundos e avanços capitais na jornada: "
        "1. No posto de guarda A5 (Event/529.evd), um hilário flagrante de Lapsey Guard falando dormindo, sonhando com lições de casa, "
        "invocando Kanade e tendo delírios embaraçosos com a Senhora Shurelia sob o olhar impassível da própria administradora, "
        "misturando o sonho com teoria técnica de energia sinfônica da Torre (FFT, lógica QT e placa de Grathnode); "
        "2. No Chifre Prateado (Event/554.evd), Ayatane e Lyner contemplam o interior da colossal estrutura em busca da [Sala da Chave], "
        "onde repousa o Cristal Hymmnos de Mir, revelando que a passagem é bloqueada pelo mortífero [Rugido de Deus] "
        "(神の咆哮 - Kami no Houkou), um vórtice brutal de energia contido por três válvulas; "
        "3. A longa subida de escadarias da Torre (Event/486.evd), com Jack comemorando o fim dos degraus enquanto Lyner avalia a altitude vertiginosa; "
        "4. A antecipação festiva de uma cerimônia na Cosmosfera (Event/760.evd); "
        "5. A operação tática de infiltração (Event/267.evd), na qual Krusche pluga o Cilindro de Energia para provocar um blecaute temporário, "
        "arrombar a porta a pontapés e resgatar Misha antes que a energia seja reativada, em contagem regressiva eletrizante; "
        "6. A constatação da barreira de escombros consertada (Event/251.evd); "
        "7. A impagável discussão armamentista na loja (Event/234.evd), onde Krusche explica a inércia mecânica da sua motosserra, "
        "Misha a chama de sinistra por usar uma ferramenta dessas, Krusche retruca que sinistra é Misha por convocar aberrações cósmicas em combate, "
        "quase explodindo a loja com Magia da Canção até o dono enxotar todo mundo e Lyner implorar por paz; "
        "8. O capricho infantil de Misha querendo continuar brincando em vez de dormir (Event/611.evd); "
        "9. A porta selada que apenas a Senhora Tastiella pode autorizar (Event/285.evd); "
        "10. O mecanismo emperrado exigindo ativação por Bomba de Raio (Event/248.evd); "
        "11. A chegada à lendária Colina do Canto (Event/347.evd - 謳う丘 Utau Oka), onde Radolf lamenta com amargura a decadência "
        "institucional e a falta de zelo da Igreja dos Santos, que enviou os guerreiros às cegas sem coordenadas precisas; "
        "12. A continuação da simulação tokusatsu/colegial de Shurelia (Event/798.evd), onde a Singer Angel e Raina (Lyner) tentam libertar "
        "Leila destruindo as três esferas de controle mental antes de sofrerem um novo Game Over sereno; "
        "13. O comovente e perturbador episódio da casa de infância de Misha (Event/622.evd), onde o pai bêbado exige dinheiro para birita, "
        "agride a filha mais velha, e Misha, indignada, ataca o próprio pai com magia, sendo deserdada e jurando nunca mais voltar; a irmã mais velha "
        "tenta manter as aparências buscando barris importados no cais e comicamente pede Lyner em namoro, gerando ciúmes explosivos em Misha e "
        "tecendo a Magia Verde [Tiro Rajada]; "
        "14. A inspeção dos cabos intrincados do elevador (Event/401.evd); "
        "15. O ápice do trauma de Misha no bosque de sua mente (Event/618.evd), onde ela tenta destruir seu próprio corpo adulto por medo "
        "de que Lyner passe a odiá-la, nocauteia Lyner com um golpe desesperado e foge, sob o escárnio analítico de Hama; "
        "16. O terrível colapso do Nível 8 da Cosmosfera (Event/655.evd), reduzido a cinzas e névoa decadente por uma Mudança de Paradigma "
        "forçada sem preparo emocional, provocando a fúria de Hama, que abandona o mundo até que ele seja restaurado; "
        "17. O delicado e tímido Primeiro Mergulho de Aurica na Loja de Mergulho (Event/951.evd), revelando que ela nunca teve parceiro na Igreja "
        "e confiando sua alma a Lyner; "
        "18. A fornalha ardente do Nível 7 em chamas (Event/644.evd); "
        "19. A hilária caçada de Jack e Lyner por um monstro (Event/41.evd) para recuperar um 'pedaço de papel' que Jack alega ser segredo de Estado "
        "de altíssimo valor, após gastar toda a sua fortuna; "
        "20. O prólogo colegial de Raina Harase em Ciel (Event/784.evd), estudante de 16 anos sem namorada num domingo de tédio, com vagas memórias "
        "do 'campo de dados'; "
        "21. O encolhimento de Misha no Reator Três (Event/961.evd); "
        "22. O tutorial de combate de Magia Vermelha de Aurica (Event/54.evd); "
        "23. E a emocionante redenção da consciência de Aurica (Event/751.evd), onde o tigre Don Leon costurado por Lyner devolve a esperança "
        "à heroína, harmoniza o conflito entre o mundo da Razão e a Aurica Maligna e desencadeia a Mudança de Paradigma em direção a Stonehenge."
    ),
    "decisoes_terminologicas": {
        "Horn (ホルン / シルヴァホルン)": "Chifre / Chifre Prateado (instalação ancestral de ressonância na Torre)",
        "Key Room (キールーム)": "[Sala da Chave] (câmara das profundezas onde repousa o Cristal Hymmnos de Mir)",
        "Voice of God / Roar of God (神の咆哮 - Kami no Houkou)": "[Rugido de Deus] (vórtice acústico mortal de energia, corrigindo o 'Voice of God' da NISA)",
        "Power Cylinder (パワーシリンダー)": "[Cilindro de Energia] (artefato mecânico usado para sobrecarregar circuitos)",
        "Thunder Bomb (雷弾)": "[Bomba de Raio] (projétil elétrico catalisador para acionamento de maquinários)",
        "Singing Hill (謳う丘 - Utau Oka)": "[Colina do Canto] (singular canônico das ruínas sacras onde repousam relíquias)",
        "Gale Shot (爆風弾)": "Magia Verde [Tiro Rajada] (magia de impacto que aciona mecanismos e espelhos)",
        "Binary Field (バイナリ野 / 情報野)": "campo de dados (harmonização contra o decalque 'campo binário' da NISA)",
        "Raina Harase (原瀬頼奈 - Harase Raina)": "Raina Harase (identidade simulada de Lyner Barsett no minigame colegial/tokusatsu)",
        "Leila / Meira (塔ヶ崎澪羅 - Tougasaki Meira)": "Leila / senhorita Tougasaki (identidade colegial de Lady Shurelia)",
        "Ciel City (詩恵留市 - Shieru-shi)": "Ciel (cidade fictícia interiorana da simulação colegial)",
        "Don Leon (どんすけ / ドンスケ)": "Don Leon (tigre de pelúcia artesanal que restaura a esperança de Aurica)",
        "Devilish Aurica (悪魔オリカ)": "Aurica Maligna (persona sombria da Cosmosfera de Aurica)",
        "Conscience / Reason (良心 / 理性)": "Consciência / Razão (aspectos estruturais da psique de Aurica em conflito)",
        "Stonehenge (ストーンヘンジ)": "[Stonehenge] (santuário circular de rito para Mudança de Paradigma)"
    },
    "alertas_para_proximo_bloco": (
        "1. O colapso do Nível 8 da Cosmosfera de Misha (Event/655.evd) deixa o mundo psíquico em ruínas e Hama ausente: "
        "atentar para os diálogos subsequentes onde Lyner deve encontrar formas de restaurar o mundo e curar o trauma de amadurecimento de Misha. "
        "2. A libertação da consciência de Aurica e a Mudança de Paradigma em Stonehenge (Event/751.evd) abrirão níveis mais profundos "
        "onde o trauma do massacre do clã e o vírus de Mir virão à tona. "
        "3. No mundo real, a expedição ao Chifre Prateado para desligar as 3 válvulas do [Rugido de Deus] e alcançar a [Sala da Chave] "
        "será o próximo passo da infiltração para recuperar o Cristal Hymmnos de Mir. "
        "4. Preservar o tratamento nobre a Radolf e seu senso de honra ferido pela Igreja decaída. "
        "5. Manter a simetria de 'Raina Harase' e 'Leila' no minigame colegial e a grafia canônica de 'Ar tonelico' e 'Colina do Canto'."
    )
}

final_output = {
    "block_id": "BLK_EVD_011",
    "axis_id": "AXIS_3",
    "axis_name": "HISTÓRIA E EVENTOS",
    "category": "HISTÓRIA E EVENTOS",
    "total_lines": len(dialogues_output),
    "line_count": len(dialogues_output),
    "lines_rewritten": lines_rewritten,
    "lines_approved_as_is": lines_approved_as_is,
    "id_range": [2635, 2873],
    "curator_notes": (
        "Curadoria editorial profunda em duas passagens de 100% das 239 falas de BLK_EVD_011 (IDs 2635 a 2873). "
        "Auditoria integral contra a Tríade de Idiomas (JP SLPS-732.49 soberano; EN SLUS-214.45 suporte; PT-BR viva). "
        "Correção crucial de erro histórico em ID 2825 (NISA inventou 'Are you relieved or disappointed?', restaurando a autêntica gabolice de Jack "
        "'será que no fim das contas a gente não é forte pra caramba?!'); erradicação de erros graves de gênero em ID 2671 (Misha tratada no masculino "
        "'nervoso') e ID 2801 (Aurica tratada no masculino 'nervoso'); resgate de '神の咆哮' como [Rugido de Deus] em vez de 'Voice of God'; "
        "restauração da vocalização fonética original de respiração em sono em IDs 2637, 2638 e 2646 superando 'Zzzz'; "
        "harmonização dos nomes da simulação colegial (Raina Harase, Ciel, Leila/Tougasaki-san); e blindagem total de terminologia canônica: "
        "'Colina do Canto', 'Mudança de Paradigma', 'Cristal Hymmnos', 'Bomba de Raio', 'Magia Verde [Tiro Rajada]', 'campo de dados', "
        "'Cilindro de Energia', 'Aurica Maligna', 'Razão', 'Consciência' e 'Don Leon'."
    ),
    "dialogues": dialogues_output,
    "curated_lines": dialogues_output,
    "scene_handoff": scene_handoff
}

with open(output_path, "w", encoding="utf-8") as out:
    json.dump(final_output, out, ensure_ascii=False, indent=2)

print(f"BLK_EVD_011_output.json generated successfully!")
print(f"Total lines: {len(dialogues_output)}")
print(f"Lines rewritten: {lines_rewritten}")
print(f"Lines approved as is: {lines_approved_as_is}")
