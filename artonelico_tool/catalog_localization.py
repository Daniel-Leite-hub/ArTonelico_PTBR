"""Conservative, game-aware PT-BR localization of non-dialogue executable labels.

These are editorial base translations, not API responses or approved reviews.
Proper names and Hymmnos terminology are intentionally left unchanged.
"""

from __future__ import annotations

import sqlite3
from collections import Counter

from .evd import encode_game_text
from .short_catalog_terms import short_catalog_term


TERMS = {
    # Character sheet and menus. Keep combat abbreviations where slots are tiny.
    "Item": "Item", "Leaf": "Leaf", "DP": "DP", "HP": "HP", "MP": "MP",
    "Lyner": "Lyner", "Aurica": "Aurica", "Ar tonelico": "Ar tonelico",
    "Pombad": "Pombad", "Syn-C": "Syn-C",
    "Time Played": "Tempo de jogo", "Weapon": "Arma",
    "Armor": "Armadura", "Accessory": "Acessório", "Attack": "Ataque",
    "F Attack": "Atq. Fogo", "I Attack": "Atq. Gelo",
    "L Attack": "Atq. Raio", "W Attack": "Atq. Vento",
    "Defense": "Defesa", "F Resist": "Res. Fogo",
    "I Resist": "Res. Gelo", "L Resist": "Res. Raio",
    "W Resist": "Res. Vento", "Agility": "Agilidade",
    "Age:": "Idade:", "Years": "anos", "Gender:": "Sexo:",
    "Male": "Masculino", "Female": "Feminino",
    "Height:": "Altura:", "Weight:": "Peso:",
    "Likes:": "Gosta de:", "Dislikes:": "Não gosta de:",
    "Dream:": "Sonho:", "Total Magic": "Magias totais",
    "Quality": "Qualidade", "Current Equipment": "Equipamento atual",
    "Named": "Nome", "Named:": "Nome:", "Category": "Categoria",
    "Equip [Accessory]": "Equipar [Acessório]", "Memo": "Anotação",
    "Recipe": "Receita", "Use Effect": "Efeito ao usar",
    "(Grathnode) Recrystallization": "Recristalização",
    "Enhancements": "Aprimoramentos",
    "Equipable Characters ": "Personagens que equipam ",
    "Change Parameter": "Alteração de atributo",
    "GD Resist": "Res. GD", "Spawn Point": "Local de aparição",
    "Dropped Items": "Itens obtidos", "Home": "Casa", "Job": "Profissão",
    "Likes": "Gosta de", "Dislikes": "Não gosta de",
    "Dream": "Sonho", "Hobbies": "Passatempos", "Motto": "Lema",
    "Amount Made": "Quantidade criada", "Old Item": "Item anterior",
    "Selling Price": "Preço de venda", "Combined Item": "Item sintetizado",
    "Number": "Quantidade", "Total Price": "Preço total",
    "Own": "Possui", "Stock": "Estoque", "Required DP": "DP necessário",
    "Enter": "Entrar", "Return to Reality": "Voltar à realidade",
    "Play Time": "Tempo de jogo", "Lazy": "Preguiçosa",
    "Don’t Sing at Start": "Sem canto inicial",
    "Don’t sing at start": "Sem canto inicial",
    "ON": "LIG.", "English": "Inglês", "Burst Chart ": "Gráfico de Burst ",
    "Explanation": "Explicação", "Magnification": "Multiplicador",
    "Required MP": "MP necessário", "Ultimate Cosmosphere": "Cosmosfera final",
    "Costumes in Possession ": "Trajes obtidos ",
    "Magics Acquired": "Magias aprendidas",
    "Cosmosphere Explored": "Cosmosfera explorada",
    "Conversations Achieved": "Conversas concluídas",
    "Past Conversations ": "Conversas anteriores ",
    "Unseen Conversations": "Conversas inéditas",
    "About to Expire": "Quase esgotado", "Required HP": "HP necessário",
    "Yes": "Sim", "No": "Não", "Use": "Usar", "Buy": "Comprar",
    "Flee": "Fugir", "Equipment": "Equipamento",
    "Formation": "Formação", "Status": "Estado", "Card": "Carta",
    "Help": "Ajuda", "System": "Sistema", "Save": "Salvar",
    "Load": "Carregar", "Current Objective": "Objetivo atual",
    "Rest": "Descansar", "Magic Reference": "Guia de magias",
    "Costume": "Traje", "Song Magic": "Magia de Canção",
    "Please select Reyvateil": "Selecione a Reyvateil",
    "Please select which one you would like to see": "Selecione o que deseja ver",
    # Cosmosphere map names; personal names and established setting terms stay intact.
    "School": "Escola", "Disappointment Mountain": "Monte da Decepção",
    "Volcano": "Vulcão", "Hope Mountain": "Monte da Esperança",
    "Church": "Igreja", "School Dormitory": "Dormitório da escola",
    "Orthodox Church": "Igreja Ortodoxa",
    "Wasted Mansion": "Mansão abandonada",
    "Overlord Castle": "Castelo do Soberano",
    "Academy": "Academia", "Weapon Shop": "Loja de armas",
    "Belzenburg Castle": "Castelo de Belzenburg",
    "Eternal Street": "Rua Eterna", "Constraint House": "Casa das Restrições",
    "Frost Mountain": "Monte Gelado",
    "Wharf of Endless Calm": "Cais da Calmaria Eterna",
    "Sleeping Forest": "Floresta Adormecida",
    "Life Hall": "Salão da Vida", "Temple": "Templo",
    "Sigzar Castle": "Castelo de Sigzar", "Bar": "Bar",
    "Eastern Plateau": "Planalto Oriental",
    "South Market Street": "Rua do Mercado Sul",
    "Under Tower School": "Escola sob a Torre",
    "Public Pool": "Piscina pública",
    "Park Overlooking the Sea": "Parque com vista para o mar",
    "Chapel": "Capela", "Town of the Second Era": "Cidade da Segunda Era",
    "Wasteland": "Terra desolada", "Tower and Door": "Torre e Porta",
    "Stonehenge": "Stonehenge", "Castle": "Castelo",
    "Eternal City": "Cidade Eterna", "School Building": "Prédio da escola",
    "Pier": "Píer", "Small Room": "Sala pequena",
    "Moon Mansion": "Mansão da Lua", "Pool": "Piscina",
    "Class": "Sala de aula", "Campus": "Campus",
    "Night Stall": "Barraca noturna", "Cafe": "Café",
    "Full Scenery": "Panorama completo", "Nemo Inn": "Pousada de Nemo",
    # Combat commands and effects. Names of named monsters are not generalized.
    "Pom Tackle": "Investida Pom", "Self Evolution": "Autoevolução",
    "Pom Blast": "Explosão Pom", "Jumping Thorn": "Espinho saltador",
    "Triple Attack": "Ataque triplo", "Chaotic Triple": "Triplo caótico",
    "Fusion Beam": "Raio de fusão", "Flower Shot": "Disparo floral",
    "Acid Rain": "Chuva ácida", "Mouthful": "Mordida voraz",
    "Sleepy Gas": "Gás sonífero", "Poisony Gas": "Gás venenoso",
    "Tingly Gas": "Gás paral.", "Collapsing Gas": "Gás debilitante",
    "Dangerous Pollen": "Pólen perigoso",
    "Invisible Pollen": "Pólen invisível",
    "Healing Pollen": "Pólen curativo", "Bite": "Mordida",
    "Sleepy Bite": "Mordida sonífera",
    "Poisonous Bite": "Mordida venenosa",
    "Paralyzing Bite": "Mordida paralisante",
    "Super Bite": "Supermordida", "Cut": "Crt",
    "Spirit": "Espírito", "Slash": "Golpe", "Thunder": "Trovão",
    "Fillet": "Filetar", "Give thy Life": "Dê sua vida",
    "Godspeed": "Velocidade divina",
    "Lightning Slash": "Golpe relâmpago",
    "Gale Slash": "Golpe de vendaval",
    "Burning Slash": "Golpe flamejante",
    "Fast Shot": "Tiro rápido", "Full Auto": "Rajada automática",
    "Super Shot": "Supertiro", "Sleep Shot": "Tiro sonífero",
    "Stun Shot": "Tiro paralisante",
    "Frostbite KEI-BO": "KEI-BO congelante",
    "Electromagnetic KEI-BO": "KEI-BO eletromagnético",
    "Full Combination": "Combinação total",
    "Temple Strike": "Golpe na têmpora", "Healing": "Cura",
    "Divine Punishment": "Punição divina",
    "Verse of Curse": "Verso da maldição",
    "Blessing": "Bênção", "Soul Drain": "Dreno de alma",
    "Shadow Attack": "Ataque sombrio",
    "Summon Hellfire": "Invocar fogo infernal",
    "Summon Tornado": "Invocar tornado",
    "Laser": "Laser", "Ice Beam": "Raio de gelo",
    "Electromagnetic Laser": "Laser eletromagnético",
    "Mystery Ray": "Raio misterioso", "Alarm": "Alarme",
    "Request Aid": "Pedir ajuda", "Bit Attack": "Ataque de bits",
    "All Range": "Alcance total", "Screw Dive": "Mergulho giratório",
    "Super Bomb": "Superbomba", "Fire Shield": "Escudo de fogo",
    "Ice Shield": "Escudo de gelo",
    "Electric Shield": "Escudo elétrico",
    "Wind Shield": "Escudo de vento",
    "Full Barrier": "Barreira total",
    "Self Recovery": "Autocura", "Mega Cannon": "Megacanhão",
    "Dive Attack": "Ataque em mergulho",
    "Sky Drive": "Voo celeste", "Single-Loader Gun": "Arma monotiro",
    "Dual Chamber Gun": "Arma dupla", "Enemy Explosion": "Explosão inimiga",
    "Homing Shot": "Tiro teleguiado",
    "Energy Drain": "Dreno de energia",
    "Flame Thrower": "Lança-chamas",
    "Absolute Zero": "Zero absoluto",
    "Induced Explosion": "Explosão induzida",
    "Assault Storm": "Tempestade de assalto",
    "Steep Descent": "Descida íngreme",
    "Fire Breath": "Sopro de fogo",
    "Poison Mist": "Névoa venenosa",
    "Call Lightning": "Invocar relâmpago",
    "Blizzard": "Nevasca", "Cyclone": "Ciclone",
    "Aurora Breath": "Sopro de aurora",
    "Tiny Fire": "Chama pequena", "Tiny Ice": "Gelo pequeno",
    "Tiny Thunder": "Trovão pequeno",
    "Flame Scythe": "Foice flamejante",
    "Hellfire": "Fogo infernal",
    "Lightning Flash": "Clarão elétrico",
    "Tornado": "Tornado", "Calamity": "Calamidade",
    "Battle Command": "Comando de batalha",
    "Broken Whistle": "Apito quebrado",
    "Beast Calling": "Chamar feras",
    "Bird Calling": "Chamar aves",
    "Machine Calling": "Chamar máquinas",
    "Energy Ball": "Esfera de energia",
    "Plasma Ball": "Esfera de plasma",
    "Sleepy Dragon": "Dragão sonolento",
    "Guardian Call": "Chamar guardião",
    "Life Warm": "Calor vital", "Life Refresh": "Renovar vida",
    "Life Shower": "Chuva de vida",
    "Regeneration": "Regeneração",
    "Poison Immunity": "Imune a veneno",
    "Paralyze Immunity": "Imune a paralisia",
    "Darkness Immunity": "Imune a cegueira",
    "Absorb Fire": "Absorver fogo", "Absorb Ice": "Absorver gelo",
    "Absorb Lightning": "Absorver raio",
    "Absorb Wind": "Absorver vento",
    "Absorb Magic": "Absorver magia",
    "Great Explosion": "Grande explosão",
    "Full Recovery": "Cura total", "Revenge": "Vingança",
    "Normal Mode": "Modo normal", "Safe Mode": "Modo seguro",
    "Dormancy": "Dormência", "Revival": "Ressurreição",
    "Warcry": "Grito de guerra",
    "Hell Breath": "Sopro infernal",
    "Cursed Breath": "Sopro amaldiçoado",
    "Mist Breath": "Sopro de névoa",
    "Shockwave": "Onda de choque",
    "Poison Shot": "Tiro venenoso",
    "Tomato Attack": "Ataque de tomate",
    "Vacuum Wave": "Onda de vácuo",
    "Palm Punch": "Golpe de palma",
    "Roundhouse Kick": "Chute giratório",
    "Deep Freeze": "Congelamento profundo",
    "Thunder Shower": "Chuva de raios",
    "Double Impact": "Impacto duplo",
    "Rock Cannon": "Canhão de pedra",
    "Pulse Laser": "Laser pulsante",
    "Double Beam": "Raio duplo",
    "High Voltage": "Alta tensão",
    "Break Spin": "Giro rompedor",
    "Needle Rain": "Chuva de agulhas",
    "Cross Cut": "Corte cruzado",
    "Flame Spray": "Jato de chamas",
    "Harm Wave": "Onda nociva",
    "Photon Spread": "Dispersão de fótons",
    "Gravity Punishment": "Punição gravitacional",
    "Meteor Burst": "Explosão meteórica",
    "Falling Sky": "Céu em queda",
    "System Break": "Falha do sistema",
    "Limit Release": "Liberar limite",
    # Item catalog: keep product names like Funbun, Kitty Candy and Dokkoi.
    "Greater heal for whole party": "Cura maior para todo o grupo",
    "HP Recovery Party 2": "Cura HP do grupo 2",
    "Tranquilizer": "Tranquilizante",
    "Recover status effect": "Remove alterações de estado",
    "Recover ": "Cura ", "Missile": "Míssil",
    "No enemy appearances": "Evita encontros com inimigos",
    "Many enemy appearances": "Mais encontros com inimigos",
    "Boost singing speed ": "Acelera o canto ",
    "Small MP recovery ": "Recupera um pouco de MP ",
    "Recover spiritual powers": "Recupera poder espiritual",
    "Reduce single enemy’s agility": "Reduz a agilidade de um inimigo",
    "Agility down": "Reduz agilidade", "Sleep": "Sono",
    "Poison and Paralysis": "Veneno e paralisia",
    "Stops enemy RT magic": "Bloqueia a magia RT inimiga",
    "Instant kill": "Morte instantânea",
    "Super restoration of RT’s MP": "Restaura muito MP da RT",
    "MP Full Recovery": "Recupera todo o MP",
    "Enter Harmonics": "Entra em Harmonia",
    "Trading Card, Number 1": "Carta colecionável nº 1",
    "Trading Card, Number 2": "Carta colecionável nº 2",
    "Trading Card, Number 3": "Carta colecionável nº 3",
    "Trading Card, Number 4": "Carta colecionável nº 4",
    "Trading Card, Number 5": "Carta colecionável nº 5",
    "Trading Card, Number 6": "Carta colecionável nº 6",
    "Trading Card, Number 7": "Carta colecionável nº 7",
    "Bastard Sword": "Espada bastarda", "Handgun": "Pistola",
    "Additional Fire Damage": "Dano de fogo adicional",
    "Chainsaw": "Motosserra", "Halberd": "Alabarda",
    "Additional Wind Damage": "Dano de vento adicional",
    "Additional Lightning Damage": "Dano elétrico adicional",
    "Additional Fire & Ice Damage": "Dano extra de fogo e gelo",
    "Element Spear": "Lança elemental",
    "Flavored Ice": "Gelo saborizado", "Shaved Ice": "Raspadinha",
    "Dried Fish": "Peixe seco", "Freeze Dry": "Liofilizado",
    "Natural Ice": "Gelo natural", "Supernatural Ice": "Gelo sobrenatural",
    "BBQ Soda": "Refrigerante BBQ", "Bunny Rice": "Arroz de coelho",
    "Mecha Bunny": "Coelho mecânico", "Food Juice": "Suco de comida",
}

