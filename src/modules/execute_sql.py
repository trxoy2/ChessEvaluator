import sqlite3
import pandas as pd
import os

def execute_sql_file(database, sql_file, message=""):
    try:
        with open(sql_file, "r") as file:
            sql_script = file.read()

        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        # Execute the SQL script
        cursor.executescript(sql_script)

        #read sql into a df if is it a select query
        if sql_script.lower().startswith(("select", "pragma")):
            df = pd.read_sql_query(sql_script, conn)
            print(message)
            if not df.empty:
                print(df)
            else:
                print("No results found.")

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
    SELECT * FROM test_table;
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