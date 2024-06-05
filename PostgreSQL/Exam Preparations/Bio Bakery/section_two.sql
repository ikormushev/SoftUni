-- Section 2
CREATE TABLE gift_recipients(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100),
    country_id INT,
    gift_sent BOOLEAN DEFAULT FALSE
);
INSERT INTO gift_recipients(name, country_id)
SELECT
    CONCAT(c.first_name, ' ', c.last_name),
    c.country_id
    FROM customers AS c;
UPDATE gift_recipients
SET gift_sent = TRUE
WHERE country_id IN (7, 8, 14, 17, 26);

UPDATE products AS p
SET price = price * 1.10
WHERE (SELECT
           SUM(f.rate)
       FROM feedbacks AS f
       WHERE f.product_id = p.id) > 8;

DELETE FROM distributors
WHERE name LIKE 'L%';
