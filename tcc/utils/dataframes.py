import pandas as pd

# DataFrame estático de prioridade
dPriority = pd.DataFrame({
    "idPriority": [1, 2, 3],
    "PriorityDescription": ["Baixa", "Média", "Alta"]
})

# DataFrame de calendário
datas = pd.date_range(start="2024-01-01", end="2024-12-31")
dCalender = pd.DataFrame({
    "Data": datas,
    "Ano": datas.year,
    "Mês": datas.month,
    "Nome do Mês": datas.strftime("%b").str.capitalize(),
    "Trimestre": datas.quarter.map(lambda x: f"T{x}"),
    "Dia": datas.day,
    "Dia da Semana": datas.strftime("%A").str.capitalize(),
})

# Processamento das tabelas estáticas
STATIC_TABLES = {
    "dPriority": dPriority,
    "dCalender": dCalender,
}