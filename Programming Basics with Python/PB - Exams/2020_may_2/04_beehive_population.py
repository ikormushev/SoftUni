starting_population = int(input())
years = int(input())

bees_num = starting_population

for i in range(1, years + 1):
    bees_num += (bees_num // 10) * 2
    if i % 5 == 0:
        bees_num -= (bees_num // 50) * 5
    bees_num -= (bees_num // 20) * 2

print(f"Beehive population: {bees_num}")
