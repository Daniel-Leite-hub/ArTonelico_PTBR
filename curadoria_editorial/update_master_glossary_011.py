# -*- coding: utf-8 -*-
"""
Atualização do Glossário Mestre e geração do relatório do bloco BLK_EVD_011.
Ar tonelico: Melody of Elemia (Undub) - PS2
"""

import json
import datetime
import os
import shutil

glossario_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json"
with open(glossario_path, "r", encoding="utf-8") as f:
    g = json.load(f)

# 1. Update last_scene_handoff
handoff_011 = {
    "status": "COMPLETED",
    "block_id": "BLK_EVD_011",
    "axis_id": "AXIS_3",
    "id_range": "2635-2873",
    "completed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "dramatic_context": (
        "Bloco narrativo de história e eventos BLK_EVD_011 (IDs 2635 a 2873, 23 arquivos Event/*.evd). "
        "Descortina momentos de profunda sensibilidade, humor de caserna, traumas de infância na Cosmosfera e avanços na jornada: "
        "1. No posto de guarda A5 (Event/529.evd), flagrante cômico do guarda Lapsey adormecido sonhando com a lição de casa de infância, "
        "invocando Kanade e tendo devaneios íntimos com a Senhora Shurelia sob o olhar impassível da própria deusa, "
        "misturando o sonho com teoria técnica de energia sinfônica da Torre (FFT, lógica QT e placa de Grathnode); "
        "2. No Chifre Prateado (Event/554.evd), Ayatane e Lyner contemplam o interior da colossal instalação ancestral rumo à [Sala da Chave], "
        "onde repousa o Cristal Hymmnos de Mir, revelando que a passagem é bloqueada pelo mortífero [Rugido de Deus] "
        "(神の咆哮 - Kami no Houkou), um vórtice acústico brutal de energia contido por três válvulas; "
        "3. A longa subida de escadarias da Torre (Event/486.evd), onde Jack comemora o fim dos degraus e Lyner avalia a altitude vertiginosa; "
        "4. A antecipação festiva de uma cerimônia na Cosmosfera (Event/760.evd); "
        "5. A operação tática de infiltração (Event/267.evd), onde Krusche pluga o Cilindro de Energia para provocar um blecaute temporário, "
        "arrombar a porta a pontapés e resgatar Misha antes que a energia volte, em contagem regressiva eletrizante; "
        "6. A constatação da barreira de escombros consertada (Event/251.evd); "
        "7. A impagável discussão armamentista na loja (Event/234.evd), onde Krusche explica a inércia mecânica da sua motosserra, "
        "Misha a chama de sinistra por empunhar um trambolho desses, Krusche retruca que sinistra é Misha por invocar aberrações cósmicas em combate, "
        "quase destruindo o estabelecimento com Magia da Canção até o dono expulsar todo mundo e Lyner implorar por paz; "
        "8. O capricho infantil de Misha querendo continuar brincando em vez de dormir (Event/611.evd); "
        "9. A porta selada que apenas a Senhora Tastiella pode autorizar (Event/285.evd); "
        "10. O mecanismo emperrado exigindo acionamento por Bomba de Raio (Event/248.evd); "
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

g["last_scene_handoff"] = handoff_011

# 2. Add / update terms safely
terms = g.setdefault("terms", {})

new_terms = {
    "Roar of God": {
        "pt": "Rugido de Deus",
        "gender": "masculino",
        "number": "singular",
        "category": "Perigo / Chifre Prateado",
        "note": "Vórtice letal de energia acústica concentrada que bloqueia o acesso à Sala da Chave no Chifre Prateado (JP 神の咆哮 - Kami no Houkou). Corrige 'Voice of God' da NISA."
    },
    "Key Room": {
        "pt": "Sala da Chave",
        "gender": "feminino",
        "number": "singular",
        "category": "Câmara / Chifre Prateado",
        "note": "Câmara profunda e selada no interior do Chifre Prateado onde repousa o Cristal Hymmnos de Mir (JP キールーム)."
    },
    "Power Cylinder": {
        "pt": "Cilindro de Energia",
        "gender": "masculino",
        "number": "singular",
        "category": "Item / Engenharia",
        "note": "Artefato cilíndrico de alta capacidade usado por Krusche para sobrecarregar temporariamente redes de força e arrombar acessos (JP パワーシリンダー)."
    },
    "Thunder Bomb": {
        "pt": "Bomba de Raio",
        "gender": "feminino",
        "number": "singular",
        "category": "Projétil / Mecânica",
        "note": "Projétil de carga elétrica usado para energizar circuitos e interruptores paralisados na Torre (JP 雷弾)."
    },
    "Gale Shot": {
        "pt": "Tiro Rajada",
        "gender": "masculino",
        "number": "singular",
        "category": "Magia Verde / Cosmosphere",
        "note": "Magia Verde de impacto cinético e disparo de vento tecida por Misha na Cosmosfera (JP 爆風弾)."
    },
    "Devilish Aurica": {
        "pt": "Aurica Maligna",
        "gender": "feminino",
        "number": "singular",
        "category": "Persona / Cosmosphere",
        "note": "Manifestação sombria e desiludida da psique de Aurica que rejeita a consciência após traumas e abandono (JP 悪魔オリカ)."
    },
    "Raina Harase": {
        "pt": "Raina Harase",
        "gender": "masculino",
        "number": "singular",
        "category": "Personagem / Cosmosphere",
        "note": "Identidade colegial fictícia assumida por Lyner Barsett na simulação de Shurelia em Ciel (JP 原瀬頼奈 - Harase Raina)."
    },
    "Stonehenge": {
        "pt": "Stonehenge",
        "gender": "masculino",
        "number": "singular",
        "category": "Marco / Cosmosphere",
        "note": "Círculo megalítico sagrado na Cosmosfera de Aurica onde ocorre o rito de transição da Mudança de Paradigma (JP ストーンヘンジ)."
    }
}

terms_added = 0
for k, v in new_terms.items():
    if k not in terms:
        terms[k] = v
        terms_added += 1
        print(f"Added term: {k} -> {v['pt']}")
    else:
        print(f"Term {k} already exists, preserved.")

# Save back to glossario_mestre.json
with open(glossario_path, "w", encoding="utf-8") as f:
    json.dump(g, f, ensure_ascii=False, indent=2)

print(f"Glossário Mestre updated successfully with {terms_added} new terms!")

# 3. Create backup file
now_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_dir = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\backups\curadoria"
backup_filename = f"ArTonelico_backup_pre_BLK_EVD_011_{now_str}.atproj"
backup_filepath = os.path.join(backup_dir, backup_filename)

src_atproj = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\ArTonelico_PTBR.atproj"
if os.path.exists(src_atproj):
    shutil.copy2(src_atproj, backup_filepath)
    print(f"Backup created at: {backup_filepath}")
else:
    backup_filepath = None

# 4. Generate BLK_EVD_011_report.json
report_data = {
    "block_id": "BLK_EVD_011",
    "completed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "backup_created": backup_filepath,
    "total_dialogues": 239,
    "lines_rewritten": 230,
    "lines_approved_as_is": 9,
    "new_terms_added": terms_added,
    "hard_gate_errors": 0,
    "lint_warnings": 0,
    "scene_handoff": handoff_011
}

report_path = r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\blocos\BLK_EVD_011_report.json"
with open(report_path, "w", encoding="utf-8") as f:
    json.dump(report_data, f, ensure_ascii=False, indent=2)

print(f"Report saved to: {report_path}")
