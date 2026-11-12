# Ar tonelico: Melody of Elemia (Undub) — Tradução PT-BR (`v0.9.0-beta`)

> **Versão da Tradução:** `v0.9.0-beta` *(Beta Pública — Foco nos Textos)*  
> **Status:** `32.641` linhas traduzidas e curadas | Zero fallbacks de capacidade | Em fase de testes in-game  
> **Aplicador Executável Incluso:** `release/Aplicador_ArTonelico_PTBR.exe` (1-Click Patcher Windows)

---

## 1. Sobre Esta Versão Beta (`v0.9.0-beta`)

- **Jogo:** *Ar tonelico: Melody of Elemia*
- **Plataforma:** PlayStation 2 (PS2)
- **Versão-Alvo:** *Undub* (Áudio original japonês com código de produto `SLUS_214.45`)
- **Compatibilidade:** Emuladores PCSX2 (v1.6+, v2.0+) e console PlayStation 2 real (via Open PS2 Loader / OPL por HDD interno, rede SMB ou USB).

### O que está incluído nesta Beta
- **Cobertura Textual (`32.641` entradas traduzidas de `32.853` totais):**
  - **História Principal & Rotas:** Eventos de enredo de todas as fases, ramificações e finais (rotas de Aurica, Misha e Shurelia).
  - **Cosmospheres & Guardiões:** Todos os 9 níveis de mergulho mental (*Dive*) de cada Reyvateil, Guardiões e *Dive Shops*, auditados contra estouros de linha e anomalias de quebra (`7.085` falas auditadas sem alertas).
  - **Sistema e Interface:** Menus de batalha, status, receitas de alquimia (*Grathmeld*), itens, equipamentos, acessórios e *Song Magic* (`212` identificadores técnicos são mantidos no original por segurança).
  - **Acampamento & NPCs:** *Talk Topics*, diálogos com moradores e eventos secundários.
- **Curadoria Filológica Tríplice (JP Original vs. EN NISA vs. PT-BR):**
  - Revisão confrontada diretamente com o roteiro original em japonês, resgatando nuances, humor e termos perdidos na localização da NISA.
- **Engine de Fontes e Expansão de Memória:**
  - Acentuação nativa do português (`á`, `à`, `â`, `ã`, `é`, `ê`, `í`, `ó`, `ô`, `õ`, `ú`, `ü`, `ç`) injetada em VRAM (`FO_HGGBP.tm2` e bitmap de menus).
  - Realocação segura de *Text Arena* no executável `SLUS_214.45`.

### Limitações conhecidas da fase Beta
- **Foco nos textos:** Esta versão `v0.9.0-beta` não inclui pacotes de vídeos `.sfd` legendados (`videos_ptbr`). Cutscenes pré-renderizadas permanecem com o vídeo da ISO base.
- **Testes em andamento:** Como se trata de uma versão Beta pública abrangendo mais de 32 mil linhas, algumas cenas ainda passam por verificação completa em gameplay real.

---

## 2. Verificação da ISO Original

Para garantir compatibilidade com o patcher, utilize a ISO americana **Undub** correspondente:

| Atributo | ISO Original (Undub) | Saída Gerada (`v0.9.0-beta`) |
| :--- | :--- | :--- |
| **Nome Padrão** | `Ar tonelico - Melody of Elemia (Undub).iso` | `ArTonelico_PTBR_v0.9.0-beta.iso` |
| **ID do Executável** | `SLUS_214.45` | `SLUS_214.45` (com Text Arena expandida) |
| **Tamanho em Bytes** | `3.110.580.224 bytes` | `3.324.903.424 bytes` |
| **SHA-256 (ISO Beta)** | — | `4feefd4c5657a6d14889d85c73990bdd8f7bc9d731fd9c49bb5e2bf32b598e93` |
| **Linhas Traduzidas** | — | `32.641` linhas verificadas (`212` originais protegidas) |
| **Fallbacks de Espaço** | — | `0` (zero truncamentos) |

> **Checksums dos artefatos de release:**  
> - `release/Aplicador_ArTonelico_PTBR.exe`: `6af0b2855358b0be338979d48e001acd451e9ca016c46bf614a1aba054929b48`  
> - `release/ArTonelico_PTBR_adaptado_108_20260926.atproj`: `e179f662a0ef8f405898b48ca240453cd9290a99045fffd620424244493ee6ee`

---

## 3. Como Aplicar a Tradução na ISO

### Método 1: Aplicador Executável Windows (Recomendado para Jogadores)

O repositório acompanha o aplicador autônomo com o banco `v0.9.0-beta` já embutido:  
**`release/Aplicador_ArTonelico_PTBR.exe`**

1. Execute `release/Aplicador_ArTonelico_PTBR.exe` dando duplo clique no Windows.
2. Em **1. Imagem ISO Original do Jogo (Undub)**, clique em **Selecionar ISO...** e escolha a sua ISO original (*Undub*). Se estiver na mesma pasta ou pasta pai, o programa a localiza automaticamente.
3. Em **2. Onde salvar a ISO Traduzida**, ajuste o destino caso deseje (padrão: `ArTonelico_PTBR_v0.9.0-beta.iso`).
4. Clique em **APLICAR TRADUÇÃO NA ISO** e aguarde a conclusão (geralmente menos de 60 segundos).

*Não é necessário instalar Python nem dependências externas para este método.*

---

### Método 2: Via Terminal / Script Python (Para Desenvolvedores)

1. **Pré-requisitos:** Python 3.10+ e Pillow:
   ```bash
   pip install pillow
   ```
2. **Redirecione o caminho da sua ISO original:**
   ```powershell
   python tools/relink_project_iso.py "release/ArTonelico_PTBR_adaptado_108_20260926.atproj" "C:\Caminho\Para\Ar tonelico - Melody of Elemia (Undub).iso"
   ```
3. **Execute o compilador:**
   ```powershell
   python tools/build_release_iso_curada.py
   ```
4. A ISO traduzida será gerada na pasta `ISOs/`.

---

## 4. Como Reportar Bugs desta Beta

Se encontrar qualquer erro durante o jogo (falas trocadas, texto encostando na borda, glifo estranho, quebra de linha ou travamento), abra uma **Issue** no GitHub informando:
- **Captura de tela (screenshot)** ou transcrição exata da fala exibida;
- **Local / cena / nível da Cosmosfera** em que ocorreu;
- Se está jogando no **PCSX2** (versão e renderizador) ou **PS2 real (OPL)**.

---

## 5. Dicas de Execução no PCSX2

- **Renderizador de Vídeo:** Vulkan ou Direct3D 11/12 para renderização nítida dos glifos acentuados e da interface.
- **Desentrelaçamento:** Bob TFF ou Blend (o jogo opera em 60i).
- **Proporção de Tela:** O jogo foi projetado nativamente para 4:3 (ou utilize patches widescreen oficiais do PCSX2 se desejar 16:9).
