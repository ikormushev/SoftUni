starting_passengers = int(input())
stops_num = int(input())

conductors_num = 0
passengers_num = starting_passengers

for p in range(1, stops_num + 1):
    if p % 2 == 1:
        passengers_num += 2
    else:
        passengers_num -= 2
    passengers_out = int(input())
    passengers_in = int(input())
    passengers_num += passengers_in - passengers_out

print(f"The final number of passengers is: {passengers_num}")
