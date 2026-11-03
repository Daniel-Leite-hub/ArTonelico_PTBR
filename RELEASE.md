# Ar tonelico: Melody of Elemia (Undub) — Tradução PT-BR Completa

> **Versão da Tradução:** v1.0.0 (Curadoria Editorial Integral)  
> **Status:** 100% dos textos traduzidos e revisados | Zero travamentos | Zero fallbacks de capacidade  
> **Aplicador Executável Incluso:** `release/Aplicador_ArTonelico_PTBR.exe` (1-Click Patcher Windows)

---

## 1. Sobre o Jogo e Esta Versão

- **Jogo:** *Ar tonelico: Melody of Elemia*
- **Plataforma:** PlayStation 2 (PS2)
- **Versão-Alvo:** *Undub* (Áudio original japonês com código de produto `SLUS-21445`)
- **Compatibilidade:** Emuladores PCSX2 (v1.6+, v2.0+) e console PlayStation 2 real (via Open PS2 Loader / OPL por HDD interno, rede SMB ou USB).

---

## 2. Resumo da Tradução

Esta localização entrega uma experiência completa e profunda de *Ar tonelico: Melody of Elemia* em Português do Brasil, construída com rigor técnico e editorial:

- **Cobertura Textual Integral (100%):**
  - **História Principal & Rotas:** Todos os eventos de enredo de todas as fases, ramificações e finais (rotas de Aurica, Misha e Shurelia).
  - **Cosmospheres (Mundos Espirituais):** Todos os 9 níveis de mergulho mental (*Dive*) de cada Reyvateil, com seus diálogos psicológicos, metáforas e conflitos internos plenamente adaptados.
  - **Sistema e Interface:** Menus de batalha, status, receitas de alquimia (*Grathmeld*), descrições de itens consumíveis, equipamentos, acessórios e canções mágicas (*Song Magic*).
  - **Interações de Acampamento & NPCs:** Todas as conversas de descanso (*Talk Topics*), diálogos com moradores e eventos secundários.
- **Curadoria Filológica Tríplice (JP Original vs. EN NISA vs. PT-BR):**
  - Ao contrário de traduções diretas do inglês da NISA (que historicamente removeu referências, suavizou piadas e pasteurizou personalidades), cada diálogo foi confrontado diretamente com o roteiro original em japonês.
  - Resgate do subtexto e do humor original, respeitando o tom rústico e mercenário de Jack, a inocência dividida de Aurica, o charme de Misha e a autoridade técnica e arcaica de Shurelia.
- **Engenharia de Fontes e Memória Sem Cortes:**
  - Injeção de caracteres acentuados nativos da língua portuguesa (`ã`, `õ`, `á`, `é`, `í`, `ó`, `ú`, `ê`, `â`, `ç`, pontuações e aspas curvas) diretamente nas texturas TM2 em VRAM.
  - Expansão dinâmica da área de texto na memória do console (*Text Arena Expansion* no Emotion Engine), permitindo que orações em português tenham seu tamanho natural preservado sem cortes forçados, abreviações estranhas ou perdas de sentido.

---

## 3. Verificação de Arquivos (Checksums)

Para garantir que a geração ocorra sem qualquer inconsistência, certifique-se de que a ISO original possui as seguintes características:

| Atributo | ISO Original (Undub) | ISO Final Compilada (PT-BR) |
| :--- | :--- | :--- |
| **Nome Padrão** | `Ar tonelico - Melody of Elemia (Undub).iso` | `ArTonelico_PTBR_completo.iso` |
| **ID do Executável** | `SLUS_214.45` | `SLUS_214.45` (com realocação MIPS) |
| **Tamanho em Bytes** | `3.110.580.224 bytes` | `3.324.913.664 bytes` |
| **Linhas Traduzidas**| — | `32.641` linhas verificadas |
| **Fallbacks de Espaço**| — | `0` (zero truncamentos) |

---

## 4. Como Aplicar a Tradução na ISO

O pacote disponibiliza duas formas de aplicação: o executável oficial para jogadores (1-clique sem necessidade de Python) e o pipeline de build via código-fonte.

### Método 1: Aplicador Executável Windows (Recomendado para Jogadores)

O release acompanha o aplicativo executável oficial:
**`release/Aplicador_ArTonelico_PTBR.exe`**

1. Abra o arquivo `release/Aplicador_ArTonelico_PTBR.exe` dando duplo clique no Windows.
2. No campo **1. Imagem ISO Original do Jogo (Undub)**, clique em **Selecionar ISO...** e aponte para a sua ISO original (*Undub*). O programa tenta localizá-la automaticamente se estiver na mesma pasta.
3. No campo **2. Onde salvar a ISO Traduzida**, escolha onde salvar a imagem gerada (por padrão `ArTonelico_PTBR_completo.iso`).
4. Clique no botão azul **APLICAR TRADUÇÃO NA ISO**.
5. Aguarde a barra de progresso (leva menos de 60 segundos). Ao término, uma mensagem confirmará as 32.641 linhas injetadas e oferecerá a opção de abrir a pasta com a ISO pronta para jogar!

*Não é necessário instalar Python, dependências ou configurar linha de comando para este método.*

---

### Método 2: Via Terminal / Script Python (Para Desenvolvedores)

Se você preferir rodar a compilação diretamente pelos fontes:

1. **Pré-requisitos:** Python 3.10+ e Pillow:
   ```bash
   pip install pillow
   ```
2. **Posicione ou redirecione a ISO:**
   ```powershell
   python tools/relink_project_iso.py "release/ArTonelico_PTBR_adaptado_108_20260926.atproj" "C:\Caminho\Para\Sua\ISO.iso"
   ```
3. **Execute o gerador:**
   ```powershell
   python tools/build_release_iso_curada.py
   ```
4. A ISO traduzida será gerada na pasta `ISOs/`.

---

## 5. Dicas de Execução e Emulação (PCSX2)

- **Renderizador de Vídeo:** Vulkan ou Direct3D 11/12 para máxima fidelidade nas texturas de interface e renderização nítida dos glifos acentuados.
- **Desentrelaçamento:** Bob tff ou Blend (o jogo roda internamente a 60i/30fps).
- **Proporção de Tela:** O jogo foi projetado nativamente para 4:3. Para telas widescreen (16:9), recomenda-se utilizar os patches de widescreen integrados ao PCSX2.
