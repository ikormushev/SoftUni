-- Task 13
SELECT
    COUNT(CASE WHEN department_id = 1 THEN 1 END) AS "Engineering",
    COUNT(CASE WHEN department_id = 2 THEN 1 END) AS "Tool Design",
    COUNT(CASE WHEN department_id = 3 THEN 1 END) AS "Sales",
    COUNT(CASE WHEN department_id = 4 THEN 1 END) AS "Marketing",
    COUNT(CASE WHEN department_id = 5 THEN 1 END) AS "Purchasing",
    COUNT(CASE WHEN department_id = 6 THEN 1 END) AS "Research and Development",
    COUNT(CASE WHEN department_id = 7 THEN 1 END) AS "Production"
FROM employees;

-- Task 14
UPDATE employees
SET
    salary = CASE
        WHEN hire_date < '2015-01-16' THEN salary + 2500
        WHEN hire_date < '2020-03-04' THEN salary + 1500
        ELSE salary
    END,
    job_title = CASE
        WHEN hire_date < '2015-01-16' THEN CONCAT_WS(' ', 'Senior', job_title)
        WHEN hire_date < '2020-03-04' THEN CONCAT('Mid-', job_title)
        ELSE job_title
    END;

-- Task 15
SELECT
    job_title,
    CASE
        WHEN AVG(salary) > 45800 THEN 'Good'
        WHEN AVG(salary) BETWEEN 27500 AND 45800 THEN 'Medium'
        ELSE 'Need Improvement'
    END AS category
FROM employees
GROUP BY job_title
ORDER BY category, job_title;

-- Task 16
SELECT
    project_name,
    CASE
        WHEN start_date IS NULL AND end_date IS NULL THEN 'Ready for development'
        WHEN end_date IS NULL THEN 'In Progress'
        ELSE 'Done'
    END AS project_status
FROM projects
WHERE project_name LIKE '%Mountain%';

-- Task 17
SELECT
    department_id,
    COUNT(department_id) AS num_employees,
    CASE
        WHEN AVG(salary) > 50000 THEN 'Above average'
        ELSE 'Below average'
    END AS salary_level
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 30000
ORDER BY department_id;

-- Task 18
CREATE VIEW view_performance_rating AS
    SELECT
        first_name,
        last_name,
        job_title,
        salary,
        department_id,
        CASE
            WHEN salary >= 25000 THEN
                CASE
                    WHEN job_title LIKE 'Senior%' THEN 'High-performing Senior'
                    ELSE 'High-performing Employee'
                END
            ELSE 'Average-performing'
        END AS performance_rating
FROM employees;

-- Task 19
CREATE TABLE employees_projects(
    id INT PRIMARY KEY,
    employee_id INT,
    project_id INT,

    FOREIGN KEY (employee_id) REFERENCES  employees(id),
    FOREIGN KEY (project_id) REFERENCES  projects(id)
);

-- Task 20
SELECT
    *
FROM
    departments AS d
JOIN
        employees AS e ON d.id = e.department_id;
