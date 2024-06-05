-- Section 4
CREATE OR REPLACE FUNCTION fn_stadium_team_name(stadium_name VARCHAR(30))
RETURNS TABLE(team_name VARCHAR(30))
AS
    $$
    DECLARE
        s_record RECORD;
    BEGIN
        RETURN QUERY (SELECT t.name FROM teams AS t
            JOIN stadiums AS s
                ON t.stadium_id = s.id
                         WHERE s.name = stadium_name
                         ORDER BY t.name);
    END;
    $$
LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE sp_players_team_name(player_name VARCHAR(50), OUT team_name VARCHAR(50))
AS
    $$
    DECLARE
        wanted_t_id INT;
    BEGIN
        SELECT p.team_id
        INTO wanted_t_id
                    FROM players AS p
                    WHERE CONCAT(p.first_name, ' ', p.last_name) = player_name;

        IF wanted_t_id IS NULL
            THEN team_name := 'The player currently has no team';
            RETURN;
        END IF;

        SELECT t.name INTO team_name FROM teams AS t WHERE t.id = wanted_t_id;
    END;
    $$
LANGUAGE plpgsql;

