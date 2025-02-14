import pandas as pd
import sqlite3
from modules.execute_sql import execute_sql_file
from modules.insert_dataframe import insert_df

db_path = "./data/malicious_urls.db"
raw_url_df = pd.read_csv("./data/malicious_urls.csv")

#conn = sqlite3.connect(db_path)
#execute sql to create url_raw table with defined schema file
execute_sql_file(db_path, "./sql/schema_url_raw.sql")

#load the df with raw data into url_raw table
insert_df(db_path, "url_raw", raw_url_df, if_exists="replace")




execute_sql_file(db_path, "./sql/test.sql", message="\n✅ Raw URL Data uploaded to database:")