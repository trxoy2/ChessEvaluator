CREATE TABLE IF NOT EXISTS chess_fens_evaluated (
    game_id TEXT,                  -- UUID or identifier for the game
    move_number INTEGER,          -- Sequential number of the move
    player_to_move TEXT,          -- Either 'white' or 'black'
    fen TEXT,                     -- FEN string representing the position
    score REAL,                   -- Evaluation score (in centipawns)
    mate_in INTEGER,              -- Mate in N moves (if available)
    best_move TEXT,               -- Best move suggested by Stockfish
    PRIMARY KEY (game_id, move_number)
);