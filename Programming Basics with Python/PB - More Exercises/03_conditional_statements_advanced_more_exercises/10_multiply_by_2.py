number = float(input())

while number >= 0:
    new_number = number * 2
    print(f"Result: {new_number:.2f}")
    number = float(input())
else:
    print("Negative number!")
