-- Task 18
CREATE TABLE bookings_calculation AS
    SELECT
        booked_for
    FROM bookings
WHERE apartment_id = 93;

ALTER TABLE bookings_calculation
ADD COLUMN multiplication NUMERIC,
ADD COLUMN modulo NUMERIC;

UPDATE bookings_calculation
SET
    multiplication = booked_for * 50,
    modulo = booked_for % 50;

-- Task 19
SELECT
    latitude,
    ROUND(latitude, 2) AS round,
    TRUNC(latitude, 2) AS trunc
FROM apartments;

-- Task 20
SELECT
    longitude,
    ABS(longitude)
FROM apartments;

-- Task 21
ALTER TABLE bookings
ADD COLUMN billing_day TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP;
SELECT
    billing_day,
    TO_CHAR(billing_day, 'DD "Day" MM "Month" YYYY "Year" HH24:MI:SS') AS "Billing Day"
FROM bookings;

-- Task 22
SELECT
    EXTRACT(YEAR FROM booked_at AT TIME ZONE 'UTC') AS YEAR,
    EXTRACT(MONTH FROM booked_at AT TIME ZONE 'UTC') AS MONTH,
    EXTRACT(DAY FROM booked_at AT TIME ZONE 'UTC') AS DAY,
    EXTRACT(HOUR FROM booked_at AT TIME ZONE 'UTC') AS HOUR,
    EXTRACT(MINUTE FROM booked_at AT TIME ZONE 'UTC') AS MINUTE,
    CEILING(EXTRACT(SECOND FROM booked_at AT TIME ZONE 'UTC')) AS SECOND
FROM bookings;

-- Task 23
SELECT
    user_id,
    AGE(starts_at, booked_at) AS early_birds
FROM bookings
WHERE AGE(starts_at, booked_at) >= INTERVAL '10 MONTHS';

-- Task 24
SELECT
    companion_full_name,
    email
FROM users
WHERE
    companion_full_name ILIKE '%aNd%'
    AND
    email NOT LIKE '%@gmail';

-- Task 25
SELECT
    LEFT(first_name, 2) AS initials,
    COUNT('initials') AS user_count
FROM users
GROUP BY initials
ORDER BY user_count DESC, initials;

-- Task 26
SELECT
    SUM(booked_for) AS total_value
FROM bookings
WHERE apartment_id = 90;

-- Task 27
SELECT
    AVG(multiplication) AS average_value
FROM bookings_calculation;
