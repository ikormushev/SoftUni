max_stars_row = int(input())

for i in range(1, max_stars_row + 1):
    print("*" * i)

for y in range(max_stars_row - 1, 0, -1):
    print("*" * y)
