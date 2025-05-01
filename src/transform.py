import pandas as pd
import sqlite3
from tqdm import tqdm
from modules.execute_sql import execute_sql_file
from modules.insert_dataframe import insert_df
from modules.evaluate_fen import evaluate_fen_full
from modules.pgn_to_fen import pgn_to_fens_df

db_path = "./data/chess.db"

# Connect to the database and load df
conn = sqlite3.connect(db_path)

df = pd.read_sql_query("SELECT * FROM chess_raw;", conn)

conn.close()

#---------------------------------
#---------Convert PGNs to FENs----
#---------------------------------

# Apply to all PGNs
all_fens = []

for idx, row in df.iterrows():
    pgn = row['pgn']
    game_id = row.get('uuid', idx) 
    fens_df = pgn_to_fens_df(pgn, game_id)
    all_fens.append(fens_df)

fens_df = pd.concat(all_fens, ignore_index=True)

#-----------------------------------
#------Evaluate FENs w Stockfish----
#-----------------------------------

# Enable tqdm for pandas
tqdm.pandas(desc="Evaluating FENs")

# Apply evaluation function with progress bar
fens_df[['score', 'mate_in', 'best_move']] = fens_df['fen'].progress_apply(
    lambda fen: pd.Series(evaluate_fen_full(fen))
)

# Preview with evaluations
print(fens_df.head())

#-----------------------------------
#------Load evaluated data----------
#-----------------------------------

print("load evaluated fen data")
#execute sql to create table
execute_sql_file(db_path, "./sql/schema_chess_fens.sql")

#load the df with raw data
insert_df(db_path, "chess_fens_evaluated", fens_df, if_exists="replace")

#-----------------------------------
#------Calculate move quality-------
#-----------------------------------

print("calculate move quality")
#execute sql to calculate if player made the best move
execute_sql_file(db_path, "./sql/calc_is_best_move.sql")
#execute sql to calculate move quality
execute_sql_file(db_path, "./sql/calc_move_quality.sql")

print("show final data")
conn = sqlite3.connect(db_path)

df = pd.read_sql_query("SELECT * FROM chess_fens_evaluated;", conn)

conn.close()

print(df.head())

#import matplotlib.pyplot as plt
#
## Function to plot a game's scores
#def plot_game_scores(fens_df, game_id):
#    game_data = fens_df[fens_df['game_id'] == game_id].copy()
#    game_data = game_data.dropna(subset=['score'])  # Drop moves without evaluation
#
#    plt.figure(figsize=(12, 6))
#    plt.plot(game_data['move_number'], game_data['score'], marker='o', linestyle='-')
#    plt.axhline(0, color='gray', linestyle='--', linewidth=1)
#    plt.title(f"Evaluation Score Over Time (Game ID: {game_id})")
#    plt.xlabel("Move Number")
#    plt.ylabel("Evaluation (Centipawns)")
#    plt.grid(True)
#    plt.tight_layout()
#    plt.show()
#
## Example usage (replace with an actual game_id from your data)
#plot_game_scores(fens_df, '152bb2ac-fe18-11ef-9793-f95eb901000f')