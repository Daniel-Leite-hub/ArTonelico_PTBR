import sys
import sqlite3

sys.path.insert(0, 'Ferramentas_Traducao')
from artonelico_tool.project import encoded_size

conn = sqlite3.connect('Ferramentas_Traducao/ArTonelico_PTBR.atproj')
c = conn.cursor()

f0505 = {
    31845: "Pelo tamanho, daria certinhoCRpara fazer um colar, não?",
    31846: "Viu só?CREntão capricha aí!",
    31847: "E sobrou pra mim fazer, né?",
    31848: "Quando tiver tempo.CRDo jeito que tá, não passaCRde uma pedrinha comum.",
    31849: "Ignora os efeitos e só ligaCRpra aparência? Ai, ai...",
    31850: 'E daí? E não usa termo científico tipoCR"Cristal". Vamos dar um nome de joia de verdade, como "Joias Ardel"!',
    31851: "Pronto!",
    31852: "...Que troço bizarro é esse?",
    31853: "Bizarro nada...CRÉ o Modulador de Febre, pra emendarCRum acerto crítico atrás do outro!",
    31854: "Emendar críticos?CRParece ótimo, mas não é perigoso?",
    31855: "Parece que força o corpoCRalém do limite... Deve fazer mal!",
    31856: "Relaxa!CRNão é nada perigoso assim.",
    31857: "Mas é vantajoso demais.CRQuando a esmola é muita, o santo desconfia! Deve ter pegadinha aí!",
    31858: 'Tô desconfiada! Vamos chamarCRde "Impulsor Demoníaco"!',
    31859: "Já falei que não tem nada!CRAi, ai, viu...",
    31860: "Pronto, terminei!CRCoisas miúdas dão um trabalhão.",
    31861: "Bom trabalho!CRAfinal, o que essa pecinha faz?",
    31862: "Só impede de cair no sono.CRNada de outro mundo, eu acho.",
    31863: "Item que corta veneno letal:CRo Anel Verde!",
    31864: "...O visual desse anel tá comCRuma cara supervenenosa.",
    31865: "O design parece de anelCRde veneno puro, fala sério!",
    31866: "Eu também acho, mas se eleCRte protege de veneno, dá praCRrelevar o visual, não dá?",
    31867: "Será que ele solta outro venenoCRpra anular o efeito na hora?",
    31868: "Já falei que o anel não temCRveneno nenhum nele!"
}

for did, txt in f0505.items():
    ob = c.execute('SELECT original_bytes FROM dialogues WHERE id = ?', (did,)).fetchone()[0]
    sz = encoded_size(txt)
    status = "OK" if sz <= ob else f"OVERFLOW (+{sz - ob})"
    print(f"ID {did}: {sz}/{ob} bytes -> {status}")
