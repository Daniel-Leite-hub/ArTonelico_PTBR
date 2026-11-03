import json
import sys
from pathlib import Path

BASE_DIR = Path("Ferramentas_Traducao")
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "tools"))

from artonelico_tool.project import encoded_size
from curadoria_validate import validate_line

with open(BASE_DIR / "curadoria_editorial/limits_blk19.json", "r", encoding="utf-8") as f:
    limits = json.load(f)

# Batch 1: IDs 25514 to 25550 (37 lines)
# Desfecho do diálogo noturno de Shurelia (tameguchi, Traje Sailor Bunny, prática de canto no parque)
batch1_curated = {
    25514: (
        "Quero falar como amiga... Só nós dois.",
        "Resolução de estouro (110B -> 79B <= 88B). Shurelia propondo falar informalmente apenas a sós com Lyner.",
        "rewritten"
    ),
    25515: (
        "Tudo bem.CRSe falasse assim em público, também criaria situações complicadas.",
        "Resolução de estouro (198B -> 153B <= 184B). Lyner concordando que a intimidade deve ser mantida longe dos olhos alheios com CR.",
        "rewritten"
    ),
    25516: (
        "Só entre nós dois, então.CRSegredo nosso.",
        "Resolução de estouro (95B -> 81B <= 88B). Pacto de segredo fraternal e romântico entre Lyner e Shurelia com CR.",
        "rewritten"
    ),
    25517: (
        "O-obrigada...",
        "Timidez fofa e gaguejo de Shurelia ao aceitar o pacto (25B <= 32B).",
        "approved"
    ),
    25518: (
        "E-então... vou falar s-sem cerimônia...",
        "Resolução de estouro (129B -> 81B <= 88B). Shurelia gaguejando ao tentar usar fala informal (tameguchi).",
        "rewritten"
    ),
    25519: (
        "M-mas faz tanto tempo que posso me atrapalhar, então não ria de mim, por favor.",
        "Shurelia insegura escorregando de volta para a polidez formal involuntária (163B <= 176B).",
        "approved"
    ),
    25520: (
        "Sem cerimônia?",
        "Correção crítica de omissão do inglês: Lyner provocando o fato de Shurelia ter usado polidez formal (30B <= 32B).",
        "rewritten"
    ),
    25521: (
        "Ah... é que d-do nada assim é tão difícil...",
        "Resolução de estouro (115B -> 90B <= 104B). Shurelia admitindo a dificuldade de largar séculos de formalidade régia.",
        "rewritten"
    ),
    25522: (
        "Diz aí, Lyner... você tem uma roupa estranha, né?",
        "Resolução de estouro (120B -> 100B <= 104B). Shurelia mudando de assunto com curiosidade inocente.",
        "rewritten"
    ),
    25523: (
        "Roupa estranha? Acho que não tenho. Como ela é?",
        "Lyner confuso sem desconfiar do que Shurelia está falando (94B <= 112B).",
        "approved"
    ),
    25524: (
        "Aquela cheia de babados e orelhas de coelho.",
        "Resolução de estouro (106B -> 89B <= 96B). Descrição cômica do traje por Shurelia.",
        "rewritten"
    ),
    25525: (
        "Ah, tá falando do Traje Sailor Bunny?",
        "Resolução de estouro (127B -> 76B <= 80B). Menção do traje Sailor Bunny (せらうさドレス).",
        "rewritten"
    ),
    25526: (
        "Afinal, pra que é essa roupa?",
        "Curiosidade genuína de Shurelia sobre a utilidade da fantasia (60B <= 64B).",
        "approved"
    ),
    25527: (
        "O visual é bizarro, eu sei, mas ela dá uma defesa e tanto, viu?",
        "Lyner defendendo as propriedades defensivas do traje (130B <= 168B).",
        "approved"
    ),
    25528: (
        "Hãã? Mas é tão fina, e...CRparece feita para algum fetiche esquisito...",
        "Restauração do tom original japonês ('変な趣味') sobre o visual fetichista da roupa com CR (146B <= 160B).",
        "rewritten"
    ),
    25529: (
        "É sério! CRe se acha que é mentira, veste pra ver! CRVai sentir o efeito na mesma hora.",
        "Resolução de estouro (214B -> 175B <= 192B). Lyner desafiando Shurelia a experimentar a roupa com CRs.",
        "rewritten"
    ),
    25530: (
        "...V-vou recusar educadamente.",
        "Resolução de estouro (89B -> 61B <= 88B). Shurelia corando e recusando firmemente vestir o traje de coelhinha.",
        "rewritten"
    ),
    25531: (
        "Falando nisso, não precisa praticar seus Cantos hoje?",
        "Lyner mudando de assunto para os ensaios de canto de Shurelia (108B <= 120B).",
        "approved"
    ),
    25532: (
        "Hã?",
        "Reação surpresa de Shurelia (8B <= 16B).",
        "approved"
    ),
    25533: (
        "Lembra quando você estavaCRcantando no parque à noite?",
        "Resolução de estouro (133B -> 113B <= 120B). Lyner relembrando o ensaio noturno no parque com CR.",
        "rewritten"
    ),
    25534: (
        "Ah... não fica lembrando disso. É meio vergonhoso...",
        "Timidez de Shurelia ao ter seus treinos secretos revelados (107B <= 112B).",
        "approved"
    ),
    25535: (
        "Não precisava cantar sozinha à noite.",
        "Resolução de estouro (82B -> 77B <= 80B). Lyner demonstrando preocupação afetuosa.",
        "rewritten"
    ),
    25536: (
        "Ainda estou treinando,CRnão dá para deixar ninguém ouvir.",
        "Resolução de estouro (140B -> 117B <= 128B). O perfeccionismo musical de Shurelia com CR.",
        "rewritten"
    ),
    25537: (
        "Não quero incomodar ninguém.",
        "Consideração de Shurelia para não perturbar os outros na estalagem (59B <= 64B).",
        "approved"
    ),
    25538: (
        "S-será?CRNão achei que você cantasse mal.",
        "Resolução de estouro (120B -> 82B <= 96B). Elogio sincero e encorajador de Lyner com CR.",
        "rewritten"
    ),
    25539: (
        "Não, ainda falta muito...CRTenho que treinar bem mais para melhorar.",
        "Resolução de estouro (155B -> 139B <= 144B). Humildade e dedicação incansável de Shurelia com CR.",
        "rewritten"
    ),
    25540: (
        "Mas eu adoro cantar,CRentão não é sacrifício nenhum!",
        "Resolução de estouro (117B -> 106B <= 112B). O amor genuíno de Shurelia pelo canto com CR.",
        "rewritten"
    ),
    25541: (
        "É...",
        "Resolução de estouro (20B -> 10B <= 16B). Assentimento carinhoso de Lyner.",
        "rewritten"
    ),
    25542: (
        "...E se eu te acompanharCRquando for treinar?",
        "Oferta gentil de Lyner para fazer companhia nos ensaios com CR (91B <= 112B).",
        "approved"
    ),
    25543: (
        "O quê!?",
        "Surpresa desconcertada de Shurelia (16B <= 16B).",
        "approved"
    ),
    25544: (
        "Pensa em mim como plateia.CRAlém disso, andar sozinha à noite é perigoso.",
        "Resolução de estouro (190B -> 153B <= 168B). Instinto protetor de Lyner com CR.",
        "rewritten"
    ),
    25545: (
        "N-não, não precisa...",
        "Timidez de Shurelia desconcertada (45B <= 56B).",
        "approved"
    ),
    25546: (
        "Mas sabe...",
        "Insistência carinhosa de Lyner (23B <= 32B).",
        "approved"
    ),
    25547: (
        "N-não... Morro de vergonhaCRde me verem treinando...",
        "Shurelia resistindo por pura timidez fofa com CR (103B <= 112B).",
        "approved"
    ),
    25548: (
        "Ah...",
        "Lyner aceitando com delicadeza (11B <= 16B).",
        "approved"
    ),
    25549: (
        "...Quando eu melhorar um pouco,CRtalvez aceite sua companhia.",
        "Resolução de estouro (136B -> 125B <= 128B). Concessão doce e promessa futura de Shurelia com CR.",
        "rewritten"
    ),
    25550: (
        "Falando nisso, você conhece a garota do gato na pousada de Nemo?",
        "Resolução de estouro (143B -> 130B <= 136B). Lyner puxando assunto com Aurica sobre Nemo.",
        "rewritten"
    )
}

if __name__ == "__main__":
    assert len(batch1_curated) == 37, f"Esperado 37, obtido {len(batch1_curated)}"
    errs = []
    for did, (text, rat, verd) in batch1_curated.items():
        lim = limits[str(did)]
        enc = encoded_size(text)
        if enc > lim:
            errs.append(f"ID {did}: enc {enc}B > limit {lim}B (+{enc - lim})")
        v_errs = validate_line(did, "", text)
        if v_errs:
            errs.append(f"ID {did} validação: {v_errs}")

    if errs:
        print(f"Erros em Batch 1 ({len(errs)}):")
        for e in errs:
            print(" ", e)
        sys.exit(1)
    else:
        print("Batch 1: 100% OK! 37 falas validadas com 0 estouros e 0 erros técnicos.")
