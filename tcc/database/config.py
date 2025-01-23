from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a URL do banco de dados da variável de ambiente
database_dw = os.getenv("DATABASE_DW")

database_odoo = os.getenv("DATABASE_ODOO")

engine_dw = create_engine(database_dw)

engine_odoo = create_engine(database_odoo)

