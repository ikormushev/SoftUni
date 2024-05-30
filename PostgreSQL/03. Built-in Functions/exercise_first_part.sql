-- Task 1
CREATE VIEW view_river_info AS
SELECT
    CONCAT_WS(' ',
              'The river',
              river_name,
              'flows into the',
              outflow,
              'and is',
              "length",
              'kilometers long.') AS "River Information"
FROM rivers
ORDER BY river_name;
SELECT * FROM view_river_info;

-- Task 2
CREATE OR REPLACE VIEW view_continents_countries_currencies_details AS
SELECT
    CONCAT_WS(': ',
            con.continent_name,
            con.continent_code)
        AS continent_details,
    CONCAT_WS(' - ',
            cou.country_name,
            cou.capital,
            cou.area_in_sq_km,
            'km2')
        AS country_information,
    CONCAT(cur.description, ' ', '(', cur.currency_code, ')')
        AS currencies
FROM continents AS con, countries AS cou, currencies AS cur
WHERE
    con.continent_code = cou.continent_code
  AND cou.currency_code = cur.currency_code
ORDER BY country_information, currencies;
SELECT * FROM view_continents_countries_currencies_details;

-- Task 3
ALTER TABLE countries
ADD COLUMN capital_code CHAR(2);
UPDATE countries
SET capital_code = SUBSTRING(capital, 1, 2);
SELECT * FROM countries;

-- Task 4
SELECT
    SUBSTRING(description, 5) AS substring
FROM currencies;

-- Task 5
SELECT
    SUBSTRING("River Information", '[0-9]{1,4}') AS river_length
FROM view_river_info;

-- Task 6
SELECT
    REPLACE(mountain_range, 'a', '@') AS replace_a,
    REPLACE(mountain_range, 'A', '$') AS replace_A
FROM mountains;

-- Task 7
SELECT
    capital,
    TRANSLATE(capital, 'áãåçéíñóú', 'aaaceinou') AS translated_name
FROM countries;

-- Task 8
SELECT
    continent_name AS trim,
    TRIM(LEADING FROM continent_name)
FROM continents;

-- Task 9
SELECT
    continent_name AS trim,
    TRIM(TRAILING FROM continent_name)
FROM continents;

-- Task 10
SELECT
    LTRIM(peak_name, 'mM') AS left_trim,
    RTRIM(peak_name, 'mM') AS right_trim
FROM peaks;

-- Task 11
SELECT
    CONCAT_WS(' ', m.mountain_range, p.peak_name) AS mountain_information,
    LENGTH(CONCAT_WS(' ', m.mountain_range, p.peak_name)) AS characters_length,
    BIT_LENGTH(CONCAT_WS(' ', m.mountain_range, p.peak_name)) AS bits_of_a_tring
FROM mountains AS m, peaks AS p
WHERE m.id = p.mountain_id;

-- Task 12
SELECT
    population,
    LENGTH(population :: TEXT) AS length
FROM countries;

-- Task 13
SELECT
    peak_name,
    LEFT(peak_name, 4) AS positive_left,
    LEFT(peak_name, -4) AS negative_left
FROM peaks;

-- Task 14
SELECT
    peak_name,
    RIGHT(peak_name, 4) AS positive_right,
    RIGHT(peak_name, -4) AS negative_right
FROM peaks;

-- Task 15
UPDATE countries
SET iso_code = UPPER(LEFT(country_name, 3))
WHERE iso_code IS NULL;

-- Task 16
UPDATE countries
SET country_code = REVERSE(LOWER(country_code));

-- Task 17
SELECT
    CONCAT_WS(' --->> ', elevation, peak_name) AS "Elevation -->> Peak Name"
FROM peaks
WHERE elevation >= 4884;
