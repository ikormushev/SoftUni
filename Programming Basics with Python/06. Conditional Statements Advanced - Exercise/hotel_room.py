month = input()
nights = int(input())

studio_price = 0
apartment_price = 0
studio_discount = 0

if month == "May" or month == "October":
    studio_price = nights * 50
    apartment_price = nights * 65
    if 7 < nights <= 14:
        studio_discount = studio_price * 0.05
        studio_price -= studio_discount
    elif nights > 14:
        studio_discount = studio_price * 0.30
        studio_price -= studio_discount
elif month == "June" or month == "September":
    studio_price = nights * 75.20
    apartment_price = nights * 68.70
    if nights > 14:
        studio_discount = studio_price * 0.20
        studio_price -= studio_discount
elif month == "July" or month == "August":
    studio_price = nights * 76
    apartment_price = nights * 77

if nights > 14:
    apartment_discount = apartment_price * 0.10
    apartment_price -= apartment_discount

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