# Fixed executable slots often have exactly as many bytes as the English label.
# These deliberate short forms are used only if the full PT-BR term does not fit.
COMPACT = {
    "ON": "LIG", "Time Played": "Tempo", "Armor": "Armad", "Accessory": "Acess.",
    "F Attack": "Atq.F", "I Attack": "Atq.G", "L Attack": "Atq.R",
    "W Attack": "Atq.V", "F Resist": "Res.F", "I Resist": "Res.G",
    "L Resist": "Res.R", "W Resist": "Res.V", "Agility": "Agilid.",
    "Age:": "Id.:", "Male": "Masc", "Likes:": "Gosta:",
    "Dislikes:": "Detesta:", "Total Magic": "Magia total",
    "Quality": "Qualid.", "Category": "Classe",
    "Equip [Accessory]": "Equip. [Acess.]", "Memo": "Nota",
    "Recipe": "Rec.", "Use Effect": "Efeito uso",
    "Enhancements": "Melhorias", "Equipable Characters ": "Quem pode equipar ",
    "Change Parameter": "Mudar atributo", "Spawn Point": "Origem",
    "Job": "At.", "Likes": "Gosta", "Dislikes": "Detesta",
    "Hobbies": "Hobby", "Amount Made": "Qtde. feita",
    "Old Item": "Item ant", "Selling Price": "Preço venda",
    "Combined Item": "Item criado", "Number": "Núm.",
    "Total Price": "Total", "Own": "Tem", "Stock": "Qtde.",
    "Required DP": "DP exigido", "Enter": "Entr.",
    "Return to Reality": "Voltar ao real", "Play Time": "Tempo",
    "Lazy": "Lenta", "Burst Chart ": "Gráf. Burst ",
    "Required MP": "MP exigido", "Magics Acquired": "Magias obtidas",
    "Past Conversations ": "Conversas passadas ", "Required HP": "HP exigido",
    "Pom Tackle": "Ataque Pom", "Pom Blast": "Bomba Pom",
    "Jumping Thorn": "Espinho ágil", "Chaotic Triple": "Triplo caos",
    "Fusion Beam": "Raio fusão", "Flower Shot": "Tiro floral",
    "Acid Rain": "Chuva ácid.", "Mouthful": "Bocada",
    "Sleepy Gas": "Gás sono", "Poisony Gas": "Gás tóxico",
    "Collapsing Gas": "Gás fraco",
    "Healing Pollen": "Pólen cura",
    "Sleepy Bite": "Mord. sono", "Poisonous Bite": "Mord. tóxica",
    "Paralyzing Bite": "Mord. paral.", "Super Bite": "Mord. forte",
    "Cut": "Crt", "Spirit": "Alma", "Fillet": "Cortar",
    "Godspeed": "Ágil", "Lightning Slash": "Golpe raio",
    "Gale Slash": "Golpe vento", "Burning Slash": "Golpe fogo",
    "Fast Shot": "Tiro ágil", "Full Auto": "Automático",
    "Sleep Shot": "Tiro sono", "Stun Shot": "Tiro atord.",
    "Temple Strike": "Golpe têmpora", "Verse of Curse": "Verso maldito",
    "Soul Drain": "Dreno alma", "Shadow Attack": "Ataque sombra",
    "Summon Hellfire": "Chamar inferno", "Summon Tornado": "Chamar tornado",
    "Ice Beam": "Raio gelo", "Electromagnetic Laser": "Laser elétrico",
    "Mystery Ray": "Raio oculto", "Alarm": "Alerta",
    "Bit Attack": "Ataque bit", "All Range": "Toda área",
    "Screw Dive": "Giro fundo", "Fire Shield": "Escudo fogo",
    "Ice Shield": "Escudo gelo", "Electric Shield": "Escudo raio",
    "Wind Shield": "Esc. vento", "Full Barrier": "Barreira",
    "Dive Attack": "Mergulho", "Homing Shot": "Tiro guiado",
    "Enemy Explosion": "Expl. inimiga", "Energy Drain": "Dreno energia",
    "Assault Storm": "Temp. de ataque", "Steep Descent": "Descida brusca",
    "Fire Breath": "Sopro fogo", "Poison Mist": "Névoa tóx.",
    "Call Lightning": "Invocar raio", "Tiny Fire": "Chama menor",
    "Tiny Ice": "Gelo menor", "Induced Explosion": "Explosão induz.",
}


