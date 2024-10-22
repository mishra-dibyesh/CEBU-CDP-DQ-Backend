import psycopg2
from psycopg2.extras import RealDictCursor
 
db_params = {
    'host': 'localhost',      
    'database': 'Dataquality',       #create a new database
    'user': 'postgres',              
    'password': '12345'              #enter your postgres password
}

def create_connection():
    try:
        conn = psycopg2.connect(**db_params, cursor_factory=RealDictCursor)
        return conn
    except Exception as e:
        print("Database connection failed")
        print("Error:", e)
        return None

def create_tables(ct):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
    
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {ct}_category_details (
                category TEXT,
                value_counts BIGINT,
                column_name TEXT,
                category_distribution TEXT
            );
            """)

             
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {ct}_col_meta_details (
                column_name TEXT,
                d_type TEXT,
                non_null_count BIGINT,
                fill_rate FLOAT,
                rank INTEGER,
                unique_count BIGINT,
                unique_rate FLOAT
            );
            """)

            
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {ct}_date_details (
                column_name TEXT,
                mon_yr TEXT,
                mon_yr_count BIGINT,
                month INTEGER,
                year INTEGER,
                min_date DATE,
                max_date DATE
            );
            """)

           
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {ct}_numerical_details (
                column_name TEXT,
                count BIGINT,
                min FLOAT,
                max FLOAT,
                percentile_05 FLOAT,
                percentile_95 FLOAT,
                percentile_25 FLOAT,
                percentile_75 FLOAT,
                median FLOAT,
                mean FLOAT,
                std_dev FLOAT,
                skewness FLOAT,
                variance FLOAT,
                first FLOAT,
                second FLOAT,
                third FLOAT,
                fourth FLOAT,
                fifth FLOAT
            );
            """)

            cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {ct}_meta_data (
                data_field BIGINT,           
                record BIGINT,              
                completeness FLOAT,         
                duplicates BIGINT,          
                numerical BIGINT,            
                categorical BIGINT,         
                date BIGINT);
            """)

            conn.commit()
            print("Tables created successfully.")
        except Exception as e:
            print("Error creating tables:", e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

create_tables('b')
create_tables('p')

def load_csv_to_db(csv_file_path, tbln):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
           
            with open(csv_file_path, 'r') as f:
                cmd = f'COPY {tbln} FROM STDIN WITH (FORMAT CSV, HEADER FALSE)'
                cursor.copy_expert(cmd, f)
                conn.commit()
                print(f"Data from {csv_file_path} loaded into {tbln} successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
 

load_csv_to_db("Booker_data//category_details_B.csv", "b_category_details")
load_csv_to_db("Booker_data//col_details_B.csv", "b_col_meta_details")
load_csv_to_db("Booker_data//date_B.csv", "b_date_details")
load_csv_to_db("Booker_data//Num_det_B.csv", "b_numerical_details")

load_csv_to_db("Passenger_data//p_categorial_det.csv", "p_category_details")
load_csv_to_db("Passenger_data//p_col_det.csv", "p_col_meta_details")
load_csv_to_db("Passenger_data//p_date_details.csv", "p_date_details")
load_csv_to_db("Passenger_data//p_num_details.csv", "p_numerical_details")

load_csv_to_db("Passenger_data//p_meta_data.csv", "p_meta_data")
load_csv_to_db("Booker_data//b_meta_data.csv", "b_meta_data")   
