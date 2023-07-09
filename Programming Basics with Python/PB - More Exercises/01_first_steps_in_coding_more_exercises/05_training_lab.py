w_m = float(input())
h_m = float(input())

w_cm = w_m * 100
h_cm = h_m * 100

h_without_corridor = h_cm - 100

number_desks = h_without_corridor // 70
number_rows = w_cm // 120

number_seats = (number_desks * number_rows) - 3

print(number_seats)