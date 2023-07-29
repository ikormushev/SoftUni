fruit_type = input()
set_size = input()
sets_number = int(input())

double_set_piece_price = {
    "Watermelon": 56,
    "Mango": 36.66,
    "Pineapple": 42.10,
    "Raspberry": 20
}

quintuple_set_piece_price = {
    "Watermelon": 28.70,
    "Mango": 19.60,
    "Pineapple": 24.80,
    "Raspberry": 15.20
}

price = 0

if set_size == "small":
    price = (double_set_piece_price[fruit_type] * 2) * sets_number
elif set_size == "big":
    price = (quintuple_set_piece_price[fruit_type] * 5) * sets_number

if 400 <= price < 1000:
    price *= 0.85
elif price > 1000:
    price *= 0.50

print(f"{price:.2f} lv.")
