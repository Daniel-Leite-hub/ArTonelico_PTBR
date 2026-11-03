"""Export a curated AT1 terminology base; never modify either game's database."""
from pathlib import Path
import csv
import hashlib
import json
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / 'release/ArTonelico_PTBR_adaptado_108_20260926.atproj'
OUT = ROOT / 'release/glossario_franquia'

# source | preferred | category | reuse | automatic | editorial note
# Full forms deliberately replace abbreviations constrained by AT1's slots.
DATA = '''Ar tonelico|Ar tonelico|Nome próprio|Compartilhado|sim|Preservar grafia e espaço; tonelico em minúscula.
Lyner|Lyner|Personagem|Referência ao primeiro jogo|sim|Manter nome; não inferir presença no segundo jogo.
Aurica|Aurica|Personagem|Referência ao primeiro jogo|sim|Manter nome.
Misha|Misha|Personagem|Referência ao primeiro jogo|sim|Manter nome.
Shurelia|Shurelia|Personagem|Compartilhado quando citada|sim|Manter nome; concordância feminina quando a referência for Shurelia.
Mir|Mir|Personagem|Compartilhado quando citada|não|Nome curto: conferir contexto antes de substituição automática.
Krusche|Krusche|Personagem|Referência ao primeiro jogo|sim|Manter nome.
Jack|Jack|Personagem|Referência ao primeiro jogo|não|Nome próprio ou palavra inglesa comum; conferir contexto.
Radolf|Radolf|Personagem|Referência ao primeiro jogo|sim|Manter nome.
Reyvateil|Reyvateil|Universo|Compartilhado|sim|Manter termo; a Reyvateil quando se referir às personagens femininas. Plural Reyvateils.
Reyvateils|Reyvateils|Universo|Compartilhado|sim|Preservar plural; concordar com as personagens de fato citadas.
Cosmosphere|Cosmosfera|Universo|Compartilhado|sim|Nome do espaço mental; feminino. Evitar cosmoesfera.
Dive|Mergulho / mergulhar|Sistema|Conferir função gramatical|não|Mergulho como substantivo; mergulhar como verbo. Merg. e Mergul. eram abreviações de interface.
Diving|mergulho / mergulhar|Sistema|Conferir função gramatical|não|Flexionar conforme a frase; não trocar mecanicamente gerúndio por substantivo.
Dive Points|Pontos de Mergulho|Sistema|Compartilhado|sim|Manter DP no HUD; explicar o nome completo na primeira apresentação pertinente.
DP|DP|Sigla|Compartilhado|não|Pontos de Mergulho. Não expandir em cada rótulo.
Song Magic|Magia da Canção|Sistema|Compartilhado|sim|Forma de referência sugerida a partir dos dois rótulos finais exatos; há Magia de Canção em dados antigos.
Red Magic|Magia Vermelha|Sistema|Conferir mecânica no segundo jogo|não|Cor de categoria; não atribuir efeitos sem conferir o tutorial do jogo II.
Blue Magic|Magia Azul|Sistema|Conferir mecânica no segundo jogo|não|Manter distinção das categorias; gênero feminino de magia.
Green Magic|Magia Verde|Sistema|Conferir mecânica no segundo jogo|não|Só aplicar quando a categoria existir; não criar equivalência com sistemas novos.
Hymn Crystal|Cristal Hymmnos|Universo|Compartilhado; padronização proposta|não|Rótulo de referência do AT1; também há Cristal do Hino nas falas. Resolver a equivalência no contexto do AT2 antes de automatizar.
Hymn Code|Código Hymmnos|Universo|Compartilhado|sim|Código de identificação; não confundir com o texto de uma canção.
Hymns|Hinos|Universo|Conferir contexto|não|Pode indicar canções/hinos; não substituir por Hymmnos em toda ocorrência.
Hymmnos|Hymmnos|Idioma / universo|Compartilhado; diretriz editorial|sim|Preservar grafia. Não traduzir a língua construída nem títulos/códigos executáveis como palavras inglesas.
Grathnode|Grathnode|Universo|Compartilhado|sim|Manter o nome tecnológico; não atribuir gênero isoladamente sem o substantivo.
Grathnode Crystal|Cristal Grathnode|Item / sistema|Compartilhado|sim|Plural Cristais Grathnode; não transformar em Cristal Hymmnos.
Grathnode Ring|Anel Grathnode|Item|Se houver o mesmo item|sim|Manter a distinção entre anel e cristal.
Recrystallization|Recristalização|Sistema|Se houver a mesma mecânica|sim|Não confundir com síntese de itens.
Install|Instalar / instalação|Sistema|Conferir função gramatical|não|Instalar em comando; instalação como operação. Não é instalação de software em toda fala.
Installer Port|Porta de instalação|Universo|Compartilhado|sim|Termo corporal/técnico; não trocar por porto ou portão. Localização anatômica depende da personagem.
Harmonics|Harmonics|Sistema|Conferir mecânica no segundo jogo|não|Nome mantido no AT1; não traduzir todo harmonics genérico nem equiparar a sistemas novos.
Burst|Burst|Sistema|Conferir contexto|não|Mantido no gráfico do AT1; em nomes de golpes foi localizado pelo efeito. Evitar regra global.
Syn-C|Syn-C|Sistema|Conferir mecânica no segundo jogo|não|Código/rótulo mantido; não inventar expansão.
Synthesis|Síntese|Sistema|Compartilhado quando a operação for a mesma|não|Sintetizar como verbo; conferir se o texto fala de fabricar, combinar ou melhorar.
Leaf|Leaf|Moeda / rótulo|Conferir moeda no segundo jogo|não|Manter no AT1. Não substituir toda ocorrência de leaf: em materiais pode ser folha.
Cole|Cole|Moeda / formato|Conferir moeda no segundo jogo|não|Preservado no formato Obtained %d Cole. Não uniformizar com Leaf sem conferir a moeda real.
Purger|Purificador|Item de história|Referência ao primeiro jogo|não|Forma de catálogo; há falas com Purger preservado. Só usar quando for o mesmo objeto.
Linker|Linker|Nome de cristal / equipamento|Referência ao primeiro jogo|não|Nome próprio mantido; não traduzir por vinculador automaticamente.
Holy Maiden|Donzela Sagrada|Título|Conferir instituição no segundo jogo|não|Título da Igreja de Elemia no contexto do AT1; não importar para funções diferentes.
Elemia Church|Igreja de Elemia|Instituição|Referência ao primeiro jogo|sim|Não equiparar automaticamente às instituições de Metafalica.
Knights of Elemia|Cavaleiros de Elemia|Instituição|Referência ao primeiro jogo|sim|Preservar o nome da organização.
Research Division|Divisão de Pesquisa|Instituição|Conferir organização|não|Aplicar a uma divisão efetivamente identificada; não inventar vínculo institucional.
Tower Administrator|Administradora da Torre / Administrador da Torre|Cargo|Conferir pessoa|não|No AT1 o rótulo é feminino; o gênero deve seguir quem ocupa o cargo em cada cena.
Tower|Torre|Cenário|Conferir referente|não|Maiúscula ao nomear a estrutura específica; minúscula em torre genérica.
Lower World|Mundo Inferior|Cenário|Referência geográfica a conferir|não|Localização do AT1; não pressupor equivalência com regiões do segundo jogo.
Upper World|Mundo Superior|Cenário|Referência geográfica a conferir|não|Manter oposição espacial quando for o mesmo conceito.
Teru Tribe|Tribo Teru|Povo|Compartilhado quando citado|sim|Teru permanece nome próprio; não inventar características do povo.
Tenba|Tenba|Instituição|Referência ao primeiro jogo|sim|Manter nome.
Platina|Platina|Local|Referência ao primeiro jogo|sim|Nome da cidade; não tratar como material metálico.
Nemo|Nemo|Local|Referência ao primeiro jogo|não|Nome curto; conferir se identifica o lugar.
Firefly Alley|Beco Vagalume|Local|Referência ao primeiro jogo|sim|Nome estabelecido no catálogo final; não alternar com Beco dos Vagalumes sem decisão explícita.
Seagull Port|Porto Gaivota|Local|Referência ao primeiro jogo|sim|Forma dos rótulos finais; existem falas com Porto Seagull. Padronização de continuidade sugerida, não uniformidade já provada.
Moonlight District|Distrito do Luar|Local|Referência ao primeiro jogo|sim|Preservar a unidade geográfica.
Silver Horn|Silver Horn|Local / nome próprio|Referência ao primeiro jogo|sim|Mantido no catálogo; não traduzir por Chifre de Prata automaticamente.
Blastline|Blastline|Local / termo próprio|Referência ao primeiro jogo|não|Mantido no catálogo; conferir se é o nome ou um uso descritivo.
Mind Guardian|Guardião mental|Universo|Conferir entidade/personagem|não|A referência de catálogo é masculina; ajustar se o sujeito identificado exigir.
Weapon|Arma|Interface|Compartilhado|não|Nome da categoria; usar arma equipada conforme a construção.
Armor|Armadura|Interface|Compartilhado|não|Categoria de equipamento; não confundir com defesa.
Accessory|Acessório|Interface|Compartilhado|não|Plural acessórios.
Equipment|Equipamento|Interface|Compartilhado|não|Equipamento como categoria; equipar como ação.
Costume|Traje|Interface|Compartilhado|não|Não tratar toda roupa citada em diálogo como nome de categoria.
Recipe|Receita|Interface|Compartilhado|não|Receita de síntese/fabricação; conservar ingrediente e quantidade.
Quality|Qualidade|Interface|Compartilhado|não|Distinguir de Quantity/Quantidade.
Quantity|Quantidade|Interface|Compartilhado; diretriz editorial|não|Distinguir de Quality/Qualidade; conferir a ordem dos valores do sistema.
Amount Made|Quantidade criada|Interface|Se o contador tiver a mesma função|não|Não confundir com estoque ou quantidade a criar.
Selling Price|Preço de venda|Interface|Compartilhado|não|Preço de venda, não de compra.
Stock|Estoque|Interface|Compartilhado|não|Conferir se é estoque da loja ou quantidade do jogador.
Attack|Ataque|Combate|Conferir substantivo/verbo|não|Ataque como atributo; atacar como comando quando adequado.
Defense|Defesa|Combate|Compartilhado|não|Distinguir atributo de ação defender.
Agility|Agilidade|Combate|Compartilhado|não|Não converter automaticamente speed em agilidade sem conferir os atributos.
Healing|Cura|Combate|Conferir construção|não|Cura como efeito; curar como verbo; curativo como adjetivo.
Paralysis|Paralisia|Estado|Compartilhado|não|Paralisado/paralisada conforme alvo; não confundir com atordoamento.
HP|HP|Sigla|Compartilhado|não|Manter na interface; explicar pontos de vida apenas quando necessário.
MP|MP|Sigla|Compartilhado|não|Manter na interface; conferir o recurso descrito no tutorial.
Save|Salvar|Interface|Conferir ação|não|Salvar para arquivo; não aplicar cegamente a save someone em diálogo.
Load|Carregar|Interface|Conferir ação|não|Carregar jogo/arquivo; outras acepções exigem contexto.
Flee|Fugir|Interface|Compartilhado|não|Manter o sentido de fuga, sem inventar sucesso garantido.
Current Objective|Objetivo atual|Interface|Compartilhado|sim|A frase do objetivo mantém tempo e agente do original.
Return to Reality|Voltar à realidade|Sistema|Se for a saída do espaço mental|sim|Não alterar para despertar se o evento não afirmar isso.
Use Effect|Efeito ao usar|Interface|Compartilhado|sim|Distinguir efeito de uso e efeito de equipamento.
Dragon Fillet|Filé de dragão|Item|Se houver o mesmo item; forma completa proposta|não|No catálogo AT1: Filé dragão por espaço. Usar forma completa no AT2 se couber; não interpretar dragão como espécie sem contexto adicional.
Handkerchief|Lenço|Item|Se houver o mesmo item|não|Não usar lença; gênero masculino.
Strong Medicine|Remédio forte|Item|Se houver o mesmo item|não|Rótulo final do AT1; não confundir com outro remédio chamado potente.
Airship|dirigível / aeronave|Cenário|Conferir veículo|não|Há dirigíveis nas falas do AT1; escolher pela representação do veículo, não por substituição global.
Church|Igreja|Instituição / cenário|Conferir referente|não|Maiúscula quando for a instituição específica; minúscula para edifício genérico.
Hymn|Hino|Universo / canção|Conferir contexto|não|Hino como canção; não equivale automaticamente a cristal, código ou idioma Hymmnos.
Grathnode Recrystallization|Recristalização de Grathnode|Sistema|Se houver a mesma mecânica; forma completa proposta|não|Rótulo curto do AT1 omite o complemento; não substituir por instalação ou síntese.
'''


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(PROJECT.resolve().as_uri() + '?mode=ro', uri=True)
    db.row_factory = sqlite3.Row
    all_rows = db.execute('SELECT id,event_file,entry_index,original,automatic,reviewed,review_status FROM dialogues').fetchall()
    entries = []
    for line in DATA.splitlines():
        if not line:
            continue
        source, target, category, reuse, automatic, note = line.split('|')
        exact = [r for r in all_rows if r['original'].strip() == source]
        contextual = exact or [r for r in all_rows if source.casefold() in r['original'].casefold()][:5]
        evidence = []
        for row in contextual[:5]:
            evidence.append(dict(row))
        entries.append(dict(original=source, traducao=target, categoria=category,
                            reutilizacao=reuse, importar_automaticamente=automatic,
                            nota=note, evidencias=evidence,
                            base='rótulo exato AT1' if exact else 'contexto AT1' if contextual else 'diretriz editorial'))
    db.close()
    assert len({e['original'] for e in entries}) == len(entries)
    with (OUT / 'Glossario_curadoria_AT2.csv').open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['original','traducao','categoria','reutilizacao','importar_automaticamente','nota','base','ids_evidencia_at1'])
        for entry in entries:
            writer.writerow([entry[k] for k in ('original','traducao','categoria','reutilizacao','importar_automaticamente','nota','base')] + [','.join(str(r['id']) for r in entry['evidencias'])])
    automatic = [e for e in entries if e['importar_automaticamente'] == 'sim']
    with (OUT / 'Glossario_importacao_EN_PT.csv').open('w', encoding='utf-8', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['original','traducao'])
        writer.writerows((e['original'],e['traducao']) for e in automatic)
    with PROJECT.open('rb') as stream:
        project_hash = hashlib.file_digest(stream, 'sha256').hexdigest()
    evidence = dict(data='2026-10-09', projeto_fonte=str(PROJECT), sha256_projeto=project_hash,
                    total_termos=len(entries), termos_importacao=len(automatic),
                    escopo='Base editorial do AT1; não revisa nem altera o catálogo do AT2.',
                    entries=entries)
    (OUT / 'Evidencias_AT1.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding='utf8')
    table = ['| Inglês | Referência PT-BR | Uso e cuidados |', '|---|---|---|']
    for e in entries:
        table.append(f"| {e['original']} | {e['traducao']} | {e['nota']} |")
    (OUT / 'Glossario_consulta.md').write_text('# Glossário de continuidade — Ar tonelico I → II\n\n'
        'Referência para curadoria, baseada no projeto revisado do primeiro jogo. Formas propostas e escolhas dependentes de contexto estão identificadas na planilha completa; não são aprovações automáticas do segundo jogo.\n\n' + '\n'.join(table) + '\n', encoding='utf8')
    print(json.dumps({'terms':len(entries),'import_terms':len(automatic),'directory':str(OUT)}, ensure_ascii=True))


if __name__ == '__main__':
    build()
