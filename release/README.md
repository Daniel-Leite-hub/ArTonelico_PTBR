# Ar tonelico PT-BR Studio

## Correção das mensagens de itens — 08/10/2026

O EXE preserva os códigos ASCII `%s` e `%d` nos formatos de obtenção de itens e dinheiro. ISO de teste com essa correção: `iso/ArTonelico_PTBR_mensagens_itens_20261008.iso`. A ISO `EVD_corrigido` continua preservada como versão anterior aprovada. 80 testes passaram; testar obtenção de item, quantidade e dinheiro no jogo. O banco e suas traduções não foram editados nesta correção.

## Entrega atual — 08/10/2026

Aplicativo: `ArTonelico_PTBR_Studio.exe`. Banco revisado: `ArTonelico_PTBR_adaptado_108_20260926.atproj`. ISO confirmada pelo usuário no trecho antes travado: `iso/ArTonelico_PTBR_EVD_corrigido_20261008.iso`, junto dos relatórios. A correção estrutural EVD vale para todos os eventos; o prólogo também aceita realocação e expansão. 32.641 traduções, 36 vídeos, zero fallback e 79 testes passaram.

Mantenha `videos_ptbr` ao lado do projeto. Os EXEs antigos foram excluídos, exceto o backup anterior à correção EVD em `historico/executaveis`. Os bancos e backups editoriais foram preservados. O histórico abaixo pode citar caminhos e restrições já substituídos.

## Correção de geração — 06/10/2026

EXE atualizado para preservar a aspa curva esquerda usada nas falas revisadas. A fonte portuguesa usa outro slot confirmado livre, mantendo a proteção contra colisões. Corrige o erro “Entrada da fonte 268 ainda usada no catálogo”. O EXE anterior está em `historico/executaveis/ArTonelico_PTBR_Studio_antes_slot268_20261006.exe`. 76 testes passaram; ISO revisada gerada em `../isos_teste/ArTonelico_PTBR_revisado_20261006.iso`, com 32.641 textos conferidos, 36 vídeos aplicados e zero fallback por capacidade. Teste no PCSX2 ainda necessário.

## Projeto atual — 03/10/2026

Abra `ArTonelico_PTBR_Studio.exe` e selecione **`ArTonelico_PTBR_adaptado_108_20260926.atproj`**: este contém a revisão editorial integral. O banco `ArTonelico_PTBR.atproj` é uma base anterior usada por scripts históricos; não confundir com o revisado. `videos_ptbr` precisa permanecer nesta pasta para aplicação dos 36 vídeos traduzidos.

Versões anteriores do EXE estão em `historico/executaveis`; documentação antiga, em `historico/documentacao`. Backups de projetos permanecem em `backups` para preservar os caminhos da trilha editorial. A limpeza não alterou o EXE atual, o banco revisado ou os vídeos. O histórico abaixo descreve etapas anteriores: não é comprovação de teste da curadoria mais recente no emulador.

## Atualização de 26/09/2026

A geração agora usa a fonte nativa portuguesa nos itens e menus, conforme o teste aprovado no jogo. O EXE anterior foi preservado como `ArTonelico_PTBR_Studio_antes_fonte_nativa.exe`.

Ao gerar a ISO, uma pergunta permite ativar **realocação experimental dos diálogos**. Ela reconstrói RPK.BIN em ordem, atualiza os setores no índice do executável e realoca o pacote para o final da ISO, atualizando o diretório ISO9660. Textos EVD maiores podem ser mantidos sem sobrescrever recursos vizinhos. Os arquivos não editados são conferidos byte a byte. A ISO aumenta de tamanho; a caixa visual e os limites de memória do jogo não aumentam. Esta expansão ainda requer teste no emulador.

`Event/1.evd` (prólogo) conserva o layout fixo já exigido pelo jogo. Nomes e outros textos fixos do executável ainda não são realocados: automáticos que não cabem usam o original; revisões grandes demais produzem aviso. Não escolher a expansão mantém os limites anteriores. O modo de fonte nativa é usado nas duas opções.

