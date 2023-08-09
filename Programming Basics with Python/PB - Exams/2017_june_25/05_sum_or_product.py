control_number = int(input())

is_combination = False

for a in range(1, 31):
    for b in range(1, 31):
        for c in range(1, 31):
            if (a < b < c) and (a + b + c == control_number):
                is_combination = True
                print(f"{a} + {b} + {c} = {control_number}")
            if (a > b > c) and (a * b * c == control_number):
                is_combination = True
                print(f"{a} * {b} * {c} = {control_number}")

if not is_combination:
    print("No!")
