/* Task 1 */
SELECT
    id,
    first_name || ' ' || last_name AS "Full Name",
    job_title as "Job Title"
FROM employees;

/* Task 2 */
SELECT
    id,
    first_name || ' ' || last_name AS full_name,
    job_title,
    salary
FROM employees
WHERE salary >= 1000.00
ORDER BY id;

/* Task 3 */
SELECT
    id,
    first_name,
    last_name,
    job_title,
    department_id,
    salary
FROM employees
WHERE department_id = 4 AND salary >= 1000
ORDER BY id;

/* Task 4 */
INSERT INTO employees (first_name, last_name, job_title, department_id, salary)
VALUES
    ('Samantha', 'Young', 'Housekeeping', 4, 900),
    ('Roger', 'Palmer', 'Waiter', 3, 928.33);
SELECT * from employees;

/* Task 5 */
UPDATE employees
SET salary = salary + 100
WHERE job_title = 'Manager';
SELECT * from employees
WHERE job_title = 'Manager';

/* Task 6 */
DELETE FROM employees
WHERE department_id = 1 OR department_id = 2;
SELECT * FROM employees
ORDER BY id;

/* Task 7 */
CREATE VIEW top_paid_employee_view AS
SELECT * FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);
SELECT * FROM top_paid_employee_view;
