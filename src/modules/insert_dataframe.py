import sqlite3
import pandas as pd
import os

def insert_df(database, table, df, if_exists="append"):
    try:
        conn = sqlite3.connect(database)
        df.to_sql(table, conn, if_exists=if_exists, index=False)
        conn.close()
    
    except Exception as e:
        raise RuntimeError(f"Error inserting DataFrame into {table}: {e}")




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