def set_cover(universe, sets):
    chosen_sets = []

    while universe:
        current_best_set = max(sets, key=lambda s: len(universe.intersection(s)))
        chosen_sets.append(current_best_set)
        universe -= current_best_set

    return chosen_sets


given_universe = set(int(x) for x in input().split(", "))
sets_num = int(input())

other_sets = [{int(x) for x in input().split(", ")} for _ in range(sets_num)]

new_sets = set_cover(given_universe, other_sets)

for i in range(len(new_sets)):
    new_sets[i] = sorted(new_sets[i])

print(f"Sets to take ({len(new_sets)}):")
[print("{ " + ", ".join(str(y) for y in x) + " }") for x in new_sets]
