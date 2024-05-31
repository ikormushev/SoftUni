-- Task 1
CREATE TABLE products(
    product_name VARCHAR(100)
);

INSERT INTO products (product_name)
VALUES
    ('Broccoli'),
    ('Shampoo'),
    ('Toothpaste'),
    ('Candy');

ALTER TABLE products
ADD COLUMN
    id SERIAL PRIMARY KEY;

-- Task 2
ALTER TABLE products
DROP CONSTRAINT products_pkey;
