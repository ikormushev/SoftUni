-- TASK 1
SELECT * FROM cities
ORDER BY id;

-- TASK 2
SELECT
    concat(name, ' ', state) as cities_information,
    area as area_km2
FROM cities
ORDER BY id;

-- TASK 3
SELECT
    DISTINCT name,
    area as area_km2
FROM cities
ORDER BY name DESC;

-- TASK 4
SELECT
    id,
    concat(first_name, ' ', last_name) AS full_name,
    job_title
FROM employees
ORDER BY first_name
LIMIT 50;

-- TASK 5
SELECT
    id AS id,
    concat(first_name, ' ', middle_name, ' ', last_name) AS full_name,
    hire_date
FROM employees
ORDER BY hire_date
OFFSET 9;

-- TASK 6
SELECT
    id,
    concat(number, ' ', street) AS address,
    city_id
FROM addresses
WHERE (id >= 20);

-- TASK 7
SELECT
    concat(number, ' ', street) AS address,
    city_id
FROM addresses
WHERE city_id > 0 AND city_id % 2 = 0
ORDER BY city_id;

-- TASK 8
SELECT
    name,
    start_date,
    end_date
FROM projects
WHERE
    start_date >= '2016-06-01 07:00:00'
  AND end_date < '2023-06-04 00:00:00'
ORDER BY start_date;

-- TASK 9
SELECT
    number,
    street
FROM addresses
WHERE
    (id >= 50 AND id <= 100)
   OR number < 1000;

-- TASK 10
SELECT
    employee_id,
    project_id
FROM employees_projects
WHERE
    employee_id IN (200, 250)
  AND project_id NOT IN (50, 100);

-- TASK 11
SELECT
    name,
    start_date
FROM projects
WHERE name IN ('Mountain', 'Road', 'Touring')
LIMIT 20;

-- TASK 12
SELECT
    concat(first_name, ' ', last_name) AS full_name,
    job_title,
    salary
FROM employees
WHERE salary IN (12500, 14000, 23600, 25000)
ORDER BY salary DESC;

-- TASK 13
SELECT
    id,
    first_name,
    last_name
FROM employees
WHERE middle_name is NULL
LIMIT 3;

-- TASK 14
INSERT INTO departments (department, manager_id)
VALUES
    ('Finance', 3),
    ('Information Services', 42),
    ('Document Control', 90),
    ('Quality Assurance', 274),
    ('Facilities and Maintenance', 218),
    ('Shipping and Receiving', 85),
    ('Executive', 109);
SELECT * FROM departments;

-- TASK 15
CREATE TABLE company_chart AS
    SELECT
        concat(first_name, ' ', last_name) AS full_name,
        job_title,
        department_id,
        manager_id
FROM employees;
SELECT * FROM company_chart;

-- TASK 16
UPDATE projects
SET end_date = start_date + INTERVAL '5 months'
WHERE end_date is NULL;
SELECT * from projects;

-- TASK 17
UPDATE employees
SET
    salary = salary + 1500,
    job_title = concat('Senior', ' ', job_title)
WHERE hire_date BETWEEN '1998-01-01' AND'2000-01-05';

-- TASK 18
DELETE FROM addresses
WHERE city_id IN (5, 17, 20, 30);

-- TASK 19
CREATE VIEW view_company_chart AS
SELECT
    full_name,
    job_title
FROM company_chart
WHERE manager_id = 184;

-- TASK 20
CREATE VIEW view_addresses AS
SELECT
    CONCAT(e.first_name, ' ', e.last_name) AS full_name,
    e.department_id,
    CONCAT(a.number, ' ', a.street) AS address
FROM
    employees AS e, addresses AS a
WHERE  a.id = e.address_id
ORDER BY address;

-- TASK 21
ALTER VIEW view_addresses RENAME TO view_employee_addresses_info;

-- TASK 22
DROP VIEW view_company_chart;

-- TASK 23
UPDATE projects
SET name = UPPER(name);

-- TASK 24
CREATE VIEW view_initials AS
SELECT
    SUBSTRING(first_name FOR 2) AS initial,
    last_name
FROM employees
ORDER BY last_name;
SELECT * FROM view_initials;

-- TASK 25
SELECT
    name,
    start_date
FROM projects
WHERE
    name LIKE 'MOUNT%'
ORDER BY id;
