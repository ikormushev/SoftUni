-- Task 1
SELECT
    COUNT(id)
FROM wizard_deposits;

-- Task 2
SELECT
    SUM(deposit_amount)
FROM wizard_deposits;

-- Task 3
SELECT
    TRUNC(AVG(magic_wand_size), 3)
        AS average_magic_wand_size
FROM wizard_deposits;

-- Task 4
SELECT
    MIN(deposit_charge)
FROM wizard_deposits;

-- Task 5
SELECT
    MAX(age)
FROM wizard_deposits;

-- Task 6
SELECT
    deposit_group,
    SUM(deposit_interest)
        AS deposit_interest
FROM wizard_deposits
GROUP BY deposit_group
ORDER BY deposit_interest DESC;

-- Task 7
SELECT
    magic_wand_creator,
    MIN(magic_wand_size) AS minimum_wand_size
FROM wizard_deposits
GROUP BY magic_wand_creator
ORDER BY minimum_wand_size
LIMIT 5;

-- Task 8
SELECT
    deposit_group,
    is_deposit_expired,
    FLOOR(AVG(deposit_interest)) AS deposit_interest
FROM wizard_deposits
WHERE
    deposit_start_date > '1985-01-01'
GROUP BY
    deposit_group,
    is_deposit_expired
ORDER BY
    deposit_group DESC,
    is_deposit_expired;

-- Task 9
SELECT
    last_name,
    COUNT(*) AS notes_with_dumbledore
FROM wizard_deposits
WHERE
    notes ILIKE '%Dumbledore%'
GROUP BY last_name;

-- Task 10
CREATE VIEW view_wizard_deposits_with_expiration_date_before_1983_08_17 AS
    SELECT
        CONCAT_WS(' ', first_name, last_name) AS wizard_name,
        deposit_start_date AS start_date,
        deposit_expiration_date AS expiration_date,
        deposit_amount AS amount
FROM wizard_deposits
WHERE deposit_expiration_date <= '1983-08-17'
GROUP BY
    wizard_name,
    start_date,
    expiration_date,
    amount
ORDER BY expiration_date;

-- Task 11
SELECT
    magic_wand_creator,
    MAX(deposit_amount) AS max_deposit_amount
FROM wizard_deposits
GROUP BY magic_wand_creator
HAVING
    MAX(deposit_amount) NOT BETWEEN 20000 AND 40000
ORDER BY max_deposit_amount DESC
LIMIT 3;

-- Task 12
SELECT
    CASE
        WHEN age BETWEEN 0 AND 10 THEN '[0-10]'
        WHEN age BETWEEN 11 AND 20 THEN '[11-20]'
        WHEN age BETWEEN 21 AND 30 THEN '[21-30]'
        WHEN age BETWEEN 31 AND 40 THEN '[31-40]'
        WHEN age BETWEEN 41 AND 50 THEN '[41-50]'
        WHEN age BETWEEN 51 AND 60 THEN '[51-60]'
        ELSE '[61+]'
    END AS age_group,
    COUNT(*) AS count
FROM wizard_deposits
GROUP BY age_group
ORDER BY age_group;
