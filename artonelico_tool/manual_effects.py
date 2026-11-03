"""Editorially authored exact effect templates, not a translation service."""
import re

def effect_translation(source):
    match=re.fullmatch(r'\[(Red Magic|Blue Magic|Green Magic|Equipment)\](CR| )(.+)',source.strip())
    if not match: return None
    kind,separator,body=match.groups()
    category={'Red Magic':'Magia vermelha','Blue Magic':'Magia azul','Green Magic':'Magia verde','Equipment':'Equipamento'}[kind]
    # Preserve the original literal CR separator rather than adding new commands.
    prefix=f'[{category}]'+separator
    exact={
        'Additional fire damage equal to base damage.':'Dano extra de fogo igual ao dano base.',
        'Additional ice damage equal to base damage.':'Dano extra de gelo igual ao dano base.',
        'Additional lightning damage equal to base damage.':'Dano extra de raio igual ao dano base.',
        'Additional wind damage equal to base damage.':'Dano extra de vento igual ao dano base.',
        '100% critical rate.':'Chance de crítico de 100%.',
        'Increases attack power by a lot.':'Aumenta muito o ataque.',
        'Decreases physical damage taken.':'Reduz o dano físico recebido.',
        'Decreases magical damage taken.':'Reduz o dano mágico recebido.',
        'Adds HP auto regeneration to equipment.':'Adiciona regeneração automática de HP.',
        'Raises abilities past the limit. Lowers GD resistance.':'Eleva os atributos além do limite, mas reduz a resistência GD.',
        'BS and Influence increased. GD resistance decreased.':'Aumenta BS e Influência, mas reduz a resistência GD.',
        'GD resistance maxed. BS and Influence decreased.':'Maximiza resistência GD, mas reduz BS e Influência.',
        'Brings out the potential abilities of the equipper.':'Libera o potencial de quem equipa.',
        'Status improvement plus increase to all resistances.':'Melhora atributos e todas as resistências.',
        'Status increase plus strong additional damage.':'Melhora atributos e adiciona dano extra forte.',
        'Huge status increase plus strong additional damage.':'Melhora muito os atributos e adiciona dano extra forte.',
        '5 extra attacks plus an increase in speed.':'Adiciona 5 ataques e aumenta a velocidade.',
        'Crazed by anger, attack power goes up, defense goes down.':'A fúria aumenta o ataque, mas reduz a defesa.',
        'Mainly strengthens all attack power and defense.':'Melhora sobretudo o ataque e a defesa.',
        'Improves mainly MP and defense.':'Melhora sobretudo o MP e a defesa.',
        'Strengthens the equipper’s defense all around.':'Melhora toda a defesa de quem equipa.',
        'HP, MP, GD resistances increased.':'Aumenta HP, MP e resistência GD.',
        'Attack power and critical value increases.':'Aumenta ataque e valor de crítico.',
        'All additional damage and defense increases.':'Aumenta todo dano extra e a defesa.',
        'HP and defense increases but agility decreases.':'Aumenta HP e defesa, mas reduz a agilidade.',
        'Quality and rarity is extremely high, but no effects.':'Qualidade e raridade altíssimas, mas sem efeitos.',
        'A [shadow] crystal. Affects attack speed and agility.':'Cristal [sombra]. Afeta velocidade de ataque e agilidade.',
        'A [galaxy] crystal. Strengthens the body’s talents.':'Cristal [galáxia]. Fortalece as capacidades físicas.',
        'A [universe] crystal. Strengthens spiritual power.':'Cristal [universo]. Fortalece o poder espiritual.',
        'A [defense] crystal. Raises defense abilties.':'Cristal [defesa]. Melhora a capacidade defensiva.',
        'A [life] crystal. Has strong regenerative abilities.':'Cristal [vida]. Tem forte poder regenerativo.',
        'A [reflect] crystal. Deflects magic damage.':'Cristal [reflexo]. Desvia dano mágico.',
        'A [shock] crystal. Huge increase in attack power.':'Cristal [choque]. Aumenta muito o ataque.',
        'An [EM] crystal. Stronger to lightning, adds paralysis.':'Cristal [EM]. Resiste a raios e adiciona paralisia.',
        'A [mystery] crystal. Increases attack power and defense.':'Cristal [mistério]. Aumenta ataque e defesa.',
        'A [dragon] crystal. Increase in attack power, add curse effect.':'Cristal [dragão]. Aumenta ataque e adiciona maldição.',
        'A [sprit] crystal. Huge increase in talents.':'Cristal [espírito]. Melhora muito as capacidades.',
        'A [harm] crystal. Increases talents with risks.':'Cristal [dano]. Melhora capacidades, mas traz riscos.',
        'A [god] crystal. Extreme increases with high risk.':'Cristal [deus]. Melhora extrema com alto risco.',
        'A phantasmal grathnode crystal from the far east.':'Cristal Grathnode fantasmagórico do extremo oriente.',
        'A crystal with the power of the four elemental spirits.':'Cristal com o poder dos quatro espíritos elementais.',
        'Completely voids certain attacks.':'Anula completamente certos ataques.',
        'Applies super acceleration effects.':'Aplica o efeito de superaceleração.',
        '100% of magic damage done returns to party.':'Devolve ao grupo 100% do dano mágico causado.',
        'Drastically increases attack abilities.':'Aumenta drasticamente as capacidades de ataque.',
        'Drastically increases Reyvateils’ abilities.':'Aumenta drasticamente as capacidades das Reyvateils.',
        'Ultimate increase in ablities of equipment.':'Melhoria suprema dos atributos do equipamento.',
        'Attack power decreased, super increase to multi hits.':'Reduz ataque e aumenta muito os golpes múltiplos.',
        'Extremely strengthens the effects of Blue Magic.':'Fortalece muito os efeitos da magia azul.',
    }
    if body in exact: return prefix+exact[body]
    rules=[
      (r'(\d+)% increase in effectiveness of Red Magic\.',r'Aumenta em \1% a potência da magia vermelha.'),
      (r'(\d+)% increase in effects by Blue Magic\.',r'Aumenta em \1% os efeitos da magia azul.'),
      (r'(\d+)% increase in equipment stats\.',r'Aumenta em \1% os atributos do equipamento.'),
      (r'(\d+)% increase to damage against opponent\.',r'Aumenta em \1% o dano contra o inimigo.'),
      (r'Temporarily increases max HP by (\d+)%\.',r'Aumenta temporariamente o HP máximo em \1%.'),
      (r'Waiting time after action shortened by (\d+)%\.',r'Reduz em \1% a espera após agir.'),
      (r'Attack power (\d+)% up, defense (\d+)% down\.',r'Ataque +\1%, defesa -\2%.'),
      (r'(\d+)% increase in Ambience Field rising rate\.',r'Aumenta em \1% a velocidade de crescimento do Campo Ambiente.'),
      (r'Adds (\d+) hit to normal attack\.',r'Adiciona \1 golpe(s) ao ataque normal.'),
      (r'(\d+) extra attacks? (?:is|are) added\.',r'Adiciona \1 ataque(s) extra(s).'),
      (r'(HP|MP) increased by (\d+)\.',r'\1 +\2.'),
      (r'In QV action, shooting is (\d+)x as effective\.',r'Na ação QV, os disparos são \1 vezes mais eficazes.'),
    ]
    for pattern,target in rules:
        if re.fullmatch(pattern,body): return prefix+re.sub(pattern,target,body)
    elements={'fire':'fogo','ice':'gelo','lightning':'raio','wind':'vento'}
    statuses={'Poison':'veneno','Sleep':'sono','Paralysis':'paralisia','Curse':'maldição','Blind':'cegueira'}
    if body.startswith('No effect to status abnormality: '):
        status=body.split(': ',1)[1].rstrip('.')
        if status in statuses: return prefix+'Imunidade a '+statuses[status]+'.'
    m=re.fullmatch(r'(Slight|Moderate|High) chance to (?:make an opponent fall asleep|poison the opponent|paralyze the opponent|curse the opponent|blind the opponent)\.',body)
    if m:
        chance={'Slight':'Baixa','Moderate':'Média','High':'Alta'}[m[1]]
        action=next(v for k,v in [('fall asleep','causar sono'),('poison','envenenar'),('paralyze','paralisar'),('curse','amaldiçoar'),('blind','cegar')] if k in body)
        return prefix+chance+' chance de '+action+' o inimigo.'
    m=re.fullmatch(r'(Slight|High) chance to apply (poison|sleep|paralysis|curse|blind) effects to opponent\.',body)
    if m: return prefix+{'Slight':'Baixa','High':'Alta'}[m[1]]+' chance de causar '+statuses[m[2].capitalize()]+' no inimigo.'
    m=re.fullmatch(r'(?:Base damage x(\d+)% (?:additional )?(fire|ice|lightning|wind)(?: damage| in lightning damage)|(?:(\d+)% of base damage as (?:additional )?(fire|ice|lightning|wind) damage))\.',body)
    if m: return prefix+f'Adiciona {m[1] or m[3]}% do dano base como dano de {elements[m[2] or m[4]]}.'
    m=re.fullmatch(r'Base damage x(\d+)% in lightning damage\.',body)
    if m: return prefix+f'Adiciona {m[1]}% do dano base como dano de raio.'
    m=re.fullmatch(r'(\d+)% of damage done returns as your MP\.',body)
    if m: return prefix+f'Recupera seu MP em {m[1]}% do dano causado.'
    m=re.fullmatch(r'(\d+)% of damage done returns as party HP\.',body)
    if m: return prefix+f'Recupera o HP do grupo em {m[1]}% do dano causado.'
    m=re.fullmatch(r'Decrease (physical|magical) damage received by (\d+)%\.',body)
    if m: return prefix+f'Reduz em {m[2]}% o dano '+{'physical':'físico','magical':'mágico'}[m[1]]+' recebido.'
    intensities={'Slightly':'levemente','Mildly':'um pouco','Moderately':'moderadamente','Greatly':'muito','Drastically':'drasticamente',
                 'Slight':'Leve','Mild':'Pequeno','Moderate':'Moderado','Great':'Grande','Drastic':'Drástico','Huge':'Enorme','Super':'Extremo','Extreme':'Extremo','Extremely':'extremamente','Amply':'bastante'}
    adv='|'.join(intensities)
    m=re.fullmatch(rf'({adv}) delay the opponent’s turn\.',body)
    if m: return prefix+f'Atrasa {intensities[m[1]]} o turno inimigo.'
    m=re.fullmatch(rf'({adv}) slows down the opponent’s speed\.',body)
    if m: return prefix+f'Reduz {intensities[m[1]]} a velocidade inimiga.'
    m=re.fullmatch(rf'({adv}) (lowers|increases) (.+)\.',body)
    if m:
        obj={"opponent’s attack power":"o ataque inimigo","opponent’s defense":"a defesa inimiga",'all resistances':'todas as resistências',
             'MP usage when using red magic':'o consumo de MP da magia vermelha','MP usage when using blue magic':'o consumo de MP da magia azul',
             'physical damage received':'o dano físico recebido','magical damage received':'o dano mágico recebido','attack power':'o ataque','defense':'a defesa','agility':'a agilidade',
             'GD resistance':'a resistência GD','the value of the Harmonics Gauge':'o valor do medidor Harmonics'}
        if m[3] in obj: return prefix+('Reduz' if m[2]=='lowers' else 'Aumenta')+' '+intensities[m[1]]+' '+obj[m[3]]+'.'
    m=re.fullmatch(rf'({adv}) lower (fire|wind|ice|lightning) resistance\.',body)
    if m: return prefix+f'Reduz {intensities[m[1]]} a resistência a {elements[m[2]]}.'
    m=re.fullmatch(rf'({adv}) increase (?:in|to) (.+)\.',body)
    if m:
        obj={'critical rate':'chance de crítico','attack power':'ataque','defense':'defesa','agility':'agilidade','HP, attack power, and defense':'HP, ataque e defesa','Harmonics Gauge':'medidor Harmonics'}
        if m[2] in obj: return prefix+intensities[m[1]]+' aumento de '+obj[m[2]]+'.'
    m=re.fullmatch(rf'({adv}) higher critical chance\.',body)
    if m: return prefix+'Aumenta '+intensities[m[1]].lower()+' a chance de crítico.'
    m=re.fullmatch(rf'({adv}) damage dealt to opponent\.',body)
    if m: return prefix+'Causa dano '+{'Slight':'leve','Mild':'baixo','Moderate':'moderado','Great':'alto','Extreme':'extremo'}[m[1]]+' ao inimigo.'
    m=re.fullmatch(rf'Adds a ({adv.lower()}) HP auto regeneration\.',body)
    if m: return prefix+'Adiciona regeneração automática de HP '+{'slight':'leve','mild':'baixa','moderate':'moderada','huge':'enorme','super':'extrema'}[m[1]]+'.'
    m=re.fullmatch(rf'({adv}) strengthens the equipper\.',body)
    if m: return prefix+'Fortalece '+intensities[m[1]]+' quem equipa.'
    m=re.fullmatch(rf'In QV action, ({adv.lower()}) quickens shooting speed\.',body)
    if m: return prefix+'Na ação QV, aumenta '+intensities[m[1].capitalize()]+' a velocidade dos disparos.'
    m=re.fullmatch(r'(Increase|Great increase|Super increase) in (fire|ice|lightning|wind|all) (?:resistance|resist|resistances) and (?:additional )?damage\.',body)
    if m:
        element='todos os elementos' if m[2]=='all' else elements[m[2]]
        degree={'Increase':'Aumenta','Great increase':'Aumenta muito','Super increase':'Aumenta enormemente'}[m[1]]
        return prefix+degree+' a resistência e o dano extra de '+element+'.'
    conversions={'Max HP slightly converted to MP.':'Converte uma pequena parte do HP máximo em MP.','Max HP moderately converted to MP.':'Converte parte moderada do HP máximo em MP.','Max HP mostly converted to MP.':'Converte a maior parte do HP máximo em MP.','Max HP converted to MP.':'Converte o HP máximo em MP.'}
    if body in conversions: return prefix+conversions[body]
    return None
