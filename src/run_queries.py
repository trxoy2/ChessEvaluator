import pandas as pd
import sqlite3
import colorama
from modules.execute_sql import execute_sql_file

colorama.init() 

# Path to your SQLite database
db_path = "./data/malicious_urls.db"

#---------------------------------
#---------------------------------Read transformed table
#---------------------------------
# Connect to the database
conn = sqlite3.connect(db_path)

# Read the url_raw table into a DataFrame
final_url_df = pd.read_sql_query("SELECT * FROM url_transform;", conn)

# Close the database connection
conn.close()

#---------------------------------
#---------------------------------Answer count questions about domains
#---------------------------------
#How many records that contain the letter A and the letter T in the domain name are considered to be malware & phishing?
count = final_url_df[
    final_url_df["domain"].str.lower().str.contains("a") & 
    final_url_df["domain"].str.lower().str.contains("t") & 
    final_url_df["type"].isin(["malware", "phishing"])
].shape[0]
print("\033[4;32mCount of malware & phishing domains containing 'A' and 'T':\033[0m", count)


print("\033[4;32mHow many domains are in each type?\033[0m")
#execute sql to answer, Output how many domains are in each type?
execute_sql_file(db_path, "./sql/question_domain_count_by_type.sql")

print("\033[4;32mWhat percentage of each type is the total table population?\033[0m")
#execute sql to answer, What percentage of each type is the total table population?
execute_sql_file(db_path, "./sql/question_type_percent.sql")

print("\033[4;32mRank and order each record:\033[0m")
#execute sql to answer, Rank and order each record
execute_sql_file(db_path, "./sql/question_records_ranked.sql")


#---------------------------------
#---------------------------------Save final table as csv
#---------------------------------
# Connect to the database
conn = sqlite3.connect(db_path)

# Read the url_raw table into a DataFrame
final_url_df = pd.read_sql_query("SELECT * FROM url_transform;", conn)

# Close the database connection
conn.close()

final_url_df.to_csv("./data/finaloutput.csv", index=False)
print("\033[4;32mFinal output of transformed data available in data folder.\033[0m")