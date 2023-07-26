joinery_num = int(input())
joinery_type = input()
delivery_type = input()

price = 0

if joinery_num <= 10:
    print("Invalid order")
else:
    if joinery_type == "90X130":
        price = 110 * joinery_num
        if 30 < joinery_num <= 60:
            price *= 0.95
        elif joinery_num > 60:
            price *= 0.92
    elif joinery_type == "100X150":
        price = 140 * joinery_num
        if 40 < joinery_num <= 80:
            price *= 0.94
        elif joinery_num > 80:
            price *= 0.90
    elif joinery_type == "130X180":
        price = 190 * joinery_num
        if 20 < joinery_num <= 50:
            price *= 0.93
        elif joinery_num > 50:
            price *= 0.88
    elif joinery_type == "200X300":
        price = 250 * joinery_num
        if 25 < joinery_num <= 50:
            price *= 0.91
        elif joinery_num > 50:
            price *= 0.86

    if delivery_type == "With delivery":
        price += 60

    if joinery_num > 99:
        price *= 0.96
    print(f"{price:.2f} BGN")
