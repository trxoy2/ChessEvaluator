"""
Function to insert a Pandas DataFrame into a SQLite database table.

Parameters:
- database (str): Path to the SQLite database file.
- table (str): Name of the table where the data should be inserted.
- df (pd.DataFrame): The DataFrame containing data to insert.
- if_exists (str, optional): Determines behavior if the table already exists.
  - "fail" (default SQLite behavior): Raises an error if the table exists.
  - "replace": Drops the existing table and creates a new one.
  - "append" (default): Adds new rows to the existing table.

Steps:
1. Establishes a connection to the SQLite database.
2. Uses Pandas' `to_sql` method to insert the DataFrame into the specified table.
3. Closes the database connection.
4. Implements error handling to catch and raise an exception if insertion fails.

Dependencies:
- sqlite3: For database interaction.
- pandas: For handling and inserting tabular data.
- os (imported but not used in this function; can be removed).

Raises:
- RuntimeError: If an error occurs during insertion.
"""

import sqlite3
import pandas as pd
import os
import json

def convert_non_string_columns(df):
    # Convert any column containing dict or list to a string
    for column in df.columns:
        # Apply json.dumps() to dict or list types to convert to string
        df[column] = df[column].apply(lambda x: json.dumps(x) if isinstance(x, (dict, list)) else str(x))
    return df

def insert_df(database, table, df, if_exists="append"):
    df = convert_non_string_columns(df)  # Convert dict and list columns to strings
    
    try:
        conn = sqlite3.connect(database)
        df.to_sql(table, conn, if_exists=if_exists, index=False)
    except Exception as e:
        raise RuntimeError(f"Error inserting DataFrame into {table}: {e}")
    finally:
        conn.close()




#test
if __name__ == "__main__":
    TEST_DB = "test_database.db"
    TEST_TABLE = "test_table"

    # Create a sample DataFrame
    test_df = pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"]
    })

    # Run function to insert test DataFrame
    insert_df(TEST_DB, TEST_TABLE, test_df, if_exists="replace")

    # Fetch and display results to verify insertion
    conn = sqlite3.connect(TEST_DB)
    result_df = pd.read_sql_query(f"SELECT * FROM {TEST_TABLE};", conn)
    conn.close()

    print("Test Table Data:")
    print(result_df)

    os.remove(TEST_DB)