number = int(input())

for i in range(ord("a"), ord("a") + number):
    for y in range(ord("a"), ord("a") + number):
        for p in range(ord("a"), ord("a") + number):
            print(f"{chr(i)}{chr(y)}{chr(p)}")
