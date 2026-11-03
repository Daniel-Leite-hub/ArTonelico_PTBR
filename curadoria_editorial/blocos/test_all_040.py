import json
import sqlite3
import sys
sys.path.insert(0, r"Ferramentas_Traducao")
sys.path.insert(0, r"Ferramentas_Traducao/tools")
from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

conn = sqlite3.connect(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\release\ArTonelico_PTBR_adaptado_108_20260926.atproj")
c = conn.cursor()
db_sizes = {r[0]: r[1] for r in c.execute("SELECT id, original_bytes FROM dialogues WHERE id BETWEEN 31557 AND 31844").fetchall()}

with open(r"Ferramentas_Traducao/curadoria_editorial/blocos/BLK_SYS_040_input.json", "r", encoding="utf-8") as f:
    input_data = json.load(f)

input_map = {d["id"]: d for d in input_data["dialogues"]}

curated = {}

# =========================================================================
# SLUS/TEXT/0493 (IDs 31557..31580)
# =========================================================================
curated[31557] = {"pt": "Só tinha aquela explicaçãozinha e vocêCRfez mesmo assim? É perigoso!", "notes": "Misha repreende síntese de bomba perigosa."}
curated[31558] = {"pt": "É, eu sei, mas... Parece forte.CRSendo bomba, tá valendo, né?", "notes": "Lyner defensivo com bomba."}
curated[31559] = {"pt": "...Parece perigosa. Quando for usar,CRvou ficar a uns 100 stons de distância.", "notes": "Misha irônica com distância em stons."}
curated[31560] = {"pt": "Deu um trabalhinho, mas tá pronta!", "notes": "Lyner comemora forja."}
curated[31561] = {"pt": "Nossa, tem um design meio redondo.", "notes": "Misha sobre design da espada."}
curated[31562] = {"pt": "Mas essa espada não é só forte. Quando equipada, ela tem o efeito curioso de fazer brotar forças lá de dentro.", "notes": "Lyner explica efeito da espada."}
curated[31563] = {"pt": "A espada é forte e você também fica mais forte, né?", "notes": "Misha resume bônus."}
curated[31564] = {"pt": "Só um pouco. Sem resistência nem nada,CRela é só ataque puro e direto!", "notes": "Lyner sobre atributos puros de ataque."}
curated[31565] = {"pt": "...Ou seja, é só uma espada forte?", "notes": "Misha cética."}
curated[31566] = {"pt": "Não tá errada, é isso mesmo.CRSem rodeios: é uma espada pura e simples.", "notes": "Lyner admite que é espada simples."}
curated[31567] = {"pt": "O que houve com a Pedra VermelhaCRe o Boltapolta usados na receita?", "notes": "Misha pergunta dos ingredientes."}
curated[31568] = {"pt": "Que lança frágil. É tão fininhaCRque parece que vai entortar fácil.CRTudo bem mesmo?", "notes": "Misha sobre espessura da lança."}
curated[31569] = {"pt": "Não julga pela aparência!CRIsso aqui é forte pra caramba.", "notes": "Lyner defende a lança."}
curated[31570] = {"pt": "Não aumenta só o ataque e a defesa,CReleva o vigor na mesma medida!", "notes": "Lyner explica atributos."}
curated[31571] = {"pt": "Nossa, que legal. O que pôs nela?", "notes": "Misha pergunta ingredientes."}
curated[31572] = {"pt": "Pus um Boltapolta e uma Caixa de Kant.", "notes": "Lyner cita Boltapolta e Caixa de Fogo de Kant."}
curated[31573] = {"pt": "Então ao atacar causa dano extraCRde raio e fogo também?", "notes": "Misha deduz raio e fogo."}
curated[31574] = {"pt": "...Não, nada desse tipo de efeito.", "notes": "Lyner desmente quebra cômica."}
curated[31575] = {"pt": "Mas você usou BoltapoltaCRe a Caixa de Kant, né?", "notes": "Misha questiona os ingredientes usados."}
curated[31576] = {"pt": "Pois é, mas não tem nada disso...", "notes": "Lyner se desculpa sem graça."}
curated[31577] = {"pt": "...Que lança bem esquisita.", "notes": "Misha conclui que é bizarra."}
curated[31578] = {"pt": "Beleza, o Vivace tá pronto!", "notes": "Lyner batiza Vivace."}
curated[31579] = {"pt": "O cano dessa arma é grandão, né?", "notes": "Misha repara no cano enorme."}
curated[31580] = {"pt": "É pra disparar com força total!", "notes": "Lyner exalta poder de fogo."}

# =========================================================================
# SLUS/TEXT/0494 (IDs 31581..31604)
# =========================================================================
curated[31581] = {"pt": "Mas só atinge a linha de frenteCRe nada da retaguarda? E sendo arma?", "notes": "Misha critica alcance."}
curated[31582] = {"pt": "...I-isso depende da pontaria de quem atira.", "notes": "Lyner culpa o atirador."}
curated[31583] = {"pt": "Haa... Parece tão potente, mas só fazCRo mesmo que uma espada? Não passaCRde arminha de chumbinho.", "notes": "Misha desdenha da arma chamando de chumbinho."}
curated[31584] = {"pt": "Até eu me surpreendi: Engrenagem Sônica pronta!", "notes": "Lyner forja Engrenagem Sônica."}
curated[31585] = {"pt": "Uau... O visual é assustador!", "notes": "Misha assustada com a engrenagem."}
curated[31586] = {"pt": "Ela gira na velocidade do somCRestraçalhando o adversário,CRentão é claro que mete medo.", "notes": "Lyner explica a serra sônica."}
curated[31587] = {"pt": "...Que nojo. Vamos chamar de \"Engrenagem Grotesca\".", "notes": "Misha sugere Engrenagem Grotesca."}
curated[31588] = {"pt": "Quem vai ouvir as reclamações do usuário sou eu, sabia?", "notes": "Lyner teme bronca do parceiro."}
curated[31589] = {"pt": "Pronto, Suzaku & Seiryuu concluídas!CRPor que katanas sempre vêm aos pares?", "notes": "Lyner estranha katanas em pares."}
curated[31590] = {"pt": "Mas isso já nem parece katana...CRTá mais pra uma versão nefasta de facãoCRdegolador de pescoço.", "notes": "Misha acha facão degolador."}
curated[31591] = {"pt": "E as costas da lâmina parecem um serrote!CRComo é que enfia isso numa bainha?", "notes": "Misha sobre lâmina de serrote."}
curated[31592] = {"pt": "É só enfiar numa bainha grandona. Dá pra carregar por aí, então tá tudo certo.", "notes": "Lyner improvisa bainha grande."}
curated[31593] = {"pt": "Ou seja: não existe bainha no mundoCRque caiba isso de verdade, né?", "notes": "Misha expõe falta de bainha real."}
curated[31594] = {"pt": "É... não posso negar...", "notes": "Lyner admite."}
curated[31595] = {"pt": "Essa espada tá soltandoCRum brilho verde...", "notes": "Misha nota brilho verde da lâmina."}
curated[31596] = {"pt": "Nem eu sei. Só misturei Placa IônicaCRe Parafuso Motorizado à Cierocerâmica.", "notes": "Lyner lista ingredientes da Ion Blade."}
curated[31597] = {"pt": "E mudou pra essa cor?CRSe a espada original era tão preta!", "notes": "Misha surpresa com a cor verde."}
curated[31598] = {"pt": "Grathmeld é cheio de mistérios, ué!CRDeixa estar.", "notes": "Lyner defende mistérios de Grathmeld."}
curated[31599] = {"pt": "Mas se tem Placa Iônica,CRdeve fazer bem pro corpo, não?", "notes": "Misha pergunta se íons fazem bem."}
curated[31600] = {"pt": "Até aumenta o HP, mas não acho que sejaCRsaudável desse jeito não...", "notes": "Lyner esclarece aumento de HP."}
curated[31601] = {"pt": "Decidido: \"Ion Blade\"!", "notes": "Misha batiza Ion Blade."}
curated[31602] = {"pt": "Nem me ouviu, né...", "notes": "Lyner é ignorado."}
curated[31603] = {"pt": "Olha só, até que é estiloso.", "notes": "Misha elogia espada de fogo."}
curated[31604] = {"pt": "Né? Chama \"Inferno\"!", "notes": "Lyner batiza Inferno."}

# =========================================================================
# SLUS/TEXT/0495 (IDs 31605..31628)
# =========================================================================
curated[31605] = {"pt": "Inferno? Não me diz que sai fogo?", "notes": "Misha pergunta se sai fogo da Inferno."}
curated[31606] = {"pt": "Claro que sai!CRMas não é tão forte assim.", "notes": "Lyner modera poder da espada."}
curated[31607] = {"pt": "Ainda assim é demais!CRAs batalhas vão ficar bem mais fáceis.", "notes": "Misha empolgada com a facilidade."}
curated[31608] = {"pt": "...Mas usei Líquido de Ionização de ingrediente.", "notes": "Lyner revela ingrediente inesperado."}
curated[31609] = {"pt": "Hã?", "notes": "Misha confusa com líquido de ionização."}
curated[31610] = {"pt": "Misturei o Líquido de Ionização com engrenagemCRe agora solta fogo! Curioso, né?", "notes": "Lyner explica a alquimia esquisita."}
curated[31611] = {"pt": "Que forçado...CR\"Inferno\" é um nome pomposo demais.", "notes": "Misha acha o nome Inferno forçado."}
curated[31612] = {"pt": "Pronto! Uma arma pesadíssima:CRo Estremo tá na mão!", "notes": "Lyner forja arma pesada Estremo."}
curated[31613] = {"pt": "Uau, que visual imponente!CRO Harm vai adorar!", "notes": "Misha diz que Harm vai amar."}
curated[31614] = {"pt": "Caprichei no visual dela!CRQueria que desse vontade de empunhar na hora.", "notes": "Lyner sobre a atração visual da arma."}
curated[31615] = {"pt": "Como assim?", "notes": "Misha pergunta significado."}
curated[31616] = {"pt": "É que ficou muito mais potente do que pensei.CRGente comum não aguenta disparar isso aqui não.", "notes": "Lyner sobre a potência inacessível a humanos normais."}
curated[31617] = {"pt": "Tão forte assim?", "notes": "Misha pergunta da força."}
curated[31618] = {"pt": "Tipo assim... se você atirasse, Misha,CRo coice deslocaria seu ombro ou, pior,CRpartiria seu osso no meio.", "notes": "Lyner avisa do coice brutal sobre Misha."}
curated[31619] = {"pt": "...S-será que o Harm consegue atirar nisso?", "notes": "Misha teme pelo braço do Harm."}
curated[31620] = {"pt": "O braço dele é mecânico, bem mais firmeCRque o normal. Vai dar certo!", "notes": "Lyner confia no braço mecânico de Jack (Harm)."}
curated[31621] = {"pt": "...E se ela explodir?", "notes": "Misha pergunta de tiro acidental."}
curated[31622] = {"pt": "......Eu tava tentando não pensar nisso.", "notes": "Lyner tenta ignorar o risco de explosão."}
curated[31623] = {"pt": "Motor Eletromagnético pronto!CRE não é só o barulho que impressiona!", "notes": "Lyner forja Motor Eletromagnético."}
curated[31624] = {"pt": "Dá pra ver... Esse vermelho pareceCRque bebeu sangue! Que pavor...", "notes": "Misha assustada com o vermelho sangue do motor."}
curated[31625] = {"pt": "A intenção foi essa! O choque visualCRjá serve pra apavorar o inimigo de cara, né?", "notes": "Lyner planejou o terror psicológico."}
curated[31626] = {"pt": "Até nós ficamos apavorados!", "notes": "Misha diz que os aliados também têm medo."}
curated[31627] = {"pt": "Beleza! Zetsuei & Zanmu concluídas!!CRAs katanas supremas, as mais fortes de todas!!", "notes": "Lyner forja katanas lendárias Zetsuei & Zanmu."}
curated[31628] = {"pt": "Hum, Lyner... Desculpa cortar sua alegria,CRmas tem fumaça saindo delas?", "notes": "Misha nota fumaça sinistra saindo das lâminas."}

# =========================================================================
# SLUS/TEXT/0496 (IDs 31629..31652)
# =========================================================================
curated[31629] = {"pt": "Fumaça não, chama de aura!CREssa aura é o segredo da força delas!", "notes": "Lyner corrige dizendo que é aura de poder."}
curated[31630] = {"pt": "Só espero que essa aura não faça malCRao corpo de quem usa...", "notes": "Lyner teme efeitos colaterais biológicos."}
curated[31631] = {"pt": "Você que fez e fala isso?!", "notes": "Misha indignada com a inconsequência do ferreiro."}
curated[31632] = {"pt": "Só segui a receita. Bem... para um espadachim,CRisso deve ser um fenômeno do cotidiano...CReu acho...", "notes": "Lyner dá desculpa esfarrapada de espadachim."}
curated[31633] = {"pt": "Quanta irresponsabilidade!", "notes": "Misha repreende o descuido."}
curated[31634] = {"pt": "Se alguém quiser usar, eu entrego. Tá valendo, né?", "notes": "Lyner descarta a responsabilidade."}
curated[31635] = {"pt": "Nossa, que espada linda!CRParece até um espelho!", "notes": "Misha elogia o brilho espelhado da espada."}
curated[31636] = {"pt": "Né? Por isso chamam de \"Silver Singer\".", "notes": "Lyner apresenta o nome Silver Singer."}
curated[31637] = {"pt": "Cantora? Sendo eu quem canta aqui,CRisso me dá uma pontinha de ciúme.", "notes": "Misha com ciúme da espada ser chamada de Cantora."}
curated[31638] = {"pt": "Pensando bem, é verdade.CRSe tiver uma ideia melhor, pode mudar.", "notes": "Lyner permite mudar o nome."}
curated[31639] = {"pt": "Que tal \"Guardiã da Cantora\"?CRLutar com ela significa me proteger também, ué!", "notes": "Misha batiza Guardiã da Cantora ligando à sua proteção."}
curated[31640] = {"pt": "Consegui! Uma lança com dano extraCRe resistência para todos os elementos!", "notes": "Lyner forja lança com todos os atributos elementais."}
curated[31641] = {"pt": "Todos?! Que demais isso!", "notes": "Misha celebra os múltiplos elementos."}
curated[31642] = {"pt": "Né? As lutas vão ficar bico.CRHora do Radolf suar a camisa!", "notes": "Lyner sobrecarrega o cavaleiro Radolf de trabalho."}
curated[31643] = {"pt": "Ele vai roubar sua cena, sabia?", "notes": "Misha alerta que Radolf roubará o protagonismo."}
curated[31644] = {"pt": "......É... fazer o quê, né?", "notes": "Lyner aceita resignado."}
curated[31645] = {"pt": "Terminei... Mas o design deu uma dorCRde cabeça dos diabos!", "notes": "Lyner desabafa sobre o design complexo da arma de fogo."}
curated[31646] = {"pt": "Até que é estilosa, mas tem caraCRde arma de vilão.", "notes": "Misha nota estética vilanesca."}
curated[31647] = {"pt": "A cara do Jack, né? Ele com certezaCRprefere esse estilo mesmo.", "notes": "Lyner associa o visual rebelde ao mercenário Jack."}
curated[31648] = {"pt": "Então bota um nome de bandido nela!", "notes": "Misha propõe batismo temático de fora-da-lei."}
curated[31649] = {"pt": "Por mim beleza... Mas sou péssimoCRpra dar nomes.", "notes": "Lyner admite falta de criatividade."}
curated[31650] = {"pt": "Deixa comigo! Que tal \"Casca-Grossa!\"?CRTão rebelde, né?!", "notes": "Misha sugere Casca-Grossa (Yoroshiku/Bad Ass!)."}
curated[31651] = {"pt": "...É só impressão minha ou soaCRa vilãozinho de esquina?", "notes": "Lyner nota tom cômico de delinquente mirim (ko-akutou)."}
curated[31652] = {"pt": "Por isso combina!CRDecidido: Casca-Grossa!", "notes": "Misha fecha o batismo definitivo."}

# =========================================================================
# SLUS/TEXT/0497 (IDs 31653..31676)
# =========================================================================
curated[31653] = {"pt": "Tentei desenhar o monstro lendárioCR\"tubarão\" no visual, mas seráCRque ficou legal assim?", "notes": "Lyner desenha tubarão."}
curated[31654] = {"pt": "Tá ótimo! Eu só vi em livros,CRmas tá praticamente idêntico.", "notes": "Misha compara com livros."}
curated[31655] = {"pt": "Mas por que desenhar isso?CRQue mistério...", "notes": "Lyner não entende a necessidade do desenho."}
curated[31656] = {"pt": "Porque o nome é Sharkgill, né?CRMas não precisava pintar até as correntes.", "notes": "Misha sobre o nome Sharkgill."}
curated[31657] = {"pt": "A tinta vai descascar se usar.CRQue tal deixar só de enfeite?", "notes": "Misha sugere deixar de enfeite."}
curated[31658] = {"pt": "Ei, ei! E todo o trabalhãoCRque eu tive pra forjar isso?!", "notes": "Lyner reclama do desperdício de esforço."}
curated[31659] = {"pt": "Beleza, KANADE tá pronta!", "notes": "Lyner forja KANADE."}
curated[31660] = {"pt": "Olha só, que estilosa!CRE parece muito forte.", "notes": "Misha elogia."}
curated[31661] = {"pt": "É forte e, ao brandir,CRela toca uma melodia linda!", "notes": "Lyner sobre a música ao brandir."}
curated[31662] = {"pt": "Ah, por isso o nome \"Kanade\".", "notes": "Misha entende Kanade."}
curated[31663] = {"pt": "Não, não! É \"KANADE\", não \"Kanade\"!CRO tom é diferente: é Ka-NAA-de!", "notes": "Lyner insiste na pronúncia estufada."}
curated[31664] = {"pt": "KANADE?CRPor que não Kanade?", "notes": "Misha não vê diferença."}
curated[31665] = {"pt": "Fica mais maneiro!", "notes": "Lyner acha mais descolado."}
curated[31666] = {"pt": "Vai destoar de tudo.CR\"Kanade\" tá ótimo, ué!", "notes": "Misha impõe Kanade simples."}
curated[31667] = {"pt": "...N-não é ruim, mas... tsc.", "notes": "Lyner faz beicinho chateado."}
curated[31668] = {"pt": "Que lança espalhafatosa!", "notes": "Misha sobre visual chamativo."}
curated[31669] = {"pt": "Nem nego: é extravagante mesmo!", "notes": "Lyner admite extravagância."}
curated[31670] = {"pt": "Né? Cheia de babado amarelo...CRDá pra lutar com isso?", "notes": "Misha questiona utilidade em batalha."}
curated[31671] = {"pt": "Mas o espalhafato não é só no visual:CRo efeito dela equipado também é estrondoso!", "notes": "Lyner exalta os bônus extremos."}
curated[31672] = {"pt": "Ataque, defesa, HP e críticoCRsobem estrondosamente!", "notes": "Lyner lista aumentos de atributos."}
curated[31673] = {"pt": "Uau!", "notes": "Misha comemora."}
curated[31674] = {"pt": "E as resistências caem a zero.", "notes": "Lyner joga o balde de água fria."}
curated[31675] = {"pt": "Estrondoso, não é?", "notes": "Lyner reafirma que foi estrondoso."}
curated[31676] = {"pt": "É...CRPobre Radolf...", "notes": "Misha tem pena de Radolf."}

# =========================================================================
# SLUS/TEXT/0498 (IDs 31677..31700)
# =========================================================================
curated[31677] = {"pt": "Tá pronta, mas ficou bemCRpesada pro meu gosto.", "notes": "Lyner surpreso com o peso."}
curated[31678] = {"pt": "Mas isso é arma mesmo?CRNão confundiu com uma bazuca?!", "notes": "Misha acha que é bazuca."}
curated[31679] = {"pt": "A receita dizia que era arma.CREntão é arma, ué.", "notes": "Lyner se fia na receita."}
curated[31680] = {"pt": "...O Harm consegue atirarCRcom esse trabuco monstro?", "notes": "Misha teme que Harm não consiga atirar."}
curated[31681] = {"pt": "É arma, mas bate como bazuca.CRSe bobear, quem atirar sai voandoCRcom o recuo do tiro.", "notes": "Lyner alerta do recuo de bazuca."}
curated[31682] = {"pt": "Por que as armas do HarmCRsão sempre tão perigosas?", "notes": "Misha pergunta do perigo constante das armas do Jack."}
curated[31683] = {"pt": "Ora, porque ele é o Jack, né?", "notes": "Lyner justifica pelo perfil de Jack."}
curated[31684] = {"pt": "Será que ele vai querer usar?", "notes": "Misha em dúvida se Jack vai equipar."}
curated[31685] = {"pt": "Com certeza. Afinal, é o Jack.", "notes": "Lyner tem certeza absoluta."}
curated[31686] = {"pt": "...Pensei no nome perfeito:CRvai se chamar \"Highend Satan\"!", "notes": "Misha batiza Highend Satan."}
curated[31687] = {"pt": "Relaxa, o Jack vai entender.", "notes": "Lyner confia no bom humor de Jack."}
curated[31688] = {"pt": "Lyner... que geringonça inumanaCRé essa que você fez aí?", "notes": "Misha pasma com a motosserra."}
curated[31689] = {"pt": "A motosserra suprema: J's Agony!CRE os ingredientes são bizarros!", "notes": "Lyner apresenta J's Agony."}
curated[31690] = {"pt": "Motosserra e levou Célula D3!CRO resto foram peças mecânicas.", "notes": "Lyner cita a infusão da Célula D3."}
curated[31691] = {"pt": "...E-ela tá viva?!", "notes": "Misha apavorada achando que tem vida."}
curated[31692] = {"pt": "Sei lá! A receita não falavaCRnada disso.", "notes": "Lyner ignora a parte biológica."}
curated[31693] = {"pt": "...Isso não é motosserra,CRé uma máquina de matar!", "notes": "Misha chama de máquina de chacina."}
curated[31694] = {"pt": "...Errada não tá.", "notes": "Lyner concorda com o apelido macabro."}
curated[31695] = {"pt": "Uau, que espada maneira!", "notes": "Misha elogia Eversong."}
curated[31696] = {"pt": "Né? É a Eversong! O visualCRé só o começo da lindeza.", "notes": "Lyner apresenta Eversong."}
curated[31697] = {"pt": "O ápice dela é a resistência a todos os elementos. E é tão leve que permite desferir golpes em alta velocidade!", "notes": "Lyner detalha os poderes superlativos de Eversong."}
curated[31698] = {"pt": "Mesmo desse tamanho?! Demais!", "notes": "Misha chocada com a leveza apesar do porte."}
curated[31699] = {"pt": "Mas dizem que a lâmina originalCRfeita pelo mestre ferreiro eraCRmuito mais absurda.", "notes": "Lyner introduz a lenda do ferreiro ancestral."}
curated[31700] = {"pt": "Pudera: forjou a partir da Reyvateil que amava!", "notes": "Lyner revela a origem romântico-trágica da espada original."}

# =========================================================================
# SLUS/TEXT/0499 (IDs 31701..31724)
# =========================================================================
curated[31701] = {"pt": "...Que papo é esse?!CRÉ conto de terror?", "notes": "Misha assustada com a história de terror."}
curated[31702] = {"pt": "Acho que não era bemCRnesse sentido, mas...", "notes": "Lyner tenta contemporizar."}
curated[31703] = {"pt": "Não me diga que derreteuCRa Reyvateil pra fazer a espada...", "notes": "Misha com medo de ter derretido a Reyvateil."}
curated[31704] = {"pt": "Para de pensar essas coisas!", "notes": "Lyner corta o devaneio macabro."}
curated[31705] = {"pt": "Nossa, que espada absurda!", "notes": "Misha sobre a espada negra sombria."}
curated[31706] = {"pt": "Pudera! A receita dizia que éCRa lâmina suprema de todas!", "notes": "Lyner confirma a espada suprema da receita."}
curated[31707] = {"pt": "Não isso: ela tem cara de vilão!CRParece arma de Lorde das Trevas...", "notes": "Misha acha que parece arma de vilão."}
curated[31708] = {"pt": "Pode parecer de vilão,CRmas o poder de corte é fenomenal!", "notes": "Lyner exalta o poder apesar da aura sombria."}
curated[31709] = {"pt": "Hum... não adianta! Pra mim,CRsó parece espada de lorde maligno.", "notes": "Misha insiste no visual de Lorde das Trevas."}
curated[31710] = {"pt": "Quer que eu pinte de outra cor?!", "notes": "Lyner pergunta se quer repintar."}
curated[31711] = {"pt": "Aí sim! Consegui!! A Asa de...", "notes": "Lyner comemora Asa de Eoria."}
curated[31712] = {"pt": "Eca, que armadura mais cafona!", "notes": "Misha acha cafona."}
curated[31713] = {"pt": "Maldade... Dizer que é a armaduraCRsuprema não é exagero nenhum!", "notes": "Lyner defende a armadura com asas."}
curated[31714] = {"pt": "Suprema? Com essas asas esvoaçantes?!CRVão achar que você é algum astro da músicaCRcom a cabeça meio perturbada!", "notes": "Misha compara a cantor pop maluco."}
curated[31715] = {"pt": "N-não esculhamba o visual!CRVai me dar vergonha na hora de vestir!", "notes": "Lyner com vergonha de vestir."}
curated[31716] = {"pt": "Se fosse normal, não teria vergonhaCRde nada do que os outros falassem!", "notes": "Misha diz que se fosse normal não teria vergonha."}
curated[31717] = {"pt": "...Só julga o visual e nem ligaCRpros atributos excelentes, né?", "notes": "Lyner reclama do foco na aparência."}
curated[31718] = {"pt": "Guardião de Elemia tá pronto!CRE é uma armadura só pra mim!", "notes": "Lyner forja Guardião de Elemia."}
curated[31719] = {"pt": "Ninguém além de você veste?", "notes": "Misha pergunta da exclusividade."}
curated[31720] = {"pt": "Pois é. E é superforte: aumentaCRa resistência a tudo!", "notes": "Lyner sobre resistências aumentadas."}
curated[31721] = {"pt": "Sério? Que desperdício ninguémCRmais poder equipar!", "notes": "Misha acha desperdício ser só dele."}
curated[31722] = {"pt": "Fazer o quê, né?", "notes": "Lyner dá de ombros."}
curated[31723] = {"pt": "Mesmo assim... Escolher quem usa?CRQue guardiãozinho mais pão-duro!", "notes": "Misha xinga o guardião de sovina."}
curated[31724] = {"pt": "Também não precisa humilhar...", "notes": "Lyner pede trégua."}

# =========================================================================
# SLUS/TEXT/0500 (IDs 31725..31748)
# =========================================================================
curated[31725] = {"pt": "Recheada de Airmetal puro:CRa Jaqueta de Airmetal tá pronta!", "notes": "Lyner forja Jaqueta de Airmetal."}
curated[31726] = {"pt": "Parece armadura, mas vestidaCRfica parecendo jaqueta.", "notes": "Misha compara armadura e jaqueta."}
curated[31727] = {"pt": "A agilidade sobe bastante!CRE a defesa é de armadura pura.", "notes": "Lyner detalha velocidade e armadura."}
curated[31728] = {"pt": "Sem zoeira: até criança veste isso!", "notes": "Lyner destaca leveza."}
curated[31729] = {"pt": "Jaqueta com armadura, né...CRQue tal \"Jaquetura\"?", "notes": "Misha cria o trocadilho Jaquetura (Jamor)."}
curated[31730] = {"pt": "Ficou parecendo nome caipira do nada...", "notes": "Lyner acha o apelido caipira."}
curated[31731] = {"pt": "Terminei! Nunca imaginei que forjarCRuma armadura desse tanto trabalho.", "notes": "Lyner cansado com a armadura pesada."}
curated[31732] = {"pt": "Mas valeu a pena o suor todo:CRo visual ficou maneiríssimo!", "notes": "Misha elogia o visual."}
curated[31733] = {"pt": "Pena que eu não posso usar.", "notes": "Lyner lamenta não poder equipar."}
curated[31734] = {"pt": "Poxa... Queria verCRvocê usando isso...", "notes": "Misha queria vê-lo na armadura."}
curated[31735] = {"pt": "Com esse estilo de armadura,CRlutar de espada não orna muito, né.", "notes": "Lyner sobre espada e armadura pesada."}
curated[31736] = {"pt": "E no fim das contas, prefiro a roupa que estou usando agora. Já me acostumei com ela.", "notes": "Lyner prefere seu traje habitual."}
curated[31737] = {"pt": "É... até pode ser...", "notes": "Misha concorda relutante."}
curated[31738] = {"pt": "Eu forjo uma forte só pra mim!", "notes": "Lyner promete forjar uma só pra si."}
curated[31739] = {"pt": "Queria ver o Lyner com essaCR\"Atrocidade de Macho Solitário\"!", "notes": "Misha batiza Atrocidade de Macho Solitário (Otoko Ippiki Gokuaku Hidou)."}
curated[31740] = {"pt": "Nome errado, nada a ver!", "notes": "Lyner rejeita o nome absurdo."}
curated[31741] = {"pt": "Pronto! O frio não pega mais a gente!", "notes": "Lyner comemora ceroulas térmicas."}
curated[31742] = {"pt": "\"Não pega\" uma ova! Se vestir isso,CRnem ando mais com você, Lyner!", "notes": "Misha se recusa a andar com Lyner de ceroula."}
curated[31743] = {"pt": "Não fala assim! É quentinhaCRe a defesa é ótima...", "notes": "Lyner defende o conforto térmico."}
curated[31744] = {"pt": "Não é isso! Lyner de ceroulaCRnão é o Lyner de verdade!", "notes": "Misha diz que Lyner de ceroula não é Lyner."}
curated[31745] = {"pt": "Lyner não pode usar ceroula de velho!CRPassa isso pro Harm!", "notes": "Misha manda dar a ceroula de velho pro Harm."}
curated[31746] = {"pt": "...Nunca fale de \"ceroula\"CRpro Jack.", "notes": "Lyner avisa para não falar isso pro Jack."}
curated[31747] = {"pt": "O nome já é péssimo. Vamos mudarCRpra disfarçar!", "notes": "Misha propõe rebatizar pra disfarçar."}
curated[31748] = {"pt": "Tanto faz pra mim...CRQue nome vai dar?", "notes": "Lyner pergunta o novo nome."}

# =========================================================================
# SLUS/TEXT/0501 (IDs 31749..31772)
# =========================================================================
curated[31749] = {"pt": "Hum... \"Camisola de Macho\"?", "notes": "Misha sugere Camisola Masculina."}
curated[31750] = {"pt": "Beleza, Camiseta Ardente pronta!", "notes": "Lyner completa Camiseta Ardente."}
curated[31751] = {"pt": "Parece camiseta normal...CRUé, isso é só pano comum?!", "notes": "Misha estranha camiseta ser só pano."}
curated[31752] = {"pt": "É camiseta, ué! Se fosse metal,CRseria uma armadura, né?", "notes": "Lyner responde com lógica pura."}
curated[31753] = {"pt": "Pra que forjar camiseta?CRNão vai barrar ataque de inimigo nenhum!", "notes": "Misha duvida da utilidade defensiva."}
curated[31754] = {"pt": "Parece, né? Mas nunca subestimeCRessa camiseta!", "notes": "Lyner manda não subestimar o item."}
curated[31755] = {"pt": "Por fora parece só uma camiseta qualquer,CRmas é mais confiável que muito trambolhoCRde armadura por aí!", "notes": "Lyner exalta a resistência superior da camiseta."}
curated[31756] = {"pt": "Um paninho desses?!", "notes": "Misha indignada com a peça de pano."}
curated[31757] = {"pt": "Tem resistência e ataque de fogo!CRÉ a chama ardente da paixão!!", "notes": "Lyner proclama os poderes de fogo."}
curated[31758] = {"pt": "...Lyner?", "notes": "Misha estranha a empolgação exagerada."}
curated[31759] = {"pt": "Se todos vestirem isso, adeus medo!CRA chama da paixão é invencível!!", "notes": "Lyner em delírio heróico."}
curated[31760] = {"pt": "Tá, tá... vai se chamar \"Camisa Suarenta\".CRAh, e o Lyner tá proibidoCRde vestir isso!", "notes": "Misha batiza Camisa Suarenta e proíbe Lyner de usar."}
curated[31761] = {"pt": "Que perversão! O Lyner temCResse tipo de fetiche?!", "notes": "Misha acusa Lyner de fetiche com roupa feminina."}
curated[31762] = {"pt": "Não fala como se eu fosse depravado!CRIsso aqui é fortíssimo, sabia?", "notes": "Lyner se defende de ser depravado."}
curated[31763] = {"pt": "Não parece nem um pouco...CRMas acho que não serve em mim, né?", "notes": "Misha nota que o tamanho não serve nela."}
curated[31764] = {"pt": "Tem defesa de armadura pesada,CRentão é pra quem luta na vanguarda.", "notes": "Lyner explica que a peça é pra vanguarda."}
curated[31765] = {"pt": "Então... a Krusche veste?", "notes": "Misha supõe que Krusche vestirá."}
curated[31766] = {"pt": "...Quem disse que tem que ser mulher?", "notes": "Lyner solta a dúvida no ar."}
curated[31767] = {"pt": "Isso é feminino, ouviu bem?!CRNem pense em vestir isso por engano!", "notes": "Misha proíbe Lyner de vestir a roupa feminina."}
curated[31768] = {"pt": "Pior que serve num homem certinho...", "notes": "Lyner constata que cabe em homem."}
curated[31769] = {"pt": "Terno Higedance pronto!CRSó não faço a menor ideia de ondeCRalguém usaria um troço desses.", "notes": "Lyner forja Terno Higedance."}
curated[31770] = {"pt": "Pra vestir isso aí, só se forCRnum concurso de fantasia, né?", "notes": "Misha sugere concurso de fantasia."}
curated[31771] = {"pt": "Pois é. Mas ao contrário do visual,CRos efeitos são monstruosos de fortes!", "notes": "Lyner destaca o poder assombroso do traje."}
curated[31772] = {"pt": "É? Parece mentira...", "notes": "Misha cética perante os bônus mágicos."}

# =========================================================================
# SLUS/TEXT/0502 (IDs 31773..31796)
# =========================================================================
curated[31773] = {"pt": "É sério! Não se julgaCRpela aparência, sabia?", "notes": "Lyner prega não julgar pela aparência."}
curated[31774] = {"pt": "Se você pensasse na aparência na hora de forjar, nada disso seria problema.", "notes": "Misha retruca sobre pensar no design."}
curated[31775] = {"pt": "Se você vestir esse bigode,CRvou fingir que nunca te vi na vida!", "notes": "Misha ameaça ignorar Lyner de bigode."}
curated[31776] = {"pt": "Para de destacar só o bigode...", "notes": "Lyner pede pra não focar no bigode."}
curated[31777] = {"pt": "Não sei onde tem Bushido nisso,CRmas tá terminado!", "notes": "Lyner termina traje com suposto Bushido."}
curated[31778] = {"pt": "Não? Pra mim parece um blocoCRpuro e maciço de Bushido!", "notes": "Misha enxerga puro Bushido no traje."}
curated[31779] = {"pt": "...Onde você tá vendoCRBushido nisso aí?", "notes": "Lyner indaga onde ela vê honra samurai."}
curated[31780] = {"pt": "No coque e no quimono?", "notes": "Misha aponta o coque e quimono."}
curated[31781] = {"pt": "Bushido se resume a isso?!", "notes": "Lyner chocado com a definição simplória."}
curated[31782] = {"pt": "Ué, e não é? Tem que ter um nomeCRque esbanje o espírito do Bushido!", "notes": "Misha quer nome com essência de Bushido."}
curated[31783] = {"pt": "Tipo assim... \"Bushidorr\"!", "notes": "Misha cria Bushidorr."}
curated[31784] = {"pt": "...E isso lá é nome de Bushido?", "notes": "Lyner ironiza o nome esquisito."}
curated[31785] = {"pt": "Opereta concluída! Eram tantosCRdetalhes miúdos que cansei legal.", "notes": "Lyner exausto com os detalhes da Opereta."}
curated[31786] = {"pt": "Nossa! Até que o Lyner temCRjeito pra detalhe!", "notes": "Misha elogia a destreza manual de Lyner."}
curated[31787] = {"pt": "Cansei porque não tenho jeito, ué.CRAi, meus olhos...", "notes": "Lyner diz que cansa por ser desajeitado."}
curated[31788] = {"pt": "Bom trabalho! Ficou lindo... Ué?CRNão tá faltando uma pontinha aqui?", "notes": "Misha nota pontinha lascada na peça."}
curated[31789] = {"pt": "Tá na margem de tolerância!CRNão dá nada não.", "notes": "Lyner diz que tá na margem aceitável."}
curated[31790] = {"pt": "Deu pra ver que foi osso.CRE ficou bem claro como o Lyner é desajeitado!", "notes": "Misha debocha do desajeito de Lyner."}
curated[31791] = {"pt": "Nossa, mas que coroa gigante!", "notes": "Misha espantada com o tamanho da coroa."}
curated[31792] = {"pt": "Pensei a mesma coisa enquanto forjava.CRSerá que alguém aguenta isso na cabeça?", "notes": "Lyner questiona quem aguenta o peso."}
curated[31793] = {"pt": "Por muito tempo nem a pau!CRO pescoço vai pro espaço na certa.", "notes": "Misha avisa que o pescoço quebra."}
curated[31794] = {"pt": "Tentei deixar o mais leve possível,CRmas ainda assim ficou nesse peso todo.", "notes": "Lyner tentou aliviar o peso da coroa."}
curated[31795] = {"pt": "...Eu não uso isso nem morta.", "notes": "Misha se recusa a colocar na cabeça."}
curated[31796] = {"pt": "Com certeza. Mas os bônus são brutais,CRentão alguém vai acabar usando.", "notes": "Lyner diz que alguém vai suportar pelo poder."}

# =========================================================================
# SLUS/TEXT/0503 (IDs 31797..31820)
# =========================================================================
curated[31797] = {"pt": "Vai ter fila de gente em dúvida:CRescolher os bônus ou salvar o pescoço?", "notes": "Misha prevê o dilema entre bônus e pescoço."}
curated[31798] = {"pt": "Anel Grathnode tá pronto!", "notes": "Lyner forja Anel Grathnode."}
curated[31799] = {"pt": "Parece um anel normal, ué.", "notes": "Misha acha anel comum."}
curated[31800] = {"pt": "No visual, sim. Mas ele temCRum poder especial bem curioso.", "notes": "Lyner destaca o poder latente."}
curated[31801] = {"pt": "Reduz o tempo de canto das cançõesCRe concede resistência a fogo e gelo!", "notes": "Lyner detalha redução de tempo de canto e resistências."}
curated[31802] = {"pt": "É? Pra tudo isso, o visualCRé bem sem gracinha...", "notes": "Misha acha a aparência apagada."}
curated[31803] = {"pt": "Mas foi feito com Airmetal puro!", "notes": "Lyner destaca a matéria-prima nobre."}
curated[31804] = {"pt": "Hum... \"Anel de Airmetal\"CRsoa bem mais valioso!", "notes": "Misha sugere rebatizar pra Anel de Airmetal."}
curated[31805] = {"pt": "Anel Parameno concluído!CRVai ser de grande ajuda!", "notes": "Lyner forja Anel Parameno."}
curated[31806] = {"pt": "É? A cor até que é bonita.", "notes": "Misha elogia a tonalidade do anel."}
curated[31807] = {"pt": "Corta pela metade o consumo de MPCRgasto durante o canto!", "notes": "Lyner revela economia de 50% de MP."}
curated[31808] = {"pt": "Mentira, que incrível!CRNão vou precisar me preocuparCRem ficar sem MP!", "notes": "Misha empolgada em nunca mais esgotar MP."}
curated[31809] = {"pt": "Viu? Parece anel comum,CRmas o efeito é outro nível!", "notes": "Lyner se gaba da utilidade prática."}
curated[31810] = {"pt": "Ouvindo assim... parece atéCRque tem uma auréola divina!", "notes": "Misha enxerga uma auréola sagrada no item."}
curated[31811] = {"pt": "Posso chamar de \"Anel da Deusa\"?", "notes": "Misha propõe Anel da Deusa."}
curated[31812] = {"pt": "Anel da Deusa?! Bem... entendiCRque você achou precioso demais...", "notes": "Lyner acha o nome grandioso, mas compreensível."}
curated[31813] = {"pt": "Que colar mais lindo!", "notes": "Misha se encanta com o colar."}
curated[31814] = {"pt": "Chama Lágrimas de Poeira Estelar.CRUma adaptação \"daquele\" anel malfalado.", "notes": "Lyner apresenta Lágrimas de Poeira Estelar (Stardust Tears)."}
curated[31815] = {"pt": "...Aquilo virou essa lindeza toda?", "notes": "Misha surpresa com a reciclagem bem-sucedida."}
curated[31816] = {"pt": "Se não fizesse assim, você nem usava!CREu também penso nas coisas, sabia?", "notes": "Lyner diz que pensou no gosto dela."}
curated[31817] = {"pt": "Obrigada! Ficou bem melhor!", "notes": "Misha agradece com carinho."}
curated[31818] = {"pt": "Posso chamar de \"Star Jewels\"CRse eu for usar?", "notes": "Misha quer apelidar de Star Jewels."}
curated[31819] = {"pt": "Por mim, beleza.", "notes": "Lyner aprova com simplicidade."}
curated[31820] = {"pt": "Pronto! Toma aqui, Misha:CRo Anel da Sogra!", "notes": "Lyner entrega o temido Anel da Sogra."}

# =========================================================================
# SLUS/TEXT/0504 (IDs 31821..31844)
# =========================================================================
curated[31821] = {"pt": "\"Toma\" nada! Eu não quero isso não!", "notes": "Misha recusa o anel pelo nome odioso."}
curated[31822] = {"pt": "É por causa do nome, né? Mas eleCRfaz o Harmonics durar mais...", "notes": "Lyner defende o prolongamento do Harmonics."}
curated[31823] = {"pt": "Mas é da sogra! Acha que garotaCRfica feliz com isso?!", "notes": "Misha indignada com o batismo matrimonial infame."}
curated[31824] = {"pt": "Sogra mete mais medo que demônio!", "notes": "Misha faz piada tradicional sobre sogras e demônios."}
curated[31825] = {"pt": "Se mudar pra \"Anel de Amor pra Misha\",CReu até uso!", "notes": "Misha faz chantagem romântica para aceitar a joia."}
curated[31826] = {"pt": "Que é isso?", "notes": "Misha pergunta o que é a touca."}
curated[31827] = {"pt": "Como assim? É uma touca de xampu!CRNão me diga que nunca viu?", "notes": "Lyner espantado com a falta de conhecimento da touca de banho."}
curated[31828] = {"pt": "...Ah, isso! É o que usaCRpra lavar o cabelo, né?", "notes": "Misha lembra da utilidade no banho."}
curated[31829] = {"pt": "Não conhecia mesmo?!CRNunca usou uma na vida?", "notes": "Lyner pergunta se ela nunca usou."}
curated[31830] = {"pt": "Eu já sabia lavar a cabeça sem isso!CRNossa, é tão fininha...", "notes": "Misha diz que lavava a cabeça sozinha desde pequena."}
curated[31831] = {"pt": "Nem é grande coisa pra vocêCRexaminar tanto...", "notes": "Lyner acha exagero examinar a touca de plástico."}
curated[31832] = {"pt": "Pra mim é puro contato imediato!", "notes": "Misha compara a touca a um contato extraterrestre."}
curated[31833] = {"pt": "Lyner faz até isso?!", "notes": "Misha admirada que Lyner fez o cordão de Dive."}
curated[31834] = {"pt": "Pois é. Mas trançar fioCRnão é nada moleza.", "notes": "Lyner fala da dificuldade de tecer o fio."}
curated[31835] = {"pt": "Mas equipar isso aumenta os PontosCRde Dive! Valeu a trabalheira.", "notes": "Lyner comemora os Pontos de Dive (DP) extras."}
curated[31836] = {"pt": "É... Mas mudando de assunto:CRcomo é que se equipa isso?", "notes": "Misha pergunta como equipar um mero cordão."}
curated[31837] = {"pt": "Ué? Não é só carregar consigo?", "notes": "Lyner sugere apenas carregar no bolso."}
curated[31838] = {"pt": "Acho que sim, mas carregarCRnão dá aquela sensação de estarCRequipando, sabe?", "notes": "Misha reclama que carregar não parece equipar."}
curated[31839] = {"pt": "E assim vai embolar tudo...", "notes": "Misha teme que o fio fique embaraçado."}
curated[31840] = {"pt": "Pode ser... Mas e daí?CROs efeitos continuam valendo, né.", "notes": "Lyner diz que o efeito funciona mesmo no bolso."}
curated[31841] = {"pt": "Já sei! Costura na roupa!CRAssim dá sensação de estar equipado.", "notes": "Misha quer costurar o fio na roupa."}
curated[31842] = {"pt": "Pra tirar vai ser um parto,CRe você vai usar a mesma roupa por dias...", "notes": "Lyner alerta para o transtorno de costurar no tecido."}
curated[31843] = {"pt": "Forjar foi fácil, mas darCRo formato certo deu trabalho.", "notes": "Lyner sobre a modelagem da joia."}
curated[31844] = {"pt": "Uau, que lindeza! Dá até vontadeCRde usar como colar.", "notes": "Misha quer usar a peça lapidada como colar."}

# Teste completo de todas as 288 falas
fails = 0
for d_id, item in sorted(curated.items()):
    orig_b = db_sizes[d_id]
    orig_en = input_map[d_id]["original_en"]
    text = item["pt"]
    sz = encoded_size(text)
    errs = validate_line(d_id, orig_en, text)
    if sz > orig_b or errs:
        fails += 1
        print(f"FAIL ID {d_id}: {sz}/{orig_b}B ({sz-orig_b:+d}B) | {errs} | '{text}'")

print(f"\n==========================================")
print(f"TOTAL TESTADO: {len(curated)} / 288 | FALHAS: {fails}")
print(f"==========================================")
