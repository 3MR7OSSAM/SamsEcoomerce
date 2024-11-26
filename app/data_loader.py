import pandas as pd
import pyodbc

class Config:
    # Using the connection string that worked for you
    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc:///?odbc_connect='
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=LAPTOP-JR84GBKF\SQLEXPRESS;'
        'DATABASE=master;'
        'Trusted_Connection=yes;'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# Function to establish the database connection
def get_connection():
    conn_str = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=LAPTOP-JR84GBKF\SQLEXPRESS;'
        'DATABASE=commerce;'
        'Trusted_Connection=yes;'
    )
    return pyodbc.connect(conn_str)

# Function to load data from SQL database
def load_data():
    conn = None
    try:
        # Establish the connection
        conn = get_connection()

        # Define your queries
        products = "SELECT * FROM Products"
       
        
        # Fetch data as pandas DataFrames
        products_df = pd.read_sql(products, conn)

        # Return the DataFrames
        return products_df

    except Exception as e:
        print(f"An error occurred: {e}")
        return None # Return a tuple of None in case of an error

    finally:
        # Close the connection if it was established
        if conn is not None:
            conn.close()

# Example of calling the functions
if __name__ == "__main__":
  
    products = load_data()

    if None in (products):
        print("Data could not be loaded correctly.")
    else:
        print("Data loaded successfully and ready for further processing.")
