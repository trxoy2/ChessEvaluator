CREATE TABLE IF NOT EXISTS chess_raw (
    url TEXT PRIMARY KEY,          -- URL of the game
    pgn TEXT,                      -- Portable Game Notation (PGN) format of the game
    time_control TEXT,             -- Type of time control (e.g., "blitz", "bullet", etc.)
    end_time TIMESTAMP,            -- End time of the game
    rated BOOLEAN,                 -- Whether the game was rated or not
    tcn TEXT,                      -- Time control notation (e.g., "3+0", "5+3", etc.)
    uuid TEXT UNIQUE,              -- Universally Unique Identifier for the game
    initial_setup TEXT,            -- Initial setup (optional, depends on your data)
    fen TEXT,                      -- Forsyth-Edwards Notation (FEN) for the position
    time_class TEXT,               -- Time class (e.g., "bullet", "blitz", etc.)
    rules TEXT,                    -- Rules used in the game (e.g., "chess", "bughouse", etc.)
    white TEXT,                    -- Name of the white player
    black TEXT,                    -- Name of the black player
    eco TEXT,                      -- ECO (Encyclopedia of Chess Openings) code for the opening
    accuracies TEXT                -- Accuracies of the game (could be JSON or other format)
);