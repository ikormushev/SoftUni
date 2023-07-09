vacation_price = float(input())
puzzles_num = int(input())
talking_dolls_num = int(input())
teddy_bears_num = int(input())
minions_num = int(input())
trucks_num = int(input())

puzzle_price = 2.6
talking_doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

toys_num = puzzles_num + talking_dolls_num + teddy_bears_num + minions_num + trucks_num

puzzles = puzzles_num * puzzle_price
talking_dolls = talking_dolls_num * talking_doll_price
teddy_bears = teddy_bears_num * teddy_bear_price
minions = minions_num * minion_price
trucks = trucks_num * truck_price
full_price = puzzles + talking_dolls + teddy_bears + minions + trucks

if toys_num >= 50:
    discount = 0.25 * full_price
    full_price = full_price - discount

rent = full_price * 0.1
full_price = full_price - rent
money_difference = abs(full_price - vacation_price)

if full_price >= vacation_price:
    print(f"Yes! {money_difference:.2f} lv left.")
else:
    print(f"Not enough money! {money_difference:.2f} lv needed.")
