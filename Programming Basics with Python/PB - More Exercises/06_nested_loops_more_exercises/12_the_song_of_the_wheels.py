number = int(input())

guesses_count = 0
password = 0
is_password = False

for a in range(1, 10):
    for b in range(1, 10):
        if a < b:
            for c in range(1, 10):
                for d in range(1, 10):
                    if c > d:
                        if ((a * b) + (c * d)) == number:
                            print(f"{a}{b}{c}{d}", end=" ")
                            guesses_count += 1
                            if guesses_count == 4:
                                is_password = True
                                password = f"{a}{b}{c}{d}"

print()
if is_password:
    print(f"Password: {password}")
else:
    print("No!")
