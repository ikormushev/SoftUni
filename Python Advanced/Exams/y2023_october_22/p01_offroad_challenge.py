from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption = deque([int(x) for x in input().split()])
total_fuel_needed = deque([int(x) for x in input().split()])

altitudes = 0
top_not_reached = False
altitudes_reached = deque()

while initial_fuel and additional_consumption and total_fuel_needed:
    altitudes += 1
    fuel = initial_fuel.pop()
    consumption = additional_consumption.popleft()

    result = fuel - consumption
    fuel_needed = total_fuel_needed.popleft()

    if result >= fuel_needed:
        print(f"John has reached: Altitude {altitudes}")
        altitudes_reached.append(altitudes)
    else:
        print(f"John did not reach: Altitude {altitudes}")
        top_not_reached = True
        break

if top_not_reached:
    print("John failed to reach the top.")
    if altitudes_reached:
        print("Reached altitudes:", end=" ")
        while altitudes_reached:
            if len(altitudes_reached) == 1:
                print(f"Altitude {altitudes_reached.popleft()}")
            else:
                print(f"Altitude {altitudes_reached.popleft()}", end=", ")
    else:
        print("John didn't reach any altitude.")

else:
    print("John has reached all the altitudes and managed to reach the top!")
