from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
bottles_capacity = [int(x) for x in input().split()]

wasted_water = 0

while cups_capacity and bottles_capacity:
    current_cup = cups_capacity.popleft()
    current_bottle = bottles_capacity.pop()
    if current_cup - current_bottle <= 0:
        wasted_water += current_bottle - current_cup
    else:
        current_cup -= current_bottle
        while current_cup > 0:
            if bottles_capacity:
                new_bottle = bottles_capacity.pop()
                current_cup -= new_bottle
            else:
                break
        else:
            wasted_water += current_cup * -1

if not cups_capacity:
    print(f"Bottles: ", end="")
    while bottles_capacity:
        if len(bottles_capacity) == 1:
            print(bottles_capacity.pop())
        else:
            print(bottles_capacity.pop(), end=" ")
else:
    print(f"Cups: ", end="")
    while cups_capacity:
        if len(cups_capacity) == 1:
            print(cups_capacity.popleft())
        else:
            print(cups_capacity.popleft(), end=" ")

print(f"Wasted litters of water: {wasted_water}")
