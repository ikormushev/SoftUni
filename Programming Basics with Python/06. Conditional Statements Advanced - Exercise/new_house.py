flower_type = input()
flowers_number = int(input())
budget = int(input())

price = 0
money_change = 0

if flower_type == "Roses":
    price = flowers_number * 5
    if flowers_number > 80:
        money_change = price * 0.10
        price -= money_change
elif flower_type == "Dahlias":
    price = flowers_number * 3.80
    if flowers_number > 90:
        money_change = price * 0.15
        price -= money_change
elif flower_type == "Tulips":
    price = flowers_number * 2.80
    if flowers_number > 80:
        money_change = price * 0.15
        price -= money_change
elif flower_type == "Narcissus":
    price = flowers_number * 3
    if flowers_number < 120:
        money_change = price * 0.15
        price += money_change
elif flower_type == "Gladiolus":
    price = flowers_number * 2.50
    if flowers_number < 80:
        money_change = price * 0.20
        price += money_change

money_left = abs(budget - price)

if budget >= price:
    print(f"Hey, you have a great garden with {flowers_number} "
          f"{flower_type} and {money_left:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_left:.2f} leva more.")
