-- Section 2
INSERT INTO clients(full_name, phone_number)
SELECT
    CONCAT_WS(' ', d.first_name, d.last_name) AS full_name,
    CONCAT('(088) 9999', d.id * 2)
FROM drivers AS d
WHERE d.id BETWEEN 10 AND 20;

UPDATE cars
SET condition = 'C'
WHERE
    (mileage >= 800000 OR mileage IS NULL)
    AND year <= 2010
    AND make != 'Mercedes-Benz'
RETURNING *;

DELETE FROM clients AS c
WHERE
    LENGTH(full_name) > 3
    AND (SELECT COUNT(*)
         FROM courses AS co WHERE c.id = co.client_id) = 0;
