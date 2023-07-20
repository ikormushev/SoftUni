hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

arrival = ""

time_of_exam_min = (hour_of_exam * 60) + minutes_of_exam
time_of_arrival_min = (hour_of_arrival * 60) + minutes_of_arrival

time_difference = time_of_exam_min - time_of_arrival_min

if time_difference > 30:
    arrival = "Early"
elif 0 <= time_difference <= 30:
    arrival = "On time"
else:
    arrival = "Late"

print(arrival)

if 1 <= time_difference < 60:
    print(f"{time_difference} minutes before the start")
elif time_difference >= 60:
    hours_difference = time_difference // 60
    minutes_difference = time_difference % 60
    print(f"{hours_difference}:{minutes_difference:02} hours before the start")
elif -60 < time_difference <= -1:
    time_difference = abs(time_difference)
    print(f"{time_difference} minutes after the start")
elif time_difference <= -60:
    time_difference = abs(time_difference)
    hours_difference = time_difference // 60
    minutes_difference = time_difference % 60
    print(f"{hours_difference}:{minutes_difference:02} hours after the start")
