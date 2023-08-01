bees_num = int(input())
bear_health = int(input())
bear_attack = int(input())

bear_won = False
while True:
    bees_num -= bear_attack  # bees have 1 health each
    bear_health -= bees_num * 5
    if bees_num < 100:
        if bees_num < 0:  # bees_num cannot be negative
            bees_num = 0
        bear_won = True
        break
    if bear_health <= 0:
        break

if bear_won:
    print(f"The bear stole the honey! Bees left {bees_num}.")
else:
    print(f"Beehive won! Bees left {bees_num}.")
