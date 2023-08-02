days = int(input())

total_distance_m = 0
total_time_m = 0

for _ in range(1, days + 1):
    running_time_m = int(input())
    distance = float(input())
    distance_unit = input()
    if distance_unit == "m":
        total_distance_m += distance
    elif distance_unit == "km":
        total_distance_m += distance * 1000
    total_time_m += running_time_m

calories_burned = (total_time_m / 20) * 400
total_distance_km = total_distance_m / 1000

print(f"He ran {total_distance_km:.2f}km for {total_time_m} minutes "
      f"and burned {calories_burned:.0f} calories.")
