first_time = int(input())
second_time = int(input())
third_time = int(input())

total_time = first_time + second_time + third_time
total_time_min = total_time // 60
total_time_sec = total_time % 60

if total_time_sec < 10:
    print(f"{total_time_min}:0{total_time_sec}")
else:
    print(f"{total_time_min}:{total_time_sec}")
  
