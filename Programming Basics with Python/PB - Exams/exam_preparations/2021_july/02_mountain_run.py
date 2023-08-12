world_record_sec = float(input())
distance_m = float(input())
time_per_m_sec = float(input())

slow_time = distance_m // 50
run_time = distance_m * time_per_m_sec + slow_time * 30

if run_time < world_record_sec:
    print(f"Yes! The new record is {run_time:.2f} seconds.")
else:
    run_diff = run_time - world_record_sec
    print(f"No! He was {run_diff:.2f} seconds slower.")
