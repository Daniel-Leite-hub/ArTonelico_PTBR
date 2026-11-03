import sys
from pathlib import Path

BASE_DIR = Path(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
from artonelico_tool.project import encoded_size

# Teste das falas dramáticas e cômicas de Don Leon (IDs 24489 a 24649)
candidates = [
    # 24489 (lim 112B)
    ("24489", 112, "Parece que não tem nada aqui.CRVou procurar noutro canto..."),
    ("24489", 112, "Não tem nada por aqui.CRMelhor procurar noutro lugar..."),
    # 24490 (lim 104B)
    ("24490", 104, "A Aurica não está aqui.CRVai embora ou o quê?"),
    ("24490", 104, "Aurica não está por aqui.CRJá vai embora?"),
    # 24491 (lim 168B)
    ("24491", 168, "Não é isso...CRMas que ruínas são essas?CRFiquei curioso desde que cheguei."),
    # 24492 (lim 192B)
    ("24492", 192, "Isto é o Stonehenge!CRUm local sagrado vital para oCRamadurecimento da senhorita Aurica!"),
    ("24492", 192, "Isto é o Stonehenge!CRUm local vital para o crescimentoCRda senhorita Aurica!"),
    # 24493 (lim 24B)
    ("24493", 24, "É-é mesmo...?"),
    ("24493", 24, "É-é mesmo?"),
    ("24493", 24, "S-sério...?"),
    # 24494 (lim 184B)
    ("24494", 184, "Com certeza!CRQuando ela ascender deste mundo,CRusará a força deste Stonehenge!"),
    # 24495 (lim 232B)
    ("24495", 232, "Bem, você entenderá a seu tempo.CRSe for capaz de apoiar Aurica e provocara Mudança de Paradigma, é claro."),
    ("24495", 232, "Entenderá na hora certa.CRSe for capaz de apoiar Aurica e causaruma Mudança de Paradigma, é claro."),
    # 24496 (lim 112B)
    ("24496", 112, "Não há ninguém aqui.CRMelhor procurar noutro lugar."),
    ("24496", 112, "Não tem ninguém aqui.CRMelhor tentar noutro lugar."),
    # 24497 (lim 48B)
    ("24497", 48, "Entendi...CREi, Don Leon."),
    # 24500 (lim 144B)
    ("24500", 144, "Que pergunta a essa altura!CRJá disse que sou o Guardião da MenteCRda senhorita Aurica!"),
    # 24501 (lim 200B)
    ("24501", 200, "Não foi isso que eu quis dizer...CRÉ que você não parece um ser vivo comum."),
    # 24502 (lim 24B) -> JP: ...ガーン!! (Zero rubricas!)
    ("24502", 24, "...Choque!!"),
    ("24502", 24, "...Quêêê?!"),
    ("24502", 24, "...Gaaan!!"),
    ("24502", 24, "...Golpe baixo!"),
    # 24503 (lim 232B)
    ("24503", 232, "Ah, te magoei? Desculpe, não era isso.CRÉ que você parece um bicho de pelúcia,uma boneca, sei lá..."),
    ("24503", 232, "Opa, ofendi? Desculpe, não quis dizerisso. É que você parece um bicho depelúcia ou um boneco..."),
    # 24504 (lim 168B)
    ("24504", 168, "...Hmph. Sou mesmo de pelúcia!CRUm bichinho que a senhorita AuricaCRsempre cuidou com muito carinho."),
    ("24504", 168, "...Hmph. Sou de pelúcia, sim!CRUm bicho que a senhorita AuricaCRsempre guardou com todo carinho."),
    # 24505 (lim 136B)
    ("24505", 136, "E-então era verdade?!CRMas como um boneco de pelúcia viraGuardião da Mente...?"),
    ("24505", 136, "E-era verdade?!CRMas por que uma pelúcia viraria oGuardião da Mente...?"),
    # 24506 (lim 160B)
    ("24506", 160, "Descubra sozinho, seu tolo!CRSó digo uma coisa: sou a criatura maisimportante para a senhorita Aurica!"),
    # 24507 (lim 64B)
    ("24507", 64, "Muito mais do que você, insolente!"),
    ("24507", 64, "Pelo menos muito mais que você!"),
    # 24509 (lim 104B)
    ("24509", 104, "A propósito... há quanto tempo você é oGuardião da Mente dela?"),
    ("24509", 104, "Pensando bem... há quanto tempo você éo Guardião da Mente dela?"),
    # 24512 (lim 184B)
    ("24512", 184, "Por aí... Espere!CRComo você sabe tanto sobre ela?!CRPor acaso virou um perseguidor?!"),
    ("24512", 184, "Por aí... Espere, insolente!CRComo sabe tanto sobre ela?!CRPor acaso virou um stalker?!"),
    # 24515 (lim 96B)
    ("24515", 96, "Desde então, sou seu Guardião da Mente."),
    ("24515", 96, "Desde então, tenho sido seu Guardião."),
    # 24516 (lim 240B)
    ("24516", 240, "Nossa. Virar Guardião logo de cara é impressionante. Para se tornar um, precisa de um vínculo afetivo enorme, não é?"),
    ("24516", 240, "Puxa. Virar Guardião logo de cara é incrível. Para se tornar um, precisa de um carinho muito profundo, né?"),
    # 24518 (lim 128B)
    ("24518", 128, "Não direi o motivo!CRSe quiser tanto saber, pergunte a ela!"),
    # 24520 (lim 200B)
    ("24520", 200, "Hã!?CRFicar muito tempo faz mal a ela?CRA Aurica fica cansada ou algo assim...?"),
    # 24523 (lim 144B)
    ("24523", 144, "Mas você mergulha na mente dela comtanta frequência... Por que faz isso?!"),
    # 24525 (lim 104B)
    ("24525", 104, "Estou perguntando por que vocêCRmergulha tanto na mente dela!"),
    # 24527 (lim 184B)
    ("24527", 184, "Quero ficar forte e apoiá-la, paraque ela consiga tecer Canções aindamais poderosas."),
    # 24528 (lim 112B)
    ("24528", 112, "...H-hmph! Não pense que ela vai seapaixonar por você só por isso!"),
    # 24529 (lim 104B)
    ("24529", 104, "Não estou fazendo isso para que elagoste de mim..."),
    # 24530 (lim 80B)
    ("24530", 80, "Tanto faz.CR...Dê o melhor de si, então."),
    # 24532 (lim 64B)
    ("24532", 64, "Hehe, é. É pela Aurica."),
    # 24533 (lim 216B)
    ("24533", 216, "...Mas escute. Não cabe a mim dizer,mas a senhorita Aurica tem feridas nomais profundas que outras Reyvateils."),
    # 24534 (lim 112B)
    ("24534", 112, "Por isso, tecer magias fortes exigetanto esforço, não acha?"),
    # 24535 (lim 176B)
    ("24535", 176, "Acha? Nunca pensei nisso. A Auricajá tece Magias da Canção bem fortes."),
    # 24537 (lim 88B)
    ("24537", 88, "...Diga, você mergulha em outrasReyvateils também?"),
    # 24540 (lim 176B)
    ("24540", 176, "Já disse que não mergulho por segundasintenções. Não acha que desconfia demais?"),
    # 24541 (lim 248B)
    ("24541", 248, "C-claro que não! Sou o Guardião da Mente dela! Se um único inseto ousar invadir, expulso com todas as minhas forças!"),
    # 24542 (lim 152B)
    ("24542", 152, "E-entendi...CRMas acho que você é rígido demais."),
    # 24543 (lim 168B)
    ("24543", 168, "Hmph, não desiste nunca, hein?CRE ainda subiu tanto de nível!"),
    # 24544 (lim 136B)
    ("24544", 136, "Falando assim, parece até que fiz algoruim... É impressão minha?"),
    # 24545 (lim 168B)
    ("24545", 168, "Não importa o quanto se esforce, elanunca se apaixonará por alguém como você!"),
    # 24549 (lim 168B)
    ("24549", 168, "Pois vou lhe contar! O motivo de elanem olhar na sua cara é..."),
    # 24550 (lim 40B) -> JP: オリカさんは面食いなのだ! (Ela só quer homens bonitos/galãs!)
    ("24550", 40, "Ela só gosta de galãs!"),
    ("24550", 40, "Ela é muito exigente!"),
    ("24550", 40, "Ela só quer galãs!"),
    # 24553 (lim 96B) -> JP: ...ガーン!! (Zero rubricas!)
    ("24553", 96, "...Choque!!CRP-por quê?! Não ficou chocado?!"),
    ("24553", 96, "...Quêêê?!CRP-por quê?! Não ficou chocado?!"),
    # 24554 (lim 232B)
    ("24554", 232, "Achei que tivesse feito algo que a magoasse e fiquei preocupado. Que alívio saber que não foi nada disso!"),
    # 24555 (lim 128B)
    ("24555", 128, "...Você não tem graça nenhuma.CRVai acabar perdendo amigos."),
    # 24557 (lim 64B)
    ("24557", 64, "Mas... você não é um sujeito mau."),
    # 24560 (lim 136B)
    ("24560", 136, "Ainda aqui?!CRJá ficou tempo demais! Vá embora logo!"),
    # 24561 (lim 168B)
    ("24561", 168, "Don Leon... pensando bem, você não mudounada desde o nível 1..."),
    # 24562 (lim 152B)
    ("24562", 152, "Já nos conhecemos há tanto tempo...CRNão podia confiar um pouco em mim?"),
    # 24563 (lim 232B)
    ("24563", 232, "Kaaah! Proibido criar laços!CRQuem confiaria em você?!CRConfiar nos outros só traz sofrimento!"),
    # 24564 (lim 224B)
    ("24564", 224, "(O modo de pensar de Aurica reflete no Don Leon... Mas acho que hoje ela está mais branda.)"),
    # 24567 (lim 128B)
    ("24567", 128, "Por que evitar? A Aurica reclamou?CRSe for o caso, eu me afasto..."),
    # 24568 (lim 280B)
    ("24568", 280, "Neste nível, qualquer descuido traz o colapso! E minhas forças já não poderão ajudar!"),
    # 24569 (lim 144B)
    ("24569", 144, "Se isso acontecer, você assume aresponsabilidade pela mente dela?!"),
    # 24570 (lim 256B)
    ("24570", 256, "Sempre assumi. Sei do perigo de uma Cosmosfera em níveis tão altos. Mas ainda quero tecer Canções com ela!"),
    # 24571 (lim 80B)
    ("24571", 80, "...Hmph! Jamais confiaria nisso!"),
    # 24572 (lim 200B)
    ("24572", 200, "Don Leon... quando vai confiar em mim?Sei que seu dever é protegê-la, mas..."),
    # 24573 (lim 152B)
    ("24573", 152, "O que você sabe sobre mim?! O Guardiãodeve proteger a mente a qualquer custo!"),
    # 24574 (lim 136B)
    ("24574", 136, "Jamais permitirei que o passado serepita... jamais!"),
    # 24575 (lim 24B)
    ("24575", 24, "O passado...?!"),
    ("24575", 24, "Passado...?!"),
    # 24576 (lim 184B)
    ("24576", 184, "Não é da sua conta! Por minha fraqueza,o coração dela se encheu de feridas..."),
    # 24577 (lim 256B)
    ("24577", 256, "Se eu fosse mais forte, a aldeia em chamas e a recusa como Donzela Sagrada não teriam deixado tantas marcas!"),
    # 24578 (lim 192B)
    ("24578", 192, "Mas restaram cicatrizes profundas...Nós dois levamos tudo a sério demais."),
    # 24579 (lim 232B)
    ("24579", 232, "Por isso me fechei. Perdoe-me, mas por mais gentil que você seja, uma coisa não anula a outra."),
    # 24582 (lim 104B)
    ("24582", 104, "Você também carrega uma ferida enormeno peito, não é...?"),
    # 24584 (lim 120B)
    ("24584", 120, "Don Leon! Que bom que voltou!CRA Aurica ficou tão feliz."),
    # 24585 (lim 88B)
    ("24585", 88, "Diga-me: por que você me ressuscitou?"),
    # 24586 (lim 224B)
    ("24586", 224, "Tentei expulsá-lo o tempo todo. Sem mim, seria bem mais fácil fazer o que quisesse com ela."),
    # 24587 (lim 168B)
    ("24587", 168, "Não é isso! Se você sumisse, Auricaficaria triste. Essa é a única razão."),
    # 24588 (lim 72B)
    ("24588", 72, "Agradeço pelo gesto. ...Obrigado."),
    # 24591 (lim 112B)
    ("24591", 112, "Não foi por mim. Aurica chegou aquipor seu próprio esforço."),
    # 24595 (lim 184B)
    ("24595", 184, "Eu deveria ser insubstituível para ela,mas você entrou aqui com pés descalços!"),
    ("24595", 184, "Eu devia ser insubstituível para ela,mas você invadiu sem pedir licença!"),
    # 24598 (lim 64B)
    ("24598", 64, "...Então era isso."),
    ("24598", 64, "...Era esse o motivo."),
    # 24600 (lim 176B)
    ("24600", 176, "Tudo bem. Fico feliz por desabafar.Isso prova que você confia em mim, né?"),
    # 24601 (lim 200B)
    ("24601", 200, "Você é único, Don Leon. Nada mudaráo fato de que Aurica estará sempre comvocê."),
    # 24603 (lim 88B)
    ("24603", 88, "Você é um sujeito nobre. Se for você..."),
    # 24604 (lim 144B)
    ("24604", 144, "Posso confiar Aurica aos seus cuidados.Por favor, proteja-a por mim."),
    # 24609 (lim 160B)
    ("24609", 160, "Você de novo? Ficando tanto tempo naCosmosfera, como fica o mundo real?"),
    # 24610 (lim 152B)
    ("24610", 152, "Não vai me dizer que virou um reclusodo Centro de Mergulho?!"),
    # 24613 (lim 240B)
    ("24613", 240, "Foi há muito tempo... Ela se apaixonou por um sujeito, mas tomou um fora tão brutal que não saía do quarto."),
    # 24614 (lim 64B)
    ("24614", 64, "Um fora?! A Aurica?! ...Puxa."),
    # 24615 (lim 240B)
    ("24615", 240, "Era um aventureiro alto e forte. Para ele, Aurica era só diversão passageira. O típico galanteador."),
    # 24616 (lim 216B) -> JP: だから、振られたときは、自殺でもしないかとヒヤヒヤしたよ。 (Quase tirou a própria vida / suicídio!)
    ("24616", 216, "Mas ela o amava de verdade. Quando foirejeitada, temi que tirasse a própriavida de tanto desespero."),
    ("24616", 216, "Mas ela o amava de verdade. Quando foirejeitada, temi que cometesse suicídiode tanto desespero."),
    # 24618 (lim 120B)
    ("24618", 120, "O quê?! Maldito! Se eu estivesse lá,teria quebrado a cara dele!"),
    # 24620 (lim 72B)
    ("24620", 72, "Ora, até que concordamos em algo!"),
    # 24621 (lim 24B)
    ("24621", 24, "Com certeza!"),
    # 24622 (lim 96B)
    ("24622", 96, "Digo... espere! Proibido criar laços!"),
    # 24625 (lim 96B)
    ("24625", 96, "Hã?! Que foi? Mau pressentimento..."),
    # 24626 (lim 112B)
    ("24626", 112, "Sabia que a senhorita Aurica tem tidoinsônia ultimamente?!"),
    # 24627 (lim 32B)
    ("24627", 32, "Hã? É-é sério?"),
    # 24629 (lim 72B)
    ("24629", 72, "C-claro que cuido! Mas por que isso...?"),
    # 24631 (lim 56B)
    ("24631", 56, "V-você sabe?! E o que é?!"),
    # 24632 (lim 192B)
    ("24632", 192, "Desde que viaja com você, quase nuncaconsegue dormir num bom cobertor!"),
    # 24633 (lim 152B)
    ("24633", 152, "É verdade...CRNos acampamentos não temos cobertor..."),
    # 24636 (lim 128B)
    ("24636", 128, "Ela só dorme abraçando o cobertorentre as pernas com força!"),
    # 24638 (lim 16B)
    ("24638", 16, "...Hã?"),
    # 24639 (lim 24B)
    ("24639", 24, "Sério?!"),
    # 24643 (lim 184B)
    ("24643", 184, "O ladrão de magia ter a forma de umgato... que ironia amarga."),
    # 24644 (lim 56B)
    ("24644", 56, "...Hum? Como assim?"),
    # 24645 (lim 176B)
    ("24645", 176, "Nada demais. Como ela ama gatos, acheia coincidência dolorosa."),
    # 24646 (lim 232B)
    ("24646", 232, "Ver o monstro que roubava seu poder naforma de um felino deve ter sidoterrivelmente penoso para ela."),
    # 24647 (lim 192B)
    ("24647", 192, "Ela gostava tanto assim de gatos?CRPensando bem, ela brincava com um naestalagem."),
    # 24649 (lim 40B)
    ("24649", 40, "M, miauês!?"),
    ("24649", 40, "F, fala felina!?"),
    ("24649", 40, "L, língua felina!?"),
]

for tag, lim, txt in candidates:
    sz = encoded_size(txt)
    ok = "OK" if sz <= lim else f"OVERFLOW (+{sz-lim}B)"
    print(f"[{ok:15s}] ID {tag} (lim {lim}B, cur {sz}B) -> '{txt}'")