Ferramenta Windows para extrair, traduzir, revisar e reinserir os diálogos de **Ar tonelico: Melody of Elemia** (SLUS-214.45).

## O que foi localizado

- A ISO contém o executável `SLUS_214.45` e o arquivo principal `RPK.BIN`.
- O índice do RPK fica embutido no executável; foram catalogados 2.703 recursos.
- Os diálogos ficam em 976 arquivos `Event/*.evd`.
- A extração desta ISO produziu 20.304 entradas. Todos os EVDs passaram em reconstrução byte a byte sem alterações.
- O texto usa caracteres latinos de largura dupla codificados em Shift-JIS/CP932.

## Uso

1. Abra `ArTonelico_PTBR_Studio.exe`.
2. Clique em **Nova a partir da ISO** e selecione a imagem original.
3. Salve o projeto `.atproj`. Esse arquivo SQLite guarda cada lote traduzido imediatamente e permite continuar depois.
4. Configure Azure ou DeepL, confira a estimativa de consumo e clique em **Traduzir pendentes** para as falas. Itens, menus, habilidades, locais e textos de referência do executável ficam na trilha de localização manual e não são enviados à API.
5. Revise primeiro as linhas marcadas como `ERRO`; linhas `ACIMA` foram preservadas, mas ultrapassam o limite conservador da frase inglesa e precisam de teste visual ou redução.
6. Preencha o campo **Texto final revisado** e use **Marcar como revisado** quando concluir a revisão. Até lá, a geração usa a resposta automática válida, se houver.
7. Clique em **Gerar ISO (revisados + automáticos)**. A ferramenta escolhe o texto final aprovado, depois a resposta automática válida, e por último o original. Edições e rascunhos sem aprovação não substituem essa escolha. A ISO original nunca é sobrescrita.

O editor separa: texto original em inglês, base automática/localizada, tradução em edição, situação técnica, texto final e estado da revisão. O campo `provider` identifica se a base veio da API ou da curadoria local; nenhuma curadoria é marcada como revisão humana aprovada. A resposta do provedor nunca é perdida quando a tradução é editada. Linhas iniciadas por `#` são comandos/Hymmnos e ficam protegidas contra tradução automática.

Alterar o texto final depois da aprovação muda seu estado para **revisão pendente**. O programa salva a edição progressivamente, mas exige uma nova ação **Marcar como revisado** antes de aplicá-la. Revisões existentes de projetos anteriores são migradas como aprovações legadas e o banco é copiado para `backups/<projeto>/` antes da migração.

## Painel de progresso

A lateral direita acompanha o projeto inteiro e é atualizada ao abrir, filtrar, salvar ou traduzir um lote:

- barra e percentual de textos finais explicitamente aprovados entre as linhas editáveis;
- total traduzido, corretos, acima dos bytes, com erro, pendentes e protegidos, com cores distintas;
- quantidade exibida pelo filtro e total existente no projeto;
- filtros separados para tamanho certo e tamanho errado;
- contador de bytes da linha atualizado durante a digitação, antes de salvar.

`Corretos + Acima dos bytes + Com erro + Pendentes` sempre corresponde ao total de linhas editáveis. A barra considera apenas textos finais aprovados; rascunhos preenchidos aparecem separadamente em **Revisão pendente**.

Textos acima dos bytes originais não são descartados nem classificados como falha. O jogo pode aceitar frases maiores, como confirmado nos testes em emulador; o aplicativo mantém a advertência e valida a capacidade real do EVD ao gerar a ISO.

## Azure e DeepL

