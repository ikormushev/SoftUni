-- Task 1
SELECT
    department_id,
    COUNT(department_id) AS employee_count
FROM employees
GROUP BY department_id
ORDER BY department_id;

-- Task 2
SELECT
    department_id,
    COUNT(salary) AS employee_count
FROM employees
GROUP BY department_id
ORDER BY department_id;

-- Task 3
SELECT
    department_id,
    SUM(salary) AS total_salaries
FROM employees
GROUP BY department_id
ORDER BY department_id;

-- Task 4
SELECT
    department_id,
    MAX(salary) AS total_salaries
FROM employees
GROUP BY department_id
ORDER BY department_id;

-- Task 5
SELECT
    department_id,
    MIN(salary) AS total_salaries
FROM employees
GROUP BY department_id
ORDER BY department_id;

-- Task 6
SELECT
    department_id,
    AVG(salary) AS total_salaries
FROM employees
GROUP BY department_id
ORDER BY department_id;

-- Task 7
SELECT
    department_id,
    SUM(salary) AS total_salaries
FROM employees
GROUP BY department_id
HAVING SUM(salary) < 4200
ORDER BY department_id;

-- Task 8
SELECT
    id,
    first_name,
    last_name,
    TRUNC(salary, 2) AS salary,
    department_id,
    CASE
        WHEN department_id = 1 THEN 'Management'
        WHEN department_id = 2 THEN 'Kitchen Staff'
        WHEN department_id = 3 THEN 'Service Staff'
        ELSE 'Other'
    END AS department_name
FROM employees
ORDER BY id;
