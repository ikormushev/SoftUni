number = int(input())

is_valid = False

for a in range(1, 9):
    if is_valid:
        break
    for b in range(9, a, -1):
        if is_valid:
            break
        for c in range(0, 9):
            if is_valid:
                break
            for d in range(9, c, -1):
                if ((a + b + c + d) == (a * b * c * d)) and number % 10 == 5:
                    is_valid = True
                    print(f"{a}{b}{c}{d}")
                    break
                elif ((a * b * c * d) // (a + b + c + d) == 3) and number % 3 == 0:
                    is_valid = True
                    print(f"{d}{c}{b}{a}")
                    break

if not is_valid:
    print("Nothing found")
