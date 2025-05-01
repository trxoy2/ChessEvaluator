import pandas as pd
import requests
from modules.execute_sql import execute_sql_file
from modules.insert_dataframe import insert_df

db_path = "./data/chess.db"

headers = {
    "User-Agent": "MyChessApp/1.0 (trxoy2@gmail.com)"  # Use your email or domain
}


def get_game_archives(username):
    url = f"https://api.chess.com/pub/player/{username}/games/archives"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json().get("archives", [])

def get_all_games(username, limit=None):
    archives = get_game_archives(username)

    if limit:
        archives = archives[-limit:]

    all_games = []

    for archive_url in archives:
        response = requests.get(archive_url, headers=headers)
        response.raise_for_status()
        monthly_games = response.json().get("games", [])
        all_games.extend(monthly_games)

    return all_games

# Fetch games and convert to DataFrame
results = get_all_games("HungryHowie4")

df = pd.DataFrame(results)


#execute sql to create table
execute_sql_file(db_path, "./sql/schema_chess_raw.sql")

#load the df with raw data
insert_df(db_path, "chess_raw", df, if_exists="replace")

#print raw data sample
#execute_sql_file(db_path, "./sql/select_chess_raw.sql", message="Raw URL table uploaded to database:")

