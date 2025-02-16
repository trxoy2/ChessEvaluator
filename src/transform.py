import pandas as pd
import sqlite3
import re
import logging
import colorama
from urllib.parse import urlparse
from modules.execute_sql import execute_sql_file
from modules.insert_dataframe import insert_df
from modules.validator import clean_and_validate_data
from modules.parse_urls import extract_domain, extract_tld, get_domain_owner, get_domain_owner_parallel

colorama.init() 
# Suppress WHOIS library logging
logging.getLogger("whois").setLevel(logging.CRITICAL)

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
execute_sql_file(db_path, "./sql/select_url_clean.sql", message="Cleaned and Validated URL table uploaded to db:")


#---------------------------------
#---------------------------------Transform the data by adding new columns to enrich data
#---------------------------------
#connect to the database
conn = sqlite3.connect(db_path)

#read the url_raw table into a DataFrame
transformed_url_df = pd.read_sql_query("SELECT * FROM url_clean;", conn)

#close the database connection
conn.close()

#add column that identifies if url is duplicate
transformed_url_df["conflicting_url"] = transformed_url_df.groupby("url")["type"].transform("nunique") > 1

#regex to validate
URL_REGEX = re.compile(
    r"^((https?|ftp|htp):\/\/)?"  # Allow common & mistyped schemes
    r"(([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}|"  # Domain name (e.g., example.com)
    r"localhost|"  # Localhost
    r"(\d{1,3}\.){3}\d{1,3})"  # OR IP address (e.g., 192.168.1.1)
    r"(:\d+)?(\/[^\s]*)?$"  # Optional port & path
)
#validate URLs using regex
transformed_url_df["is_valid_url"] = transformed_url_df["url"].apply(lambda x: bool(URL_REGEX.match(str(x))) if x else False)

#---------------------------------
#---------------------------------Transform the data by extracting domain, tld, and domain owners
#---------------------------------
print("Extracting domains...")
#apply extract_domain function to create a new column
transformed_url_df["domain"] = transformed_url_df["url"].apply(extract_domain)
print("Extracting top level domains...")
#apply extract_tld function to create a new column
transformed_url_df["tld"] = transformed_url_df["domain"].apply(extract_tld)
print("Finding domain owners...")
#apply get_domain_owner using WHOIS lookup and store the owner in a new column
transformed_url_df = get_domain_owner_parallel(transformed_url_df, "domain")
#How many times does letter E appear in each domain?
transformed_url_df["e_count"] = transformed_url_df["domain"].str.lower().str.count("e")

#---------------------------------
#---------------------------------Clean and Validate data again before saving final transformed table
#---------------------------------

transformed_url_df = clean_and_validate_data(transformed_url_df)

execute_sql_file(db_path, "./sql/schema_url_transform.sql")

insert_df(db_path, "url_transform", transformed_url_df, if_exists="replace")

execute_sql_file(db_path, "./sql/select_url_transform.sql", message="Transformed URL table uploaded to db:")
