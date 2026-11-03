import sys
sys.path.insert(0, r"Ferramentas_Traducao")
from artonelico_tool.project import encoded_size
from tools.curadoria_validate import validate_line

max_map_0284 = {
    26978: 184, 26979: 96, 26980: 152, 26981: 72, 26982: 72, 26983: 104,
    26984: 96, 26985: 120, 26986: 152, 26987: 96, 26988: 104, 26989: 176,
    26990: 128, 26991: 160, 26992: 80, 26993: 88, 26994: 56, 26995: 136,
    26996: 160, 26997: 144, 26998: 96, 26999: 64, 27000: 168, 27001: 184
}

calib_0284 = {
    26978: ("Tinha medo de você não gostar de mim,CRalém de outros motivos que euCRtinha também.", "Misha expressando o medo infantil de rejeição com CRs. (171B <= 184B)"),
    26979: ("Mas andei mudando de ideiaCRultimamente.", "Misha notando a mudança gradual de pensamento com CR. (81B <= 96B)"),
    26980: ("Será que você não me odiariaCRmesmo adulta?... Ou é ilusão minha?", "Misha indagando com vulnerabilidade sobre aceitação com CR. (136B <= 152B)"),
    26981: ("Lyner, o que você acha do Leard?", "Misha perguntando sobre o pai de Lyner com termo canônico. (66B <= 72B)"),
    26982: ("Acho que nada de especial, né?", "Lyner respondendo de forma descontraída sobre o pai. (62B <= 72B)"),
    26983: ("...Bem, é uma resposta bem a sua cara.", "Misha rindo da resposta despojada de Lyner. (78B <= 104B)"),
    26984: ("O Leard me ensinou MagiaCRda Canção no passado.", "Misha relembrando o aprendizado com Leard e termo canônico com CR. (95B <= 96B)"),
    26985: ("Mas eu detestava aquilo...CRNem imagina o quanto sofri...", "Misha lamentando o rigor do aprendizado com CR. (115B <= 120B)"),
    26986: ("Só agora que vi que posso te ajudarCRé que comecei a gostar de verdade.", "Misha revelando que a utilidade para Lyner mudou seu sentimento com CR. (145B <= 152B)"),
    26987: ("Dizer isso pra me ajudarCRme deixa sem jeito.", "Lyner ficando encabulado com a confissão com CR. (91B <= 96B)"),
    26988: ("É verdade! Agora até souCRum pouco grata a ele.", "Misha admitindo uma ponta de gratidão a Leard com CR. (97B <= 104B)"),
    26989: ("Era um treino tão espartano...CRGritava comigo... falava horrores...", "Misha recordando os abusos verbais do treinamento com CRs. (138B <= 176B)"),
    26990: ("Mas aquele treino infernal...CRMinha infância aos pedaços...", "Misha desabafando sobre o sofrimento infantil com CRs. (123B <= 128B)"),
    26991: ("...Mas se é pra te ajudar, Lyner...CRTenho que agradecer... só um tiquinho...", "Misha equilibrando mágoa e carinho por Lyner com CRs. (157B <= 160B)"),
    26992: ("...Devo pedir perdão no lugar dele?", "Lyner se sentindo responsável pelas ações do pai. (72B <= 80B)"),
    26993: ("Misha... por acasoCRvocê tá passando mal?", "Lyner demonstrando cuidado com a saúde de Misha com CR. (85B <= 88B)"),
    26994: ("Tô ótima! Aconteceu algo?", "Misha respondendo com vivacidade e energia. (53B <= 56B)"),
    26995: ("É?... Achei que você tava meio pálidaCRou algo assim...", "Lyner explicando sua preocupação com CR. (114B <= 136B)"),
    26996: ("Sério?! Que vergonha... Odeio que meCRvejam assim, tão abatida.", "Misha ficando constrangida por parecer abatida com CR. (129B <= 160B)"),
    26997: ("Ah, não, deve ser impressão minha.CRNem precisa esquentar a cabeça...", "Lyner tentando tranquilizá-la com CR. (142B <= 144B)"),
    26998: ("...Tomara. Mas agora fiqueiCRcucada com isso...", "Misha remoendo a insegurança estética com CR. (95B <= 96B)"),
    26999: ("Eu sempre sonhei em ser livre.", "Misha declarando seu anseio visceral por liberdade. (61B <= 64B)"),
    27000: ("Quando eu era pequena... digo,CRde idade, não de tamanho, tá bom?", "Misha fazendo trocadilho com sua baixa estatura com CR. (133B <= 168B)"),
    27001: ("Desde aquela época, vivia presaCRa bobagens como fado e destino,CRtodo santo dia.", "Misha criticando o determinismo que a aprisionou com CRs. (164B <= 184B)")
}

all_ok = True
for tid, (txt, rat) in calib_0284.items():
    maxb = max_map_0284[tid]
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
    print("=== 0284 100% PERFEITO ===")
