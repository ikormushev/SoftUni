-- Task 4
CREATE OR REPLACE FUNCTION fn_is_game_over(IN is_game_over BOOLEAN)
RETURNS TABLE(name VARCHAR(50), game_type_id INT, is_finished BOOLEAN)
AS
    $$
    BEGIN
        RETURN QUERY
        SELECT
            g.name,
            g.game_type_id,
            g.is_finished
        FROM games AS g
        WHERE g.is_finished = is_game_over;
    END;
    $$
LANGUAGE plpgsql;

-- Task 5
CREATE OR REPLACE FUNCTION fn_difficulty_level(IN level INT)
RETURNS VARCHAR
AS
    $$
    DECLARE
        difficulty_level VARCHAR(50);
    BEGIN
        CASE
            WHEN level <= 40 THEN difficulty_level := 'Normal Difficulty';
            WHEN level > 40 AND level <= 60 THEN difficulty_level := 'Nightmare Difficulty';
            ELSE difficulty_level := 'Hell Difficulty';
        END CASE;
        RETURN difficulty_level;
    END;
    $$
LANGUAGE plpgsql;

SELECT
    user_id,
    level,
    cash,
    fn_difficulty_level(level) AS difficulty_level
FROM users_games
ORDER BY user_id;

-- Task 6
CREATE OR REPLACE FUNCTION fn_cash_in_users_games(game_name VARCHAR(50))
RETURNS TABLE(total_cash NUMERIC)
AS
    $$
    DECLARE
        wanted_game_id INT;
    BEGIN
        SELECT id INTO wanted_game_id FROM games AS g WHERE g.name = game_name;
        RETURN QUERY
        SELECT
            TRUNC(SUM(cash), 2) AS total_cash
        FROM
        (SELECT
             ug.cash,
             ROW_NUMBER() OVER (ORDER BY ug.cash DESC) AS row
         FROM users_games AS ug
         WHERE ug.game_id = wanted_game_id) AS s
        WHERE row % 2 = 1;
    END;
    $$
LANGUAGE plpgsql;

SELECT * FROM fn_cash_in_users_games('Love in a mist');
