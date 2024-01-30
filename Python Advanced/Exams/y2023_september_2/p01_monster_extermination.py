from collections import deque

monsters_armor = deque([int(x) for x in input().split(",")])
soldiers_impact = [int(x) for x in input().split(",")]

monsters_killed = 0

while monsters_armor and soldiers_impact:
    monster = monsters_armor.popleft()
    soldier = soldiers_impact.pop()
    if monster <= soldier:
        soldier -= monster
        monsters_killed += 1
        if soldier > 0:
            if soldiers_impact:
                next_soldier = soldiers_impact.pop()
                soldier += next_soldier
            soldiers_impact.append(soldier)
    else:
        monster -= soldier
        monsters_armor.append(monster)

if not monsters_armor:
    print("All monsters have been killed!")

if not soldiers_impact:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")
