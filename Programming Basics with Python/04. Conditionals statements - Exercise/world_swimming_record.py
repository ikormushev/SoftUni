record_time_sec = float(input())
distance_m = float(input())
time_for_one_meter_sec = float(input())

swimming_time = distance_m * time_for_one_meter_sec
slowing_down_num = distance_m // 15

water_resistance_sec = 12.5
slowing_down_time = slowing_down_num * water_resistance_sec

full_swimming_time = swimming_time + slowing_down_time

if full_swimming_time < record_time_sec:
    print(f"Yes, he succeeded! The new world record is {full_swimming_time:.2f} seconds.")
else:
    time_difference = full_swimming_time - record_time_sec
    print(f"No, he failed! He was {time_difference:.2f} seconds slower.")
