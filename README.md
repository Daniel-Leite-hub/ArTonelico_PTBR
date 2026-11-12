# Ar tonelico: Melody of Elemia — Localization Engineering Framework

[![Release](https://img.shields.io/badge/Release-v0.9.0--beta-yellow.svg)](RELEASE.md)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Database](https://img.shields.io/badge/Database-SQLite3-lightgrey.svg)](https://www.sqlite.org/)
[![Architecture](https://img.shields.io/badge/Architecture-MIPS%20R5900%20%2F%20PS2%20EE-orange.svg)]()
[![Platform](https://img.shields.io/badge/Platform-PlayStation%202-003791.svg)]()
[![AI Pipeline](https://img.shields.io/badge/AI%20Pipeline-Multi--Agent%20LLM%20Curation-purple.svg)]()
[![Build](https://img.shields.io/badge/Build-Zero%20Capacity%20Fallbacks-brightgreen.svg)]()

Um framework robusto de engenharia reversa, pipeline de dados, automação de compilação binária e curadoria orientada por Inteligência Artificial (LLMs), desenvolvido para localizar o clássico do PlayStation 2 ***Ar tonelico: Melody of Elemia (Undub)*** para o Português do Brasil (PT-BR).

O projeto soluciona restrições arquiteturais críticas de consoles legados dos anos 2000 — incluindo limitações rígidas de memória RAM, alinhamento estrito de setores em disco (ISO9660 LBA), remapeamento de tabelas de ponteiros em binários executáveis MIPS e rasterização de fontes nativas em VRAM —, integrando um pipeline moderno de engenharia de software com orquestração agêntica de IA e governança estrita de dados.

---

## 1. Resumo da Tradução & Versão Beta (`v0.9.0-beta`)

- **Jogo Base:** *Ar tonelico: Melody of Elemia*
- **Edição:** *Undub* (Áudio original japonês preservado; executável `SLUS-21445`)
- **Versão Atual:** **`v0.9.0-beta`** — *Beta pública com foco nos textos e diálogos*
- **Plataforma:** PlayStation 2 (PCSX2 e console real via OPL)
- **Escopo da Beta (`v0.9.0-beta`):**
  - **Cobertura Textual (`32.641` entradas traduzidas de `32.853` totais):** diálogos de enredo, mundos mentais (*Cosmospheres* de Misha, Aurica e Shurelia), Guardiões, *Talk Topics*, missões secundárias, descrições de alquimia (*Grathmeld*), itens, habilidades e menus (`212` identificadores técnicos são mantidos no original por segurança).
  - **Curadoria Baseada no Script Japonês:** Confronto pela Tríade de Idiomas (JP original / EN NISA / PT-BR) para resgatar nuances, termos técnicos, humor e subtexto perdidos na adaptação norte-americana.
  - **Engine Gráfica de Acentos & Expansão de Memória:** Tipografia nativa compatível com caracteres portugueses (`á`, `à`, `â`, `ã`, `é`, `ê`, `í`, `ó`, `ô`, `õ`, `ú`, `ü`, `ç`) renderizada em VRAM (TM2), aliada à realocação de *Text Arena* no executável MIPS (`SLUS_214.45`).
  - **Limitações Conhecidas desta Beta:**
    - Esta compilação foca integralmente nos **textos e menus do jogo**; vídeos pré-renderizados (`.sfd` / `videos_ptbr/`) não acompanham este repositório nem o aplicador Beta.
    - O projeto encontra-se em **validação contínua em gameplay real**; eventuais ajustes de quebra de linha (`CR`), diagramação ou contexto de cena devem ser reportados via *Issues*.

---

## 2. Visão Geral da Arquitetura

O sistema opera como um pipeline de engenharia ponta a ponta dividido em extração binária, governança de dados, curadoria agêntica assistida por IA, validação determinística e injeção compilada no sistema de arquivos da imagem de disco:

```mermaid
flowchart TD
    subgraph S1["1. Extração & Engenharia Reversa"]
        ISO["ISO Base (Undub PS2)"] -->|ISO9660 Parser| EVD_RAW["Scripts Binários EVD"]
        ISO -->|ELF Disassembler| MIPS["Binário SLUS_214.45 (MIPS R5900)"]
        ISO -->|VRAM Extractor| TM2["Texturas de Fonte TM2"]
    end

    subgraph S2["2. Engenharia de Dados & Armazenamento"]
        EVD_RAW -->|Binary Decoder / Shift-JIS| SQLite[("Repositório SQLite Unificado<br/>• 32.641 Linhas<br/>• Tríade de Idiomas (JP/EN/PT)<br/>• Hashes Criptográficos SHA-256")]
        GLOSS["Glossário Mestre Normalizado"] --> SQLite
    end

    subgraph S3["3. Curadoria com IA & Validação Determinística"]
        SQLite -->|Batch Dispatcher| AGENTS["Agentes Autônomos de IA (LLM)<br/>Análise Filológica Tríplice"]
        AGENTS -->|Propostas de Tradução| GUARD["Guardrails Determinísticos<br/>• AST Syntax Validator<br/>• Preservação de Tokens de Script (#1, CR, Variáveis)<br/>• Limites Físicos de VRAM & Linha"]
        GUARD -->|Commits Validados| SQLite
    end

    subgraph S4["4. Automação de Build & Patching Binário"]
        SQLite -->|Binary Recompiler| EVD_NEW["EVDs Reestruturados & Alinhados"]
        TM2 -->|Font Rasterizer (Pillow)| TM2_NEW["Atlas de Glifos Acentuados"]
        MIPS -->|MIPS Text Reference Patching| ELF_NEW["SLUS com Text Arena Expandida"]
        EVD_NEW & TM2_NEW & ELF_NEW -->|ISO9660 LBA Master| ISO_FINAL["ISO PT-BR Final (32.641 Linhas Verificadas)"]
    end
```

---

## 3. Pilares de Competência Técnica

### A. Automação & Engenharia de Sistemas (DevOps & Build Pipelines)

- **Manipulação de Baixo Nível do Sistema de Arquivos ISO9660:**
  - Leitor e escritor de disco implementados do zero em Python ([`artonelico_tool/iso.py`](artonelico_tool/iso.py)), capazes de analisar o diretório raiz, calcular Logical Block Addresses (LBA), reconstruir caminhos de arquivos e reescrever setores contíguos de 2048 bytes respeitando o alinhamento físico estrito exigido pelo PlayStation 2.
- **Desmontagem e Reestruturação de Scripts EVD Proprietários:**
  - O motor do jogo utiliza arquivos `.evd` contendo código de máquina interpretado, tabelas de controle de fluxo e sequências de texto em formato binário fechado. O módulo [`artonelico_tool/evd.py`](artonelico_tool/evd.py) executa parsing binário, decodificação customizada com escape `#1` para caracteres acentuados, recalibração de ponteiros de salto e reempacotamento de comandos contextuais.
- **Engenharia Reversa MIPS R5900 & Expansão de Text Arena:**
  - O executável ELF do jogo (`SLUS_214.45`) possuía tabelas estáticas de ponteiros e limites rígidos de alocação de memória no buffer original da PlayStation 2.
  - Implementação de injeção em Assembly MIPS ([`artonelico_tool/text_arena.py`](artonelico_tool/text_arena.py) e [`artonelico_tool/mips_text_reference.py`](artonelico_tool/mips_text_reference.py)) que redireciona referências em tempo de execução para uma área dinâmica de heap (*Text Arena Expansion*), eliminando restrições de tamanho de caracteres e prevenindo estouro de pilha (*stack overflow*).
- **Pipeline de Compilação Automatizada (Continuous Build):**
  - Script autônomo ([`tools/build_release_iso_curada.py`](tools/build_release_iso_curada.py)) que gera a imagem ISO traduzida completa em menos de 60 segundos, executando pré-auditoria de integridade, cálculo de SHA-256 de todas as entradas, injeção dos assets e validação contra fallbacks de capacidade.
- **Suite de Testes de Regressão Automatizados:**
  - Testes unitários contínuos em [`tests/`](tests/) validando sintaxe de formato, codificação de caracteres acentuados, renderização de fontes e integridade de estruturas binárias.

---

### B. Engenharia de Dados & Arquitetura de Informação (Data Pipelines & ETL)

- **Single Source of Truth (SSOT) Relacional Estruturado:**
  - Arquitetura de dados em SQLite ([`release/ArTonelico_PTBR_adaptado_108_20260926.atproj`](release/ArTonelico_PTBR_adaptado_108_20260926.atproj)) projetada com esquema relacional transacional para suportar múltiplos estágios do ciclo de vida dos dados:
    - Roteiro original em japonês (*ground truth* filológica).
    - Roteiro em inglês da NISA (referência estrutural legada).
    - Rascunhos automatizados brutos.
    - Textos curados aprovados.
    - Metadados de rastreabilidade (hash SHA-256 do texto, procedência, timestamps de revisão e tags de controle).
- **Integridade Criptográfica & Trilha de Auditoria:**
  - Cada registro modificado gera um digest criptográfico (`reviewed_hash = SHA256(texto)`). Qualquer divergência acidental de caracteres ou descompasso estrutural invalida a chave e bloqueia a injeção em disco, assegurando idempotência e rastreabilidade irrefutável.
- **Modelagem e Normalização de Glossário Terminológico:**
  - Catálogo normalizado de entidades nomeadas e terminologias de fantasia/ficção científica (Reyvateils, Hymmnos, conceitos técnicos de ondas sonoras, cidades, monstros e itens), com regras de de-duplicação e validação cruzada entre diálogos de eventos e tabelas de sistema ([`release/glossario_franquia/`](release/glossario_franquia/)).
- **Resiliência a Falhas & Transações ACID:**
  - Tratamento transacional com SQLite WAL (*Write-Ahead Logging*) que viabilizou centenas de sessões de processamento concorrente em lote sem qualquer corrupção de catálogo.

---

### C. Inteligência Artificial & Engenharia Agêntica (Multi-Agent LLM Orchestration)

- **Pipeline Agêntico de Curadoria em Larga Escala:**
  - Sistema de orquestração com subagentes especializados que processou autonomamente 134 blocos de roteiro (90 blocos de eventos narrativos + 44 blocos de sistema/interface), cobrindo mais de 32 mil diálogos.
- **Metodologia Filológica da Tríade de Idiomas:**
  - Modelagem de prompts orientados por contexto onde o modelo de IA opera confrontando simultaneamente:
    1. **Japonês Original (Autoridade Canônica):** Resgate de nuances, jogos de palavras, gírias e subtexto relacional.
    2. **Inglês NISA (Estrutura e Mapeamento de Layout):** Referência de segmentação de caixas de texto pré-existentes.
    3. **Português Brasileiro (Adaptação Idiomática):** Expressividade nativa, fluidez dramática e adequação de registro de fala conforme a personalidade de cada personagem.
- **Guardrails Determinísticos Pós-Inferência:**
  - A saída gerada pela IA nunca é inserida cegamente no banco de dados. Um pipeline de validação sintática determinística inspeciona:
    - **Preservação de Comandos de Controle:** Verificação rígida de tags internas (`CR` para quebra de página, `#1` para acentos e flags hexadecimais de cor/efeito).
    - **Proteção de Variáveis Procedurais:** Impedimento de alucinação de variáveis de inventário, nomes dinâmicos de personagens ou tokens de itens.
    - **Cálculo Físico de Capacidade:** Análise prévia de largura visual em pixels da fonte e limite de bytes por slot, evitando cortes de tela (*overflow*) ou sobreposições de renderizador.

---

## 4. Estrutura do Repositório

```text
ArTonelico_PTBR_Git/
├── .gitignore                      # Exclui ISOs, vídeos (.sfd/videos_ptbr), backups e temporários
├── README.md                       # Documentação técnica de arquitetura e pipeline
├── RELEASE.md                      # Manual do jogador e notas da versão v0.9.0-beta
├── aplicador.py                    # Código-fonte da interface Windows do Aplicador (v0.9.0-beta)
├── Aplicador_ArTonelico_PTBR.spec  # Configuração PyInstaller do Aplicador autônomo
├── main.py                         # Ponto de entrada do aplicativo Studio
├── ArTonelico_PTBR_Studio.spec     # Configuração PyInstaller para geração do Studio Windows
│
├── artonelico_tool/                # Pacote Python principal (Core Engine)
│   ├── evd.py                      # Parser, compilador e validador de scripts binários EVD
│   ├── gui.py                      # Interface gráfica de desktop para revisão e injeção
│   ├── iso.py                      # Parser e manipulador do sistema de arquivos ISO9660
│   ├── mips_text_reference.py      # Analisador de referências cruzadas e ponteiros MIPS
│   ├── patcher.py                  # Orquestrador de injeção, realocação e compilação
│   ├── portuguese_font.py          # Renderizador de atlas de fonte e injeção em texturas TM2
│   ├── text_arena.py               # Algoritmos de expansão de Text Arena na memória RAM
│   └── project.py                  # Camada de abstração e persistência SQLite
│
├── tools/                          # Utilitários de automação, dados e compilação
│   ├── build_release_iso_curada.py # Script de compilação da ISO traduzida
│   ├── curadoria_apply.py          # Mecanismo de aplicação automatizada de lotes revisados
│   ├── curadoria_validate.py       # Validador de conformidade determinística e integridade
│   ├── relink_project_iso.py       # Utilitário de redirecionamento de caminho da ISO-base
│   ├── analyze_font_metrics.py     # Análise de largura visual e métricas tipográficas
│   └── ...                         # Scripts de suporte técnico e auditoria
│
├── curadoria_editorial/            # Trilha do pipeline agêntico de Inteligência Artificial
│   └── blocos/                     # Manifestos JSON (inputs, outputs e relatórios) dos 134 blocos
│
├── tests/                          # Suite de testes unitários e de regressão
│   ├── test_formats.py             # Testes de integridade EVD, codificação, fontes e projetos
│   ├── test_string_relocation.py   # Testes de realocação de strings em memória
│   ├── test_text_arena.py          # Testes de expansão de Text Arena
│   └── ...
│
├── release/                        # Artefatos consolidados da versão Beta
│   ├── Aplicador_ArTonelico_PTBR.exe # Aplicativo Windows (1-clique, v0.9.0-beta) para aplicar na ISO
│   ├── ArTonelico_PTBR_adaptado_108_20260926.atproj  # Banco SQLite mestre curado (~22 MB)
│   ├── glossario_franquia/         # Base terminológica consolidada
│   └── iso/                        # Relatórios estruturais e metadados de compilação
│
├── localization_manual/            # Tabelas complementares de itens, habilidades e menus
└── docs/                           # Especificações técnicas e mapas de memória
```

---

## 5. Como Executar e Compilar

### Opção 1: Aplicador Executável Windows (Recomendado para Jogadores — `v0.9.0-beta`)
O release inclui um executável autônomo com interface gráfica amigável e banco curado embutido:
```text
release/Aplicador_ArTonelico_PTBR.exe
```
Basta executar o aplicativo, selecionar a imagem ISO original de *Ar tonelico (Undub)* e clicar em **"APLICAR TRADUÇÃO NA ISO"**. O software gera a imagem `ArTonelico_PTBR_v0.9.0-beta.iso` aplicando todos os textos curados, fontes acentuadas e realocações de memória sem exigir Python instalado. *(Nota: esta versão Beta foca nos textos; vídeos SFD legendados não são embutidos no aplicador.)*

### Opção 2: Compilação via Pipeline Python (Para Engenheiros e Desenvolvedores)
- **Pré-requisitos:** Python 3.10+ e Pillow:
  ```bash
  pip install pillow
  ```
- **Execução dos Testes Automatizados:**
  ```powershell
  python -B -m unittest discover -s tests
  ```
  *(Em um clone limpo sem os arquivos binários extraídos da ISO em `work/`, testes que exigem assets proprietários do jogo são ignorados automaticamente enquanto toda a suíte unitária do motor executa normalmente.)*
- **Compilando a Imagem ISO Traduzida:**
  ```powershell
  python tools/relink_project_iso.py "release/ArTonelico_PTBR_adaptado_108_20260926.atproj" "C:\Caminho\Para\Ar tonelico - Melody of Elemia (Undub).iso"
  python tools/build_release_iso_curada.py
  ```
O compilador executa a verificação completa das `32.641` entradas traduzidas, recalcula os offsets binários, expande a Text Arena e gera a imagem traduzida na pasta `ISOs/`.

Para instruções detalhadas de configuração no PCSX2, compatibilidade com consoles reais e guia da versão Beta, consulte o arquivo [`RELEASE.md`](RELEASE.md).

---

## 6. Métricas & Resultados Consolidados (`v0.9.0-beta`)

| Métrica | Valor Verificado |
| :--- | :--- |
| **Versão do Release** | `v0.9.0-beta` (Foco nos Textos) |
| **Registros no Catálogo / Linhas Traduzidas** | `32.853` totais / `32.641` traduzidas (`212` técnicos protegidos) |
| **Blocos Narrativos e de Sistema Curados** | `134` (90 eventos + 44 sistema) |
| **Área Mental Auditada (Cosmospheres + Guardiões)** | `7.085` falas (`0` erros críticos / `0` alertas) |
| **Fallbacks por Estouro de Capacidade** | `0` (Zero perda textual) |
| **Suporte a Acentuação Gráfica em VRAM** | `100%` funcional em diálogos e menus |
| **Tempo de Compilação Automatizada da ISO** | `< 60 segundos` |
