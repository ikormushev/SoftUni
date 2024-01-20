from collections import deque

bees_values = deque([int(x) for x in input().split()])
nectar_values = [int(x) for x in input().split()]
symbols = deque(input().split())

operations = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x / y
}

total_honey = 0

while bees_values and nectar_values:
    bee = bees_values.popleft()
    nectar = nectar_values.pop()
    if nectar >= bee:
        used_symbol = symbols.popleft()
        if nectar == 0 and used_symbol == "/":
            continue
        result = abs(operations[used_symbol](bee, nectar))
        total_honey += result
    else:
        bees_values.appendleft(bee)
        continue

print(f"Total honey made: {total_honey}")
if bees_values:
    print("Bees left: ",end="")
    print(*bees_values, sep=", ")
if nectar_values:
    print("Nectar left: ", end="")
    print(*nectar_values, sep=", ")
