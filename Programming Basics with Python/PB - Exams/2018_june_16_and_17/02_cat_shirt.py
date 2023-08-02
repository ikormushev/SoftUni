sleeve_size_cm = float(input())
front_part_size_cm = float(input())
cloth_type = input()
tie = input()

cloths_prices_m = {
    "Linen": 15,
    "Cotton": 12,
    "Denim": 20,
    "Twill": 16,
    "Flannel": 11
}

shirt_size_cm = 2.2 * (sleeve_size_cm + front_part_size_cm)
shirt_size_m = shirt_size_cm / 100

price = 10 + shirt_size_m * cloths_prices_m[cloth_type]

if tie == "Yes":
    price *= 1.20

print(f"The price of the shirt is : {price:.2f}lv.")
