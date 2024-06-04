-- Section 4
CREATE FUNCTION fn_creator_with_board_games(_first_name VARCHAR(30))
RETURNS INT
AS
    $$
    DECLARE
        wanted_creator_id INT;
        total_games INT := 0;
    BEGIN
        SELECT c.id INTO wanted_creator_id FROM creators AS c WHERE c.first_name = _first_name;

        SELECT COUNT(*) INTO total_games FROM creators_board_games AS cbg WHERE cbg.creator_id = wanted_creator_id;

        RETURN total_games;
    END;
    $$
LANGUAGE plpgsql;

CREATE TABLE search_results(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50),
    release_year INT,
    rating FLOAT,
    category_name VARCHAR(50),
    publisher_name VARCHAR(50),
    min_players VARCHAR(50),
    max_players VARCHAR(50)
);

CREATE OR REPLACE PROCEDURE usp_search_by_category(category VARCHAR(50))
AS
    $$
    DECLARE
        wanted_category_record RECORD;
    BEGIN
        TRUNCATE TABLE search_results;
        FOR wanted_category_record IN (SELECT
            bg.name,
            bg.release_year,
            bg.rating,
            c.name AS category_name,
            p.name AS publisher_name,
            CONCAT(pr.min_players, ' ', 'people') AS min_players,
            CONCAT(pr.max_players, ' ', 'people') AS max_players
        FROM board_games AS bg
        JOIN categories AS c ON c.id = bg.category_id
        JOIN publishers AS p ON bg.publisher_id = p.id
        JOIN players_ranges AS pr ON bg.players_range_id = pr.id
        WHERE c.name = category
        ORDER BY publisher_name, bg.release_year DESC) LOOP
        INSERT INTO search_results (name, release_year, rating,
                                    category_name, publisher_name, min_players, max_players)
        VALUES (wanted_category_record.name,
                wanted_category_record.release_year,
                wanted_category_record.rating,
                wanted_category_record.category_name,
                wanted_category_record.publisher_name,
                wanted_category_record.min_players,
                wanted_category_record.max_players);
        END LOOP;
    END;
    $$
LANGUAGE plpgsql;

