square_meters_for_greening = float(input())

price_for_greening = square_meters_for_greening * 7.61
discount = price_for_greening * 0.18
final_price = price_for_greening - discount

print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount} lv.')