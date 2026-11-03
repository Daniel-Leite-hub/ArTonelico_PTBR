# -*- coding: utf-8 -*-
"""Atualiza o glossario_mestre.json com as decisões canônicas do bloco BLK_EVD_053."""

import json
from pathlib import Path

GLOSSARY_PATH = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\glossario_mestre.json")

with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
    glossary = json.load(f)

# Novos termos do bloco
new_terms = {
    "Teacher's Tears": {
        "pt": "Lágrimas da Professora",
        "gender": "feminino",
        "number": "plural",
        "category": "Item / Cosmosphere",
        "note": "先生の涙. Ingrediente lendário de alquimia coletado das lágrimas de desespero docente da professora Ingrid no crossover de Atelier Marie na Cosmosfera de Aurica (ID 12569)."
    },
    "Aurica No. 1": {
        "pt": "Aurica nº 1",
        "gender": "feminino",
        "number": "singular",
        "category": "Magia Vermelha / Cosmosphere",
        "note": "オリカ一号. Engenhoca alquímica cômica e explosiva sintetizada por Aurica personificada como Marie, convertida em feitiço de combate de Magia Vermelha (ID 12584, 12620)."
    },
    "Frost Mountain": {
        "pt": "Montanha Geada",
        "gender": "feminino",
        "number": "singular",
        "category": "Localização / Cosmosphere",
        "note": "樹氷山 (Juhyōzan). Montanha glacial na Cosmosfera de Misha onde ocorre o duelo interior decisivo entre a faceta madura/guardiã e a persona infantil deprimida (ID 12539; padronizado com BLK_SYS_011 ID 23234)."
    },
    "Holy War": {
        "pt": "Guerra Santa",
        "gender": "feminino",
        "number": "singular",
        "category": "Lore / Religião",
        "note": "聖戦 (seisen). Pretexto fanático bradado pelos cavaleiros rebeldes e corrompidos da Igreja de Elemia para saquear e espalhar terror pelas ruas de Platina (ID 12639)."
    },
    "Atelier Marie: Alchemist of Salburg": {
        "pt": "Atelier Marie: A Alquimista de Salburg",
        "gender": "masculino",
        "number": "singular",
        "category": "Crossover / Meta",
        "note": "マリーのアトリエ・ザールブルグの錬金術士. Primeiro título clássico da franquia Atelier desenvolvido pela Gust em 1997, parodiado e divulgado com quebra de quarta parede por Aurica na Cosmosfera (ID 12593)."
    }
}

for term, data in new_terms.items():
    glossary["terms"][term] = data

# Atualização de nuances de personagens
if "Radolf" in glossary.get("characters", {}):
    glossary["characters"]["Radolf"]["address_matrix"]["Igreja de Elemia (Crise)"] = "Responsabilidade ética inabalável. Mesmo caluniado de traição (謀反の濡れ衣), assume perante Lyner e Platina todo o peso moral dos desmandos praticados pelos cavaleiros clericais na dita Guerra Santa."

if "Aurica" in glossary.get("characters", {}):
    glossary["characters"]["Aurica"]["address_matrix"]["Lyner (Nível 9)"] = "Transparência afetiva absoluta e desarmamento total ('Não sobrou mais nada. Já não tenho mais nada para te mostrar, Lyner. Não tenho mais nenhum segredo guardado de você')."

# Atualização de handoff
glossary["last_scene_handoff"] = {
    "resumo_dramatico": "O bloco BLK_EVD_053 consolida três momentos capitais de alta densidade psicológica, comédia metalinguística e drama ético-militar: (1) Na profundeza da Cosmosfera de Misha (Event/658.evd), Lyner é arrastado por um pesadelo sufocante onde cópias distorcidas de Aurica e Misha tentam executá-lo em meio a torturas mentais; a persona infantil e deprimida de Misha tenta seduzi-lo a um pacto suicida para trancarem-se juntos para sempre em um quarto suspenso no nada até morrerem dormindo; a faceta madura de Misha invade o local e denuncia a baixeza da chantagem psicológica; perante a impossibilidade de coexistência pacífica, as duas metades partem para a Montanha Geada para um duelo de aniquilação mútua; Hama, a Guardiã da Mente, resgata Lyner à beira do desespero e o conclama a impedir o duelo fraticida que destruiria a existência da garota. (2) Na Cosmosfera de Aurica (Event/778.evd), vive-se a paródia antológica de Atelier Marie: Aurica encarna Marie às vésperas do fim do prazo de 5 anos da Academia de Salburg; a temida professora Ingrid invade o ateliê aos berros e Lyner consegue coletar o item de síntese 'Lágrimas da Professora' diretamente do pranto de desgosto da mestra; Aurica sintetiza a caótica 'Aurica nº 1' e faz propaganda do jogo em quebra hilária da 4ª parede; de volta à Cosmosfera, o espírito do mistério se reintegra à alma de Aurica, permitindo que a heroína atinja a transparência emocional absoluta e teça suas magias finais com Lyner. (3) No rescaldo do confronto contra o Bispo Falss (Event/369.evd), o prelado conspirador desaba perante Radolf, Ayatane e Lyner, amaldiçoando-os por terem destruído a última esperança de deter o declínio do mundo através do poder civilizatório de Mir; após a morte do bispo, Radolf pede perdão a Lyner e Ayatane pela devassidão provocada pelos cavaleiros rebeldes da Igreja em Platina sob o estandarte de uma 'Guerra Santa', enquanto Ayatane contempla com respeito assombroso a integridade inabalável do comandante militar que se recusa a abandonar seu senso de responsabilidade mesmo tendo sido caluniado como traidor.",
    "decisoes_terminologicas": {
        "Montanha Geada": "樹氷山 (palco do confronto entre as facetas de Misha, padronizado com BLK_SYS_011)",
        "Lágrimas da Professora": "先生の涙 (item de síntese colhido do pranto de Ingrid)",
        "Aurica nº 1": "オリカ一号 (engenhoca alquímica e Magia Vermelha tecida no Nível 9)",
        "Figurino \"Marlone\"": "コスチューム「マルローネ」 (traje de Marie adquirido após a simulação)",
        "Guerra Santa": "聖戦 (falso estandarte religioso usado na pilhagem de Platina)",
        "Atelier Marie: A Alquimista de Salburg": "マリーのアトリエ・ザールブルグの錬金術士 (metalinguagem e 4ª parede)",
        "Falsa acusação de traição": "謀反の濡れ衣 (calúnia política imposta a Radolf)"
    },
    "alertas_para_proximo_bloco": "A narrativa avança para a chegada dos heróis a Platina devastada pelo motim religioso da Igreja e a preparação solene para o avanço em direção ao clímax cósmico, exigindo coerência sobre a dor moral de Radolf e o amadurecimento heroico de Lyner."
}

with open(GLOSSARY_PATH, "w", encoding="utf-8") as f:
    json.dump(glossary, f, indent=2, ensure_ascii=False)

print(f"[SUCESSO] Glossário mestre atualizado em {GLOSSARY_PATH}")
