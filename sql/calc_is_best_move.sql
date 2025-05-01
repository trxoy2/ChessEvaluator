ALTER TABLE chess_fens_evaluated
ADD COLUMN is_best_move BOOLEAN;

UPDATE chess_fens_evaluated
SET is_best_move = (actual_move_uci = best_move);