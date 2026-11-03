import json
import sqlite3
import sys
from pathlib import Path

sys.path.append(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao")
from artonelico_tool.project import encoded_size

with open(r"G:\JOGO\PS2\Ar tonelico - Melody of Elemia (Undub)\Ferramentas_Traducao\curadoria_editorial\curadoria_config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

conn = sqlite3.connect(config["database_path"])
c = conn.cursor()
c.execute("SELECT id, event_file, original, original_jp, original_bytes, automatic FROM dialogues WHERE id BETWEEN 21021 AND 21170 AND original_bytes > 60 ORDER BY id")
rows = c.fetchall()
conn.close()

# Dicionário de descrições refinadas, concisas e dramáticas
REFINED_DESC = {
    # 21022: Pom (Cap 272B)
    21022: "Animal parecido com uma castanha. A cabeça é pontuda, com a ponta rosa. É macio e gelatinoso, por isso suas investidas não machucam muito.",
    # 21025: Marron Pom (Cap 304B) - Fixes "melão" -> "castanho/marrom"
    21025: "Na forma e na cor, é puro marrom. O corpo pouco difere do Pom comum, mas a ponta de sua cabeça é castanha. Também não machuca muito.",
    # 21028: Peachy Pom (Cap 264B)
    21028: "Pom de corpo rosa e cabeça branca. Continua macio como os outros, mas é bem agressivo. Não baixe a guarda.",
    # 21031: Kneaded Pom (Cap 344B)
    21031: "É tão azul que a cabeça se confunde com o corpo. Lembra uma gota d'água. Diferente dos outros Poms, tem textura mais elástica.",
    # 21034: Metal Pom (Cap 336B)
    21034: "Não se chama Metal à toa. Quase nenhum ataque afeta essa massa dura, e seus golpes doem horrores. Mesmo assim, continua macio e saltitante.",
    # 21037: Prism Pom (Cap 344B)
    21037: "Um Pom multicolorido e deslumbrante. Dá vontade de capturá-lo para uma coleção, mas sua força torna isso muito difícil.",
    # 21040: Trio de Pom (Cap 296B)
    21040: "Três Poms. Um sozinho é fraco, mas juntos ficam fortes. Seus ataques triplos perfeitamente sincronizados são um espetáculo.",
    # 21043: Big Pom (Cap 312B)
    21043: "Versão colossal do Pom. Ainda é macio, mas tem uma massa que faz o chão tremer. Ser atingido ou esmagado por ele é um pesadelo.",
    # 21046: Tiny Pom (Cap 312B) - Restores comedic JP punchline
    21046: "Versão menor de um Pom já pequeno. É difícil acertá-lo e seus botes causam dor pontual como picadas. Cuidado redobrado para quem tem vista fraca!",
    # 21049: Hulaflower (Cap 360B)
    21049: "Flor com a metade superior de uma pessoa no centro. As raízes servem de pernas para se mover. O cabelo na cabeça é, na verdade, um botão de flor.",
    # 21052: Yodelflower (Cap 320B)
    21052: "Ao contrário da Hulaflower, a figura entre as pétalas tem cor de pele. Muita gente se aproxima por engano e acaba sendo atacada.",
    # 21055: Gospelflower (Cap 320B)
    21055: "Flor acinzentada e sombria, mas bastante agressiva: ela própria avança sobre você. É bem resistente, então convém ter cautela.",
    # 21058: Yumyumflower (Cap 304B)
    21058: "Não é a flor que serve de comida. A figura no centro devora qualquer coisa. Se um viajante passar por perto... nhac, nhac!",
    # 21061: Cannonflower (Cap 272B)
    21061: "Uma Hulaflower que cresceu demais. As pétalas e a figura humana no centro aumentaram, tornando-a imensa e intimidadora.",
    # 21064: Guillotineflower (Cap 256B)
    21064: "Parece dourada, mas está coberta de pólen espesso. Suas folhas cortam com a afiação de lâminas de guilhotina.",
    # 21067: Gigaflower (Cap 280B)
    21067: "O que a fez crescer tanto? A flor e a pessoa no centro são titânicas. A sensação é de lutar contra um verdadeiro gigante.",
    # 21070: Stray Dog (Cap 304B)
    21070: "Parece mais um cão selvagem que um monstro. Não subestime as feras: ele continuará atacando ferozmente até abater você.",
    # 21073: Mad Dog (Cap 296B)
    21073: "Cão raivoso e traiçoeiro. Presas e garras afiadas, com investidas rápidas, tornam-no irritante. Fica eufórico ao ver sangue.",
    # 21076: Feral Wolf (Cap 176B)
    21076: "Lobo branco muito mais feroz que o Mad Dog. Move-se com extrema rapidez.",
    # 21079: Night Stalker (Cap 296B)
    21079: "Essas feras rondam a noite atrás de presas distraídas. Anulam ataques físicos com facilidade, tornando-se rivais difíceis.",
    # 21082: Mist Walker (Cap 376B)
    21082: "Dizem ser o mais forte dos lobos. Ao encontrar uma presa, ataca implacável a qualquer hora. Golpes físicos não funcionam contra ele.",
    # 21085: Mercenary (Cap 288B)
    21085: "Soldados de aluguel sem lealdade fixa. Aceitam qualquer serviço conforme a recompensa e o contrato. Quase todos são brutos.",
    # 21088: Wandering Swordsman (Cap 256B)
    21088: "Ninguém sabe de onde veio nem para onde vai. Viaja sem destino certo enquanto lapida a maestria de sua espada.",
    # 21091: Samuraiman (Cap 152B)
    21091: "Um samurai que usa espada em vez de katana. Por isso atende por Samuraiman.",
    # 21094: Sword Adept (Cap 264B)
    21094: "Espadachim veterano com anos de treino árduo. Não é derrotado com facilidade. Muitos têm porte intimidador de guarda-costas.",
    # 21097: Rogue (Cap 248B)
    21097: "Vivem em becos e vielas escuras. Costumam agir em bando quando resolvem cercar e intimidar suas vítimas.",
    # 21100: Blademaster (Cap 208B)
    21100: "Espadachim supremo que atingiu o ápice da arte marcial. Aperfeiçoou todas as formas de esgrima existentes.",
    # 21103: Tenba Security (Cap 296B)
    21103: "Guardas particulares do Conglomerado Tenba. Estão em todas as suas instalações. Não são fortes, mas surgem em bandos chatos.",
    # 21106: Guardsman (Cap 264B)
    21106: "Vigilantes de instalações diversas. Sozinhos são fracos, mas nunca fazem ronda desacompanhados: prepare-se para enfrentar vários.",
    # 21109: Armed Guard (Cap 272B)
    21109: "Guarda com equipamento tático especial. Protege setores mais importantes e é muito mais forte que os vigias comuns.",
    # 21112: Crusader (Cap 296B)
    21112: "Guardas das instalações mais críticas. São perigosos e não hesitam em matar para impedir o avanço de invasores.",
    # 21115: Shadowman (Cap 272B)
    21115: "Guardas munidos de armas devastadoras. Se você levantar qualquer suspeita, atacarão sem aviso até cessar seus movimentos.",
    # 21118: Specialist (Cap 248B)
    21118: "A elite dos guardas. Com 95% de taxa de sucesso, garantem que nenhum intruso passará por suas patrulhas.",
    # 21121: Priest Spirit (Cap 328B)
    21121: "Espectros de sacerdotes com armaduras pesadas e lanças. Não sabemos como morreram, mas atacam enfurecidos brandindo suas armas.",
    # 21124: Temple Guard (Cap 272B)
    21124: "Guardas que protegem o Templo. Além das lanças, usam magias de cura e ataque. Avançar sem cautela trará sérias dores de cabeça.",
    # 21127: Temple Master (Cap 248B)
    21127: "Guardas de santuários sagrados. Não usam lanças como os Vigias do Templo, mas desferem artes mágicas perigosas.",
    # 21130: Fanatic (Cap 288B)
    21130: "Especialistas em magia que empunham cajados. Atacam e se curam simultaneamente, revelando-se oponentes bem irritantes.",
    # 21133: Heretic Disciple (Cap 288B)
    21133: "Discípulos da heresia trajando máscaras estranhas. Possuem atributos altos no ataque e na defesa, atormentando com magias arcanas.",
    # 21136: Deathroid (Cap 264B) - Restores anatomical detail from JP
    21136: "Pela falta da metade inferior do corpo, nota-se que não são humanos. São espíritos de guardas caídos com forças ampliadas.",
    # 21139: Falcon Hawk (Cap 304B)
    21139: "Ave monstruosa colossal que ataca com garras e bico afiados. O tamanho assusta à primeira vista, mas é fraca e fácil de abater.",
    # 21142: Vulture (Cap 216B)
    21142: "Ave monstruosa enorme. Não chega a ser muito forte, mas sua velocidade transforma a luta em um estorvo.",
    # 21145: Roc (Cap 240B)
    21145: "Ave colossal que encarna um monstro temível. Possui garras enormes nas asas, usadas para dilacerar seus adversários.",
    # 21148: Garuda (Cap 256B) - Lowers capitalization of 'Ataques Armazenados'
    21148: "A ave monstruosa mais rápida e forte. Seus golpes carregados causam estragos imensos: derrote-a antes que concentre poder.",
    # 21151: Bit Ball (Cap 392B)
    21151: "Parece uma simples esfera, mas dispara lasers pelo orifício vermelho central. Se não for destruída logo, chamará reforços.",
    # 21154: Bit Ball v2 (Cap 320B)
    21154: "Versão aprimorada da Bit Ball. Além de disparar lasers mais potentes, possui blindagem reforçada. Jamais a subestime.",
    # 21157: Blast Eye (Cap 272B)
    21157: "Uma Bit Ball um pouco maior. Sua rigidez estrutural e seu poder de destruição também aumentaram bastante.",
    # 21160: Hyper Bit (Cap 248B)
    21160: "Várias Bit Balls reunidas em grupo. Juntas têm grande poder destrutivo, e seus disparos individuais são bem fortes.",
    # 21163: Flame Guarder (Cap 264B)
    21163: "Bit Ball modificada para resistir a ataques especiais. Uma barreira mágica ao seu redor a protege contra o fogo.",
    # 21166: Ice Guarder (Cap 264B)
    21166: "Bit Ball modificada para resistir a ataques especiais. Uma barreira mágica ao seu redor a protege contra o gelo.",
    # 21169: Electric Guarder (Cap 272B)
    21169: "Bit Ball modificada para resistir a ataques especiais. Uma barreira mágica ao seu redor a protege contra raios."
}

print(f"Total refined descriptions: {len(REFINED_DESC)}")
all_fit = True
for r in rows:
    d_id = r[0]
    cap = r[4]
    txt = REFINED_DESC.get(d_id)
    if not txt:
        print(f"MISSING ID {d_id}!")
        all_fit = False
        continue
    sz = encoded_size(txt)
    if sz > cap:
        print(f"OVERFLOW ID {d_id}: Cap={cap}B, Sz={sz}B (Diff: +{sz-cap}B) -> '{txt}'")
        all_fit = False
    else:
        print(f"ID {d_id} OK: {sz}B <= {cap}B (Margem: {cap-sz}B)")

if all_fit:
    print("\nALL 50 DESCRIPTIONS FIT PERFECTLY WITHIN CAPACITY!")
