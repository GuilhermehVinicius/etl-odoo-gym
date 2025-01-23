from utils.sql_queries import  QUERIES
from utils.dataframes import STATIC_TABLES
from utils.db_utils import query_and_save, save_to_db

# Processamento das tabelas dinâmicas
for table_name, query in QUERIES.items():
    query_and_save(table_name, query)


for table_name, df in STATIC_TABLES.items():
    save_to_db(df, table_name)
