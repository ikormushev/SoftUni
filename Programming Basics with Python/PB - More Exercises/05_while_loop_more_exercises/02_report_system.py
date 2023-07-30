expected_amount = int(input())

paying_cash_num = 0
cash = 0
paying_card_num = 0
card = 0

paying_num = 0
collected_amount = 0
is_successful_transaction = True

while collected_amount < expected_amount:
    data = input()
    if data == "End":
        break
    product_price = int(data)
    paying_num += 1
    if paying_num % 2 == 1:
        if product_price > 100:
            is_successful_transaction = False
        else:
            is_successful_transaction = True
            paying_cash_num += 1
            cash += product_price
    else:
        if product_price < 10:
            is_successful_transaction = False
        else:
            is_successful_transaction = True
            paying_card_num += 1
            card += product_price
    if is_successful_transaction:
        collected_amount += product_price
        print("Product sold!")
    else:
        print("Error in transaction!")

if collected_amount < expected_amount:
    print("Failed to collect required money for charity.")
else:
    average_cash = cash / paying_cash_num
    average_card = card / paying_card_num
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}")
