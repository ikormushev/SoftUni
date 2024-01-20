from collections import deque


def crafting_present(given_result):
    if given_result == 150:
        presents["Doll"] += 1
    elif given_result == 250:
        presents["Wooden train"] += 1
    elif given_result == 300:
        presents["Teddy bear"] += 1
    elif given_result == 400:
        presents["Bicycle"] += 1
    else:
        return False
    return True


boxes = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

presents = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0
}

while boxes and magic_levels:
    box = boxes.pop()
    magic = magic_levels.popleft()
    result = box * magic
    if crafting_present(result):
        continue

    if result < 0:
        new_material = box + magic
        boxes.append(new_material)
    elif result > 0:
        box += 15
        boxes.append(box)
    else:
        if box == 0 and magic != 0:
            magic_levels.appendleft(magic)
        if magic == 0 and box != 0:
            boxes.append(box)

if ((presents["Doll"] >= 1 and presents["Wooden train"] >= 1) or
        (presents["Teddy bear"] >= 1 and presents["Bicycle"] >= 1)):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes:
    print("Materials left: ", end="")
    while boxes:
        if len(boxes) == 1:
            print(boxes.pop())
        else:
            print(boxes.pop(), end=", ")

if magic_levels:
    print("Magic left: ", end="")
    print(*magic_levels, sep=", ")

sorted_presents = dict(sorted(presents.items()))

for toy, crafts in sorted_presents.items():
    if crafts != 0:
        print(f"{toy}: {crafts}")
