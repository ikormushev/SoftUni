age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toys_num = 0
money_gift = 0
money_collected = 0

for b in range(1, age + 1):  # b == birthday
    if b % 2 == 1:
        toys_num += 1
    else:
        money_gift += 10
        money_collected += money_gift
        money_collected -= 1

toys = toy_price * toys_num
total_money = toys + money_collected

money_diff = abs(washing_machine_price - total_money)

if total_money >= washing_machine_price:
    print(f"Yes! {money_diff:.2f}")
else:
    print(f"No! {money_diff:.2f}")