def apply_catalog_localization(db: sqlite3.Connection) -> Counter:
    """Fill safe exact matches, preserving all existing automatic/reviewed work."""
    result: Counter = Counter()
    rows = db.execute(
        "SELECT id,original,original_bytes FROM dialogues "
        "WHERE translation_track='localization' AND locked=0 "
        "AND automatic='' AND translation='' AND reviewed=''"
    ).fetchall()
    for row in rows:
        target = short_catalog_term(row["original"])
        if target is None:
            target = TERMS.get(row["original"])
        if target is None:
            result["unmapped"] += 1
            continue
        if target == row["original"]:
            result["retained_term"] += 1
        size = len(encode_game_text(target))
        if size > row["original_bytes"]:
            compact = COMPACT.get(row["original"], "")
            compact_size = len(encode_game_text(compact)) if compact else 0
            if compact and compact_size <= row["original_bytes"]:
                target, size = compact, compact_size
            else:
                db.execute(
                    "UPDATE dialogues SET automatic=?,translation=?,translated_bytes=?,"
                    "size_ok=0,provider='curadoria_local',error='' WHERE id=?",
                    (target, target, size, row["id"]),
                )
                result["over_capacity_saved"] += 1
                continue
        db.execute(
            "UPDATE dialogues SET automatic=?,translation=?,translated_bytes=?,"
            "size_ok=1,provider='curadoria_local',error='' WHERE id=?",
            (target, target, size, row["id"]),
        )
        result["localized"] += 1

    # Short locked identifiers are structural/model labels, not untranslated
    # prose. Record the intentional retention so the editor does not present
    # them as forgotten entries; `locked=1` still prevents reinsertion.
    protected = db.execute(
        "SELECT id,original,original_bytes FROM dialogues "
        "WHERE translation_track='localization' AND locked=1 "
        "AND automatic='' AND translation='' AND reviewed=''"
    ).fetchall()
    for row in protected:
        if len(row["original"].split()) > 3:
            continue
        size = len(encode_game_text(row["original"]))
        db.execute(
            "UPDATE dialogues SET automatic=?,translation=?,translated_bytes=?,"
            "size_ok=1,provider='identificador_tecnico',error='' WHERE id=?",
            (row["original"], row["original"], size, row["id"]),
        )
        result["protected_identifier"] += 1
    db.commit()
    return result
