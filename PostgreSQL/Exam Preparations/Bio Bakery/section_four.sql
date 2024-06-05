-- Section 4
CREATE OR REPLACE FUNCTION fn_feedbacks_for_product(product_name VARCHAR(25))
RETURNS TABLE(
    customer_id INT,
    customer_name VARCHAR(75),
    feedback_description VARCHAR(255),
    feedback_rate NUMERIC(4, 2))
AS
    $$
    BEGIN
        RETURN QUERY (SELECT
                          f.customer_id,
                          c.first_name AS customer_name,
                          f.description AS feedback_description,
                          f.rate AS feedback_rate
                      FROM feedbacks AS f
                        JOIN products AS p ON f.product_id = p.id
                      JOIN customers AS c ON f.customer_id = c.id
                      WHERE p.name = product_name
                      ORDER BY f.customer_id);
    END;
    $$
LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE sp_customer_country_name(customer_full_name VARCHAR(50), OUT country_name VARCHAR(50))
AS
    $$
    BEGIN
        SELECT c.name INTO country_name
            FROM customers AS cu
                JOIN countries AS c
                    ON cu.country_id = c.id
            WHERE CONCAT(cu.first_name, ' ', cu.last_name) = customer_full_name;
    END;
    $$
LANGUAGE plpgsql;
