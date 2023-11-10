cars_num = int(input())

cars = {}

for _ in range(cars_num):
    car_info = input().split("|")
    car_name = car_info[0]
    car_mileage = int(car_info[1])
    car_fuel = int(car_info[2])

    cars[car_name] = {}
    cars[car_name]["mileage"] = car_mileage
    cars[car_name]["fuel"] = car_fuel

while True:
    command = input()
    if command == "Stop":
        break
    action = command.split(" : ")
    car_in_action = action[1]
    if action[0] == "Drive":
        distance = int(action[2])
        fuel = int(action[3])
        if cars[car_in_action]["fuel"] - fuel < 0:
            print("Not enough fuel to make that ride")
        else:
            cars[car_in_action]["mileage"] += distance
            cars[car_in_action]["fuel"] -= fuel
            print(f"{car_in_action} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if cars[car_in_action]["mileage"] >= 100000:
                del cars[car_in_action]
                print(f"Time to sell the {car_in_action}!")

    elif action[0] == "Refuel":
        fuel = int(action[2])
        if cars[car_in_action]["fuel"] + fuel > 75:
            fuel = 75 - cars[car_in_action]["fuel"]
            cars[car_in_action]["fuel"] = 75
        else:
            cars[car_in_action]["fuel"] += fuel
        print(f"{car_in_action} refueled with {fuel} liters")

    elif action[0] == "Revert":
        kilometers = int(action[2])
        if cars[car_in_action]["mileage"] - kilometers < 10000:
            cars[car_in_action]["mileage"] = 10000
        else:
            cars[car_in_action]["mileage"] -= kilometers
            print(f"{car_in_action} mileage decreased by {kilometers} kilometers")

for (car, stats) in cars.items():
    print(f'{car} -> Mileage: {stats["mileage"]} kms, Fuel in the tank: {stats["fuel"]} lt.')
