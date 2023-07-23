age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money += 10 * (i / 2)
        money -= 1
    else:
        money += toy_price

money_diff = abs(money - washing_machine_price)

if money >= washing_machine_price:
    print(f"Yes! {money_diff}")
else:
    print(f"No! {money_diff}")
