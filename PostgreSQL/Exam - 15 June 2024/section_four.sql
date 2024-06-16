-- Section 4
CREATE OR REPLACE FUNCTION udf_accounts_photos_count(account_username VARCHAR(30))
RETURNS INT
AS
    $$
    DECLARE
        given_account_id INT;
        photos_num INT;
    BEGIN
        SELECT a.id INTO given_account_id FROM accounts as a WHERE a.username = account_username;

        SELECT
            COUNT(ap.photo_id)
        INTO photos_num
        FROM accounts_photos AS ap
        WHERE ap.account_id = given_account_id;

        IF photos_num IS NULL THEN photos_num = 0;
        END IF;
        RETURN photos_num;
    END;
    $$
LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE udp_modify_account(address_street VARCHAR(30), address_town VARCHAR(30))
AS
    $$
    DECLARE
        given_account_id INT;
    BEGIN
        SELECT
            a.account_id
        INTO given_account_id FROM addresses AS a
        WHERE a.street = address_street AND a.town = address_town;

        IF given_account_id IS NULL THEN RETURN;
        END IF;

        UPDATE accounts
        SET job_title = CONCAT('(Remote) ', job_title)
        WHERE id = given_account_id;
    END;
    $$
LANGUAGE plpgsql;
