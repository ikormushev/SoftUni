-- Section 3
SELECT
    p.name,
    p.recipe,
    p.price
FROM products AS p
WHERE p.price > 10 AND p.price < 20
ORDER BY p.price DESC;

SELECT
    f.product_id,
    f.rate,
    f.description,
    c.id AS customer_id,
    c.age,
    c.gender
FROM feedbacks AS f
JOIN customers AS c ON f.customer_id = c.id
WHERE f.rate < 5.0 AND c.gender = 'F' AND c.age > 30
ORDER BY f.product_id DESC;

SELECT
    p.name AS product_name,
    TRUNC(AVG(p.price), 2) AS average_price,
    COUNT(*) AS total_feedbacks
FROM products AS p
JOIN feedbacks AS f ON p.id = f.product_id
WHERE p.price > 15
GROUP BY p.name
HAVING COUNT(*) > 1
ORDER BY total_feedbacks;

SELECT
    i.name AS ingredient_name,
    p.name AS product_name,
    d.name AS distributor_name
FROM ingredients AS i
JOIN products_ingredients AS pi ON i.id = pi.ingredient_id
JOIN products AS p ON pi.product_id = p.id
JOIN distributors AS d ON i.distributor_id = d.id
WHERE i.name ILIKE 'mustard' AND d.country_id = 16
ORDER BY product_name;

SELECT
    d.name AS distributor_name,
    i.name AS ingredient_name,
    p.name AS product_name,
    AVG(f.rate) AS average_rate
FROM distributors AS d
JOIN ingredients AS i ON d.id = i.distributor_id
JOIN products_ingredients AS pi ON i.id = pi.ingredient_id
JOIN products AS p ON pi.product_id = p.id
JOIN feedbacks AS f ON p.id = f.product_id
GROUP BY d.name, i.name, p.name
HAVING AVG(f.rate) BETWEEN 5 AND 8
ORDER BY distributor_name, ingredient_name, product_name;
