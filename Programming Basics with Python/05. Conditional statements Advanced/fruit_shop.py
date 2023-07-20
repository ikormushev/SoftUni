fruit = input()
day = input()
amount = float(input())

price = 0

valid_fruit = fruit == "banana" or fruit == "apple" \
              or fruit == "orange" or fruit == "grapefruit" \
              or fruit == "kiwi" or fruit == "pineapple" or fruit == "grapes"
valid_day = day == "Monday" or day == "Tuesday" \
            or day == "Wednesday" or day == "Thursday" \
            or day == "Friday" or day == "Saturday" or day == "Sunday"

if day != "Saturday" and day != "Sunday":
    if fruit == "banana":
        price = 2.50 * amount
    elif fruit == "apple":
        price = 1.20 * amount
    elif fruit == "orange":
        price = 0.85 * amount
    elif fruit == "grapefruit":
        price = 1.45 * amount
    elif fruit == "kiwi":
        price = 2.70 * amount
    elif fruit == "pineapple":
        price = 5.50 * amount
    elif fruit == "grapes":
        price = 3.85 * amount
else:
    if fruit == "banana":
        price = 2.70 * amount
    elif fruit == "apple":
        price = 1.25 * amount
    elif fruit == "orange":
        price = 0.90 * amount
    elif fruit == "grapefruit":
        price = 1.60 * amount
    elif fruit == "kiwi":
        price = 3.00 * amount
    elif fruit == "pineapple":
        price = 5.60 * amount
    elif fruit == "grapes":
        price = 4.20 * amount

if valid_fruit and valid_day:
    print(f"{price:.2f}")
else:
    print("error")
