from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]

healing_items = {
    "Patch": {"count": 0, "resources_needed": 30},
    "Bandage": {"count": 0, "resources_needed": 40},
    "MedKit": {"count": 0, "resources_needed": 100},
}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    result = textile + medicament

    if result == healing_items["Patch"]["resources_needed"]:
        healing_items["Patch"]["count"] += 1

    elif result == healing_items["Bandage"]["resources_needed"]:
        healing_items["Bandage"]["count"] += 1

    elif result >= healing_items["MedKit"]["resources_needed"]:
        healing_items["MedKit"]["count"] += 1

        if result > healing_items["MedKit"]["resources_needed"]:
            result -= healing_items["MedKit"]["resources_needed"]
            if medicaments:
                next_medicament = medicaments.pop() + result
                medicaments.append(next_medicament)
            else:
                medicaments.append(result)

    else:
        medicament += 10
        medicaments.append(medicament)

if not textiles and medicaments:
    print("Textiles are empty.")
elif not medicaments and textiles:
    print("Medicaments are empty.")
elif not medicaments and not textiles:
    print("Textiles and medicaments are both empty.")

ordered_healing_items = dict(sorted(healing_items.items(), key=lambda d: (-d[1]["count"], d[0])))

for (heal_item, info) in ordered_healing_items.items():
    if info["count"]:
        print(f"{heal_item} - {info['count']}")

if medicaments:
    print("Medicaments left:", end=" ")
    while medicaments:
        if len(medicaments) == 1:
            print(medicaments.pop())
        else:
            print(medicaments.pop(), end=", ")

if textiles:
    print("Textiles left:", end=" ")
    print(*textiles, sep=", ")
