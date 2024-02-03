from collections import  deque

caffeine_milligrams = [int(x) for x in input().split(", ")]
energy_drinks = deque([int(x) for x in input().split(", ")])

max_caffeine = 300
initial_caffeine = 0

while caffeine_milligrams and energy_drinks:
    caffeine = caffeine_milligrams.pop()
    drink = energy_drinks.popleft()

    result = caffeine * drink
    if result + initial_caffeine <= max_caffeine:
        initial_caffeine += result
    else:
        energy_drinks.append(drink)
        if initial_caffeine > 30:
            initial_caffeine -= 30

if energy_drinks:
    print("Drinks left:", end=" ")
    print(*energy_drinks, sep=", ")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {initial_caffeine} mg caffeine.")
