import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

tests = [
    # 32231 (cap 168): É sério?! Então é a vitória da uniãoCRdo Grathmeld com a tecnologia da Primeira Era! (+7B)
    (32231, "É sério?! Vitória da uniãoCRdo Grathmeld com a tecnologia da 1ª Era!", 168),
    (32231, "É sério?! É a vitória do GrathmeldCRunido à tecnologia da Primeira Era!", 168),
    (32231, "Viu?! É a vitória da união do GrathmeldCRcom a tecnologia da Primeira Era!", 168),

    # 32233 (cap 216): Mas espere, não é hora de elogios!CRDesmonte e descarte isso já! Pode engatilharCRa destruição total da Terceira Era! (+22B)
    (32233, "Não é hora de elogios! Desmonte e livre-seCRdisso já! Pode engatilhar a destruiçãoCRcompleta da Terceira Era!", 216),
    (32233, "Não é hora de elogios! Desmonte isso já!CRPode engatilhar a ruína totalCRda Terceira Era!", 216),

    # 32234 (cap 96): Que exagero! Eu contiveCRa potência dela direitinho... (+14B)
    (32234, "Não exagere! Eu contiveCRa potência dela...", 96),
    (32234, "Calma! Eu limiteiCRa potência dela...", 96),
    (32234, "Que exagero! Eu limiteiCRo poder dela...", 96),

    # 32236 (cap 104): Claro! O alcance é de no máximoCRuns dois stons de raio. (+11B)
    (32236, "Claro! O alcance é sóCRde uns dois stons de raio.", 104),
    (32236, "Claro! Pega no máximoCRuns dois stons de raio.", 104),

    # 32240 (cap 80): ...Esse formato miudinhoCRaté que é bonitinho... (+19B)
    (32240, "...Ela pequenina assimCRaté que é bonitinha...", 80),
    (32240, "...Tão pequenina assimCRaté que é bonitinha...", 80),
    (32240, "...Esse tamaninhoCRé até bonitinho...", 80),

    # 32244 (cap 56): Ai... Também achou isso, né... (+7B)
    (32244, "Ai... Também achou, né...", 56),
    (32244, "Também achou isso, né...", 56),
    (32244, "Também achou, é...?", 56),

    # 32245 (cap 96): M-mas acho que combinaCRmuito bem com você, Lyner! (+6B)
    (32245, "M-mas acho que combinaCRmuito com você, Lyner!", 96),
    (32245, "M-mas acho que fica bemCRem você, Lyner!", 96),

    # 32250 (cap 104): Nem eu imaginava que chamariamCRminha lança de galho seco... (+18B)
    (32250, "Nem imaginei que chamariamCRminha lança de galho seco...", 104),
    (32250, "Nunca pensei que chamariamCRela de galho seco...", 104),
    (32250, "Nem pensei que chamariamCRminha lança de galho seco...", 104),

    # 32258 (cap 112): ...Dá calafrios imaginarCRalguém sendo retalhado por ela. (+5B)
    (32258, "...Dá calafrios imaginarCRalguém cortado por ela.", 112),
    (32258, "...Dá medo imaginar alguémCRsendo retalhado por ela.", 112),

    # 32276 (cap 56): Essa lança parece um machado. (+4B)
    (32276, "Essa lança parece machado.", 56),
    (32276, "A lança parece um machado.", 56),
    (32276, "Parece até um machado.", 56),

    # 32297 (cap 136): Mais ainda: dá pra falar mal delaCRo quanto quisermos sem ela notar. (+2B)
    (32297, "Dá pra falar mal delaCRo quanto quisermos sem ela notar.", 136),
    (32297, "Dá pra falar mal delaCRà vontade sem ela nem notar.", 136),

    # 32299 (cap 96): ...N-não, nenhum!CREra só um exemplo... Um exemplo! (+9B)
    (32299, "...N-não, nenhum!CREra só um exemplo... Só isso!", 96),
    (32299, "...N-não, nada!CREra só um exemplo... Um exemplo!", 96),
    (32299, "...N-não! Foi só umCRexemplo... Um exemplo!", 96),

    # 32300 (cap 112): Enfim! Da próxima, fabriqueCRalgo silencioso e poderoso. (+2B)
    (32300, "Enfim! Da próxima vez, façaCRalgo quieto e poderoso.", 112),
    (32300, "Enfim! Da próxima vez, crieCRalgo silencioso e forte.", 112),
    (32300, "Enfim! Da próxima, façaCRalgo silencioso e potente.", 112),
]

for d_id, s, cap in tests:
    sz = encoded_size(s)
    diff = sz - cap
    status = "OK" if diff <= 0 else f"+{diff}B"
    print(f"ID {d_id} ({sz}B / {cap}B -> {status}): {s}")
