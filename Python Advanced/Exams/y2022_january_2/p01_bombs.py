from collections import deque


bombs = {
    "Datura Bombs": {"power": 40, "count": 0, "is_filled": False},
    "Cherry Bombs": {"power": 60, "count": 0, "is_filled": False},
    "Smoke Decoy Bombs": {"power": 120, "count": 0, "is_filled": False},
}
bomb_effects = deque([int(x) for x in input().split(",")])
bomb_casings = [int(x) for x in input().split(",")]

are_all_bombs_filled = False

while bomb_effects and bomb_casings and not are_all_bombs_filled:
    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()

    values_sum = effect + casing

    for (bomb, info) in bombs.items():
        if values_sum == info["power"]:
            bombs[bomb]["count"] += 1
            if bombs[bomb]["count"] == 3:
                bombs[bomb]["is_filled"] = True
            break
    else:
        casing -= 5
        bomb_casings.append(casing)
        bomb_effects.appendleft(effect)
        continue

    bombs_filled = []

    for (bomb, info) in bombs.items():
        bombs_filled.append(info["is_filled"])

    if all(bombs_filled):
        are_all_bombs_filled = True

if are_all_bombs_filled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

print("Bomb Effects:", end=" ")
if bomb_effects:
    print(*bomb_effects, sep=", ")
else:
    print("empty")

print("Bomb Casings:", end=" ")
if bomb_casings:
    print(*bomb_casings, sep=", ")
else:
    print("empty")

ordered_bombs = dict(sorted(bombs.items(), key=lambda d: d[0]))

for (bomb, info) in ordered_bombs.items():
    print(f"{bomb}: {info['count']}")
