# Correção estrutural EVD, sem reduzir traduções

## Evidência

O travamento da ISO com arena e da variante sem arena ocorre no interpretador EVD (`0x196220`). No estado preservado, o evento é 5, carregado após o prólogo. Isso não é evidência de que a arena causou a falha.

O carregador em `SLUS_214.45`, endereço virtual `0x196EC8`, percorre os registros sequencialmente. Após o cabeçalho de 24 bytes, usa estas instruções:

```text
196FD0 addiu t7,t3,3
196FD4 slti  t6,t3,0
196FD8 movz  t7,t3,t6
196FDC sra   t7,t7,2
196FE0 sll   t7,t7,2
196FE4 addu  t7,s1,t7
196FE8 addiu s1,t7,4
```

Para comprimentos positivos, `movz` restaura o comprimento sem somar 3. O próximo registro começa em `text_start + (length // 4) * 4 + 4`. A fórmula antiga `(length + 3) & ~3` era incorreta quando o comprimento era múltiplo de quatro. O cursor passava a ler texto como cabeçalho/comandos, produzindo comprimentos e endereços inválidos.

Todos os 976 EVDs originais são compatíveis com a regra determinística. Os nove registros múltiplos de quatro existentes nos originais possuem quatro bytes de padding; seus bytes não nulos são conservados na reconstrução sem tradução. Os cinco arquivos antes interpretados como excepcionais não exigem busca heurística do próximo cabeçalho.

## Alterações

- `evd.py`: parser estrito, padding correto e verificador independente do percurso nativo, campos de controle e trailer original.
- `patcher.py`: valida antes da gravação e após reabrir a ISO; prólogo usa a mesma reconstrução relocável dos demais eventos.
- Interface: removida a mensagem de que o prólogo permanece com registros fixos.
- Testes: todas as classes de resto de comprimento, rejeição do padding omitido, 976 originais, todas as traduções atuais, prólogo maior que seu registro original.

## Resultado

- 79 testes passaram (a primeira execução restrita encontrou bloqueio de acesso a diretórios temporários; reexecutados com sucesso fora dessa restrição).
- ISO anterior sem arena: 709 EVDs rejeitados, de 976, incluindo Event/5.
- ISO corrigida: 976/976 EVDs aprovados, todos os scripts/trailers originais preservados.
- 32.641 traduções aplicadas e reabertas, 36 vídeos traduzidos, zero fallback por capacidade.
- ISO-base e projeto com os mesmos SHA-256 antes/depois; nenhuma nova adaptação/abreviação editorial.
- Nova ISO: `isos_teste/ArTonelico_PTBR_EVD_corrigido_20261008.iso`.
- SHA-256: `afd62438db0741203634f5a2ad9832a7824b0eeb1b703caa1c602938343587aa`.

Auditoria completa em `isos_teste/ArTonelico_PTBR_EVD_corrigido_20261008.build.json`. Executáveis extraídos para auditoria em `work/evd_padding_20261008/`. A ISO e o EXE anteriores permanecem preservados.

## Limite da validação

Não foi realizado teste de execução da nova ISO: o controle de computador falhou antes de acessar o PCSX2 (`failed to write kernel assets`, erro 3). A auditoria implementa o cálculo de avanço de registros do jogo, mas não emula toda a VM de eventos nem todas as cenas. Não afirmar validação completa do jogo.

Testar a nova ISO com boot limpo e Novo Jogo (ou save normal de memory card). Savestates antigos contêm executável e eventos antigos em RAM e não servem para verificar a reconstrução. Esta correção preserva integralmente o banco atual, mas não restaura automaticamente versões anteriores das falas encurtadas em trabalhos passados.
