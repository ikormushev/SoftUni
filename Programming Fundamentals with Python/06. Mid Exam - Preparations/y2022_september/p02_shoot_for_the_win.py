def printing_targets(targets: list):
    for y in range(len(targets)):
        if y == 0:
            print(f"Shot targets: {len(shot_indexes)} -> {targets[y]}", end=" ")
        elif y == len(targets) - 1:
            print(targets[y])
        else:
            print(targets[y], end=" ")


integers = list(map(int, input().split(" ")))
shot_indexes = []
while True:
    command = input()
    if command == "End":
        break
    index = int(command)
    if index < 0 or index >= len(integers) or index in shot_indexes:
        continue
    current_target = integers[index]
    shot_indexes.append(index)
    for i in range(len(integers)):
        if integers[i] > current_target and integers[i] != -1:
            integers[i] -= current_target
        elif integers[i] <= current_target and integers[i] != -1:
            integers[i] += current_target
    integers[index] = -1

printing_targets(integers)
