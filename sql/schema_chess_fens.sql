CREATE TABLE IF NOT EXISTS chess_fens_evaluated (
    game_id TEXT,                  -- UUID or identifier for the game
    move_number INTEGER,           -- Sequential number of the move
    player_to_move TEXT,           -- Either 'white' or 'black'
    fen TEXT,                      -- FEN string representing the position
    score REAL,                    -- Evaluation score (in centipawns)
    mate_in INTEGER,               -- Mate in N moves (if available)
    best_move TEXT,                -- Best move suggested by Stockfish at this position
    actual_move_uci TEXT,          -- Move actually played (UCI format)
    actual_move_san TEXT,          -- Move actually played (SAN format)
    is_best_move BOOLEAN,          -- Whether the player made the best move
    cp_loss REAL,                  -- Centipawn loss (calculated as the difference between the actual move and best move evaluations)
    move_quality TEXT,             -- Move quality label ('best', 'good', 'inaccuracy', 'mistake', 'blunder')
    PRIMARY KEY (game_id, move_number)
);