# Realocação conservadora de strings — 2026-09-26

## Estado mais recente: expansão parcial para os outros textos

Misha foi confirmada em jogo pelo usuário. O modo experimental agora reconhece sequências de pelo menos três registros adjacentes de conversa de 24 bytes, com opcode 2/3, metadados limitados e campo +20 contendo ponteiro catalogado. Exige todas as referências conhecidas elegíveis. Não presume que outros tipos de tabelas sejam iguais.

Também compacta runs estritamente contíguos de slots catalogados, todos sem referência interior/página LUI, somente quando todas as traduções completas cabem no bloco total. Nesses runs os textos originais são reorganizados; a regra anterior de conservar a origem refere-se ao modo de cópia em caudas, não à compactação. Nada atravessa gaps desconhecidos. Traduções completas exatamente iguais podem compartilhar um destino.

ISO v2 de bancos de conversa: 27.376 textos aplicados, 125 a mais que Misha, 524 registros reorganizados, 7 cópias compartilhadas. 48 testes passaram e auditoria estrutural passou. Ainda falta testar esta ampliação em jogo. 5.259 fallbacks continuam: 3.449 páginas LUI, 262 referências/layout não comprovados, 60 sem ponteiro direto, 1.488 sem capacidade elegível. Logo, aplicar a todos os pendentes ainda NÃO foi alcançado. Não encurtar nem declarar estes textos inseridos.

Artefato: `testes pt br/Ar tonelico PTBR bancos de conversa expandidos v2 20260926.iso`, SHA-256 `b2f4b4e88b400c019643ded6ad3e6fa860a41c097c6499515140234778c8e808`. Reproduzir/auditar com `python tools/build_expanded_conversation_iso.py`. EXE atualizado, anterior preservado com sufixo `_antes_bancos_20260926.exe`.

Esta variante é experimental: verificações estáticas não comprovam todos os endereços calculados em tempo de execução. Não substitui teste no emulador.

## Implementação

- Opção independente na geração da ISO. Desativada quando o usuário responde Não.
- Preserva tamanho, cabeçalhos e instruções do executável; não injeta código nem amplia heap/BSS.
- Usa exclusivamente caudas de slots de textos catalogados cuja tradução selecionada é menor, depois do novo terminador NUL.
- Conserva o conteúdo original das strings realocadas; atualiza somente suas referências elegíveis em tabelas de dados.
- Exige todas as referências literais encontradas em tabelas com pelo menos três ponteiros consecutivos para inícios de strings conhecidas.
- Pesquisa referências literais inclusive desalinhadas e bloqueia slots com referências ao interior.
- Bloqueia páginas que aparecem em qualquer instrução LUI do código, incluindo a variante de parte baixa com sinal. Isso é deliberadamente restritivo; ainda não interpreta todos os caminhos de execução.
- Não usa os agrupamentos de 24 textos como se fossem bancos reais.
- Fontes nativas e proteção dos registros do prólogo continuam no fluxo anterior.

## Limites

### Exceção pontual: fala de Misha

Após o usuário confirmar ausência de travamento na primeira variante e mostrar a fala inglesa, foi investigado `SLUS/TEXT/0334:0x8D4F70`. A tradução completa é `Misha, posso falar com você?`, 58 bytes contra 56 no slot. O único ponteiro alinhado ao início é `0x5B394C` -> VA `0x9D3F70`, campo +20 de registro de 24 bytes. A exceção exige o registro original `(3,1,0,0,65535,0x9D3F70)` e as duas frases vizinhas exatas nos campos de ponteiro a ±24 bytes. Não habilita outras tabelas/strings.

Não há instrução LUI no código com a página da origem ou seu ajuste de sinal. Existem 18 sequências desalinhadas que parecem endereços interiores `0x9D3F80`; não são modificadas nem consideradas ponteiros comprovados. O conteúdo inteiro da origem permanece byte a byte intacto, não é doador e não é reutilizado. Assim, essas referências aparentes não são invalidadas. Apenas o ponteiro específico da tabela passa a apontar para a tradução completa. Possíveis acessos calculados ainda exigem teste no jogo.

ISO pontual: `testes pt br/Ar tonelico PTBR Misha texto completo 20260926.iso`; SHA-256 `67865fde5b7625fde90c643785aa074147dcb9f036ad9da370d0de60dad3ee90`. 27.251 textos conferidos, 85 realocações, 5.384 fallbacks. A auditoria confirmou o payload completo de 58 bytes no destino, ponteiro atualizado, conteúdo original e metadados vizinhos intactos, todas as instruções e cabeçalhos intactos. 44 testes passaram. O EXE incorpora esta exceção na opção experimental de realocação de strings, sem mudança no banco e sem autorização geral para mover outras tabelas.

O saldo global de bytes não significa que os espaços podem ser compartilhados livremente. As restrições atuais habilitam 84 realocações no catálogo selecionado, não os 5.469 casos do relatório inicial. Outros 5.383 falham na elegibilidade de referências e dois não encontram cauda elegível suficiente. Os textos restantes são preservados no projeto e continuam recebendo fallback para o original.

A análise não comprova ausência de referências calculadas por indexação, acesso relativo a GP ou limites internos de buffers de consumidores. Não declarar a variante segura em jogo com base nos testes unitários ou na conferência dos bytes. Uma próxima expansão exige análise dos consumidores e/ou rastreamento no emulador, não flexibilização automática destes filtros.

## Validação e reteste

- 43 testes unitários passaram, incluindo cauda própria, ponteiro alterado, referência interior e bloqueio por LUI.
- ISO gerada: `testes pt br/Ar tonelico PTBR realocacao strings conservadora 20260926.iso`. 27.250 textos reabertos/conferidos, 84 realocados no SLUS, 5.385 fallbacks restantes. SHA-256 `ea01e55b65245a0324615f082fecd47386011ed894a17da30dc5e892cb973621`.
- Auditoria da ISO confirmou todas as seções executáveis, cabeçalhos ELF e tabela ativa `0x97BE30–0x97C230` intactos.
- EXE entregue em `release/ArTonelico_PTBR_Studio.exe`, SHA-256 `0d7667bf34819d55896ad4d936ece07b584f0f4bc569b0f6063850bb1bf4ee22`; iniciou sem encerrar com erro e atingiu estado de entrada da interface. Não equivale a teste visual completo da opção ou do jogo. Backup anterior: `release/ArTonelico_PTBR_Studio_antes_realocacao_strings_20260926.exe`.
- O gerador reabre a ISO e confere os textos e todos os ponteiros atualizados.
- Relatório por ISO: `.string_relocation.json` (origens, destinos e posições dos ponteiros). `.capacity_fallbacks.json` inclui motivo de bloqueio.
- Testar boot limpo, Novo Jogo, carregamento de memory card, seleção de Filé dragão/Lenço/Remédio, menus de tópicos, batalha e descrições de itens.
- Conferir visualmente as traduções maiores: realocação não aumenta caixas nem buffers.
- Manter a ISO anterior aprovada. A ISO experimental tem outro nome e o EXE anterior fica preservado.
