from fastapi import FastAPI,Depends
from pydantic import BaseModel
from typing import List 
from datetime import date
from pydantic import BaseModel
import psycopg2     
from  psycopg2.extras import RealDictCursor

app = FastAPI()

class ColumnMeta(BaseModel):
    column_name: str
    d_type: str
    non_null_count: int
    fill_rate: float
    rank: int
    unique_count: int
    unique_rate: float

class NumericalDetail(BaseModel):
    column_name: str
    count: int
    min: float
    max: float
    percentile_05: float
    percentile_95: float
    percentile_25: float
    percentile_75: float
    median: float
    mean: float
    std_dev: float
    skewness: float=0.0
    variance: float
    first: float
    second: float
    third: float
    fourth: float
    fifth: float

class CategoryDetail(BaseModel):
    category: str
    value_counts: int
    column_name: str
    category_distribution: str

class DateDetail(BaseModel):
    column_name: str
    mon_yr: str
    mon_yr_count: int
    month: int
    year: int
    min_date: date
    max_date: date

try:
    conn=psycopg2.connect(host='localhost',database='postgres',user='postgres',password='12345',cursor_factory=RealDictCursor)
    cursor=conn.cursor()
    print("Database connection was successful")
except Exception as e:
    print("Database connection was Failed")
    print("Error :",e)
    

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

#  ----------------------------------------------PASSENGER PROFILING DATA----------------------------------------------#

@app.get("/p_col_meta/", response_model=List[ColumnMeta])
async def get_col_meta():
    query='select * from p_col_meta_details'
    cursor.execute(query)
    col_meta_df = cursor.fetchall()
    return [ColumnMeta(**row ) for row in col_meta_df ]

@app.get("/p_numerical_details/", response_model=List[NumericalDetail])
async def get_numerical_details():
    
    query='select * from p_numerical_details'
    cursor.execute(query)
    num_details_df = cursor.fetchall()
    return [NumericalDetail(**row ) for row in num_details_df ]

@app.get("/p_category_details/", response_model=List[CategoryDetail])
async def get_category_details():
    query='select * from p_category_details'
    cursor.execute(query)
    cat_details_df = cursor.fetchall()
    return [CategoryDetail(**row ) for row in cat_details_df ]

@app.get("/p_date_details/", response_model=List[DateDetail])
async def get_date_details():

    query='select * from p_date_details'
    cursor.execute(query)
    date_details_df = cursor.fetchall()
   
    return [DateDetail(**row ) for row in date_details_df ]


#  ----------------------------------------------BOOKER PROFILING DATA----------------------------------------------#

@app.get("/b_col_meta/", response_model=List[ColumnMeta])
async def get_col_meta():
    query='select * from b_col_meta_details'
    cursor.execute(query)
    col_meta_df = cursor.fetchall()

    return [ColumnMeta(**row ) for row in col_meta_df]
 
@app.get("/b_numerical_details/", response_model=List[NumericalDetail])
async def get_numerical_details():
    
    query='select * from b_numerical_details'
    cursor.execute(query)
    num_details_df = cursor.fetchall()
    return [NumericalDetail(**row ) for row in num_details_df ]

@app.get("/b_category_details/", response_model=List[CategoryDetail])
async def get_category_details():
    query='select * from b_category_details'
    cursor.execute(query)
    cat_details_df = cursor.fetchall()
   
    
    return [CategoryDetail(**row ) for row in cat_details_df ]

@app.get("/b_date_details/", response_model=List[DateDetail])
async def get_date_details():

    query='select * from b_date_details'
    cursor.execute(query)
    date_details_df = cursor.fetchall()
   
   
    return [DateDetail(**row ) for row in date_details_df ]

