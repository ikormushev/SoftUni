from collections import deque

starting_water = int(input())
people = deque([])
action = input()

while action != "Start":
    people.append(action)
    action = input()

action = input()
while action != "End":
    command = action.split(" ")
    if command[0] == "refill":
        starting_water += int(command[1])
    else:
        wanted_water = int(command[0])
        if wanted_water > starting_water:
            print(f"{people.popleft()} must wait")
        else:
            starting_water -= wanted_water
            print(f"{people.popleft()} got water")
    action = input()

print(f"{starting_water} liters left")
