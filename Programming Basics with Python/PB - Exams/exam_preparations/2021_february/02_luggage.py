luggage_over_20_kg_price = float(input())
luggage_kg = float(input())
days_left = int(input())
luggage_num = int(input())

luggage_price = 0

if luggage_kg < 10:
    luggage_price = 0.20 * luggage_over_20_kg_price
elif 10 <= luggage_kg <= 20:
    luggage_price = 0.50 * luggage_over_20_kg_price
else:
    luggage_price = luggage_over_20_kg_price

if days_left > 30:
    luggage_price *= 1.10
elif 7 <= days_left <= 30:
    luggage_price *= 1.15
else:
    luggage_price *= 1.40

total_price = luggage_price * luggage_num

print(f"The total price of bags is: {total_price:.2f} lv.")
