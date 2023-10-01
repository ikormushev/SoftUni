time_needed = input().split(" ")

time_needed_integers = []

for i in range(len(time_needed)):
    time_needed_integers.append(int(time_needed[i]))

left_car_time = 0
right_car_time = 0
winner = ""
winner_time = 0

for y in range(len(time_needed_integers) // 2):
    if time_needed_integers[y] == 0:
        left_car_time *= 0.80
        continue
    left_car_time += time_needed_integers[y]

time_needed_integers.reverse()
for j in range(len(time_needed_integers) // 2):
    if time_needed_integers[j] == 0:
        right_car_time *= 0.80
        continue
    right_car_time += time_needed_integers[j]

if left_car_time > right_car_time:
    winner = "right"
    winner_time = right_car_time
elif right_car_time > left_car_time:
    winner = "left"
    winner_time = left_car_time

print(f"The winner is {winner} with total time: {winner_time:.1f}")
