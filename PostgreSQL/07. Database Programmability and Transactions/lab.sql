-- Task 1
CREATE OR REPLACE FUNCTION fn_count_employees_by_town(
    IN town_name VARCHAR, OUT count INT) AS
$$
    BEGIN
        SELECT COUNT(*)
        FROM employees AS e
        JOIN addresses AS a USING(address_id)
        JOIN towns AS t USING(town_id)
        WHERE t.name = town_name
        INTO count;
    END;
$$
LANGUAGE plpgsql;

-- Task 2
CREATE PROCEDURE sp_increase_salaries(IN department_name VARCHAR)
AS
$$
    BEGIN
        UPDATE employees AS e
        SET salary = salary * 1.05
        WHERE e.department_id = (SELECT d.department_id
                                 FROM departments AS d
                                 WHERE d.name = department_name);
    END;
$$
LANGUAGE plpgsql;
