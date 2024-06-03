-- Task 7
CREATE OR REPLACE PROCEDURE sp_retrieving_holders_with_balance_higher_than(searched_balance NUMERIC)
AS
    $$
    DECLARE
        holder RECORD;
    BEGIN
        FOR holder IN
            (SELECT
                 ah.first_name,
                 ah.last_name,
                 a.balance
             FROM account_holders AS ah
             JOIN accounts AS a ON ah.id = a.id
             WHERE a.balance > searched_balance)
        LOOP
            RAISE NOTICE 'NOTICE: % % - %', holder.first_name, holder.last_name, holder.balance;
        END LOOP;
    END;
    $$
LANGUAGE plpgsql;


CALL sp_retrieving_holders_with_balance_higher_than(200000);

-- Task 8
CREATE OR REPLACE PROCEDURE sp_deposit_money(account_id INT, money_amount NUMERIC)
AS
    $$
    BEGIN
        UPDATE accounts
        SET balance = balance + money_amount WHERE id = account_id;
        COMMIT;
    END;
    $$
LANGUAGE plpgsql;

-- Task 9
CREATE OR REPLACE PROCEDURE sp_withdraw_money(account_id INT, money_amount NUMERIC)
AS
    $$
    BEGIN
        IF money_amount > (SELECT balance FROM accounts WHERE id = account_id)
            THEN
            RAISE NOTICE 'NOTICE: Insufficient balance to withdraw %', money_amount;
            RETURN;
        END IF;
        UPDATE accounts
        SET balance = balance - money_amount WHERE id = account_id;
        COMMIT;
    END;
    $$
LANGUAGE plpgsql;

CALL sp_withdraw_money(3, 5050.7500);

-- Task 10
CREATE OR REPLACE PROCEDURE sp_transfer_money(sender_id INT, receiver_id INT, amount NUMERIC)
AS
    $$
    BEGIN
        CALL sp_withdraw_money(sender_id,amount);
        CALL sp_deposit_money(receiver_id, amount);
    END;
    $$
LANGUAGE plpgsql;

-- Task 11
DROP PROCEDURE sp_retrieving_holders_with_balance_higher_than;

-- Task 12
CREATE TABLE logs(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    account_id INT,
    old_sum NUMERIC,
    new_sum NUMERIC
);

CREATE OR REPLACE FUNCTION trigger_fn_insert_new_entry_into_logs()
RETURNS TRIGGER
AS
    $$
    BEGIN
        INSERT INTO logs(account_id, old_sum, new_sum)
        VALUES (OLD.id, OLD.balance, NEW.balance);
        RETURN NEW;
    END;
    $$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER tr_account_balance_change
AFTER UPDATE ON accounts
FOR EACH ROW
WHEN (NEW.balance != OLD.balance)
EXECUTE FUNCTION trigger_fn_insert_new_entry_into_logs();

-- Task 13
CREATE TABLE notification_emails(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    recipient_id INT,
    subject TEXT,
    body TEXT
);

CREATE FUNCTION trigger_fn_send_email_on_balance_change()
RETURNS TRIGGER
AS
    $$
    BEGIN
        INSERT INTO notification_emails(recipient_id, subject, body)
        VALUES (OLD.account_id,
                CONCAT('Balance change for account: ', OLD.account_id),
                CONCAT_WS(' ', 'On', CURRENT_DATE,
                          'your balance was changed from',
                          OLD.balance, 'to', NEW.balance));
    END;
    $$
LANGUAGE plpgsql;

CREATE TRIGGER tr_send_email_on_balance_change
AFTER UPDATE ON logs
FOR EACH ROW
EXECUTE FUNCTION trigger_fn_send_email_on_balance_change();
