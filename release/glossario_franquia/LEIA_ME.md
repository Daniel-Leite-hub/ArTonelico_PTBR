# Base de curadoria para Ar tonelico II

Esta base usa o banco revisado do primeiro jogo, não traduções lembradas de outros projetos. O catálogo do segundo jogo ainda precisa ser confrontado com ela: termos novos, instituições, mecânicas e personagens não devem ser preenchidos por suposição.

## Arquivos

- `Glossario_consulta.md`: leitura rápida dos termos e notas.
- `Glossario_curadoria_AT2.csv`: referência completa em UTF-8 com BOM, incluindo categoria, alcance, notas e IDs do primeiro jogo.
- `Glossario_importacao_EN_PT.csv`: subconjunto com duas colunas `original,traducao`, para ferramentas que aceitem esse formato. Não inclui formas com alternativas, termos ambíguos nem escolhas ainda pendentes. A compatibilidade de importação precisa ser conferida no Studio do segundo jogo; não é um glossário remoto DeepL já criado.
- `Evidencias_AT1.json`: trechos originais, traduções existentes, IDs e hash do banco usado. A evidência guarda o estado real de aprovação; curadoria anterior não é convertida em aprovação humana.

## Decisões de continuidade

**Cosmosfera**, **Pontos de Mergulho**, **Cristal Grathnode**, **Porta de instalação** e **Recristalização** são referências úteis. Manter Reyvateil, nomes próprios e siglas reconhecidas. Usar formas completas primeiro; abreviar só depois de medir a interface do segundo jogo. Não transportar limites de bytes nem códigos de fonte do AT1 para o AT2.

`Dive` precisa ser traduzido como **Mergulho** ou **mergulhar**, conforme sua função. `Install` pode ser **Instalar** ou **instalação**. `Tower Administrator` precisa concordar com a pessoa identificada na cena; o rótulo feminino do primeiro jogo não determina o gênero de todos os cargos da franquia.

Há divergências reais no AT1, conservadas na evidência:

- `Song Magic`: os dois rótulos finais são **Magia da Canção**; dados anteriores e algumas frases usam **Magia de Canção**. Recomenda-se a primeira como forma de referência para a nova curadoria.
- `Hymn Crystal`: o catálogo diz **Cristal Hymmnos**, e algumas falas dizem **Cristal do Hino**. A primeira é a referência proposta; confirmar que o segundo jogo se refere ao mesmo conceito antes de impor a escolha. **Hino**, **Hymmnos**, **Código Hymmnos** e **Cristal Hymmnos** não são intercambiáveis.
- `Purger`: há **Purificador** em rótulos e **Purger** em falas. É um objeto específico do primeiro jogo; conferir eventuais referências no segundo.
- `Seagull Port`: o catálogo final usa **Porto Gaivota**; há falas com **Porto Seagull**. Recomenda-se Porto Gaivota quando for o mesmo lugar.
- `Dragon Fillet`: o AT1 usa **Filé dragão** por espaço. A referência editorial completa é **Filé de dragão**, proposta para o segundo jogo se esse item existir e a interface permitir.
- `Leaf` e `Cole` aparecem no AT1. Não substituir um pelo outro nem presumir a moeda do AT2. `leaf` também pode ser folha em contexto comum.
- `Burst`, `Harmonics` e `Syn-C` têm usos técnicos no AT1. Não atribuir os mesmos efeitos aos sistemas do AT2 sem ler os tutoriais dele.

## Regras para revisar as falas do segundo jogo

1. Leia a fala com o original e o contexto da cena. Preserve humor, hesitação, informalidade, intenção e diferença entre vozes; não formalize todos os personagens.
2. Confira o agente e o destinatário antes de ajustar gênero, número e pronome. Identificador vizinho não prova quem fala. Quando faltar evidência, registre a dúvida.
3. Revise negação, tempos verbais e modalidade: **pode**, **deve**, **vai** e **já fez** não têm o mesmo sentido. Não acrescente certeza, obrigação ou sujeito que o original não fornece.
4. Diferencie atributo, comando e descrição. Ataque/atacar, cura/curar e equipamento/equipar dependem da função.
5. Preserve números, unidades, nomes de itens, qualificadores e condições. Em particular, não troque qualidade por quantidade, preço de venda por preço de compra nem cura por ressurreição.
6. Preserve marcadores, substituições e a ordem exigida pelo sistema. `%s`, `%d`, quebras e tags não são texto para traduzir; confirme o formato próprio do AT2. Não reutilize a codificação do primeiro jogo por analogia.
7. Maiúsculas indicam nomes/títulos definidos, não toda ocorrência de uma palavra do glossário. Plurais e preposições devem soar naturais em português brasileiro.
8. Primeiro produza a frase completa e fiel. A versão abreviada de interface deve ser separada da forma de referência; evite eliminar informação apenas por causa do limite original.
9. Nomes e títulos de canções em Hymmnos exigem identificação. Não traduzir a língua construída como se fosse inglês, nem inventar versões de nomes exclusivos do segundo jogo.

## Como ampliar

Acrescente os termos exclusivos do AT2 após lê-los no catálogo original e em suas cenas. Para cada termo novo, registre inglês, PT-BR, definição contextual, categoria, variantes, personagem/instituição, ID de origem, estado da decisão e exemplos. Uma decisão de curadoria deve indicar se é proposta, confirmada ou dependente de contexto.

Nenhum banco, tradução, EXE ou ISO foi alterado para montar estes arquivos.
