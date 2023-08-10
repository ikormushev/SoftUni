winter_honey = float(input())

honey_collected = 0

while True:
    command = input()
    if command == "Winter has come":
        break
    bee_name = command
    for i in range(1, 7):
        honey_per_month = float(input())
        honey_collected += honey_per_month
    if honey_collected < 0:
        print(f"{bee_name} was banished for gluttony")

honey_diff = abs(winter_honey - honey_collected)

if honey_collected >= winter_honey:
    print(f"Well done! Honey surplus {honey_diff:.2f}.")
else:
    print(f"Hard Winter! Honey needed {honey_diff:.2f}.")
