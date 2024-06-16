-- Section 2
INSERT INTO addresses(street, town, country, account_id)
SELECT
    a.username,
    a.password,
    a.ip,
    a.age
FROM accounts AS a
WHERE gender = 'F';

UPDATE addresses
SET country = CASE
    WHEN country LIKE 'B%' THEN 'Blocked'
    WHEN country LIKE 'T%' THEN 'Test'
    WHEN country LIKE 'P%' THEN 'In Progress'
    ELSE country
END;

DELETE FROM addresses
WHERE id % 2 = 0 AND street ILIKE '%r%';
