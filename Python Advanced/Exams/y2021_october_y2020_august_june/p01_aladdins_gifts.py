from collections import deque


def add_presents(given_result):
    if 100 <= given_result <= 199:
        presents["Gemstone"] += 1
    elif 200 <= given_result <= 299:
        presents["Porcelain Sculpture"] += 1
    elif 300 <= given_result <= 399:
        presents["Gold"] += 1
    elif 400 <= given_result <= 499:
        presents["Diamond Jewellery"] += 1


materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

presents = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0,
}

while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()
    result = material + magic

    add_presents(result)
    if result < 100:
        if result % 2 == 0:
            material *= 2
            magic *= 3
            result = material + magic
            add_presents(result)
        else:
            result *= 2
            add_presents(result)
    else:
        if result > 499:
            result /= 2
            add_presents(result)

crafting_successful = False
if presents["Gemstone"] >= 1 and presents["Porcelain Sculpture"] >= 1:
    crafting_successful = True
elif presents["Gold"] >= 1 and presents["Diamond Jewellery"] >= 1:
    crafting_successful = True

if crafting_successful:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print("Materials left:", end=" ")
    print(*materials, sep=", ")

if magic_levels:
    print("Magic left:", end=" ")
    print(*magic_levels, sep=", ")

for (present, amount) in sorted(presents.items(), key=lambda d: d[0]):
    if amount:
        print(f"{present}: {amount}")
