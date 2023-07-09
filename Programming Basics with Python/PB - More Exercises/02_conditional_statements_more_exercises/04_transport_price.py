kilometers = int(input())
time_of_day = input()

taxi = 0
taxi_use_fee = 0.70
taxi_day_fee = 0.79
taxi_night_fee = 0.90

bus = 0
bus_day_night_fee = 0.09

train = 0
train_day_night_fee = 0.06

if kilometers < 20:
    if time_of_day == "day":
        taxi = taxi_use_fee + (kilometers * taxi_day_fee)
    elif time_of_day == "night":
        taxi = taxi_use_fee + (kilometers * taxi_night_fee)
    print(f"{taxi:.2f}")

elif 20 <= kilometers < 100:
    if time_of_day == "day":
        taxi = taxi_use_fee + (kilometers * taxi_day_fee)
        bus = kilometers * bus_day_night_fee
    elif time_of_day == "night":
        taxi = taxi_use_fee + (kilometers * taxi_night_fee)
        bus = kilometers * bus_day_night_fee
    lowest_price = min(taxi, bus)
    print(f"{lowest_price:.2f}")

elif kilometers >= 100:
    if time_of_day == "day":
        taxi = taxi_use_fee + (kilometers * taxi_day_fee)
        bus = kilometers * bus_day_night_fee
        train = kilometers * train_day_night_fee
    elif time_of_day == "night":
        taxi = taxi_use_fee + (kilometers * taxi_night_fee)
        bus = kilometers * bus_day_night_fee
        train = kilometers * train_day_night_fee
    lowest_price = min(taxi, bus, train)
    print(f"{lowest_price:.2f}")
