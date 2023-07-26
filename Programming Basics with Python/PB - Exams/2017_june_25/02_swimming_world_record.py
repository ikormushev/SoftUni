record_sec = float(input())
distance_m = float(input())
time_per_m_sec = float(input())

swimming_time_sec = distance_m * time_per_m_sec

water_resistance_num = distance_m // 15
water_resistance_sec = water_resistance_num * 12.5

time_total = swimming_time_sec + water_resistance_sec

if time_total < record_sec:
    print(f"Yes, he succeeded! "
          f"The new world record is {time_total:.2f} seconds.")
else:
    time_diff = time_total - record_sec
    print(f"No, he failed! He was {time_diff:.2f} seconds slower.")
