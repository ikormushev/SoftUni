from math import floor, ceil

first_brother_time = float(input())
second_brother_time = float(input())
third_brother_time = float(input())
fishing_time = float(input())

cleaning_time_per_hour = 1 / ((1 / first_brother_time) + (1 / second_brother_time) + (1 / third_brother_time))

rest = cleaning_time_per_hour * 0.15
cleaning_time = cleaning_time_per_hour + rest

time_left = fishing_time - cleaning_time

print(f"Cleaning time: {cleaning_time:.2f}")
if time_left > 0:
    print(f"Yes, there is a surprise - time left -> {floor(time_left)} hours.")
else:
    time_shortage = cleaning_time - fishing_time
    print(f"No, there isn't a surprise - shortage of time -> {ceil(time_shortage)} hours.")
