from fastapi import FastAPI, Path
from typing import List
from datetime import date
import psycopg2    
from psycopg2.extras import RealDictCursor
from schema import ColumnMeta, NumericalDetail, CategoryDetail, DateDetail,MetaData
 
app = FastAPI()
 
try:
    conn = psycopg2.connect(host='localhost', database='Dataquality', user='postgres', password='12345', cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("Database connection was successful")
except Exception as e:
    print("Database connection failed")
    print("Error:", e)
 
@app.get("/")
async def read_root():
    return {"message": "Welcome to the DataQuality application!"}
 
def get_table_prefix(table_type: str) -> str:
    if table_type.lower() == 'passenger':
        return 'p'
    elif table_type.lower() == 'booker':
        return 'b'
    else:
        raise ValueError("Invalid data type. Must be 'passenger' or 'booker'.")
    
@app.get("/table_meta/{table_type}", response_model=List[MetaData])
async def get_col_meta(table_type: str = Path(..., description="Either 'passenger' or 'booker'")):
    prefix = get_table_prefix(table_type)
    query = f'SELECT * FROM {prefix}_meta_data'
    cursor.execute(query)
    meta_df = cursor.fetchall()
    return [MetaData(**row) for row in meta_df]
 
@app.get("/kde_index/{table_type}", response_model=List[ColumnMeta])
async def get_col_meta(table_type: str = Path(..., description="Either 'passenger' or 'booker'")):
    prefix = get_table_prefix(table_type)
    query = f'SELECT * FROM {prefix}_col_meta_details'
    cursor.execute(query)
    col_meta_df = cursor.fetchall()
    return [ColumnMeta(**row) for row in col_meta_df]
 
@app.get("/numerical_details/{table_type}", response_model=List[NumericalDetail])
async def get_numerical_details(table_type: str = Path(..., description="Either 'passenger' or 'booker'")):
    prefix = get_table_prefix(table_type)
    query = f'SELECT * FROM {prefix}_numerical_details'
    cursor.execute(query)
    num_details_df = cursor.fetchall()
    return [NumericalDetail(**row) for row in num_details_df]
 
@app.get("/category_details/{table_type}", response_model=List[CategoryDetail])
async def get_category_details(table_type: str = Path(..., description="Either 'passenger' or 'booker'")):
    prefix = get_table_prefix(table_type)
    query = f'SELECT * FROM {prefix}_category_details'
    cursor.execute(query)
    cat_details_df = cursor.fetchall()
    return [CategoryDetail(**row) for row in cat_details_df]
 
@app.get("/date_details/{table_type}", response_model=List[DateDetail])
async def get_date_details(table_type: str = Path(..., description="Either 'passenger' or 'booker'")):
    prefix = get_table_prefix(table_type)
    query = f'SELECT * FROM {prefix}_date_details'
    cursor.execute(query)
    date_details_df = cursor.fetchall()
    return [DateDetail(**row) for row in date_details_df]