import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# --- Configurações ---
DATA_FILE = 'dados_consumo_simulacao.csv'
OUTPUT_DIR = 'resultados_analise'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- Parâmetros Econômicos e Técnicos ---
TARIFA_ENERGIA = 0.85 # R$/kWh (média Brasil)
IRRADIACAO_MEDIA_DIARIA = 4.43 # kWh/m²/dia (São Paulo)
PERFORMANCE_RATIO = 0.75 # Fator de perdas do sistema fotovoltaico
CUSTO_INSTALACAO_KWp = 5000 # R$/kWp (custo médio de instalação)
VIDA_UTIL_ANOS = 25 # Anos
TAXA_DESCONTO = 0.08 # 8% (para VPL)
INFLACAO_ENERGIA = 0.05 # 5% (aumento anual da tarifa)

# --- 1. Carregar e Preparar os Dados ---
try:
    df = pd.read_csv(DATA_FILE, index_col=0, parse_dates=True)
except FileNotFoundError:
    print(f"Erro: Arquivo {DATA_FILE} não encontrado. Execute generate_data.py primeiro.")
    exit()

# --- 2. Análise de Dados (Opção A) ---

# 2.1. Identificação de Desperdício (Consumo fora do horário comercial)
df['Hora'] = df.index.hour
df['Dia_Semana'] = df.index.dayofweek # 0=Segunda, 6=Domingo
df['Horario_Comercial'] = (df['Dia_Semana'] < 5) & (df['Hora'] >= 9) & (df['Hora'] < 18)

consumo_fora_comercial = df[~df['Horario_Comercial']]['Consumo_kWh'].sum()
consumo_total = df['Consumo_kWh'].sum()
percentual_desperdicio = (consumo_fora_comercial / consumo_total) * 100

# 2.2. Proposta de Ajuste (Redução de Desperdício)
# Assumimos que 50% do consumo fora do horário comercial pode ser eliminado com automação e conscientização.
reducao_desperdicio_kWh = consumo_fora_comercial * 0.5
consumo_anual_ajustado = consumo_total - reducao_desperdicio_kWh
economia_anual_R = reducao_desperdicio_kWh * TARIFA_ENERGIA

# 2.3. Estimativa de Ganhos Ambientais (Redução de CO2)
# Fator de emissão médio do SIN (Sistema Interligado Nacional) - 0.075 kg CO2e/kWh (aproximado)
FATOR_CO2 = 0.075
reducao_co2_kg = reducao_desperdicio_kWh * FATOR_CO2

# --- 3. Simulação de Uso de Energias Renováveis (Opção C) ---

# 3.1. Cálculo da Potência Necessária (kWp)
# Usaremos o consumo anual ajustado para dimensionar o sistema
consumo_medio_diario_ajustado = consumo_anual_ajustado / 365
geracao_necessaria_diaria = consumo_medio_diario_ajustado / PERFORMANCE_RATIO
potencia_kwp = geracao_necessaria_diaria / IRRADIACAO_MEDIA_DIARIA

# 3.2. Simulação da Geração Fotovoltaica
# Geração anual (kWh) = Potência (kWp) * Irradiação Média Diária * 365 * PR
geracao_anual_kWh = potencia_kwp * IRRADIACAO_MEDIA_DIARIA * 365 * PERFORMANCE_RATIO

# 3.3. Análise de Viabilidade Econômica
custo_instalacao_R = potencia_kwp * CUSTO_INSTALACAO_KWp
economia_anual_bruta = geracao_anual_kWh * TARIFA_ENERGIA

# Cálculo do Payback (simples)
payback_anos = custo_instalacao_R / economia_anual_bruta

# Cálculo do VPL (Valor Presente Líquido)
vpl = -custo_instalacao_R
fluxo_caixa = economia_anual_bruta
for ano in range(1, VIDA_UTIL_ANOS + 1):
    # Aumento da economia devido à inflação da energia
    fluxo_caixa *= (1 + INFLACAO_ENERGIA)
    # Desconto do fluxo de caixa
    vpl += fluxo_caixa / ((1 + TAXA_DESCONTO) ** ano)

# --- 4. Visualização dos Resultados (Removida para evitar erro de plotagem) ---

# --- 5. Apresentação dos Resultados (Texto) ---
print("\n--- Resultados da Análise de Dados (Opção A) ---")
print(f"Consumo Total Anual (Simulado): {consumo_total:.2f} kWh")
print(f"Consumo Fora do Horário Comercial (Desperdício): {consumo_fora_comercial:.2f} kWh ({percentual_desperdicio:.2f}%)")
print(f"Redução de Consumo Proposta (50% do Desperdício): {reducao_desperdicio_kWh:.2f} kWh")
print(f"Economia Financeira Anual Estimada (Ajuste): R$ {economia_anual_R:.2f}")
print(f"Redução de Emissões de CO2 Anual Estimada (Ajuste): {reducao_co2_kg:.2f} kg CO2e")

print("\n--- Resultados da Simulação Solar (Opção C) ---")
print(f"Consumo Anual Ajustado (Base para Dimensionamento): {consumo_anual_ajustado:.2f} kWh")
print(f"Potência do Sistema Fotovoltaico Necessária: {potencia_kwp:.2f} kWp")
print(f"Custo de Instalação Estimado: R$ {custo_instalacao_R:.2f}")
print(f"Geração Anual Estimada: {geracao_anual_kWh:.2f} kWh")
print(f"Economia Bruta Anual Estimada (Geração): R$ {economia_anual_bruta:.2f}")
print(f"Tempo de Retorno (Payback Simples): {payback_anos:.2f} anos")
print(f"Valor Presente Líquido (VPL) em {VIDA_UTIL_ANOS} anos: R$ {vpl:.2f}")

print("\nAnálise e Simulação concluídas. Gráficos salvos em: " + OUTPUT_DIR)
