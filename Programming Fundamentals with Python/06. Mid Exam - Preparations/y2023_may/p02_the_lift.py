def printing_wagons(lift: list):
    for y in range(len(lift)):
        if y == len(lift) - 1:
            print(lift[y])
        else:
            print(lift[y], end=" ")


people = int(input())
lift_current_state = list(map(int, input().split(" ")))

lift_max_size = 4
people_left = people
lifts_num = len(lift_current_state)

for i in range(lifts_num):
    if people_left <= 0:
        break
    if lift_current_state[i] + people_left > lift_max_size:
        people_in = lift_max_size - lift_current_state[i]
        lift_current_state[i] = lift_max_size
        people_left -= people_in
    else:
        lift_current_state[i] += people_left
        people_left -= people_left

if people_left > 0 and sum(lift_current_state) == 4 * len(lift_current_state):
    print(f"There isn't enough space! {people_left} people in a queue!")
    printing_wagons(lift_current_state)
elif people_left <= 0 and sum(lift_current_state) < 4 * len(lift_current_state):
    print("The lift has empty spots!")
    printing_wagons(lift_current_state)
else:
    printing_wagons(lift_current_state)
