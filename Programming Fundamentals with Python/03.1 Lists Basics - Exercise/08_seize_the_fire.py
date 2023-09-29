fire_levels = input().split(" = ")
water_amount = int(input())

effort = 0
total_fire = 0
water_left = water_amount

new_fire_levels = []
for _ in range(len(fire_levels)):
    new_fire_levels.append("")

for i in range(len(fire_levels)):
    symbol_seen = False
    if i == 0:
        new_fire_levels[i] = fire_levels[i]
    elif i < len(fire_levels) - 1:
        if "#" in fire_levels[i]:
            for y in range(len(fire_levels[i])):
                    if fire_levels[i][y] == "#":
                        symbol_seen = True
                        continue
                    if not symbol_seen:
                        new_fire_levels[i - 1] += fire_levels[i][y]
                    else:
                        new_fire_levels[i] += fire_levels[i][y]
    else:
        new_fire_levels[i - 1] += fire_levels[i]
new_fire_levels.pop(-1)

print("Cells:")
for j in range(len(new_fire_levels)):
    fire_level = 0
    if "High" in new_fire_levels[j]:
        fire_level = int(new_fire_levels[j].replace("High", ""))
        if 81 <= fire_level <= 125:
            water_left -= fire_level
            effort += fire_level * 0.25
        else:
            continue
    if "Medium" in new_fire_levels[j]:
        fire_level = int(new_fire_levels[j].replace("Medium", ""))
        if 51 <= fire_level <= 80:
            water_left -= fire_level
            effort += fire_level * 0.25
        else:
            continue
    if "Low" in new_fire_levels[j]:
        fire_level = int(new_fire_levels[j].replace("Low", ""))
        if 1 <= fire_level <= 50:
            water_left -= fire_level
            effort += fire_level * 0.25
        else:
            continue

    if water_left < 0:
        water_left += fire_level
        effort -= fire_level * 0.25
        continue
    total_fire += fire_level
    print(f" - {fire_level}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
