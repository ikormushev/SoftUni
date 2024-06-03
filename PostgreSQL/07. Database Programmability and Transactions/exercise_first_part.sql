-- Task 1
CREATE FUNCTION fn_full_name(first_name VARCHAR, last_name VARCHAR)
RETURNS VARCHAR
AS
    $$
    BEGIN
        IF first_name IS NULL AND last_name IS NULL
            THEN RETURN NULL;
        END IF;
        IF first_name IS NULL
            THEN RETURN INITCAP(last_name);
        END IF;
        IF last_name IS NULL
            THEN RETURN INITCAP(first_name);
        END IF;
        RETURN CONCAT(INITCAP(first_name), ' ', INITCAP(last_name));
    END;
    $$
LANGUAGE plpgsql;

-- Task 2
CREATE FUNCTION fn_calculate_future_value(IN initial_sum NUMERIC,
                                          IN yearly_interest_rate NUMERIC,
                                          IN number_of_years INT,
                                          OUT future_value numeric)
AS
    $$
    BEGIN
        future_value :=
            TRUNC(initial_sum * ((1 + yearly_interest_rate)^number_of_years), 4);
    END;
    $$
LANGUAGE plpgsql;

-- Task 3
CREATE FUNCTION fn_is_word_comprised(IN set_of_letters VARCHAR(50), IN word VARCHAR(50))
RETURNS BOOL
AS
    $$
    DECLARE
        new_word VARCHAR(50) := LOWER(word);
        new_set VARCHAR(50) := LOWER(set_of_letters);
        word_length INT := LENGTH(word);
        current_num INT := 1;
        current_letter CHAR;
    BEGIN
        WHILE current_num <= word_length LOOP
            current_letter := SUBSTRING(new_word FROM current_num FOR 1);

            IF current_letter ~ '[a-z]' THEN
                IF POSITION(current_letter IN new_set) = 0 THEN
                    RETURN FALSE;
                END IF;
            END IF;
            current_num := current_num + 1;
        END LOOP;
        RETURN TRUE;
    END;
    $$
LANGUAGE plpgsql;
