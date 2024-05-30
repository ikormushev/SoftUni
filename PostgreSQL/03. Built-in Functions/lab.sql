-- Task 1
SELECT
    title
FROM books
WHERE
    SUBSTRING(title, 1, 3) = 'The'
ORDER BY id;

-- Task 2
SELECT REPLACE(title, 'The', '***')
FROM books
WHERE SUBSTRING(title, 1, 3) = 'The'
ORDER BY id;

-- Task 3
SELECT
    id,
    (side * height) * 1/2 AS area
FROM triangles
ORDER BY id;

-- Task 4
SELECT
    title,
    TRUNC(cost, 3) AS modified_price
FROM books
ORDER BY id;

-- Task 5
SELECT
    first_name,
    last_name,
    EXTRACT(year FROM born) AS year
FROM authors;

-- Task 6
SELECT
    last_name AS "Last Name",
    TO_CHAR(born, 'DD (Dy) Mon YYYY') AS "Date of Birth"
FROM authors;

-- Task 7
SELECT
    title
FROM books
WHERE
    title LIKE 'Harry Potter%'
ORDER BY id;
