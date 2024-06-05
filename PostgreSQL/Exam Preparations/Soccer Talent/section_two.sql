-- Section 2
INSERT INTO coaches(first_name, last_name, salary, coach_level)
SELECT
    p.first_name,
    p.last_name,
    p.salary * 2 AS salary,
    CHAR_LENGTH(p.first_name) AS coach_level
    FROM players AS p WHERE p.hire_date < '2013-12-13 07:18:46';

UPDATE coaches AS c
SET salary = salary * coach_level
WHERE
    first_name LIKE 'C%'
  AND (SELECT COUNT(*) FROM players_coaches AS pc
                       WHERE pc.coach_id = c.id) >= 1;

DELETE FROM players_coaches
WHERE player_id IN (SELECT p.id FROM players AS p WHERE hire_date < '2013-12-13 07:18:46');

DELETE FROM players
WHERE hire_date < '2013-12-13 07:18:46';
