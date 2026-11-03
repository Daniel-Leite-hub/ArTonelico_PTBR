# Diagnóstico após falha de inicialização

## Atualização: extensão nativa sem injeção de código (2026-09-26)

Localizada a origem real da fonte: 405 bitmaps 24x24, 4 bits por pixel, no executável a partir de `0x548020`. A rotina `0x131704` resolve o par CP932 pela tabela `0x547CF0` e copia 288 bytes por glifo para o cache. Os pares E040–E05B não tinham entrada, causando leitura de glifo inválido.

O novo método substitui 28 entradas não utilizadas nos textos originais ou traduzidos do catálogo, seus bitmaps e suas medidas proporcionais em `0x490A0E + índice*2`. As letras minúsculas preservam o corpo nativo; maiúsculas com acento superior mantêm a linha de base, com corpo reduzido verticalmente para reservar espaço ao acento. Não há comandos de fonte nos nomes nem código novo.

ISO: `testes pt br/Ar tonelico PTBR fonte nativa dados apenas 20260926.iso`. SHA-256: `7e2acfaeffd5eee96ec37a2ecba465c86f2b47da123bcaa0fe96823ae12406f6`.

Validação: 36 testes; 24.954 textos reabertos; todos os 84 blocos de dados de fonte conferidos na ISO; todas as seções executáveis ELF idênticas ao original; tabela ativa anteriormente destruída preservada. A auditoria de colisões cobre o catálogo, não todos os caminhos possíveis do jogo. Ainda falta confirmação no emulador de boot, Novo Jogo e seleção repetida de Filé dragão, Lenço e Remédio potente. EXE padrão não promovido antes dessa confirmação. As seções abaixo descrevem o diagnóstico histórico, não o método atual.

## Evidências verificadas

- O payload mais recente tem 592 bytes e sobrescreve `SLUS_214.45:0x97BE30–0x97C07F`.
- A região original contém mensagens do SDK gráfico, não espaço livre.
- A partir de `0x97C030`, contém uma tabela de destinos (`0x33FC8C`, `0x33FC98`, `0x33FCAC`, `0x33FCCC` etc.).
- A rotina em `0x33FC70` carrega o endereço virtual dessa tabela (`0xA7B030`), lê um destino em `0x33FC80` e faz `jr a0` em `0x33FC84`. A tabela destruída é usada como código de controle, não apenas como texto diagnóstico.
- O acessor `0x2D8C88` admite retorno zero; o wrapper não verificava esse retorno antes de ler memória.
- As funções originais usam salvamento de registradores de 64 bits (`sd/ld`) e o ELF declara `.mdebug.eabi64`; a justificativa anterior de ABI o32 não foi demonstrada e deve ser descartada.
- A captura de letras em blocos comprova falha visual, mas isoladamente não prova que um hook não foi executado. As afirmações anteriores sobre o caminho executado eram inferências sem trace.

## Fonte realmente selecionada

No estado salvo existente em `work/savestate_analysis/eeMemory.bin`, o descritor padrão em `0x40D770` aponta para a tabela de células em `0x40F6B0`. Cada registro tem 20 bytes: índice de textura, retângulo, medidas e campos de controle. O primeiro registro usa textura 12 e célula de 19x24 pixels. A tabela alternativa em `0x4102B8` usa textura 16 e células de 22 pixels de altura. Portanto, não se pode aplicar o atlas alternativo e suas métricas à fonte padrão presumindo que sejam equivalentes.

O mapeamento padrão em `0x58FB20` aponta para 405 pares CP932 em `0x646CF0`. Os pares `E040–E05B` não estão nessa lista. Uma implementação correta precisa definir tanto a resolução desses códigos quanto as células da textura padrão; substituir somente bitmaps no atlas alternativo não atende a isso.

## Estado e próximo requisito técnico

O injetor experimental está bloqueado antes de qualquer mutação. A ISO que não abre permanece como evidência; nenhuma nova ISO experimental foi produzida nesta investigação. O modo padrão do EXE continua disponível com transliteração dos menus.

A solução de acentos ainda não está concluída. É necessário localizar no pacote a textura de índice 12, identificar o caminho de fallback para códigos ausentes e criar um mapeamento para células portuguesas com as métricas originais. Qualquer rotina adicional deve ter área de código e dados demonstravelmente reservada, proteção de ponteiro nulo e preservação de registradores conforme o ABI real. Testes de arquivo não substituem boot e seleção no emulador.
