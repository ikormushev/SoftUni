from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])

total_matches = 0
not_all_worms_in_holes = False

while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()

    if worm == hole:
        total_matches += 1
        continue
    else:
        worm -= 3
        if worm <= 0:
            not_all_worms_in_holes = True
            continue
        worms.append(worm)

if total_matches:
    print(f"Matches: {total_matches}")
else:
    print("There are no matches.")

if not worms:
    if not_all_worms_in_holes:
        print("Worms left: none")
    else:
        print("Every worm found a suitable hole!")

if worms:
    print("Worms left:", end=" ")
    print(*worms, sep=", ")

if holes:
    print("Holes left:", end=" ")
    print(*holes, sep=", ")
else:
    print("Holes left: none")
