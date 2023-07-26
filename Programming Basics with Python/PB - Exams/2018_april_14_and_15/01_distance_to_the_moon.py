from math import ceil

average_speed = float(input())
fuel_per_100_km_lt = float(input())

distance = 384400 * 2
travel_time = ceil(distance / average_speed) + 3
fuel = (fuel_per_100_km_lt * distance) / 100

print(travel_time)
print(f"{fuel:.0f}")
