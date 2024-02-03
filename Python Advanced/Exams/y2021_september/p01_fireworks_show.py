from collections import deque

fireworks = {
    "Palm Fireworks": {"count": 0, "perfect_show": False},
    "Willow Fireworks": {"count": 0, "perfect_show": False},
    "Crossette Fireworks": {"count": 0, "perfect_show": False}
}
firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]

perfect_show = False

while firework_effects and explosive_power and not perfect_show:
    firework = firework_effects.popleft()
    if firework <= 0:
        continue
    power = explosive_power.pop()
    if power <= 0:
        firework_effects.appendleft(firework)
        continue

    values_sum = firework + power

    if values_sum % 3 == 0 and values_sum % 5:
        fireworks["Palm Fireworks"]["count"] += 1
        if fireworks["Palm Fireworks"]["count"] == 3:
            fireworks["Palm Fireworks"]["perfect_show"] = True
    elif values_sum % 5 == 0 and values_sum % 3:
        fireworks["Willow Fireworks"]["count"] += 1
        if fireworks["Willow Fireworks"]["count"] == 3:
            fireworks["Willow Fireworks"]["perfect_show"] = True
    elif values_sum % 3 == 0 and values_sum % 5 == 0:
        fireworks["Crossette Fireworks"]["count"] += 1
        if fireworks["Crossette Fireworks"]["count"] == 3:
            fireworks["Crossette Fireworks"]["perfect_show"] = True
    else:
        firework -= 1
        firework_effects.append(firework)
        explosive_power.append(power)
        continue

    all_fireworks = []

    for (firework, info) in fireworks.items():
        all_fireworks.append(info["perfect_show"])

    if all(all_fireworks):
        perfect_show = True

if perfect_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print("Firework Effects left:", end=" ")
    print(*firework_effects, sep=", ")

if explosive_power:
    print("Explosive Power left:", end=" ")
    print(*explosive_power, sep=", ")

for (firework, info) in fireworks.items():
    print(f"{firework}: {info['count']}")
