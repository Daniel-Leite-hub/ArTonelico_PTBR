from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path

from artonelico_tool.evd import encode_game_text, parse
from artonelico_tool.project import connect


ROOT = Path(__file__).resolve().parents[1]
PROJECTS = (ROOT / "ArTonelico_PTBR.atproj", ROOT / "release/ArTonelico_PTBR.atproj")
EVENT = "Event/1.evd"

# Concise PT-BR adaptations for the fixed-size new-game prologue records.
# These remain automatic/editable translations; this script does not approve
# them as if they had been reviewed by the user.
ADAPTED = {
    0: "BANPRESTO & GUST TRAZEM",
    3: "O mundo foi destruído duas vezes.",
    4: "A primeira foi obra humana.",
    5: "A segunda, por vidas artificiais.",
    7: 'Nasceu uma "vida indesejada"...',
    8: "Vírus",
    9: "Esses vírus eram dados ocultos na torre e se alimentavam dela.",
    10: "Surgiram no mundo real e atacaram humanos.",
    11: "Ameaçada pelos vírus, a humanidade vivia em terror.",
    12: "No caos, surgiu um raio de esperança.",
    13: "As Reyvateil, Donzelas do Canto, vieram com os Cristais do Hino.",
    17: "As Donzelas e seus fiéis ficaram na torre para conter os vírus.",
    18: 'Eram os "Apóstolos de Elemia", respeitados por todos.',
    19: "A base deles virou uma cidade...",
    20: "Platina, a Cidade Flutuante.",
    21: 'Com Platina e os "Apóstolos de Elemia", a vida voltou ao normal.',
    22: "Agora, uma terceira crise ameaça destruir o mundo.",
    23: "3770 d.C. [Altar]",
    24: "...O que houve!? Reporte!",
    25: "Sim! Vírus no [Altar dos Apóstolos]!",
    26: "Classe e nível: desconhecidos. Sem dados!",
    27: "...Um novo vírus? O tremor piorou.",
    30: "Idiota! Em público, é Comandante!",
    32: "Classe e nível desconhecidos. Não temos dados.",
    33: "...Ótimo. Esperei por um inimigo assim.",
    34: "Vamos! Agora!",
    35: "Lyner! Pare!",
    39: "Se esperarmos, os vírus destruirão a cidade!",
    40: "A quem você serve? Responda, Lyner!",
    41: "...Sou cavaleiro de Shurelia.",
    42: "Então, obedeça às ordens de Shurelia.",
    43: "É o dever de um Cavaleiro de Elemia!",
    47: "O [Altar dos Apóstolos] foi tomado por vírus.",
    48: "Nada sabemos sobre esses vírus. Estamos às cegas.",
    49: "Entendido. Investigaremos. Lyner, venha comigo.",
    50: "Certo!",
    51: "Eu disse, pai! Ela confia em mim, não como você! Viu?",
    53: "Temos que ir. Leard, proteja a cidade.",
    54: "Sim! Não se preocupe, Lady Shurelia!",
    56: "Você não ajudará. Só evite problemas.",
    57: "...Não tema! Eu vencerei esses vírus. Juro!",
    58: "Hmph... quando você vai crescer?",
    59: "O que é!?",
    61: "...Eles saem do [Altar dos Apóstolos]! O que houve?",
    62: "Chega. Todos, preparem-se para lutar!",
    63: "Certo! Acabem logo com eles!",
    64: "Espere, Lyner. Vamos analisá-los.",
    66: "...Confirmado... não batem com nenhuma amostra.",
    67: "Padrão e características desconhecidos... Não sei como será a batalha.",
    69: "Lyner! Aguarde as ordens de Shurelia.",
    71: "...É perigoso, mas temos que agir.",
    72: "Vou entoar o canto. Vocês dois, me protejam!",
    73: "O que é... está transparente! O que houve...?",
    75: "Atravessaram-nos! Nossos ataques não os ferem!",
    76: "Esses vírus... são...!",
    79: "Não temos chance contra eles!",
    80: "...Lyner, Ayatane, vamos recuar.",
    81: "Quê!?",
    82: "Ela tem razão. Vamos voltar.",
    83: "Espere! Somos Cavaleiros de Elemia. Devemos destruir vírus!",
    84: "Não podemos desistir na dificuldade!",
    87: "Pense melhor. Se morrermos, quem protegerá nossa terra?",
    89: "Eu entendo, mas um cavaleiro deve decidir com razão.",
    91: "Certo...",
    96: "Que som é esse...?",
    97: "Lady Shurelia! É...",
    98: "As linhas sinfônicas daqui foram danificadas.",
    101: "Não... isto é como os dois desastres passados...",
    102: "Voltemos a Platina para uma reunião de emergência.",
    103: "Está chegando!",
    109: "Mas... impossível!",
    110: "Sem tempo para discutir!",
    111: "Lady Shurelia, Lyner, perdão.",
    114: "...Lyner. Logo tomarão esta área. Depressa, para Platina.",
    115: "Quer que eu abandone Ayatane!? Não posso...",
    116: "Também não quero deixá-lo...",
    117: "Mas ficar aqui não ajuda.",
    121: "Ayatane, resista!",
    123: "O quê!?",
    124: "Droga! De novo!",
    125: "Desgraçado!",
    126: "Lyner, seus golpes não afetam esses vírus!",
    127: "Vamos recuar!",
    128: "Ayatane... não",
    129: "Também corremos perigo... Se bloquearem a estrada, não voltaremos a Platina.",
    130: "Lady Shurelia, Ayatane não importa? Como fica tão calma?",
    131: "Estou no comando... Não posso julgar com emoção.",
    136: "...Então, somos impotentes...",
    137: "...Há um jeito.",
    138: "Hã? O quê?",
    140: "Usemos o [Cristal do Hino].",
    141: "O Cristal do Hino! As Donzelas o usaram para salvar o mundo...",
    142: "Sim. Precisamos do tipo [Purger].",
    143: "O Cristal [Purger]...",
    144: "Mas esse cristal não está em Platina.",
    145: "Está nas [Asas de Horus], continente a milhares de stons.",
    146: "...No Mundo Inferior!? Pensei que descer fosse proibido!",
    150: "Hã!? Mas a aeronave...",
    151: "É uma emergência. Autorizo o uso especial.",
    152: "M, mas... tudo ocorre tão rápido!",
    153: "O mundo está em crise! Se não agirmos, será a terceira vez!",
    154: "Lady Shurelia...",
    155: "...Perdão por gritar.",
    156: "Mas entenda: só alguns podem cumprir esta missão.",
    157: "Lyner, é minha primeira escolha. Eu lhe peço...",
    160: "Eu... comando.",
    161: "Não posso sair com os vírus à solta.",
    162: "Não! Não vou deixá-la!",
    164: "Rápido! Temos pouco tempo!",
    166: "Lyner... Tome isto...",
    169: "Isso deve ajudar.",
    170: "Obteve [Broche Hino]!",
    173: "Por favor... o cristal...",
    175: "Só você pode.",
    177: "Lady Shurelia... trarei o [Purger]. Prometo...",
    178: "Resista até eu voltar.",
    180: "Primeiro, ative o campo ambiente no alvo.",
}


