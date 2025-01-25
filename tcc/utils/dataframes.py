import pandas as pd

# DataFrame estático de prioridade
dPriority = pd.DataFrame({
    "idPriority": [0, 1, 2, 3],
    "PriorityDescription": ["Não Definida", "Baixa", "Média", "Alta"]
})

# DataFrame de calendário
datas = pd.date_range(start="2024-01-01", end="2025-12-31")
dCalender = pd.DataFrame({
    "Date": datas,
    "Year": datas.year,
    "Month": datas.month,
    "NameMonth": datas.strftime("%b").str.capitalize(),
    "Quarter": datas.quarter.map(lambda x: f"T{x}"),
    "Day": datas.day,
    "WeekDay": datas.strftime("%A").str.capitalize(),
})

dGymWellhub = pd.read_csv('/home/gui/scraping-wellhub/wellhub/gyms_franca_wellhub.csv',sep=',')
dGymWellhub.columns = ['Name' , 'BasePlan', 'Address', 'Services', 'Comorbidities', 'ValuePlan', 'Date']

# Processamento das tabelas estáticas
STATIC_TABLES = {
    "dPriority": dPriority,
    "dCalender": dCalender,
    "dGymWellhub" : dGymWellhub
}