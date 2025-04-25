import sqlite3
import pandas as pd
import os
from tabulate import tabulate

def execute_sql_file(database, sql_file, message=""):

    if not os.path.exists(sql_file):
        raise FileNotFoundError(f"SQL file not found: {sql_file}")

    try:
        with open(sql_file, "r", encoding="utf-8") as file:
            sql_script = file.read()

        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        queries = sql_script.strip().split(";")  # Split SQL script into individual queries

        if message:
            print(f"{message}")

        for query in queries:
            query = query.strip()
            if not query:  # Skip empty queries
                continue

            if query.lower().startswith(("select", "pragma")):
                df = pd.read_sql_query(query, conn)

                if df.empty:
                    print("No results found.")
                else:
                    print(tabulate(df, headers="keys", tablefmt="grid"))  # Pretty print table
            else:
                cursor.execute(query)  # Execute non-SELECT queries

        conn.commit()
        conn.close()

    except Exception as e:
        raise RuntimeError(f"Error executing {sql_file}: {e}")



#test
if __name__ == "__main__":
    # Test configuration
    TEST_DB_NAME = "test_database.db"
    TEST_SQL_FILE = "test_schema.sql"
    TEST_SQL_FILE_SELECT = "test_query.sql"

    # Create a simple test SQL file
    test_sql_content = """
    CREATE TABLE IF NOT EXISTS test_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );

    INSERT INTO test_table (name) VALUES ('Alice'), ('Bob');
    """
    test_sql_select_content = """SELECT * FROM test_table;
    """
    
    with open(TEST_SQL_FILE, "w") as f:
        f.write(test_sql_content)
    
    with open(TEST_SQL_FILE_SELECT, "w") as f:
        f.write(test_sql_select_content)

    # Run the function with test parameters
    execute_sql_file(TEST_DB_NAME, TEST_SQL_FILE)
    execute_sql_file(TEST_DB_NAME, TEST_SQL_FILE_SELECT)

    # Cleanup test SQL file (optional)
    os.remove(TEST_SQL_FILE)
    os.remove(TEST_SQL_FILE_SELECT)
    os.remove(TEST_DB_NAME)