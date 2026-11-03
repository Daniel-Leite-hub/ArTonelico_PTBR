# Cobertura conhecida — Ar tonelico PT-BR Studio

## Interpretado e validado tecnicamente

- ISO americana identificada pelo executável `SLUS_214.45`.
- Índice do `RPK.BIN`: 2.703 recursos.
- Diálogos/eventos: 976 arquivos `Event/*.evd`, total de 20.304 entradas.
- Reconstrução original dos 976 EVDs: igualdade byte a byte.
- Texto EVD: CP932/Shift-JIS com terminador, alinhamento e cabeçalhos preservados.
- Fonte de diálogo `FO_HGGBP.tm2`: biblioteca PT-BR nativa por aliases e marcadores locais `#1`.
- 70 entradas vazias, técnicas ou iniciadas por comando permanecem protegidas.

## Evidência prática disponível

- As falas de teste em `107.evd:5` e `108.evd:0` iniciaram no emulador e exibiram acentos portugueses após os ajustes do atlas.
- Essa evidência vale para a cena e a fonte de diálogo testadas; não comprova todos os menus, atlas, páginas ou hardware original.

## Ainda não interpretado como catálogo traduzível

- Os 1.727 recursos do RPK que não são `Event/*.evd` não foram todos classificados como texto ou recurso não textual.
- Menus, itens, habilidades, descrições, tutoriais, perfis e enciclopédias fora dos EVDs.
- Strings visíveis embutidas no executável e em arquivos secundários.
- Texto presente em imagens e variantes ornamentadas de fonte.

## Limite da declaração

O programa cobre o catálogo EVD conhecido. Isso não equivale a cobertura textual completa do jogo. Uma frase ausente deve ser localizada no recurso real antes de ampliar o extrator.
