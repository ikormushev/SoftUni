neighborhood = list(map(int, input().split("@")))
current_index = 0
house_index = 0

while True:
    command = input()
    if command == "Love!":
        break

    jump_command = command.split(" ")
    jump_length = int(jump_command[1])
    house_index = jump_length + current_index

    if house_index >= len(neighborhood):
        house_index = 0

    current_index = house_index
    if neighborhood[house_index] == 0:
        print(f"Place {house_index} already had Valentine's day.")
        continue

    neighborhood[house_index] -= 2
    if neighborhood[house_index] == 0:
        print(f"Place {house_index} has Valentine's day.")

print(f"Cupid's last position was {house_index}.")

if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    failed_houses_count = 0
    for i in range(len(neighborhood)):
        if neighborhood[i] != 0:
            failed_houses_count += 1
    print(f"Cupid has failed {failed_houses_count} places.")
