from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import psycopg2
import pandas as pd
import os

app = FastAPI()

templates_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')

print("templaes:", templates_dir)

templates = Jinja2Templates(directory=templates_dir)

username = 'gmb'
password = 'rykU,t=5(8-ROE~K' # Replace with the actual password or use getpass.getpass()
public_ip_address = '34.133.118.52'
db_name = 'gmb'

# Connection function
def get_cursor():
    conn = psycopg2.connect(
        dbname=db_name,
        user=username,
        password=password,
        host=public_ip_address
    )
    return conn.cursor()

def show_tables(cursor):
    query_tables = """ 
    select tablename
    from pg_catalog.pg_tables
    where schemaname != 'pg_catalog' AND
          schemaname != 'information_schema';
    """
    cursor.execute(query_tables)
    return [table[0] for table in cursor.fetchall()]

def show_sample_data(cursor, table_name):
    query_sample = f"select * from {table_name} limit 5;"
    return pd.read_sql(query_sample, cursor.connection)

# welcome page
@app.get("/", response_class=HTMLResponse)
def welcome(request: Request):
    return templates.TemplateResponse("welcome.html", {"request": request})

# tables page
@app.get("/tables", response_class=HTMLResponse)
def get_tables(request: Request, cursor=Depends(get_cursor)):
    tables = show_tables(cursor)
    return templates.TemplateResponse("tables.html", {"request": request, "tables": tables})

# sample page
@app.get("/sample-data/{table_name}", response_class=HTMLResponse)
def sample_data(request: Request, table_name: str, cursor=Depends(get_cursor)):
    data = show_sample_data(cursor, table_name)
    return templates.TemplateResponse("sample_data.html", {"request": request, "table_name": table_name, "data": data})

