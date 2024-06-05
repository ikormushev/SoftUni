-- Section 3
SELECT
    CONCAT(p.first_name, ' ', p.last_name) AS full_name,
    p.age,
    p.hire_date
FROM players AS p
WHERE p.first_name LIKE 'M%'
ORDER BY p.age DESC, full_name;

SELECT
    p.id,
    CONCAT(p.first_name, ' ', p.last_name) AS full_name,
    p.age,
    p.position,
    p.salary,
    sd.pace,
    sd.shooting
FROM players AS p
JOIN skills_data AS sd ON p.skills_data_id = sd.id
WHERE
    p.team_id IS NULL
  AND p.position = 'A'
  AND (sd.pace + sd.shooting > 130);

SELECT
    t.id AS team_id,
    t.name AS team_name,
    CASE
        WHEN COUNT(p.id) IS NOT NULL THEN  COUNT(p.id)
        ELSE 0
    END AS player_count,
    t.fan_base
FROM teams AS t
LEFT JOIN players AS p ON t.id = p.team_id
WHERE t.fan_base > 30000
GROUP BY t.id, t.name, t.fan_base
ORDER BY player_count DESC, t.fan_base DESC;

SELECT
    CONCAT(c.first_name, ' ', c.last_name) AS coach_full_name,
    CONCAT(p.first_name, ' ', p.last_name) AS player_full_name,
    t.name AS team_name,
    sd.passing,
    sd.shooting,
    sd.speed
FROM players_coaches AS pc
JOIN players AS p ON pc.player_id = p.id
JOIN coaches AS c ON pc.coach_id = c.id
JOIN teams AS t ON p.team_id = t.id
JOIN skills_data AS sd ON p.skills_data_id = sd.id
ORDER BY coach_full_name, player_full_name DESC;
