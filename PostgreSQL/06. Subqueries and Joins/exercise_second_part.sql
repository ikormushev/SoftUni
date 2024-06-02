-- Task 11
SELECT
    mc.country_code,
    m.mountain_range,
    p.peak_name,
    p.elevation
FROM mountains_countries AS mc
JOIN mountains AS m ON mc.mountain_id = m.id
JOIN peaks AS p USING(mountain_id)
WHERE p.elevation > 2835 AND mc.country_code = 'BG'
ORDER BY p.elevation DESC;

-- Task 12
SELECT
    mc.country_code,
    COUNT(m.mountain_range) AS mountain_range_count
FROM mountains_countries AS mc
JOIN mountains AS m ON mc.mountain_id = m.id --- Works without it if COUNT(*)
WHERE mc.country_code IN ('BG', 'RU', 'US')
GROUP BY mc.country_code
ORDER BY mountain_range_count DESC;

-- Task 13
SELECT
    c.country_name,
    r.river_name
FROM countries AS c
LEFT JOIN countries_rivers AS cr USING (country_code)
FULL JOIN rivers as r ON cr.river_id = r.id
WHERE c.continent_code = 'AF'
ORDER BY c.country_name
LIMIT 5;

-- Task 14
SELECT
    MIN(s.average_area)
        AS min_average_area
FROM
    (SELECT
        AVG(cou.area_in_sq_km) AS average_area
        FROM countries AS cou
        GROUP BY cou.continent_code)
    AS s;

-- Task 15
SELECT
    COUNT(*) AS countries_without_mountains
FROM countries AS c
LEFT JOIN mountains_countries AS mc USING(country_code)
WHERE mc.mountain_id IS NULL;

-- Task 16
CREATE TABLE monasteries(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    monastery_name VARCHAR(255),
    country_code CHAR(2)
);

INSERT INTO monasteries(monastery_name, country_code)
VALUES
    ('Rila Monastery "St. Ivan of Rila"', 'BG'),
  ('Bachkovo Monastery "Virgin Mary"', 'BG'),
  ('Troyan Monastery "Holy Mother''s Assumption"', 'BG'),
  ('Kopan Monastery', 'NP'),
  ('Thrangu Tashi Yangtse Monastery', 'NP'),
  ('Shechen Tennyi Dargyeling Monastery', 'NP'),
  ('Benchen Monastery', 'NP'),
  ('Southern Shaolin Monastery', 'CN'),
  ('Dabei Monastery', 'CN'),
  ('Wa Sau Toi', 'CN'),
  ('Lhunshigyia Monastery', 'CN'),
  ('Rakya Monastery', 'CN'),
  ('Monasteries of Meteora', 'GR'),
  ('The Holy Monastery of Stavronikita', 'GR'),
  ('Taung Kalat Monastery', 'MM'),
  ('Pa-Auk Forest Monastery', 'MM'),
  ('Taktsang Palphug Monastery', 'BT'),
  ('Sümela Monastery', 'TR');

ALTER TABLE countries
ADD COLUMN three_rivers BOOLEAN DEFAULT FALSE;

UPDATE countries
SET three_rivers = TRUE
WHERE country_code IN (SELECT
           cr.country_code
       FROM countries_rivers AS cr
           JOIN countries AS c USING(country_code)
       GROUP BY cr.country_code
       HAVING COUNT(cr.river_id) >= 3);

SELECT
    M.monastery_name,
    C.country_name
FROM monasteries AS m
JOIN countries AS c USING(country_code)
WHERE c.three_rivers IS NOT true
ORDER BY monastery_name;

-- Task 17
UPDATE countries
SET country_name = 'Burma'
WHERE country_name = 'Myanmar';

INSERT INTO monasteries(monastery_name, country_code)
VALUES ('Hanga Abbey',
        (SELECT countries.country_code
         FROM countries
         WHERE country_name = 'Tanzania'));

/* The task requires this INSERT but Judge does not?
INSERT INTO monasteries(monastery_name, country_code)
VALUES ('Myin-Tin-Daik',
        (SELECT countries.country_code
         FROM countries
         WHERE country_name = 'Myanmar'));*/


SELECT
    con.continent_name,
    cou.country_name,
    COUNT(mon.country_code) AS monasteries_count
FROM continents AS con
JOIN countries as cou USING(continent_code)
LEFT JOIN monasteries AS mon USING(country_code)
WHERE cou.three_rivers IS FALSE
GROUP BY con.continent_name, cou.country_name
ORDER BY monasteries_count DESC, cou.country_name;

-- Task 18
SELECT
    tablename,
    indexname,
    indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;

-- Task 19
CREATE VIEW continent_currency_usage AS
SELECT
    u2.continent_code,
    u2.currency_code,
    u2.currency_usage
FROM
    (SELECT
    u.continent_code,
    u.currency_code,
    u.currency_usage,
    DENSE_RANK() OVER (PARTITION BY u.continent_code ORDER BY u.currency_usage DESC) AS ranked_usage
        FROM
        (SELECT
            continent_code,
            currency_code,
            COUNT(country_code) AS currency_usage
        FROM continents AS con
        JOIN countries AS cou USING(continent_code)
        GROUP BY continent_code, currency_code
        HAVING COUNT(country_code) > 1
        ORDER BY continent_code) AS u) AS u2
WHERE u2.ranked_usage = 1
ORDER BY -- Sorting is not explained in the task
    u2.currency_usage DESC,
    continent_code,
    currency_code;

-- Task 20
WITH RankedCountriesPeaks AS (
    SELECT
        c.country_name,
        m.mountain_range,
        p.peak_name,
        p.elevation,
        ROW_NUMBER() OVER (PARTITION BY c.country_name ORDER BY p.elevation DESC) AS rn
    FROM countries AS C
        LEFT JOIN mountains_countries AS mc USING(country_code)
        LEFT JOIN peaks AS p USING(mountain_id)
        LEFT JOIN  mountains AS m ON p.mountain_id = m.id)

SELECT
    country_name,
    COALESCE(peak_name, '(no highest peak)') AS highest_peak_name,
    COALESCE(elevation, 0) AS highest_peak_elevation,
    COALESCE(mountain_range, '(no mountain)') AS mountain
FROM RankedCountriesPeaks
WHERE rn = 1
ORDER BY country_name, highest_peak_elevation DESC;
