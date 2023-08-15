luggage_capacity = float(input())

luggage_num = 0
space_left = luggage_capacity

while True:
    command = input()
    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    luggage_volume = float(command)
    luggage_num += 1
    if luggage_num % 3 == 0:
        luggage_volume *= 1.10

    space_left -= luggage_volume

    if space_left < 0:
        print("No more space!")
        luggage_num -= 1
        break

print(f"Statistic: {luggage_num} suitcases loaded.")
