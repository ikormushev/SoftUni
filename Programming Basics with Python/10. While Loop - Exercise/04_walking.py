goal = 10000
total_steps = 0

while total_steps < goal:
    data = input()
    if data == "Going home":
        steps = int(input())
        total_steps += steps
        break
    steps = int(data)
    total_steps += steps

steps_diff = abs(total_steps - goal)

if total_steps < goal:
    print(f"{steps_diff} more steps to reach goal.")
else:
    print("Goal reached! Good job!")
    print(f"{steps_diff} steps over the goal!")
