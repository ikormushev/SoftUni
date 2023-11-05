dragons_to_follow = int(input())

dragons = {}

for i in range(dragons_to_follow):
    stats = input().split(" ")
    dragon_type = stats[0]
    dragon_name = stats[1]
    dragon_damage = stats[2]
    dragon_health = stats[3]
    dragon_armor = stats[4]

    if dragon_damage == "null":
        dragon_damage = 45
    else:
        dragon_damage = int(stats[2])

    if dragon_health == "null":
        dragon_health = 250
    else:
        dragon_health = int(stats[3])

    if dragon_armor == "null":
        dragon_armor = 10
    else:
        dragon_armor = int(stats[4])

    if dragon_type not in dragons:
        dragons[dragon_type] = {}

    dragons[dragon_type][dragon_name] = [dragon_damage, dragon_health, dragon_armor]


for (dr_type, all_dragons) in dragons.items():
    dragons[dr_type] = dict(sorted(dragons[dr_type].items(), key=lambda d: d[0]))

for (dr_type, all_dragons) in dragons.items():
    average_damage = 0
    average_health = 0
    average_armor = 0

    for (name, dr_stats) in all_dragons.items():
        average_damage += dr_stats[0]
        average_health += dr_stats[1]
        average_armor += dr_stats[2]

    average_damage /= len(all_dragons.keys())
    average_health /= len(all_dragons.keys())
    average_armor /= len(all_dragons.keys())

    print(f"{dr_type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")

    for (name, dr_stats) in all_dragons.items():
        print(f"-{name} -> damage: {dr_stats[0]}, health: {dr_stats[1]}, armor: {dr_stats[2]}")
