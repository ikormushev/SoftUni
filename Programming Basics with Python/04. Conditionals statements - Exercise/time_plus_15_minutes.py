hours = int(input())
minutes = int(input())

extra_tim_min = 15
hours_to_min = hours * 60
total_time = hours_to_min + minutes + extra_tim_min

total_time_hours = total_time // 60
total_time_min = total_time % 60

if total_time_hours > 23:
    total_time_hours = 0

print(f'{total_time_hours}:{total_time_min:02}')
