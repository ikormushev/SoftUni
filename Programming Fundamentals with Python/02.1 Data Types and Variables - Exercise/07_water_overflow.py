lines_num = int(input())

tank_capacity = 255

for _ in range(lines_num):
    water = int(input())
    if water > tank_capacity:
        print("Insufficient capacity!")
        continue
    tank_capacity -= water

print(255 - tank_capacity)
