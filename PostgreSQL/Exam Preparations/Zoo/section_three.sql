-- Section 3
SELECT
    v.name,
    v.phone_number,
    v.address,
    v.animal_id,
    v.department_id
FROM volunteers AS v
ORDER BY v.name, v.animal_id, v.department_id;

SELECT
    a.name,
    at.animal_type,
    TO_CHAR(a.birthdate, 'DD.MM.YYYY') AS birthdate
FROM animals AS a
JOIN animal_types AS at ON a.animal_type_id = at.id
ORDER BY a.name;

SELECT
    o.name,
    COUNT(a.id) AS count_of_animals
FROM animals AS a
JOIN owners AS o ON a.owner_id = o.id
GROUP BY o.name
ORDER BY count_of_animals DESC, o.name
LIMIT 5;

SELECT
    CONCAT(o.name, ' - ', a.name) AS "owners-animals",
    o.phone_number,
    ac.cage_id
FROM animals AS a
JOIN animal_types AS at ON a.animal_type_id = at.id
JOIN owners AS o ON a.owner_id = o.id
JOIN animals_cages AS ac ON a.id = ac.animal_id
WHERE at.animal_type = 'Mammals'
ORDER BY o.name, a.name DESC;

SELECT
    v.name AS volunteers,
    v.phone_number,
    SUBSTRING(TRIM(REPLACE(v.address, 'Sofia', '')) FROM 3) AS address
FROM volunteers_departments AS vd
JOIN volunteers AS v ON vd.id = v.department_id
WHERE
    vd.department_name = 'Education program assistant'
    AND v.address LIKE '%Sofia%'
ORDER BY v.name;

SELECT
    a.name,
    EXTRACT(YEAR FROM birthdate) AS birth_year,
    at.animal_type
FROM animals AS a
JOIN animal_types AS at ON a.animal_type_id = at.id
WHERE
    at.animal_type != 'Birds'
    AND a.owner_id IS NULL
    AND a.birthdate > (DATE '01/01/2022' - INTERVAL '5 YEARS')
ORDER BY a.name;
