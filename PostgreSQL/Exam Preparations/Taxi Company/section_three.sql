-- Section 3
SELECT
    c.make,
    c.model,
    c.condition
FROM cars AS c
ORDER BY c.id;

SELECT
    d.first_name,
    d.last_name,
    c.make,
    c.model,
    c.mileage
FROM drivers AS d
JOIN cars_drivers AS cd ON d.id = cd.driver_id
JOIN cars AS c ON cd.car_id = c.id
WHERE c.mileage IS NOT NULL
ORDER BY c.mileage DESC,
         d.first_name;

SELECT
    c.id AS car_id,
    c.make,
    c.mileage,
    COUNT(co.car_id) AS count_of_courses,
    ROUND(AVG(co.bill), 2) AS average_bill
FROM cars AS c
LEFT JOIN courses AS co ON c.id = co.car_id
GROUP BY c.id, c.make, c.mileage
HAVING COUNT(co.car_id) != 2
ORDER BY count_of_courses DESC, c.id;

SELECT
    cl.full_name,
    COUNT(c.client_id) AS count_of_cars,
    SUM(c.bill) AS total_sum
FROM courses AS c
JOIN clients AS cl ON c.client_id = cl.id
WHERE SUBSTRING(cl.full_name FROM 2 FOR 1) = 'a'
GROUP BY cl.full_name
HAVING COUNT(c.client_id) > 1
ORDER BY full_name;

SELECT
    a.name,
    CASE
        WHEN EXTRACT(HOUR FROM c.start) BETWEEN 6 AND 20 THEN 'Day'
        ELSE 'Night'
    END AS day_time,
    c.bill,
    cl.full_name,
    ca.make,
    ca.model,
    cat.name
FROM courses AS c
JOIN addresses AS a ON c.from_address_id = a.id
JOIN clients AS cl ON c.client_id = cl.id
JOIN cars AS ca ON c.car_id = ca.id
JOIN categories AS cat ON ca.category_id = cat.id
ORDER BY c.id;
