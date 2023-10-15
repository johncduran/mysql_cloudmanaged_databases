import os
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy import create_engine, inspect

load_dotenv('/home/john_duran/mysql_cloudmanaged_databases/.env') 


DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

db_engine = create_engine(conn_string, echo=False)

def get_tables(engine):
    inspector = inspect(engine)
    return inspector.get_table_names()

def execute_query_to_dataframe(query: str, engine):
    return read_sql(query, engine)

tables = get_tables(db_engine)
print("Tables in the database:", tables)    

sql_query = "SELECT * FROM patients"  
df = execute_query_to_dataframe(sql_query, db_engine)
print(df)