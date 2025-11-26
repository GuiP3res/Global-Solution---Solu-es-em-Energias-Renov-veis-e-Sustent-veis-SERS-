# GLOBAL SOLUTION - SOLUÇÕES EM ENERGIAS RENOVÁVEIS E SUSTENTÁVEIS (SERS)

## Proposta de Solução: Análise de Dados e Simulação Fotovoltaica

Este projeto apresenta uma solução integrada, combinando a **Análise de Dados (Opção A)** de consumo energético com a **Simulação de Uso de Energias Renováveis (Opção C)**, focada na otimização e sustentabilidade de um ambiente de trabalho.

### 1. Cenário e Metodologia

O estudo de caso simula um **Escritório de Pequeno Porte** (20 funcionários) em São Paulo, com um consumo anual simulado de **16.788,50 kWh**.

A metodologia seguiu duas etapas principais:
1.  **Análise de Desperdício (Opção A):** Identificação do consumo fora do horário comercial (9h às 18h, Seg-Sex) e proposição de ajustes operacionais.
2.  **Simulação Fotovoltaica (Opção C):** Dimensionamento e análise de viabilidade econômica para a instalação de um sistema de energia solar, utilizando o consumo ajustado como base.

### 2. Resultados da Análise de Dados (Opção A)

A análise exploratória dos dados simulados revelou um padrão de consumo significativo fora do horário de pico, indicando potencial desperdício.

| Indicador | Valor | Percentual |
| :--- | :--- | :--- |
| Consumo Total Anual | 16.788,50 kWh | 100% |
| Consumo Fora do Horário Comercial (Desperdício) | 3.519,44 kWh | 20,96% |
| **Redução Proposta (50% do Desperdício)** | **1.759,72 kWh** | **10,48%** |

**Ganhos Estimados com a Otimização (Ajuste Operacional):**

| Indicador | Valor |
| :--- | :--- |
| Economia Financeira Anual (Tarifa R$ 0,85/kWh) | **R$ 1.495,76** |
| Redução de Emissões de CO2 Anual (Fator 0,075 kg CO2e/kWh) | **131,98 kg CO2e** |

A implementação de automação (ex: temporizadores, sensores de presença) e conscientização pode reduzir o consumo anual para **15.028,79 kWh**, servindo como base para o dimensionamento do sistema renovável.

### 3. Resultados da Simulação Fotovoltaica (Opção C)

A simulação dimensionou o sistema fotovoltaico necessário para atender 100% do consumo ajustado do escritório, considerando a irradiação solar média de São Paulo (4,43 kWh/m²/dia) e um fator de perdas (Performance Ratio) de 0,75.

| Indicador | Valor |
| :--- | :--- |
| Consumo Anual Base (Ajustado) | 15.028,79 kWh |
| **Potência do Sistema Necessária** | **12,39 kWp** |
| Geração Anual Estimada | 15.028,79 kWh |
| Custo de Instalação Estimado (R$ 5.000/kWp) | **R$ 61.963,52** |
| Economia Bruta Anual Estimada | **R$ 12.774,47** |

**Análise de Viabilidade Econômica (25 Anos):**

| Indicador | Valor |
| :--- | :--- |
| **Tempo de Retorno (Payback Simples)** | **4,85 anos** |
| **Valor Presente Líquido (VPL)** | **R$ 164.062,88** |

O projeto demonstra ser altamente viável economicamente, com um rápido retorno do investimento e um VPL positivo e robusto ao longo da vida útil do sistema.

### 4. Conexão com o Futuro do Trabalho

A solução proposta promove a **eficiência energética** e a **sustentabilidade corporativa**, pilares do futuro do trabalho. A análise de dados e a modelagem de simulação são ferramentas que permitem:
*   **Otimização de Recursos:** Redução de custos operacionais e uso mais eficiente da energia.
*   **Responsabilidade Ambiental:** Diminuição da pegada de carbono da empresa.
*   **Inovação:** Uso de tecnologias de simulação para tomada de decisão estratégica.

### 5. Orientações de Execução

Para replicar a análise e gerar os gráficos (que não puderam ser gerados no ambiente atual), siga os passos:

1.  **Instalar Dependências:** Certifique-se de ter Python 3 e as bibliotecas `pandas`, `numpy` e `matplotlib` instaladas.
    ```bash
    pip install pandas numpy matplotlib
    ```
2.  **Executar Geração de Dados:**
    ```bash
    python3 generate_data.py
    ```
    Este script criará o arquivo `dados_consumo_simulacao.csv`.
3.  **Executar Análise e Simulação:**
    ```bash
    python3 analyze_and_simulate.py
    ```
    Este script imprimirá os resultados numéricos e tentará gerar os gráficos (se o ambiente permitir).

---
**Arquivos no Repositório:**
*   `README.md`: Este documento.
*   `global_solution_proposal.md`: Proposta de solução e escopo.
*   `generate_data.py`: Script para gerar os dados simulados.
*   `analyze_and_simulate.py`: Script para análise de dados e simulação fotovoltaica.
*   `dados_consumo_simulacao.csv`: Dataset simulado de consumo e irradiação.
*   `roteiro_video.md`: Roteiro detalhado para o vídeo explicativo.
*   Link do Video: https://youtu.be/f4wlHppBgUU
