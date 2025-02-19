import pandas as pd
from database.config import engine_dw, engine_odoo
from bs4 import BeautifulSoup


# Função para salvar DataFrame no banco de dados
def save_to_db(df, table_name):
    try:
        df.to_sql(table_name, con=engine_dw, if_exists = 'append', index=False)
        print(f"Tabela '{table_name}' salva com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar a tabela '{table_name}': {e}")

# Função para consultar e salvar no banco de dados
def query_and_save(table_name, query):
    try:      
        df = pd.read_sql_query(query, engine_odoo)

        if table_name == "fPipelineCRM":
            df['Interest'] = df['Interest'].apply(extract_list_items)
            
        save_to_db(df, table_name)
    except Exception as e:
        print(f"Erro ao consultar a tabela '{table_name}': {e}")

def extract_list_items(html):
    if html is None:
        return None
    
    soup = BeautifulSoup(html, 'html.parser')
    return ', '.join([li.text for li in soup.find_all('li')])




