from datetime import date
from pydantic import BaseModel

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


class MetaData(BaseModel):
    data_field: int                   
    record: int                    
    completeness: float             
    duplicates: int                   
    numerical: int                 
    categorical: int              
    date: int                      


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


