import pandas as pd
import sqlite3
from modules.execute_sql import execute_sql_file
from modules.insert_dataframe import insert_df
from modules.validator import clean_and_validate_data

# Path to your SQLite database
db_path = "./data/malicious_urls.db"

#---------------------------------
#---------------------------------Clean and Validate data 
#---------------------------------
# Connect to the database
conn = sqlite3.connect(db_path)

# Read the url_raw table into a DataFrame
raw_url_df = pd.read_sql_query("SELECT * FROM url_raw;", conn)

# Close the database connection
conn.close()

clean_url_df = clean_and_validate_data(raw_url_df)

#execute sql to create url_clean table with defined schema file
execute_sql_file(db_path, "./sql/schema_url_clean.sql")

#load the df with raw data into url_raw table
insert_df(db_path, "url_clean", clean_url_df, if_exists="replace")

#show clean url data
execute_sql_file(db_path, "./sql/select_url_clean.sql", message="\n✅ Cleaned and Validated URL table uploaded to db:")


#---------------------------------
#---------------------------------Transform the data by adding new columns to enrich data
#---------------------------------
# Connect to the database
conn = sqlite3.connect(db_path)

# Read the url_raw table into a DataFrame
transformed_url_df = pd.read_sql_query("SELECT * FROM url_clean;", conn)

# Close the database connection
conn.close()

#add column that identifies if url is duplicate
transformed_url_df["conflicting_url"] = transformed_url_df.groupby("url")["type"].transform("nunique") > 1

#execute sql to create url_clean table with defined schema file
execute_sql_file(db_path, "./sql/schema_url_transform.sql")
#load the df with raw data into url_raw table
insert_df(db_path, "url_transform", transformed_url_df, if_exists="replace")
#show clean url data
execute_sql_file(db_path, "./sql/select_url_transform.sql", message="\n✅ Transformed URL table uploaded to db:")
