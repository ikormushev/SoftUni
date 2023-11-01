commands_num = int(input())

parking_lot = {}

for _ in range(commands_num):
    command = input().split(" ")
    username = command[1]

    if "unregister" in command:
        if username in parking_lot:
            parking_lot.pop(username)
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

    elif "register" in command:
        license_plate = command[2]

        if username not in parking_lot:
            parking_lot[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")

[print(f"{name} => {plate}") for (name, plate) in parking_lot.items()]
