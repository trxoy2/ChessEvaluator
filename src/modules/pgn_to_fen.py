import pandas as pd
import chess.pgn
import io

def pgn_to_fens_df(pgn_str, game_id):
    game = chess.pgn.read_game(io.StringIO(pgn_str))
    board = game.board()

    fens_data = []
    move_number = 1

    for move in game.mainline_moves():
        move_uci = move.uci()
        move_san = board.san(move)
        board.push(move)

        fens_data.append({
            'game_id': game_id,
            'move_number': move_number,
            'fen': board.fen(),
            'player_to_move': 'white' if board.turn else 'black',
            'actual_move_uci': move_uci,
            'actual_move_san': move_san
        })

        move_number += 1

    return pd.DataFrame(fens_data)

if __name__ == "__main__":
    # Example PGN for testing
    test_pgn = """
    [Event "F/S Return Match"]
    [Site "Belgrade, Serbia JUG"]
    [Date "1992.11.04"]
    [Round "29"]
    [White "Fischer, Robert J."]
    [Black "Spassky, Boris V."]
    [Result "1/2-1/2"]

    1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7
    """
    df = pgn_to_fens_df(test_pgn, "test_game")
    print(df.head())
