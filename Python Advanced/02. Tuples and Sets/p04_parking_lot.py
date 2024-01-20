commands_num = int(input())

cars = set()

for _ in range(commands_num):
    direction, number = input().split(", ")
    if direction == "IN":
        cars.add(number)
    else:
        cars.remove(number)

if cars:
    [print(x) for x in cars]
else:
    print("Parking Lot is Empty")
