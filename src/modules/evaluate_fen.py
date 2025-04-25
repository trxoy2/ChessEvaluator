from stockfish import Stockfish

# Path to your Stockfish executable
stockfish_path = r".\tools\stockfish\stockfish-windows-x86-64-avx2.exe"

# Initialize Stockfish
stockfish = Stockfish(
    path=stockfish_path,
    depth=15,
    parameters={
        "Threads": 2,
        "Minimum Thinking Time": 30
    }
)

# Function to evaluate a FEN using Stockfish and get the best move
def evaluate_fen_full(fen):
    try:
        stockfish.set_fen_position(fen)
        result = stockfish.get_evaluation()
        
        # Get the best move
        best_move = stockfish.get_best_move()
        
        # Return both evaluation score, mate-in (if applicable), and the best move
        if result['type'] == 'cp':
            return result['value'], None, best_move  # Centipawn evaluation, no mate
        elif result['type'] == 'mate':
            return 100000 if result['value'] > 0 else -100000, result['value'], best_move  # Mate score
        else:
            return None, None, best_move
    except Exception as e:
        print(f"Error evaluating FEN: {fen}\n{e}")
        return None, None, None

# Testing the function when the script is run directly
if __name__ == "__main__":
    # Example test FENs for evaluation
    example_fens = [
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",  # Standard starting position
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b KQkq - 0 1",  # Black to move
    ]

    # Evaluate and print results for example FENs
    for fen in example_fens:
        score, mate_in, best_move = evaluate_fen_full(fen)
        print(f"FEN: {fen}")
        print(f"Score: {score}, Mate-in: {mate_in}, Best Move: {best_move}\n")