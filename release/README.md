# Artefatos de Release — `v0.9.0-beta`

Esta pasta reúne os binários e relatórios consolidados da tradução em Português do Brasil de **Ar tonelico: Melody of Elemia (Undub)** (`SLUS-214.45`), na versão **`v0.9.0-beta`** (foco nos textos).

## Conteúdo da Pasta

- **`Aplicador_ArTonelico_PTBR.exe`** — Aplicativo Windows autônomo (1-clique) que aplica a tradução diretamente sobre a imagem ISO original *(Undub)* do PlayStation 2, sem exigir Python instalado. O banco SQLite curado mais recente está embutido no próprio executável (e também é lido da pasta ao lado caso exista).
- **`ArTonelico_PTBR_adaptado_108_20260926.atproj`** — Banco de dados SQLite mestre com `32.853` registros totais (`32.641` entradas traduzidas/curadas pela Tríade JP/EN/PT-BR e `212` identificadores técnicos preservados no original).
- **`ArTonelico_PTBR_adaptado_108_20260926.glossario.csv`** — Glossário terminológico auxiliar vinculado ao projeto.
- **`glossario_franquia/`** — Base terminológica consolidada da franquia para referência e continuidade editorial.
- **`iso/`** — Manifestos JSON estruturais (relatório de compilação, realocação de strings e fallbacks de capacidade) gerados pela compilação verificável da versão `v0.9.0-beta`.

## Escopo desta Versão Beta (`v0.9.0-beta`)

- **Incluído:** Todos os diálogos de história e *Cosmospheres* (Misha, Aurica, Shurelia e Guardiões), *Talk Topics*, itens, equipamentos, *Grathmeld*, *Song Magic*, tutoriais e menus, além da fonte portuguesa acentuada em VRAM (TM2) e expansão de *Text Arena* no executável `SLUS_214.45`.
- **Fora do escopo desta Beta:** Legendas em vídeo pré-renderizado (`.sfd` / `videos_ptbr`) não acompanham este release.
- **Uso:** Consulte o guia completo em [`../RELEASE.md`](../RELEASE.md) ou execute `Aplicador_ArTonelico_PTBR.exe`.
