ALTER TABLE chess_fens_evaluated
ADD COLUMN cp_loss REAL;

ALTER TABLE chess_fens_evaluated
ADD COLUMN move_quality TEXT;

UPDATE chess_fens_evaluated
SET 
    -- Calculate cp_loss as the absolute difference between the current move's score and the best move's score
    cp_loss = ABS(score - 
        (SELECT score FROM chess_fens_evaluated AS best
         WHERE best.game_id = chess_fens_evaluated.game_id
           AND best.move_number = chess_fens_evaluated.move_number - 1));

UPDATE chess_fens_evaluated
SET 
    -- Classify move quality based on cp_loss
    move_quality = CASE 
        WHEN cp_loss = 0 THEN 'best'
        WHEN cp_loss BETWEEN 1 AND 49 THEN 'good'
        WHEN cp_loss BETWEEN 50 AND 99 THEN 'inaccuracy'
        WHEN cp_loss BETWEEN 100 AND 299 THEN 'mistake'
        WHEN cp_loss >= 300 THEN 'blunder'
        ELSE 'unknown' -- For any cases without a valid cp_loss
    END;