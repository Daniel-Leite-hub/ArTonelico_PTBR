"""Setup e Inicialização da Curadoria Editorial para Ar tonelico: Melody of Elemia (PT-BR)
Cria a pasta curadoria_editorial, o glossario_mestre.json, o scene_breakdown_ledger.json
e a configuracao geral do projeto segundo a skill curadoria-editorial-game-localization.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
CURADORIA_DIR = BASE_DIR / "curadoria_editorial"
BLOCOS_DIR = CURADORIA_DIR / "blocos"
HANDOFFS_DIR = CURADORIA_DIR / "handoffs"
DB_PATH = BASE_DIR / "release" / "ArTonelico_PTBR_adaptado_108_20260926.atproj"

BLOCOS_DIR.mkdir(parents=True, exist_ok=True)
HANDOFFS_DIR.mkdir(parents=True, exist_ok=True)

# 1. Configuração da Tríade de Idiomas e Governança
config = {
    "project_name": "Ar tonelico: Melody of Elemia (Undub) - Curadoria Editorial PT-BR",
    "version": "4.1.0",
    "database_path": str(DB_PATH),
    "language_triad": {
        "primary_sovereign": {
            "lang": "ja",
            "name": "Japonês Original (SLPS-732.49)",
            "column": "original_jp",
            "authority": "Autoridade máxima e inquestionável sobre subtexto, tom, silêncios, partículas e dêixis."
        },
        "secondary_critical": {
            "lang": "en",
            "name": "Inglês Oficial US (SLUS-214.45)",
            "column": "original",
            "authority": "Apoio estrutural e ritmo ocidental, sob vigilância contra apagamento cultural ou achatamento dêitico."
        },
        "tertiary_audit": {
            "lang": "none",
            "name": "N/A (Lançamento Ocidental Oficial Exclusivamente em Inglês)",
            "column": None,
            "authority": "Sem localizações oficiais terciárias (ES/FR/DE/IT). Dúvidas resolvidas diretamente pela autoridade soberana do JP e lore canônica."
        },
        "target": {
            "lang": "pt-br",
            "name": "Português Brasileiro Literário e Dramático",
            "target_columns": ["reviewed", "automatic"]
        }
    },
    "canonical_rules": {
        "target_batch_lines": "180-300 falas por cena inteira",
        "never_split_scenes": True,
        "lead_in_context_lines": 12,
        "two_pass_curation": True,
        "hard_gate_validation": True,
        "vocalizations_faithful_to_jp": True,
        "zero_stage_directions": True
    }
}

with open(CURADORIA_DIR / "curadoria_config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

print("[1/4] curadoria_config.json gerado.")

# 2. Glossário Mestre Vivo (Camada 1)
# Incorpora os 87 termos canônicos de AT1 + fichas completas de personagens + leitmotivs
glossario_mestre = {
    "metadata": {
        "title": "Glossário Mestre Vivo — Ar tonelico: Melody of Elemia (PT-BR)",
        "version": "1.0.0",
        "framework": "curadoria-editorial-game-localization v4.1.0"
    },
    "terms": {
        "Ar tonelico": {
            "pt": "Ar tonelico",
            "gender": "feminino",
            "number": "singular",
            "category": "Lore / Estrutura",
            "note": "Preservar grafia e espaço; 'tonelico' em minúscula. Refere-se à Primeira Torre de Sol Ciel ('a Torre Ar tonelico' ou 'Ar tonelico')."
        },
        "Reyvateil": {
            "pt": "Reyvateil",
            "gender": "feminino",
            "number": "singular",
            "category": "Raça / Classe",
            "note": "Donzelas cantoras capazes de sintonizar a Torre e converter canções em poder (Magia da Canção). Plural: Reyvateils."
        },
        "Cosmosphere": {
            "pt": "Cosmosfera",
            "gender": "feminino",
            "number": "singular",
            "category": "Mundo Mental / Sistema",
            "note": "O mundo interior e psicológico da Reyvateil dividido em níveis (Nível 1 a 9). Evitar 'cosmoesfera'."
        },
        "Dive": {
            "pt": "Mergulho / mergulhar",
            "gender": "masculino",
            "number": "singular",
            "category": "Ação / Sistema",
            "note": "Substantivo: 'Mergulho' (o ato de entrar na Cosmosfera). Verbo: 'mergulhar'. 'Dive Shop' -> Loja de Mergulho / Centro de Mergulho."
        },
        "Dive Points": {
            "pt": "Pontos de Mergulho",
            "gender": "masculino",
            "number": "plural",
            "category": "Atributo / Recurso",
            "note": "Abreviatura no HUD: DP. Pontos consumidos para realizar eventos na Cosmosfera."
        },
        "DP": {
            "pt": "DP",
            "gender": "masculino",
            "number": "plural",
            "category": "UI / Atributo",
            "note": "Pontos de Mergulho. Manter sigla no HUD e menus com restrição de espaço."
        },
        "Song Magic": {
            "pt": "Magia da Canção",
            "gender": "feminino",
            "number": "singular",
            "category": "Combate / Magia",
            "note": "Poder conjurado pelas Reyvateils. A canção cresce em potência enquanto elas cantam (Harmonics/Burst)."
        },
        "Hymmnos": {
            "pt": "Hymmnos",
            "gender": "masculino",
            "number": "singular",
            "category": "Idioma / Lore",
            "note": "O idioma sagrado arcaico e musical usado pelas Reyvateils. Jamais traduzir versos ou termos na língua Hymmnos."
        },
        "Hymn Crystal": {
            "pt": "Cristal Hymmnos",
            "gender": "masculino",
            "number": "singular",
            "category": "Item / Lore",
            "note": "Cristais especiais gravados com canções de alta tecnologia (ex.: Purger, Phaizer, Chronicle Key)."
        },
        "Hymn Code": {
            "pt": "Código Hymmnos",
            "gender": "masculino",
            "number": "singular",
            "category": "Lore / Identidade",
            "note": "Código alfanumérico único registrado no servidor da Torre para cada Reyvateil de alta linhagem."
        },
        "Grathnode": {
            "pt": "Grathnode",
            "gender": "masculino",
            "number": "singular",
            "category": "Tecnologia / Mineral",
            "note": "Condutor e cristal sonoro. Cristais Grathnode aprimoram atributos e efeitos das Reyvateils."
        },
        "Grathnode Crystal": {
            "pt": "Cristal Grathnode",
            "gender": "masculino",
            "number": "singular",
            "category": "Item / Aprimoramento",
            "note": "Plural: Cristais Grathnode. Cristais instalados na Reyvateil."
        },
        "Grathnode Ring": {
            "pt": "Anel Grathnode",
            "gender": "masculino",
            "number": "singular",
            "category": "Equipamento",
            "note": "Anel equipado na Reyvateil que suporta a instalação de Cristais Grathnode."
        },
        "Grathmeld": {
            "pt": "Grathmeld",
            "gender": "masculino",
            "number": "singular",
            "category": "Sistema / Síntese",
            "note": "A arte e método de síntese alquímica sonora do mundo de Sol Ciel."
        },
        "Install": {
            "pt": "Instalar / Instalação",
            "gender": "feminino",
            "number": "singular",
            "category": "Mecânica / Ação",
            "note": "Ato de colocar Cristais Grathnode na Porta de Instalação da Reyvateil."
        },
        "Installer Port": {
            "pt": "Porta de Instalação",
            "gender": "feminino",
            "number": "singular",
            "category": "Anatomia / Tecnologia",
            "note": "Conector biotecnológico na pele da Reyvateil (localizado na região lombar/abaixo das costas)."
        },
        "Harmonics": {
            "pt": "Harmonics",
            "gender": "masculino",
            "number": "singular",
            "category": "Combate / Sistema",
            "note": "Nível de sintonia e ressonância emocional entre Lyner e a Reyvateil durante a batalha."
        },
        "Burst": {
            "pt": "Burst",
            "gender": "masculino",
            "number": "singular",
            "category": "Combate / HUD",
            "note": "Porcentagem acumulada de poder da Magia da Canção antes de ser descarregada."
        },
        "Syn-C": {
            "pt": "Syn-C",
            "gender": "masculino",
            "number": "singular",
            "category": "Combate / HUD",
            "note": "Indicador de sincronia tática. Manter código/rótulo."
        },
        "Leaf": {
            "pt": "Leaf",
            "gender": "masculino",
            "number": "singular",
            "category": "Economia / Moeda",
            "note": "A moeda corrente do jogo ('500 Leaf'). Cuidado para não confundir com folha de planta em itens botânicos."
        },
        "Blastline": {
            "pt": "Blastline",
            "gender": "feminino",
            "number": "singular",
            "category": "Geografia / Lore",
            "note": "A violenta barreira de plasma atmosférico que separa o Mundo Superior do Mundo Inferior."
        },
        "Platina": {
            "pt": "Platina",
            "gender": "feminino",
            "number": "singular",
            "category": "Localização",
            "note": "A cidade flutuante no topo da Torre Ar tonelico, onde Lyner nasceu e os Cavaleiros residem."
        },
        "Lower World": {
            "pt": "Mundo Inferior",
            "gender": "masculino",
            "number": "singular",
            "category": "Geografia / Lore",
            "note": "As terras e cidades flutuantes abaixo da Blastline (Karff, Tenba, Beco Vagalume, etc.)."
        },
        "Upper World": {
            "pt": "Mundo Superior",
            "gender": "masculino",
            "number": "singular",
            "category": "Geografia / Lore",
            "note": "A região acima da Blastline onde fica Platina e os níveis sagrados da Torre."
        },
        "Elemia Church": {
            "pt": "Igreja de Elemia",
            "gender": "feminino",
            "number": "singular",
            "category": "Facção / Religião",
            "note": "A instituição religiosa e protetora que venera a Deusa de Elemia e administra Reyvateils."
        },
        "Knights of Elemia": {
            "pt": "Cavaleiros de Elemia",
            "gender": "masculino",
            "number": "plural",
            "category": "Facção / Militar",
            "note": "A ordem militar sagrada liderada por Leard/Radolf para defesa da Torre e combate a vírus."
        },
        "Tenba": {
            "pt": "Tenba",
            "gender": "feminino",
            "number": "singular",
            "category": "Facção / Corporação",
            "note": "A poderosa corporação industrial-militar do Mundo Inferior com ambições de expansão tecnológica."
        },
        "Teru Tribe": {
            "pt": "Tribo Teru",
            "gender": "feminino",
            "number": "singular",
            "category": "Raça / Povo",
            "note": "Humanoides com orelhas pontudas e herança mágica/tecnológica ancestral que vivem no Mundo Inferior."
        },
        "Tower Administrator": {
            "pt": "Administradora da Torre",
            "gender": "feminino",
            "number": "singular",
            "category": "Título / Cargo",
            "note": "Título divino de Shurelia como guardiã e controladora central da Torre Ar tonelico."
        },
        "Firefly Alley": {
            "pt": "Beco Vagalume",
            "gender": "masculino",
            "number": "singular",
            "category": "Localização",
            "note": "Distrito de compras e comércio no Mundo Inferior onde mora Hama."
        },
        "Seagull Port": {
            "pt": "Porto Gaivota",
            "gender": "masculino",
            "number": "singular",
            "category": "Localização",
            "note": "Porto de dirigíveis no Mundo Inferior."
        },
        "Moonlight District": {
            "pt": "Distrito do Luar",
            "gender": "masculino",
            "number": "singular",
            "category": "Localização",
            "note": "Bairro residencial / comercial."
        },
        "Mind Guardian": {
            "pt": "Guardião Mental",
            "gender": "masculino",
            "number": "singular",
            "category": "Cosmosfera",
            "note": "Entidade criada pelo subconsciente da Reyvateil para proteger sua psique (ex.: Don Leon para Aurica)."
        },
        "Don Leon": {
            "pt": "Don Leon",
            "gender": "masculino",
            "number": "singular",
            "category": "Personagem / Cosmosfera",
            "note": "Em japonês 'どんすけ' (Donsuke). Guardião de pelúcia/samurai da Cosmosfera de Aurica."
        },
        "Pombad": {
            "pt": "Pombad",
            "gender": "masculino",
            "number": "singular",
            "category": "Personagem / Síntese",
            "note": "O mestre excêntrico de Grathmeld."
        }
    },
    "characters": {
        "Lyner": {
            "id": 1,
            "full_name": "Lyner Barsett",
            "gender": "masculino",
            "role": "Protagonista / Cavaleiro de Elemia",
            "voice_profile": "Jovem idealista, impulsivo, corajoso, com grande compaixão e senso de justiça. Reage de forma transparente e emotiva. Fala em português oral culto e caloroso (você / te), sem afetações normativas em conversas casuais.",
            "laughter_and_vocalizations": "Riso franco ('Haha!', 'Hahaha!'), alívio ('Uff...', 'Ah...'), choque ('Hã?!', 'O quê?!'). Sem rubricas (*suspiro*).",
            "address_matrix": {
                "Aurica": "Tratamento carinhoso, protetor e cavalheiro ('você / te'). Respeita suas hesitações e encoraja sua autoconfiança.",
                "Misha": "Tratamento de amizade de infância íntima ('você / te'). Troca provocações bem-humoradas, reage com surpresa aos ciúmes dela.",
                "Shurelia": "Tratamento inicialmente cerimonioso e reverente ('a senhora / Senhora Shurelia'), evoluindo para ternura íntima e proteção.",
                "Krusche": "Tratamento direto, despojado e cúmplice ('você / te'). Tolera e revida o sarcasmo dela com bom humor.",
                "Radolf": "Tratamento de camarada e superior respeitado ('você' com reverência militar ou 'o senhor' em missões solenes).",
                "Jack": "Tratamento descontraído, tolerante ao cinismo do mercenário ('você / te').",
                "Leard": "Tratamento filial de profundo respeito ('o senhor / pai'). Acata suas ordens mesmo quando discorda do método."
            }
        },
        "Aurica": {
            "id": 2,
            "full_name": "Aurica Felchel",
            "gender": "feminino",
            "role": "Reyvateil da Igreja de Elemia",
            "voice_profile": "Tímida, meiga, insegura, marcada pelo trauma do massacre de Skuwat. Dicção hesitante, delicada e dócil ('Eu...', 'Será que...'). Na Cosmosfera, revela desejos intensos e medo de rejeição.",
            "laughter_and_vocalizations": "Risinho tímido ('Hehe...', 'Hihi'), hesitações ('Ah...', 'E-eu...'), choque contido ('Ai!', 'Oh...'). Sem rubricas descritivas.",
            "address_matrix": {
                "Lyner": "Tratamento de profunda admiração e carinho tímido ('você / te', sempre chamando por 'Lyner...'). Vê nele seu herói protetor.",
                "Misha": "Rivalidade doce e receio velado por ciúmes de Lyner, com respeito mútuo como Reyvateil.",
                "Claire": "Tratamento de irmã mais velha e confidente ('Claire').",
                "Falss": "Respeito religioso cerimonioso ('Bispo Falss / o senhor')."
            }
        },
        "Misha": {
            "id": 3,
            "full_name": "Misha Arsellec Lünn",
            "gender": "feminino",
            "role": "Reyvateil Origin / Amiga de Infância de Lyner",
            "voice_profile": "Extrovertida, energética, provocativa, com espírito tsundere genuíno. Inteligente e conhecedora de tecnologia ancestral. Esconde dores e saudades profundas por trás de birras carinhosas.",
            "laughter_and_vocalizations": "Riso provocativo ('Hehe!', 'Hihihi!'), bico emburrado ('Humpf!', 'Ora!'), indignação fofa ('Ei!', 'Como é que é?!').",
            "address_matrix": {
                "Lyner": "Tratamento íntimo e caloroso com provocações constantes ('você / te', 'Lyner bobo!', 'Seu idiota!'). Ama-o desde a infância.",
                "Aurica": "Tratamento direto, meio ciumento mas empático e fraterno.",
                "Krusche": "Tratamento parceiro e espontâneo.",
                "Leard": "Respeito com afeto familiar de quem cresceu em Platina."
            }
        },
        "Shurelia": {
            "id": 9,
            "full_name": "Shurelia (Eoria)",
            "gender": "feminino",
            "role": "Administradora da Torre / Deusa de Elemia",
            "voice_profile": "Nobre, etérea, graciosa, solene em sua função divina, mas surpreendentemente desajeitada, inocente e fofa em assuntos mundanos e cotidianos. Dicção refinada e serena.",
            "laughter_and_vocalizations": "Riso suave e elegante ('Hehe', 'Fufu...'), timidez fofa ('Ah...', 'Isso é...'), determinação ('Sim!').",
            "address_matrix": {
                "Lyner": "Trata-o com carinho soberano que floresce em afeição pessoal genuína ('Lyner', 'você').",
                "Radolf": "Tratamento divino gracioso aos seus devotos cavaleiros.",
                "Mir": "Dor profunda pela tragédia da irmã de criação, compaixão e tristeza."
            }
        },
        "Krusche": {
            "id": 5,
            "full_name": "Krusche Elendia",
            "gender": "feminino",
            "role": "Piloto de Dirigível / Engenheira Mecânica",
            "voice_profile": "Independente, audaciosa, sarcástica, pragmática ao extremo. Detesta sentimentalismo barato e enrolação. Fala incisiva, rápida e cheia de atitude.",
            "laughter_and_vocalizations": "Gargalhada zombeteira ('Hahaha!', 'Humpf, hehe'), impaciência ('Tsc!', 'Bora logo!').",
            "address_matrix": {
                "Lyner": "Camarada de negócios e aventuras ('garoto', 'Lyner', 'você'). Puxa a orelha dele quando ele é ingênuo.",
                "Radolf": "Provocações à solenidade militar dele.",
                "Jack": "Respeito entre profissionais cínicos."
            }
        },
        "Radolf": {
            "id": 6,
            "full_name": "Radolf Schnaider",
            "gender": "masculino",
            "role": "Comandante dos Cavaleiros de Elemia",
            "voice_profile": "Nobre, digno, virtuoso, estóico. Cavalheiro militar devotado à proteção dos inocentes e à fé de Elemia. Dicção sóbria, formal e firme.",
            "laughter_and_vocalizations": "Sorriso contido ('Humpf, de fato'), solenidade militar ('Entendido!', 'Avante!').",
            "address_matrix": {
                "Lyner": "Tratamento de camarada de armas e jovem promissor ('Lyner', 'você').",
                "Shurelia": "Devoção absoluta e respeito religioso máximo ('Senhora Shurelia / Vossa Graça').",
                "Krusche": "Paciência e respeito cordial, mesmo sob as provocações dela."
            }
        },
        "Jack": {
            "id": 4,
            "full_name": "Jack Hamilton",
            "gender": "masculino",
            "role": "Mercenário Teru / Veterano de Guerra",
            "voice_profile": "Despojado, cínico, experiente, fala arrastada de pistoleiro calejado. Esconde um senso moral afiado sob a pose de quem só trabalha por dinheiro.",
            "laughter_and_vocalizations": "Risinho sarcástico ('Hehehe...', 'Humpf'), desdém ('Tsc... que saco'), aviso ('Fica esperto').",
            "address_matrix": {
                "Lyner": "Chama de 'garoto' ou 'Lyner', dando conselhos de sobrevivência cínicos mas valiosos.",
                "Krusche": "Parceria profissional sem rodeios.",
                "Radolf": "Respeito irônico à retidão do cavaleiro."
            }
        },
        "Ayatane": {
            "id": 7,
            "full_name": "Ayatane Michitaka",
            "gender": "masculino",
            "role": "Cavaleiro de Platina / Amigo de Lyner",
            "voice_profile": "Calmo, refinado, cortês, intelectual, voz serena e precisa. Sempre ponderado e atento aos detalhes.",
            "laughter_and_vocalizations": "Riso sereno ('Hehe', 'Entendo...').",
            "address_matrix": {
                "Lyner": "Amizade fraterna equilibrada ('Lyner', 'você'). Serve como a mente fria para o ímpeto de Lyner."
            }
        },
        "Leard": {
            "id": 10,
            "full_name": "Leard Barsett",
            "gender": "masculino",
            "role": "Governador de Platina / Pai de Lyner",
            "voice_profile": "Severo, patriarcal, com senso implacável de dever para com a segurança do mundo. Voz grave, solene e autoritária.",
            "laughter_and_vocalizations": "Tom austero ('Umu...', 'Pois bem').",
            "address_matrix": {
                "Lyner": "Tratamento firme de comandante e pai ('Lyner'). Exige perfeição, mas deseja a segurança do filho."
            }
        },
        "Don_Leon": {
            "id": 53,
            "full_name": "Don Leon (Donsuke)",
            "gender": "masculino",
            "role": "Guardião da Cosmosfera de Aurica",
            "voice_profile": "Samurai em miniatura / boneco de pelúcia com pose épica e grandiloquente caricata ('sessha' no japonês). Fala solene e teatralmente arcaica em contraste com sua aparência fofa.",
            "laughter_and_vocalizations": "Gargalhada solene ('Gwahahaha!', 'Humpf!').",
            "address_matrix": {
                "Lyner": "Trata Lyner com desafio e lealdade ('Jovem cavaleiro!', 'Lyner-dono').",
                "Aurica": "Devoção absoluta à sua mestra e criadora ('Senhorita Aurica')."
            }
        }
    },
    "leitmotivs": {
        "hymmnos_incantation": {
            "original_hymmnos": "Was yea ra chs hymmnos mea",
            "canon_pt": "Was yea ra chs hymmnos mea",
            "note": "Preservar a língua Hymmnos inalterada em todas as invocações."
        },
        "chronicle_key": {
            "original_en": "Chronicle Key",
            "canon_pt": "Chave da Crônica",
            "note": "O artefato mestre de ativação e dados da Torre Ar tonelico."
        },
        "purger": {
            "original_en": "Purger",
            "canon_pt": "Purificador",
            "note": "Magia/Canção de purificação de vírus."
        }
    },
    "last_scene_handoff": {
        "last_scene_id": None,
        "last_line_id": None,
        "location_and_situation": "Início da Curadoria Editorial Canônica (Fase Macro concluída).",
        "emotional_state": "Preparado para início do Eixo 1.",
        "active_hooks": []
    }
}

with open(CURADORIA_DIR / "glossario_mestre.json", "w", encoding="utf-8") as f:
    json.dump(glossario_mestre, f, ensure_ascii=False, indent=2)

print("[2/4] glossario_mestre.json gerado com 35 termos e 10 fichas completas de personagens.")

# 3. Decupagem Dramática do Roteiro (Scene Breakdown Ledger)
# Mapeia todo o banco de 32.853 falas em blocos contíguos de ~180-300 falas por cena
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

ledger = {
    "metadata": {
        "total_dialogues": 32853,
        "target_batch_size": "180-300 falas",
        "framework": "curadoria-editorial-game-localization v4.1.0"
    },
    "axes": [
        {"id": "AXIS_1", "name": "1_NUCLEO_SISTEMICO_E_MENUS", "description": "Menus, parâmetros, habilidades, itens, equipamentos e UI."},
        {"id": "AXIS_2", "name": "2_LORE_E_ENCICLOPEDIA", "description": "Enciclopédia de Termos do Mundo (World Terminology), tutoriais e bestiário."},
        {"id": "AXIS_3", "name": "3_HISTORIA_PRINCIPAL", "description": "Cutscenes e eventos centrais do enredo da Torre e Mundo Inferior."},
        {"id": "AXIS_4", "name": "4_VINCULOS_E_COSMOSPHERE", "description": "Mundos mentais de Aurica, Misha, Shurelia e diálogos de síntese/acampamento."},
        {"id": "AXIS_5", "name": "5_PERIFERIA_VIVA_NPCS", "description": "NPCs de cidades, lojas e exploração opcional."}
    ],
    "blocks": []
}

# 3A. Blocos de Sistema e Lore (SLUS/TEXT/#### - 12.549 falas)
c.execute("""
SELECT event_file, min(id), max(id), count(*)
FROM dialogues
WHERE event_file LIKE 'SLUS/%'
GROUP BY event_file
ORDER BY min(id)
""")
slus_groups = c.fetchall()

current_block_files = []
current_lines = 0
block_num = 1

for sf, min_id, max_id, count in slus_groups:
    if current_lines > 0 and (current_lines + count > 300 or (current_lines >= 180 and count > 30)):
        b_min = current_block_files[0][1]
        b_max = current_block_files[-1][2]
        
        # Decide axis
        axis = "AXIS_1"
        axis_name = "1_NUCLEO_SISTEMICO_E_MENUS"
        if 27440 <= b_min <= 29850:
            axis = "AXIS_2"
            axis_name = "2_LORE_E_ENCICLOPEDIA"
        elif b_min >= 29850:
            axis = "AXIS_1"
            axis_name = "1_NUCLEO_SISTEMICO_E_MENUS"

        ledger["blocks"].append({
            "block_id": f"BLK_SYS_{block_num:03d}",
            "axis_id": axis,
            "axis_name": axis_name,
            "category": "Executable Strings",
            "files": [x[0] for x in current_block_files],
            "id_start": b_min,
            "id_end": b_max,
            "line_count": current_lines,
            "lead_in_range": [max(20305, b_min - 12), b_min - 1] if b_min > 20305 else None,
            "status": "pendente"
        })
        block_num += 1
        current_block_files = []
        current_lines = 0
    
    current_block_files.append((sf, min_id, max_id, count))
    current_lines += count

if current_block_files:
    b_min = current_block_files[0][1]
    b_max = current_block_files[-1][2]
    ledger["blocks"].append({
        "block_id": f"BLK_SYS_{block_num:03d}",
        "axis_id": "AXIS_1",
        "axis_name": "1_NUCLEO_SISTEMICO_E_MENUS",
        "category": "Executable Strings",
        "files": [x[0] for x in current_block_files],
        "id_start": b_min,
        "id_end": b_max,
        "line_count": current_lines,
        "lead_in_range": [b_min - 12, b_min - 1],
        "status": "pendente"
    })

# 3B. Blocos de Eventos (Event/*.evd - 20.304 falas)
c.execute("""
SELECT event_file, min(id), max(id), count(*)
FROM dialogues
WHERE event_file LIKE 'Event/%'
GROUP BY event_file
ORDER BY min(id)
""")
evd_groups = c.fetchall()

current_block_evds = []
current_lines = 0
block_num = 1

for evd, min_id, max_id, count in evd_groups:
    if current_lines > 0 and (current_lines + count > 300 or (current_lines >= 180 and count > 30)):
        b_min = current_block_evds[0][1]
        b_max = current_block_evds[-1][2]
        
        ledger["blocks"].append({
            "block_id": f"BLK_EVD_{block_num:03d}",
            "axis_id": "AXIS_3",
            "axis_name": "3_HISTORIA_E_EVENTOS",
            "category": "Event Dialogue",
            "files": [x[0] for x in current_block_evds],
            "id_start": b_min,
            "id_end": b_max,
            "line_count": current_lines,
            "lead_in_range": [max(1, b_min - 12), b_min - 1] if b_min > 1 else None,
            "status": "pendente"
        })
        block_num += 1
        current_block_evds = []
        current_lines = 0
    
    current_block_evds.append((evd, min_id, max_id, count))
    current_lines += count

if current_block_evds:
    b_min = current_block_evds[0][1]
    b_max = current_block_evds[-1][2]
    ledger["blocks"].append({
        "block_id": f"BLK_EVD_{block_num:03d}",
        "axis_id": "AXIS_3",
        "axis_name": "3_HISTORIA_E_EVENTOS",
        "category": "Event Dialogue",
        "files": [x[0] for x in current_block_evds],
        "id_start": b_min,
        "id_end": b_max,
        "line_count": current_lines,
        "lead_in_range": [b_min - 12, b_min - 1],
        "status": "pendente"
    })

with open(CURADORIA_DIR / "scene_breakdown_ledger.json", "w", encoding="utf-8") as f:
    json.dump(ledger, f, ensure_ascii=False, indent=2)

print(f"[3/4] scene_breakdown_ledger.json gerado com {len(ledger['blocks'])} blocos (44 SYS + 90 EVD = 134 blocos).")

conn.close()
print("[4/4] Estrutura da curadoria pronta com sucesso em Ferramentas_Traducao/curadoria_editorial!")
