lines_num = int(input())

tank_capacity = 255
tank_capacity_left = tank_capacity

for _ in range(lines_num):
    water = int(input())
    if water > tank_capacity_left:
        print("Insufficient capacity!")
        continue
    tank_capacity_left -= water

print(tank_capacity - tank_capacity_left)
