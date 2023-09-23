group_size = int(input())
days_num = int(input())

total_coins = 0

for i in range(1, days_num + 1):
    if i % 10 == 0:
        group_size -= 2

    if i % 15 == 0:
        group_size += 5

    total_coins += 50
    total_coins -= 2 * group_size

    if i % 3 == 0:
        total_coins -= 3 * group_size

    if i % 5 == 0:
        total_coins += 20 * group_size
        if i % 3 == 0:
            total_coins -= 2 * group_size

coins_per_companion = int(total_coins / group_size)

print(f"{group_size} companions received {coins_per_companion} coins each.")
