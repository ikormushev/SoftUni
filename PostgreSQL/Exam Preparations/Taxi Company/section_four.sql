-- Section 4
CREATE FUNCTION fn_courses_by_client(phone_num VARCHAR(20))
RETURNS INT
AS
    $$
    DECLARE
        wanted_id INT;
        courses_num INT := 0;
    BEGIN
        SELECT id INTO wanted_id
                  FROM clients AS c
                  WHERE c.phone_number = phone_num;

        SELECT COUNT(*) INTO courses_num
        FROM courses AS c
        WHERE c.client_id = wanted_id;

        RETURN courses_num;
    END;
    $$
LANGUAGE plpgsql;

CREATE TABLE search_results(
    id SERIAL PRIMARY KEY,
    address_name VARCHAR(50),
    full_name VARCHAR(100),
    level_of_bill VARCHAR(20),
    make VARCHAR(30),
    condition CHAR(1),
    category_name VARCHAR(50)
);

CREATE OR REPLACE PROCEDURE sp_courses_by_address(address_name VARCHAR(100))
AS
    $$
    DECLARE
        wanted_address_id INT;
        info RECORD;
    BEGIN
        TRUNCATE TABLE search_results;
        SELECT a.id INTO wanted_address_id
                    FROM addresses AS a
                    WHERE a.name = address_name;

        FOR info IN (SELECT
                         cl.full_name,
                         CASE
                            WHEN c.bill <= 20 THEN 'Low'
                            WHEN c.bill <= 30 THEN 'Medium'
                            ELSE 'High'
                            END AS level_of_bill,
                        ca.make,
                        ca.condition,
                        cat.name AS category_name
                     FROM courses AS c
                     JOIN clients AS cl ON c.client_id = cl.id
                     JOIN cars AS ca ON c.car_id = ca.id
                     JOIN categories AS cat ON ca.category_id = cat.id
                     WHERE c.from_address_id =
                           wanted_address_id
                     ORDER BY ca.make, cl.full_name) LOOP
        INSERT INTO search_results(address_name, full_name, level_of_bill, make, condition, category_name)
        VALUES (address_name,
                info.full_name,
                info.level_of_bill,
                info.make,
                info.condition,
                info.category_name);
        END LOOP;
    END;
    $$
LANGUAGE plpgsql;
