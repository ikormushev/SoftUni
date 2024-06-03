-- Section 4
CREATE FUNCTION fn_get_volunteers_count_from_department(searched_volunteers_department VARCHAR(30))
RETURNS INT
AS
    $$
    DECLARE
        total_volunteers INT := 0;
        wanted_department_id INT;
    BEGIN
        SELECT vd.id INTO wanted_department_id
                  FROM volunteers_departments AS vd
                  WHERE vd.department_name = searched_volunteers_department;

        SELECT
            COUNT(*)
        INTO total_volunteers
        FROM volunteers
        WHERE department_id = wanted_department_id;
        RETURN total_volunteers;
    END;
    $$
LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE sp_animals_with_owners_or_not(IN animal_name VARCHAR(30), OUT owner VARCHAR(50))
AS
    $$
    DECLARE
        given_animal_id INT;
    BEGIN
        SELECT a.id INTO given_animal_id FROM animals AS a WHERE a.name = animal_name;
        SELECT
            o.name
        INTO owner
        FROM animals AS a
        JOIN owners AS o ON a.owner_id = o.id
        WHERE a.id = given_animal_id;

        IF owner IS NULL
            THEN owner := 'For adoption';
        END IF;
    END;
    $$
LANGUAGE plpgsql;
