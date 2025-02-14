import pandas as pd
import sqlite3
from modules.execute_sql import execute_sql_file
from modules.insert_dataframe import insert_df

db_path = "./data/malicious_urls.db"

raw_url_df = pd.read_csv("./data/malicious_urls.csv")

#execute sql to create url_raw table with defined schema file
execute_sql_file(db_path, "./sql/schema_url_raw.sql")

#load the df with raw data into url_raw table
insert_df(db_path, "url_raw", raw_url_df, if_exists="replace")

#print raw data sample
execute_sql_file(db_path, "./sql/select_url_raw.sql", message="\n✅ Raw URL table uploaded to database:")