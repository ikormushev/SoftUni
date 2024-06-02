-- Task 1
SELECT
    CONCAT_WS(' ', a.address, a.address_2) AS apartment_address,
    b.booked_for AS nights
FROM apartments AS a
JOIN bookings AS b USING(booking_id)
ORDER BY a.apartment_id;

-- Task 2
SELECT
    a.name AS name,
    a.country AS country,
    b.booked_at::DATE AS booked_at
FROM apartments AS a
LEFT JOIN bookings AS b USING (booking_id)
LIMIT 10;

-- Task 3
SELECT
    b.booking_id AS booking_id,
    b.starts_at::DATE AS starts_at,
    b.apartment_id AS apartment_id,
    CONCAT_WS(' ', c.first_name, c.last_name) AS customer_name
FROM bookings AS b
RIGHT JOIN customers AS c
    ON b.customer_id = c.customer_id
ORDER BY customer_name
LIMIT 10;

-- Task 4
SELECT
    b.booking_id,
    a.name AS apartment_owner,
    a.apartment_id,
    CONCAT_WS(' ', c.first_name, c.last_name) AS customer_name
FROM bookings AS b
FULL JOIN apartments AS a USING (booking_id)
FULL JOIN customers AS c USING (customer_id)
ORDER BY b.booking_id, apartment_owner, customer_name;

-- Task 5
SELECT
    b.booking_id,
    c.first_name AS customer_name
FROM bookings AS b
CROSS JOIN customers AS c
ORDER BY customer_name;

-- Task 6
SELECT
    booking_id,
    apartment_id,
    c.companion_full_name
FROM bookings AS b
JOIN customers AS c USING(customer_id)
WHERE b.apartment_id IS NULL;

-- Task 7
SELECT
    apartment_id,
    booked_for,
    first_name,
    country
FROM bookings AS b
JOIN customers AS c USING(customer_id)
WHERE c.job_type = 'Lead';

-- Task 8
SELECT
    COUNT(*)
FROM bookings
JOIN customers USING(customer_id)
WHERE last_name = 'Hahn';

-- Task 9
SELECT
    a.name,
    SUM(b.booked_for)
FROM apartments AS a
JOIN bookings AS b USING (apartment_id)
GROUP BY a.name
ORDER BY a.name;

-- Task 10
SELECT
    a.country,
    COUNT(b.booking_id) AS booking_count
FROM bookings AS b
JOIN apartments AS a
    USING (apartment_id)
WHERE
    b.booked_at > '2021-05-18 07:52:09.904+03' AND
    b.booked_at < '2021-09-17 19:48:02.147+03'
GROUP BY country
ORDER BY booking_count DESC;
