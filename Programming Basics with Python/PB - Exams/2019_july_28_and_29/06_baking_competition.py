participants_num = int(input())

pastries_prices = {
    "cookies": 1.50,
    "cakes": 7.80,
    "waffles": 2.30
}

pastries = {
    "cookies": 0,
    "cakes": 0,
    "waffles": 0
}

total_sum = 0
total_pastries_num = 0

for i in range(1, participants_num + 1):
    pastries["cookies"] = 0
    pastries["cakes"] = 0
    pastries["waffles"] = 0
    participant_name = input()
    while True:
        command = input()
        if command == "Stop baking!":
            break
        pastry_type = command
        pastries_num = int(input())
        pastries[pastry_type] += pastries_num

        total_pastries_num += pastries_num
        total_sum += (pastries_prices[pastry_type] * pastries_num)

    print(f'{participant_name} baked {pastries["cookies"]} cookies, '
          f'{pastries["cakes"]} cakes and {pastries["waffles"]} waffles.')

print(f"All bakery sold: {total_pastries_num}")
print(f"Total sum for charity: {total_sum:.2f} lv.")
