budget = int(input())
towel_price = float(input())
discount = int(input()) / 100

umbrella_price = towel_price * 2/3
flip_flops_price = umbrella_price * 0.75
bag_price = (towel_price + flip_flops_price) * 1/3

price = towel_price + umbrella_price + flip_flops_price + bag_price
price *= 1 - discount

money_diff = abs(budget - price)

if budget >= price:
    print(f"Annie's sum is {price:.2f} lv. She has {money_diff:.2f} lv. left.")
else:
    print(f"Annie's sum is {price:.2f} lv. She needs {money_diff:.2f} lv. more.")
