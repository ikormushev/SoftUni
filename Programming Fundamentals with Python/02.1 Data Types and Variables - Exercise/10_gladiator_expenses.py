lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmets_broken = 0
swords_broken = 0
shields_broken = 0
armors_broken = 0

for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        helmets_broken += 1
    if i % 3 == 0:
        swords_broken += 1
    if i % 6 == 0:
        shields_broken += 1
        if shields_broken % 2 == 0:
            armors_broken += 1

final_price = ((helmet_price * helmets_broken) + (swords_broken * sword_price) +
               (shields_broken * shield_price) + (armors_broken * armor_price))

print(f"Gladiator expenses: {final_price:.2f} aureus")