O Azure usa lotes curtos, limite padrão de 30.000 caracteres/minuto (editável) e distribuição uniforme da cota. A documentação oficial permite até 50.000 caracteres e 1.000 itens por solicitação; o nível F0 deve consumir aproximadamente 33.300 caracteres/minuto de forma uniforme. Consulte [limites do Azure Translator](https://learn.microsoft.com/en-us/azure/ai-services/translator/service-limits).

O DeepL usa requisições JSON abaixo de 128 KiB, pausa mínima entre lotes e repetição exponencial com jitter para HTTP 429 e 5xx. O resultado de cada lote é armazenado antes do próximo. Consulte [limites do DeepL](https://developers.deepl.com/docs/resources/usage-limits) e [tratamento de erros](https://developers.deepl.com/docs/best-practices/error-handling).

Antes do envio ao Azure ou DeepL, o programa une as quebras visuais do roteiro em um único espaço. Isso inclui o formato com uma barra invertida no fim da linha. A API recebe a frase completa e contínua, enquanto o texto original guardado no projeto permanece inalterado. Comandos literais do jogo, como `\\n`, continuam protegidos. O DeepL também recebe `split_sentences=nonewlines` para impedir que quebras residuais sejam interpretadas como parágrafos separados.

No DeepL, cada lote pertence a um único `Event/*.evd` e recebe o parâmetro nativo `context`. O contexto contém uma descrição factual curta de Ar tonelico, o arquivo da cena, IDs dos falantes e todas as falas inglesas disponíveis naquele evento, limitado por padrão a 8.000 caracteres. Ele serve para resolver ambiguidades e continuidade entre falas; não é usado como prompt de instruções. O corpo JSON completo é recusado antes do envio se alcançar 128 KiB. O limite de contexto pode ser ajustado na configuração da sessão.

Ao abrir um projeto, o programa cria ao lado dele um arquivo `*.glossario.csv`, com as colunas `original,traducao` e termos próprios de Ar tonelico. Na configuração do Azure é possível selecionar outro glossário e informar uma categoria personalizada. Termos do glossário e comandos como `#0`, `#1` e códigos hexadecimais são protegidos durante a requisição; a tradução é rejeitada se a API remover ou duplicar um marcador.

Antes de iniciar uma tradução automática, uma cópia consistente do banco é gravada em `backups/<projeto>/`. Cada lote bem-sucedido salva separadamente a resposta original do provedor e a cópia editável, portanto **Parar** conserva todo o trabalho concluído. As chaves existem somente na memória da sessão e não são gravadas no projeto, relatórios ou executável.

## Planilha e relatórios

O botão **Exportar CSV/relatórios** cria uma central de revisão compatível com o fluxo dos projetos mais recentes:

- `Traducao_PTBR.csv`: planilha mestre UTF-8 com original, resposta automática, edição, situação, texto final, aprovação, origem, bytes, provedor e erro;
- `relatorio_revisao.json`: somente textos finais explicitamente aprovados;
- `relatorio_revisoes_pendentes.json`: textos finais preenchidos que ainda exigem aprovação;
- `relatorio_bytes_excedentes.json`: linhas acima do limite conservador e quantidade excedente;
- `manifesto_fonte_portugues.json`: biblioteca de acentos e aliases usados nesta versão.

O editor salva a linha aberta ao fechar o programa, impede duas operações pesadas simultâneas e destaca visualmente textos corretos, excedentes e erros reais.

O botão **Importar CSV** localiza cada registro por arquivo e ID estáveis, cria backup antes de alterar o projeto e nunca substitui a resposta original da API. Traduções e textos finais são importados; uma aprovação exportada só é restaurada quando seu estado e hash ainda correspondem ao texto. Caso contrário, a linha volta como revisão pendente.

## Geração verificável

A geração centraliza a prioridade: **revisado aprovado → resposta automática válida → original**. Respostas automáticas com caracteres não codificáveis ou comandos do jogo alterados são ignoradas; a tradução em edição e o rascunho final não são aplicados. Antes da geração há outro backup do projeto. A ferramenta confere o tamanho e o hash do executável da ISO-base quando esses dados existem no projeto, valida a capacidade real de cada EVD, preserva o tamanho total da imagem, reabre todos os EVDs modificados e compara os bytes gravados com cada texto selecionado. Ao terminar, informa quantos textos vieram de revisão, automática e original, além do SHA-256 da ISO produzida.

Se um EVD ultrapassar seus setores reservados, a ferramenta não corta nem corrompe o texto. Revisões aprovadas continuam obrigatórias; entre as respostas automáticas ainda não revisadas, ela retorna ao inglês apenas as falas que economizam mais bytes, no menor número necessário para o arquivo caber. A conclusão informa a quantidade desses fallbacks e grava, ao lado da ISO, um arquivo `.capacity_fallbacks.json` com as falas que precisam ser encurtadas ou revisadas. Se nem isso for suficiente, a geração para e pede a redução de uma revisão aprovada.

O prólogo `Event/1.evd`, carregado somente ao começar uma partida nova, possui layout fixo por registro. O gerador mantém o tamanho original de cada fala, o campo de comprimento e a posição de todos os cabeçalhos internos. Traduções automáticas que não cabem no espaço da própria fala voltam ao inglês e são marcadas como `startup_fixed_record`. Revisões aprovadas nunca são removidas: o programa pede que sejam encurtadas quando ultrapassam o espaço original.

As 117 traduções originalmente maiores do prólogo foram adaptadas para PT-BR conciso. As 181 linhas traduzidas agora cabem nos respectivos registros sem fallback no `Event/1.evd`. O utilitário reproduzível `tools/adapt_event1_portuguese.py` valida os bytes antes de atualizar os projetos e cria backups datados.

Além dos 20.304 registros extraídos de `Event/*.evd`, o Studio detecta 12.549 textos full-width incorporados diretamente em `SLUS_214.45`. Eles aparecem em grupos `SLUS/TEXT/####`, com contexto local de até 24 falas para o DeepL. A reinserção é feita no próprio offset e nunca desloca o executável. O limite de cada string inclui agora o preenchimento zero contíguo até o próximo dado, limitado a 15 bytes extras; somente bytes comprovadamente vazios são reutilizados. Traduções automáticas ainda maiores voltam ao original (`executable_slot`) e revisões aprovadas maiores exigem que o usuário encurte o texto.

O banco do executável agora possui trilhas explícitas: 27.705 falas continuam na fila do DeepL/Azure, enquanto 5.148 entradas de interface, catálogo e referência não são enviadas. A curadoria PT-BR registra 2.995 rótulos: 2.238 cabem nos slots e 757 traduções maiores permanecem visíveis como `Acima dos bytes`, sem serem aplicadas à ISO até sua adaptação. Outros 126 identificadores técnicos curtos e bloqueados ficam registrados como `identificador_tecnico`: o editor mostra que foram mantidos de propósito, mas eles continuam protegidos contra reinserção. Não resta nenhuma entrada desbloqueada de até três palavras vazia na trilha manual; 2.031 textos maiores ainda aguardam localização. Termos mantidos intencionalmente, como `Leaf`, `DP`, `HP`, `MP`, `Lyner`, `Syn-C`, nomes próprios e códigos de modelos, recebem proveniência explícita e deixam de parecer pendências. Para reaplicar a curadoria aos projetos existentes: `python tools/localize_catalog.py ArTonelico_PTBR.atproj release/ArTonelico_PTBR.atproj` (o comando cria backup antes de alterar cada banco).

A busca direta divide trechos colados/OCR em palavras e ignora temporariamente o filtro de situação, evitando que descrições existentes fiquem ocultas em outra categoria. Correções confirmadas por captura ou teste dentro do jogo ficam reproduzíveis em `tools/apply_reported_corrections.py`; elas continuam como base automática, sem aprovação humana implícita. O nome de inventário `Dragon Fillet` usa `Filé dragão` (25 bytes), dentro dos 27 bytes do conteúdo original, sem consumir a folga de alinhamento do registro.

Itens, descrições e opções de menu usam um renderizador diferente das caixas de diálogo. O escape de fonte `#1` desenhava acentos com métricas incompatíveis nessas telas e provocava travamento ao selecionar itens. O banco continua guardando `Filé dragão`, `Lenço`, `Remédio` e demais traduções editoriais com acentos, mas o gerador translitera somente a saída binária da trilha `localization` e dos grupos de tópicos `SLUS/TEXT/0339` e `0341`. Assim, esses campos não contêm `#1`; diálogos continuam usando a biblioteca portuguesa acentuada.

Os arquivos [COBERTURA.md](COBERTURA.md) e [CONTINUIDADE.md](CONTINUIDADE.md) registram o alcance real, decisões, evidências e pendências sem confundir catálogo de diálogos com localização completa do jogo.

## Acentos PT-BR

O CP932 original não representa os diacríticos portugueses. A geração da ISO agora inclui uma extensão do atlas latino `FO_HGGBP.tm2` quando algum texto final revisado contém acentos.

- Biblioteca: `á à â ã é ê í ó ô õ ú ü ç`, as respectivas maiúsculas, `ª` e `º`.
- Cada trecho consecutivo de acentos recebe imediatamente antes dele o marcador interno `#1`, que ativa o atlas latino para os aliases de um byte. Um caractere Shift-JIS de dois bytes cancela esse modo; por isso um único marcador no começo da frase não é suficiente. Sem o marcador local, os pares ficam desalinhados e aparecem blocos/símbolos no jogo.
- Cada glifo usa um alias de um byte no atlas latino; as demais letras continuam em Shift-JIS de largura dupla. Os limites de desenho vêm das coordenadas UV usadas pelo executável, evitando corte ou deslocamento dos acentos.
- A posição vertical de cada glifo acentuado acompanha a linha-base da letra equivalente sem acento; o acento e a cedilha são mantidos dentro da célula do atlas.
- Os aliases são escolhidos pela largura de avanço: variantes da mesma vogal usam células equivalentes, e `í/Í` usam células estreitas. Isso evita espaços irregulares ao redor dos caracteres substituídos.
- O cálculo de tamanho usa os bytes realmente gravados: cada acento ocupa um byte e cada trecho consecutivo de acentos usa um marcador de dois bytes.
- Textos Hymmnos iniciados por `#0` usam outro modo de fonte e permanecem protegidos.
- A fonte é recomprimida em LZR e validada contra o espaço de 6.144 bytes reservado no `fpack/font.fp`.

A alteração é específica para a edição americana `SLUS-214.45` desta ISO Undub. Faça o primeiro teste em emulador e mantenha a ISO original intacta.

## Organização do projeto

- `Ar tonelico - Melody of Elemia (Undub).iso`: imagem-base original, nunca sobrescrita;
- `ArTonelico_PTBR.atproj` e `ArTonelico_PTBR.glossario.csv`: catálogo de trabalho e glossário ativos;
- `artonelico_tool/`, `main.py` e `tests/`: código-fonte e testes automatizados;
- `tools/`: utilitários de análise; ferramentas externas de referência ficam em `tools/vendor/`;
- `work/`: arquivos técnicos usados pelos testes e pela engenharia reversa;
- `release/`: somente o EXE, projeto portátil, glossário e documentação atuais;
- `backups/`: marcos recuperáveis do banco de tradução;
- `testes pt br/`: relatório e prévia visual mais recentes.

As pastas `build/`, `dist/`, caches Python e saídas intermediárias não fazem parte do projeto permanente. Elas são recriadas quando o EXE ou os testes são executados.

## Limites e cópias de segurança

- A reinserção mantém todos os LBAs e o tamanho da ISO. Cada EVD precisa caber nos setores já reservados.
- O indicador por linha é conservador: compara os bytes da tradução aos bytes da linha inglesa original. A geração também valida a capacidade real de cada arquivo EVD.
- Guarde a ISO original. A saída deve usar outro nome.
- Textos desenhados diretamente em imagens e legendas dentro de vídeos SFD não fazem parte dos 976 EVDs.
# Vídeos PT-BR — atualização de 26/09/2026

O EXE inclui automaticamente os 36 vídeos do pacote `videos_ptbr` ao gerar a ISO. Mantenha essa pasta junto do arquivo `.atproj`; não copie somente o EXE. Os SFD já estão renderizados com Trebuchet e fundo de 65%, e não precisam de FFmpeg para inserção. Arquivos incompletos, alterados ou incompatíveis com a ISO-base bloqueiam a geração. A mensagem final informa quantos vídeos foram aplicados e o relatório `.movies.json` confere cada arquivo reaberto.

A abertura foi testada pelo usuário. O lote restante passou pela validação técnica, mas precisa de testes nas respectivas cenas do PCSX2. Originais e EXE anterior foram preservados.