def validate() -> None:
    evd = parse((ROOT / "work/extracted/Event/1.evd").read_bytes())
    failures = []
    for index, text in ADAPTED.items():
        used = len(encode_game_text(text))
        available = len(evd.dialogues[index].raw)
        if used > available:
            failures.append((index, used, available, text))
    if failures:
        details = "\n".join(
            f"{index}: {used}>{available} bytes: {text}"
            for index, used, available, text in failures
        )
        raise ValueError(f"Adaptações ainda excedem os registros:\n{details}")


def apply(project: Path) -> None:
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = project.with_name(f"{project.stem}.antes_event1_conciso_{stamp}{project.suffix}")
    shutil.copy2(project, backup)
    db = connect(project)
    try:
        for index, text in ADAPTED.items():
            row = db.execute(
                "SELECT review_status FROM dialogues WHERE event_file=? AND entry_index=?",
                (EVENT, index),
            ).fetchone()
            if row is None:
                raise ValueError(f"Fala ausente: {EVENT}:{index}")
            if row["review_status"] == "approved":
                raise ValueError(f"Revisão aprovada não será alterada: {EVENT}:{index}")
            size = len(encode_game_text(text))
            db.execute(
                "UPDATE dialogues SET automatic=?,translation=?,translated_bytes=?,size_ok=1,error='' "
                "WHERE event_file=? AND entry_index=?",
                (text, text, size, EVENT, index),
            )
        db.commit()
    finally:
        db.close()
    print(f"Atualizado: {project}")
    print(f"Backup: {backup}")


def main() -> None:
    validate()
    for project in PROJECTS:
        apply(project)
    print(f"Adaptações válidas: {len(ADAPTED)}")


if __name__ == "__main__":
    main()
