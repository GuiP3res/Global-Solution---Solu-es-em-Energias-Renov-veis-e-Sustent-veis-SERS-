import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# --- Parâmetros de Simulação ---
# Cenário: Escritório de Pequeno Porte (20 funcionários)
# Consumo médio diário estimado (kWh): 40 kWh (20 funcionários * 2 kWh/dia por pessoa, incluindo equipamentos e AC)
# Consumo anual total estimado: 40 kWh/dia * 365 dias = 14600 kWh
# Irradiação Solar Média Diária (São Paulo): 4.43 kWh/m²/dia [1]

# --- 1. Geração da Série Temporal ---
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31, 23, 45)
date_range = pd.date_range(start=start_date, end=end_date, freq='15min')
df = pd.DataFrame(index=date_range)

# --- 2. Geração do Consumo Energético (kW) ---
# Consumo base (sempre ligado): 0.5 kW (servidores, geladeira, etc.)
# Consumo de pico (horário comercial): 5.0 kW (computadores, iluminação, AC)
# Consumo médio: 14600 kWh / 8760 horas = 1.66 kW (aproximadamente)

def generate_consumption(timestamp):
    hour = timestamp.hour
    day_of_week = timestamp.dayofweek # Segunda=0, Domingo=6
    
    base_consumption = 0.5 + np.random.uniform(-0.1, 0.1) # Variação na base
    
    # Horário comercial (Segunda a Sexta, 9h às 18h)
    if day_of_week < 5 and 9 <= hour < 18:
        # Pico de consumo
        peak_consumption = 5.0 + np.random.uniform(-0.5, 0.5)
        # Simular picos de uso (ex: ar condicionado ligando)
        if np.random.rand() < 0.1:
            peak_consumption += np.random.uniform(1.0, 2.0)
        return base_consumption + peak_consumption
    
    # Fora do horário comercial (noite e fins de semana)
    else:
        # Simular desperdício (equipamento esquecido ligado)
        if np.random.rand() < 0.05: # 5% de chance de um consumo extra
            return base_consumption + np.random.uniform(0.5, 1.5)
        return base_consumption

df['Consumo_kW'] = df.index.map(generate_consumption)

# Converter kW para kWh (consumo em 15 minutos)
df['Consumo_kWh'] = df['Consumo_kW'] * (15 / 60)

# --- 3. Geração da Irradiação Solar (GHI - Global Horizontal Irradiance) ---
# Usaremos um modelo simplificado de irradiação solar
# Irradiação de pico (kW/m²)
PEAK_IRRADIANCE = 1.0 
# Fator de irradiação média diária (para ajustar a curva)
DAILY_IRRADIANCE_FACTOR = 4.43 / 5.0 # 5.0 é um valor de pico teórico

def generate_solar_irradiance(timestamp):
    hour = timestamp.hour
    minute = timestamp.minute
    day_of_year = timestamp.timetuple().tm_yday
    
    # Simular variação sazonal (inverno menos sol)
    # Pico no verão (dia 172 - Junho) e mínimo no inverno (dia 355 - Dezembro)
    # Inverti a lógica para o hemisfério sul: pico em Dez/Jan e mínimo em Jun/Jul
    
    # Ajuste sazonal:
    # Usando uma função seno para simular a variação da duração do dia
    # Pico em torno do dia 355 (Dezembro) e dia 1 (Janeiro)
    # Mínimo em torno do dia 172 (Junho)
    
    # Ajuste para pico em Dez/Jan (dia 1 e 365) e mínimo em Jun/Jul (dia 182)
    # A função cosseno com fase de 0 (dia 1) tem pico, e mínimo em 182.5
    seasonal_factor = (np.cos((day_of_year - 1) * 2 * np.pi / 365) + 1) / 2 * 0.4 + 0.6 # Varia entre 0.6 e 1.0
    
    # Curva diária (simulação de sinusoide)
    time_of_day = hour + minute / 60
    
    # Sol nasce por volta das 6h e se põe por volta das 18h
    if 6 <= time_of_day < 18:
        # Função seno para simular a curva solar
        angle = (time_of_day - 6) * np.pi / 12
        irradiance = PEAK_IRRADIANCE * np.sin(angle)
        
        # Adicionar ruído e aplicar fator sazonal
        irradiance = irradiance * seasonal_factor + np.random.uniform(-0.05, 0.05)
        
        # Garantir que não seja negativo
        return max(0, irradiance)
    else:
        return 0.0

df['Irradiacao_kW_m2'] = df.index.map(generate_solar_irradiance)

# --- 4. Salvar o Dataset ---
df.to_csv('dados_consumo_simulacao.csv')

print(f"Dataset gerado com {len(df)} registros (1 ano em intervalos de 15 minutos).")
print(f"Consumo total anual simulado: {df['Consumo_kWh'].sum():.2f} kWh")
print(f"Irradiação média diária simulada: {df['Irradiacao_kW_m2'].sum() / 365 / 4:.2f} kWh/m²/dia (aproximadamente)")
print("Arquivo 'dados_consumo_simulacao.csv' criado com sucesso.")

# [1] Referência para irradiação solar: https://albaenergia.com.br/incidencia-solar-o-que-e-e-como-ela-influencia-a-geracao-de-energia-fotovoltaica/ (Média de São Paulo)
