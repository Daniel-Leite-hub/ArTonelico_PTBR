# Ar tonelico: Melody of Elemia — Localization Engineering Framework

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Database](https://img.shields.io/badge/Database-SQLite3-lightgrey.svg)](https://www.sqlite.org/)
[![Architecture](https://img.shields.io/badge/Architecture-MIPS%20R5900%20%2F%20PS2%20EE-orange.svg)]()
[![Platform](https://img.shields.io/badge/Platform-PlayStation%202-003791.svg)]()
[![AI Pipeline](https://img.shields.io/badge/AI%20Pipeline-Multi--Agent%20LLM%20Curation-purple.svg)]()
[![Build](https://img.shields.io/badge/Build-Zero%20Capacity%20Fallbacks-brightgreen.svg)]()

Um framework robusto de engenharia reversa, pipeline de dados, automação de compilação binária e curadoria orientada por Inteligência Artificial (LLMs), desenvolvido para localizar integralmente o clássico do PlayStation 2 ***Ar tonelico: Melody of Elemia (Undub)*** para o Português do Brasil (PT-BR).

O projeto soluciona restrições arquiteturais críticas de consoles legados dos anos 2000 — incluindo limitações rígidas de memória RAM, alinhamento estrito de setores em disco (ISO9660 LBA), remapeamento de tabelas de ponteiros em binários executáveis MIPS e rasterização de fontes nativas em VRAM —, integrando um pipeline moderno de engenharia de software com orquestração agêntica de IA e governança estrita de dados.

---

## 1. Resumo da Tradução & Versão do Jogo

- **Jogo Base:** *Ar tonelico: Melody of Elemia*
- **Edição:** *Undub* (Áudio original japonês preservado; executável `SLUS-21445`)
- **Plataforma:** PlayStation 2 (executável nativamente em console real via OPL e emuladores PCSX2)
- **Escopo Concluído:**
  - **100% dos Textos do Jogo:** 32.641 linhas de diálogos, eventos, mundos mentais (*Cosmospheres*), missões secundárias, descrições de alquimia (*Grathmeld*), itens e menus traduzidos e curados.
  - **Curadoria Baseada no Script Japonês:** Reversão sistemática de censuras, cortes de contexto e simplificações da localização norte-americana legada (NISA), restabelecendo piadas originais, termos técnicos e subtexto sociolinguístico.
  - **Engine Gráfica de Acentos & Expansão de Memória:** Tipografia nativa compatível com caracteres portugueses (`ã`, `õ`, `é`, `ê`, `á`, `à`, `ó`, `ô`, `í`, `ú`, `ç`) renderizada em VRAM (TM2), aliada a uma expansão dinâmica de *Text Arena* na RAM do console que viabiliza sentenças longas sem abreviações ou perda de sentido.
  - **Confiabilidade:** 0 travamentos, 0 corrupções de ponteiros e 0 fallbacks por falta de espaço físico.

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
├── .gitignore                      # Configuração estrita excluindo ISOs, vídeos e temporários
├── README.md                       # Documentação técnica de arquitetura e competências
├── RELEASE.md                      # Manual completo para jogadores e compilação da tradução
├── main.py                         # Ponto de entrada do aplicativo Studio
├── ArTonelico_PTBR_Studio.spec     # Configuração PyInstaller para geração do executável Windows
│
├── artonelico_tool/                # Pacote Python principal (Core Engine)
│   ├── evd.py                      # Parser, compilador e validador de scripts binários EVD
│   ├── gui.py                      # Interface gráfica de desktop para revisão e injeção
│   ├── iso.py                      # Parser e manipulador do sistema de arquivos ISO9660
│   ├── mips_text_reference.py      # Analisador de referências cruzadas e ponteiros MIPS
│   ├── patcher.py                  # Orquestrador de injeção, realocação e compilação
│   ├── portuguese_font.py          # Renderizador de atlas de fonte e injeção em texturas TM2
│   ├── text_arena.py               # Algoritmos de expansão de Text Arena na memória RAM
│   └── translation_project.py      # Camada de abstração e persistência SQLite
│
├── tools/                          # Utilitários de automação, dados e compilação
│   ├── build_release_iso_curada.py # Script de compilação da ISO traduzida final
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
│   ├── test_formats.py             # Testes de integridade do formato EVD
│   ├── test_string_relocation.py   # Testes de realocação de strings em memória
│   ├── test_text_arena.py          # Testes de expansão de Text Arena
│   └── ...
│
├── release/                        # Artefatos consolidados e banco autoritativo
│   ├── ArTonelico_PTBR_adaptado_108_20260926.atproj  # Banco SQLite mestre curado (23 MB)
│   ├── glossario_franquia/         # Base terminológica consolidada
│   └── iso/                        # Relatórios estruturais e metadados de compilação
│
├── localization_manual/            # Tabelas complementares de itens, habilidades e menus
└── docs/                           # Especificações técnicas e mapas de memória
```

---

## 5. Como Executar e Compilar

### Pré-requisitos
- Python 3.10 ou superior.
- Biblioteca de processamento de imagens (Pillow):
  ```bash
  pip install pillow
  ```
- Imagem ISO do jogo *Ar tonelico: Melody of Elemia (Undub)* (`SLUS-21445`).

### Executando os Testes Automatizados
Para rodar a suite de testes de integridade e validar os parsers binários:
```powershell
python -B -m unittest discover -s tests
```

### Compilando a Imagem ISO Traduzida
Com a ISO original posicionada ou devidamente vinculada no banco de dados:
```powershell
python tools/build_release_iso_curada.py
```
O compilador executa a verificação completa das 32.641 entradas, recalcula os offsets binários, expande a Text Arena e entrega a imagem em `ISOs/ArTonelico_PTBR_completo_curado_20261101.iso`.

Para instruções detalhadas de configuração no PCSX2, compatibilidade com consoles reais e guia do jogador, consulte o arquivo [`RELEASE.md`](RELEASE.md).

---

## 6. Métricas & Resultados Consolidados

| Métrica | Valor Verificado |
| :--- | :--- |
| **Linhas de Texto Processadas** | `32.641` |
| **Blocos Narrativos e de Sistema Curados** | `134` (90 eventos + 44 sistema) |
| **Fallbacks por Estouro de Capacidade** | `0` (Zero perda textual) |
| **Integridade de Hashes SHA-256** | `100%` validado em banco |
| **Suporte a Acentuação Gráfica em VRAM** | `100%` funcional |
| **Tempo de Compilação Automatizada da ISO** | `< 60 segundos` |
