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

-- Task 3
CREATE PROCEDURE sp_increase_salary_by_id(IN id INT)
AS
    $$
    BEGIN
        IF (SELECT salary
            FROM employees
            WHERE employee_id = id) IS NULL
            THEN ROLLBACK;
        ELSE
        UPDATE employees
        SET salary = salary * 1.05 WHERE employee_id = id;
        END IF;
        COMMIT;
    END;
    $$
LANGUAGE plpgsql;

-- Transaction example
CREATE TABLE bank(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50),
    money FLOAT
);

INSERT INTO bank (name, money) VALUES ('Moncho', 1000), ('Doncho', 500);

CREATE OR REPLACE PROCEDURE money_transfer(IN sender_id INT, IN receiver_id INT, IN transfer_amount FLOAT, OUT status VARCHAR)
AS
    $$
    DECLARE
        sender_savings FLOAT;
        receiver_savings FLOAT;
    BEGIN
        SELECT money FROM bank WHERE id = sender_id INTO sender_savings;
        IF sender_savings < transfer_amount THEN
            status := 'Sender Insufficient funds';
            RETURN;
        END IF;
        SELECT money FROM bank WHERE id = receiver_id INTO receiver_savings;
        UPDATE bank SET money = money - transfer_amount WHERE id = sender_id;
        UPDATE bank SET money = money + transfer_amount WHERE id = receiver_id;

        IF (SELECT money FROM bank WHERE id = sender_id) != sender_savings - transfer_amount THEN
            status := 'Sender Error';
            ROLLBACK;
            RETURN;
        END IF;
        IF (SELECT money FROM bank WHERE id = receiver_id) != receiver_savings + transfer_amount THEN
            status := 'Receiver Error';
            ROLLBACK;
            RETURN;
        END IF;

        status := 'Transaction successful'
        COMMIT;
    END;
    $$
LANGUAGE plpgsql;

CALL money_transfer(2, 1, 1000, null);
SELECT * FROM bank;

-- Task 4
CREATE TABLE deleted_employees(
    employee_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    middle_name VARCHAR(20),
    job_title VARCHAR(50),
    department_id INT,
    salary DECIMAL(19, 4));

CREATE OR REPLACE FUNCTION delete_function()
RETURNS TRIGGER
AS
    $$
    BEGIN
        INSERT INTO deleted_employees(first_name, last_name, middle_name, job_title, department_id, salary)
        VALUES (OLD.first_name, OLD.last_name, OLD.middle_name, OLD.job_title, OLD.department_id, OLD.salary);
        RETURN NULL;
    END;
    $$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER delete_employee_trigger
AFTER DELETE ON employees
FOR EACH ROW EXECUTE FUNCTION delete_function();
