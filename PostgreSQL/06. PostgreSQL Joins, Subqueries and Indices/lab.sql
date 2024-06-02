-- Task 1
SELECT
    towns.town_id,
    towns.name AS town_name,
    addresses.address_text
FROM towns
JOIN addresses
    ON addresses.town_id = towns.town_id
WHERE towns.name IN ('San Francisco', 'Sofia', 'Carnation')
ORDER BY town_id, addresses.address_id;

-- Task 2
SELECT
    employees.employee_id,
    CONCAT_WS(' ', employees.first_name, employees.last_name) AS full_name,
    departments.department_id,
    departments.name AS department_name
FROM employees
RIGHT JOIN departments
    ON departments.manager_id = employees.employee_id
ORDER BY employee_id
LIMIT 5;

-- Task 3
SELECT
    e.employee_id,
    CONCAT_WS(' ', e.first_name, e.last_name) AS full_name,
    p.project_id,
    p.name AS project_name
FROM employees AS e
JOIN employees_projects AS e_projects
    ON e.employee_id = e_projects.employee_id
JOIN projects AS p ON e_projects.project_id = p.project_id
WHERE p.project_id = 1;

-- Task 4
SELECT
    COUNT(*)
FROM employees AS e
WHERE e.salary >
      (SELECT AVG(salary)
       FROM employees);
