-- Task 11
ALTER TABLE countries
ADD
    CONSTRAINT fk_countries_continents
    FOREIGN KEY
        (continent_code)
        REFERENCES
            continents(continent_code)
        ON DELETE CASCADE,
ADD
    CONSTRAINT fk_countries_currencies
    FOREIGN KEY
        (currency_code)
        REFERENCES
            currencies(currency_code)
        ON DELETE CASCADE;

-- Task 12
ALTER TABLE countries_rivers
ADD CONSTRAINT fk_rivers
FOREIGN KEY (river_id) REFERENCES rivers(id) ON UPDATE CASCADE,
ADD CONSTRAINT fk_countries
FOREIGN KEY (country_code) REFERENCES countries(country_code) ON UPDATE CASCADE;

-- Task 13
CREATE TABLE customers(
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(50)
);

CREATE TABLE contacts(
    id SERIAL PRIMARY KEY,
    contact_name VARCHAR(50),
    phone VARCHAR(30),
    email VARCHAR(30),
    customer_id INT,

    CONSTRAINT fk_customer_id
    FOREIGN KEY (customer_id)
    REFERENCES customers(id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);

INSERT INTO customers(customer_name)
VALUES
    ('BlueBird Inc'),
    ('Dolphin LLC');

INSERT INTO contacts(contact_name, phone, email, customer_id)
VALUES
    ('John Doe', '(408)-111-1234', 'john.doe@bluebird.dev', 1),
    ('Jane Doe', '(408)-111-1235', 'jane.doe@bluebird.dev', 1),
    ('David Wright', '(408)-222-1234', 'david.wright@dolphin.dev', 2);

DELETE FROM customers WHERE id = 1;

-- Task 14
SELECT
    mountain_range,
    peak_name,
    elevation
FROM peaks
JOIN mountains
ON peaks.mountain_id = mountains.id
WHERE mountain_range LIKE '%Rila%'
ORDER BY elevation DESC;

-- Task 15
SELECT
    COUNT(*) AS countries_without_rivers
FROM
    countries
LEFT JOIN countries_rivers
ON countries.country_code = countries_rivers.country_code
WHERE river_id IS NULL;
