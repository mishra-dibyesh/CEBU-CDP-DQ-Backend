# Data Quality Application

This project is a FastAPI-based application for analyzing and presenting data quality metrics for passenger and booker profiling data. It provides endpoints to retrieve various statistical details about the datasets.

## Project Structure

The project consists of the following main files:

- `fetchdata.py`: Contains the FastAPI application and database connection logic.
- `load_data.py`: Handles the creation of database tables and loading of CSV data into the database.
- `schema.py`: Defines Pydantic models for data validation and serialization.
- `requirements.txt`: Lists all Python dependencies for the project.

## Setup

1. Ensure you have Python 3.7+ installed on your system.

2. Clone this repository:
   ```
   git clone <repository-url>
   cd <repository-name>
   ```

3. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up a PostgreSQL database named `Dataquality`.

6. Update the database connection parameters in both `fetch_data.py` and `load_data.py` with your PostgreSQL credentials.

7. Run the `load_data.py` script to create tables and load data:
   ```
   python load_data.py
   ```
   ***Note:*** Make sure you have updated "db_params"
      ```
      db_params = {
          'host': 'localhost',
          'database': 'Dataquality',
          'user': 'postgres',
          'password': 'YOUR_DB_PASSWORD'
      }
      ```

## Running the Application

To start the FastAPI server, run:

```
uvicorn fetch_data:app --reload
```
   ***Note:*** Make sure you have updated "password" in fetch_data.py file.

         try:
             conn=psycopg2.connect(host='localhost',database='Dataquality',user='postgres',password='YOUR_DB_PASSWORD',cursor_factory=RealDictCursor)
             cursor=conn.cursor()
             print("Database connection was successful")
         except Exception as e:
             print("Database connection was Failed")
             print("Error :",e)
         
         
   

- The API will be available at `http://localhost:8000`.
- You can use Swagger UI for better experience.  `http://localhost:8000/docs`

## API Endpoints

The application provides the following endpoints for both passenger (p) and booker (b) data:

- `/`: Welcome message
- `/table_meta/{table_type}`: table metadata
- `/kde_index/{table_type}` : Column metadata 
- `/numerical_details/{table_type}`: numerical column details
- `/category_details/{table_type}`: Categorical column details
- `/date_details/{table_type}`: Date column details
  
     ***Note:*** "{table_type}" should be either 'Booker' or 'Passenger'.


## Data Files

Ensure that your CSV data files are placed in the correct directories:

- Booker data: `Booker_data/`
- Passenger data: `Passenger_data/`

## Authors
- Author: Dibyesh Mishra, Biswajit Das
- Copyright: MindGraph Technologies
- Version: 0.1.0
- Maintainers:
   - Biswajit Das
   - Dibyesh Mishra
- Email:
   - mishra.d@mind-graph.com
   - biswajit.d@mind-graph.com
- Status: Development
- Date: 07/Oct/2024

## License

- Copyright (c) 2024. MindGraph Technologies. All rights reserved.
- Proprietary and confidential. Copying and distribution is strictly prohibited.
