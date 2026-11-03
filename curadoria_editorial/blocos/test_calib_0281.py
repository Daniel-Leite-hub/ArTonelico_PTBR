import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0281 = {
    26906: 136, 26907: 184, 26908: 120, 26909: 152, 26910: 168, 26911: 184,
    26912: 48, 26913: 104, 26914: 160, 26915: 168, 26916: 104, 26917: 224,
    26918: 96, 26919: 160, 26920: 64, 26921: 200, 26922: 40, 26923: 144,
    26924: 168, 26925: 40, 26926: 56, 26927: 120, 26928: 120, 26929: 112
}

calib_0281 = {
    26906: ("É verdade.CRProtege até a ponta dos dedos.", "Lyner confirmando a couraça envolvente com CR."),
    26907: ("Com isso, não seria mais útilCReu lutar no braço em vez de cantar?", "Misha cogitando combate físico com CR."),
    26908: ("Tipo gritar: 'Lyner, cuidado!'CRe descer a mão no monstro!", "Misha imaginando salvar Lyner no soco com CR."),
    26909: ("Cantar e bater ao mesmo tempoCRnão seria unir o útil ao agradável?", "Misha sugerindo versatilidade guerreira com CR."),
    26910: ("Reyvateil lutadora? Bater cantandoCRparece até coisa de vilão de história.", "Lyner achando bizarra a combinação de canto e porrada com CR."),
    26911: ("E a roupa de Sailor Girl?CRNão adianta dar desculpa, aquilo éCRfetiche seu e pronto!", "Misha acusando Lyner de tara pelo uniforme colegial com quebras CR."),
    26912: ("D-de onde tirou isso?!", "Lyner perplexo com a acusação."),
    26913: ("É um visual feito sob medidaCRpro gosto dos homens!", "Misha expondo o apelo masculino do figurino com CR."),
    26914: ("E você me põe pra cantar assim!CRSó posso concluir isso mesmo.", "Misha reafirmando a suspeita contra Lyner com CR."),
    26915: ("Aquele Quimono Nupcial...CRNão acho uma boa usar em batalha.", "Misha relutante em manchar o traje sagrado com CR."),
    26916: ("Pra uma garota, aquilo éCRmuito especial, sabe...?", "Misha expressando o valor emocional do quimono shiromuku com CR."),
    26917: ("Não que eu não goste!CRÉ que eu queria guardar pra aqueleCRmomento especial... sabe?", "Misha sonhando com o casamento ao lado de Lyner com quebras CR."),
    26918: ("Quer que eu troque de roupa?", "Lyner oferecendo a troca do traje."),
    26919: ("Hã?! B-bom... não é que eu odeie...CRe já que vesti... ai, não sei...", "Misha indecisa e constrangida com quebras CR."),
    26920: ("Deixo você decidir...", "Misha passando a decisão para Lyner."),
    26921: ("Além do medo de altura e de escuro,CRvou acabar desenvolvendo fobia social!", "Misha reclamando de vergonha pública com CR."),
    26922: ("O quê?! Do nada?!", "Lyner assustado com a nova fobia."),
    26923: ("Você me faz lutar só de camisaCRsocial e ainda pergunta por quê?!", "Misha indignada com a roupa reveladora de camisa social com CR."),
    26924: ("Imagina como me sinto com o povoCRme encarando na rua feito maluca!", "Misha expondo a vergonha dos olhares públicos com CR."),
    26925: ("D-desculpa...", "Lyner sem jeito diante da bronca."),
    26926: ("...É algum fetiche seu?", "Misha desconfiada de fetiches voyeuristas."),
    26927: ("Esquece...CREu tô viajando na maionese.", "Misha desconversando com expressão coloquial com CR."),
    26928: ("Sabe a roupa de Elfir?CRAcho que já vi em algum lugar...", "Misha reconhecendo o easter egg de Atelier Elie com CR."),
    26929: ("Acho que vi essa roupaCRnum mangá ou num jogo...", "Misha lembrando a referência da mídia com CR.")
}

all_ok = True
for tid, (txt, rat) in calib_0281.items():
    maxb = max_map_0281[tid]
    sz = encoded_size(txt)
    diff = sz - maxb
    if diff > 0:
        all_ok = False
        print(f"OVERFLOW ID {tid}: {sz}B > {maxb}B (+{diff}) -> {txt}")
    else:
        errs = validate_line(tid, "", txt)
        if errs:
            all_ok = False
            print(f"ERRO VALIDACAO ID {tid}: {errs} -> {txt}")
        else:
            print(f"OK ID {tid}: {sz}B <= {maxb}B")

if all_ok:
    print("=== 0281 100% PERFEITO ===")
