number = int(input())

passwords_count = 0
secret_password = ""
is_secret_password = False

for a in range(1, 10):
    for b in range(1, 10):
        if a < b:
            for c in range(1, 10):
                for d in range(1, 10):
                    if c > d and ((a * b) + (c * d) == number):
                        password = f"{a}{b}{c}{d}"
                        passwords_count += 1
                        print(password, end=" ")
                        if passwords_count == 4:
                            secret_password = password
                            is_secret_password = True

print()
if not secret_password:
    print("No!")
else:
    print(f"Passwords: {secret_password}")
