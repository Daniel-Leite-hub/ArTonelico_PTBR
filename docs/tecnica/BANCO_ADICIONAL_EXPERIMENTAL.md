# Banco adicional de textos — 2026-09-26

## Pendentes v2 — entrega mais recente

O usuário confirmou que os testes da primeira ISO de banco adicional passaram. Essa ISO foi preservada. A nova candidata `testes pt br/Ar tonelico PTBR pendentes banco adicional v2 20260926.iso` aplica e confere na reabertura **32.527 textos**, mais **516**, sem novos fallbacks entre os anteriormente aplicados. São 5.361 strings realocadas; restam **108 fallbacks**: 70 referências não comprovadas e 38 sem referência direta reconhecida. SHA-256: `2ed730495b5da20f09ecedbc06335db6b98ffec5323c695f5529ea43a72db2f4`.

Reconhecimento ampliado para mais espaçamentos de tabelas, sempre exigindo três campos para strings conhecidas na mesma seção. Foram liberados 494 textos por esses formatos e outros 22 por 25 pares adjacentes LUI+ADDIU/ORI. Apenas código MIPS alocado/executável é analisado; overlays não alocados e microcódigo `.vutext` são excluídos. Não são reescritas bases compartilhadas, pares separados, delay slots ou pares cujo segundo membro é alvo direto de salto. Opcodes e registradores são preservados e cada par é conferido antes da escrita. A distinção entre imediato assinado ADDIU e ORI segue a [explicação técnica do GNU binutils](https://sourceware.org/pipermail/binutils/2024-April/133267.html); isso não comprova segurança dos consumidores do jogo.

Banco agora com 626.688 bytes (612 KiB), início inalterado, heap novo `0xDDE000`, reserva de 627.974 bytes. São 40 KiB a mais que a variante testada. Originais, BSS, tabela ativa e código fora dos imediatos autorizados foram auditados. 63 testes passaram. A candidata v2 ainda NÃO tem validação em jogo; o EXE foi recompilado, sem confirmação de inicialização nesta entrega.

Retestar por boot limpo e memory card, sem savestate antigo: Novo Jogo, menus de síntese/compra/venda, seleção de Reyvateil, mensagens formatadas, itens acentuados, batalhas e mudanças de área. Buffers internos podem impor limites diferentes do espaço de armazenamento. Os 108 restantes continuam protegidos: não flexibilizar referências desconhecidas para forçar a inserção.

## Resultado e limites

A ISO de teste `testes pt br/Ar tonelico PTBR banco adicional experimental 20260926.iso` aplica 32.011 textos, 4.635 a mais que a variante v2 de bancos de conversa. Nenhuma tradução anteriormente aplicada recebeu novo fallback. São 4.845 strings maiores copiadas para o banco adicional e 624 fallbacks restantes: 564 referências/layout não comprovados e 60 sem referência direta. Não foi concluída a inserção de todos os textos.

SHA-256 da ISO: `288b186be919f772c4c484705a4a565e4010525b329e44255e891a4e9ae87297`.

56 testes e auditoria estrutural passaram. Isto NÃO confirma boot, limite de buffers ou estabilidade durante o jogo. Cópias antigas permanecem intactas: caminhos que calculam o endereço original em instruções podem continuar exibindo inglês; a contagem de textos gravados não é uma comprovação de cobertura de todas as rotas de execução.

## Mecanismo

- Novo segmento ELF `PT_LOAD`, somente leitura, offset de arquivo `0x99B000`, endereço RAM `0xD45000`, tamanho `0x8F000` = 585.728 bytes (572 KiB).
- Executável expandido anexado à ISO; registro ISO9660 de `SLUS_214.45` atualizado em ambos os endians e verificado na reabertura. Original não sobrescrito.
- Segmento original e BSS preservados. O laço de zeragem continua terminando em `0xD44AFA`, NÃO no novo final: se estendido, apagaria o banco recém-carregado.
- Inicialização `SetupHeap` ajustada apenas nas instruções `0x11E4` e `0x11EC`, para começar em `0xDD4000`.
- Cursor inicial da biblioteca `sbrk`, no arquivo `0x746C64` / VA `0x845C64`, também ajustado. Uso confirmado por loads em VA `0x345428`, `0x34542C`, `0x345440`. Alterar só SetupHeap deixaria o cursor antigo capaz de sobrescrever traduções.
- Reserva: 587.014 bytes a menos para heap (inclui alinhamento), NÃO RAM extra. Limite de proteção experimental de 1 MiB; bancos maiores são recusados. Não é prova de que todos os consumidores usam apenas esse alocador.
- Nenhum hook, cave arbitrária ou troca da fonte. Todas as outras instruções e tabela ativa anteriormente envolvida no travamento foram conferidas intactas.
- Realocações em modo de cópia, sem reutilizar os originais, atualizam somente campos reconhecidos de tabelas. Outros formatos repetidos exigem pelo menos três ponteiros para strings conhecidas na mesma seção de dados e espaçamentos definidos; isso é reconhecimento estático, não prova de execução.

## Uso e reteste necessário

Preserve a ISO aprovada. No EXE, o banco adicional é uma opção separada experimental, com resposta padrão Não. Para gerar essa variante escolha Sim somente quando quiser testá-la.

Comece por boot limpo, sem restaurar savestate antigo (ele contém o layout de RAM e heap anteriores). Verifique Novo Jogo, carregamento por memory card, diálogos de Firefly, itens acentuados, menus, batalhas e transições de áreas. Além de encaixe visual, observar falta de memória, crashes tardios e quaisquer rotas ainda inglesas.

Não alterar configurações do emulador para simular RAM extra. Não instalar sobre o jogo original. Não promover esta variante como estável antes de testes reais.

Reprodução/auditoria: `python tools/build_text_arena_iso.py`. Relatórios por ISO: `.string_relocation.json`, `.capacity_fallbacks.json`, `.arena_audit.json`.

Referências consultadas: [PS2SDK startup e SetupHeap](https://github.com/ps2dev/ps2sdk/blob/master/ee/startup/src/crt0.c), [API de heap do PS2SDK](https://ps2dev.github.io/ps2sdk/kernel_8h.html), [estruturas ELF no PCSX2](https://github.com/PCSX2/pcsx2/blob/master/pcsx2/Elfheader.h). Essas fontes apoiam os conceitos, não comprovam que o alocador deste jogo é idêntico; a localização dos três ajustes veio da inspeção do executável específico.
