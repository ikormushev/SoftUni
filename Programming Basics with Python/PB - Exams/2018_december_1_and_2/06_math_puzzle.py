key = int(input())

flag = False

for a in range(1, 31):
    for b in range(1, 31):
        for c in range(1, 31):
            if (a < b < c) and (a + b + c == key):
                flag = True
                print(f"{a} + {b} + {c} = {key}")
            if (a > b > c) and (a * b * c == key):
                flag = True
                print(f"{a} * {b} * {c} = {key}")

if not flag:
    print("No!")
