run_record_sec = float(input())
distance_m = float(input())
time_for_meter = float(input())

run_time = distance_m * time_for_meter
slow_time_num = distance_m // 50
slow_time_sec = slow_time_num * 30

total_run_time = run_time + slow_time_sec


if total_run_time < run_record_sec:
    print(f"Yes! The new record is {total_run_time:.2f} seconds.")
else:
    time_diff = total_run_time - run_record_sec
    print(f"No! He was {time_diff:.2f} seconds slower.")
