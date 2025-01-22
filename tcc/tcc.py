import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Configurações do banco de dados (Data Warehouse)
DB_DW_CONFIG = {
    "user": "*",
    "password": "*",
    "host": "*",
    "port": "*",
    "database": "*",
}
engine = create_engine(
    f"postgresql+psycopg2://{DB_DW_CONFIG['user']}:{DB_DW_CONFIG['password']}@{DB_DW_CONFIG['host']}:{DB_DW_CONFIG['port']}/{DB_DW_CONFIG['database']}"
)

# Configurações do banco de dados (Fonte - Odoo)
DB_SOURCE_CONFIG = {
    "host": "*",
    "port": "*",
    "database": "*",
    "user": "*",
    "password": "*",
}

# Consultas SQL
QUERIES = {
    "dProducts": """
        SELECT 
            id AS "idProducts",
            UPPER(name ->> 'pt_BR') AS "ProductDescription"
        FROM product_template pt;
    """,
    "dLoss": """
        SELECT 
            id AS "idLoss",
            UPPER(name ->> 'pt_BR') AS "LossDescription"
        FROM crm_lost_reason;
    """,
    "dContacts": """
        SELECT 
            id AS "idContacts",
            UPPER(name) AS "Name",
            UPPER(street) AS "Address", 
            UPPER(city) AS "City",
            UPPER(REPLACE(SPLIT_PART(tz, '/', 2), '_', ' ')) AS "State"
        FROM res_partner rp;
    """,
    "dStates": """
        SELECT 
            id AS "idStates",
            UPPER(name ->> 'pt_BR') AS "StatesDescription"
        FROM crm_stage cs;
    """,
    "fPipelineCRM": """
        SELECT 
            cl.id AS idCrm,
            cl.date_open::DATE AS DateOpen,
            cl.partner_id AS idContacts,
            cl.stage_id AS idStage,
            cl.priority AS idPriority,
            cl.date_closed::DATE AS DateClosed,
            cl.lost_reason_id AS idLoss,
            cl.description AS Interest,
            so.currency_rate AS qtd_people,
            so.amount_total AS value
        FROM crm_lead cl 
        LEFT JOIN sale_order so ON so.opportunity_id = cl.id;
    """,
}

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

# Função para salvar DataFrame no banco de dados
def save_to_db(df, table_name):
    try:
        df.to_sql(table_name, con=engine, if_exists="replace", index=False)
        print(f"Tabela '{table_name}' salva com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar a tabela '{table_name}': {e}")

# Função para consultar e salvar no banco de dados
def query_and_save(table_name, query):
    try:
        with psycopg2.connect(**DB_SOURCE_CONFIG) as conn:
            df = pd.read_sql_query(query, conn)
        save_to_db(df, table_name)
    except Exception as e:
        print(f"Erro ao consultar a tabela '{table_name}': {e}")

# Processamento das tabelas dinâmicas
for table_name, query in QUERIES.items():
    query_and_save(table_name, query)

# Processamento das tabelas estáticas
STATIC_TABLES = {
    "dPriority": dPriority,
    "dCalender": dCalender,
}

for table_name, df in STATIC_TABLES.items():
    save_to_db(df, table_name)
