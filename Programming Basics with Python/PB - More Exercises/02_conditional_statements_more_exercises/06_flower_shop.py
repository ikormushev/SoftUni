from math import ceil, floor

magnolias_num = int(input())
hyacinths_num = int(input())
roses_num = int(input())
cacti_num = int(input())
gift_price = float(input())

magnolia_price = 3.25
hyacinth_price = 4
rose_price = 3.50
cactus_price = 8

magnolias = magnolias_num * magnolia_price
hyacinths = hyacinths_num * hyacinth_price
roses = roses_num * rose_price
cacti = cacti_num * cactus_price

flowers_full_price = magnolias + hyacinths + roses + cacti
tax = flowers_full_price * 0.05
full_price = flowers_full_price - tax

money_difference = abs(full_price - gift_price)

if full_price >= gift_price:
    money_difference = floor(money_difference)
    print(f"She is left with {money_difference} leva.")
else:
    money_difference = ceil(money_difference)
    print(f"She will have to borrow {money_difference} leva.")
