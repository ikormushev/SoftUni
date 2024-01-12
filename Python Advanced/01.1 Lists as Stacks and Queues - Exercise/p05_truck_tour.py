from collections import deque

petrol_pumps_count = int(input())
index = -1
petrol_pumps = deque()

for _ in range(petrol_pumps_count):
    info = input().split()
    petrol_amount = int(info[0])
    distance = int(info[1])
    petrol_pumps.append([petrol_amount, distance])

best_station = 0
maximum_petrol_capacity = 0

for _ in range(len(petrol_pumps)):
    petrol_capacity = 0
    index += 1
    petrol, distance = petrol_pumps.popleft()
    circle = petrol_pumps.copy()

    petrol_capacity += petrol - distance
    petrol_pumps.append([petrol, distance])
    if petrol_capacity < 0:
        continue

    while circle:
        new_petrol, new_distance = circle.popleft()
        petrol_capacity += new_petrol - new_distance
        if petrol_capacity < 0:
            break
    else:
        if petrol_capacity > maximum_petrol_capacity:
            best_station = index
            maximum_petrol_capacity = petrol_capacity

print(best_station)
