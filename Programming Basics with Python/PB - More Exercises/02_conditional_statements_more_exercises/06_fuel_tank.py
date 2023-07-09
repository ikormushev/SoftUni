gas_type = input()
fuel_lt = float(input())

gas_list = ["Diesel", "Gasoline", "Gas"]

if gas_type in gas_list:
    if fuel_lt >= 25:
        print(f"You have enough {gas_type.lower()}.")
    else:
        print(f"Fill your tank with {gas_type.lower()}!")
else:
    print("Invalid fuel!")
