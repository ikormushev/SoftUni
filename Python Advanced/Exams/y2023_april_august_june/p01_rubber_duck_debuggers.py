from collections import deque

programmers_time = deque([int(x) for x in input().split()])
tasks_num = [int(x) for x in input().split()]

ducks_count = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}

while programmers_time and tasks_num:
    given_time = programmers_time.popleft()
    given_tasks = tasks_num.pop()

    total_value = given_time * given_tasks

    if 0 <= total_value <= 60:
        ducks_count["Darth Vader Ducky"] += 1
    elif 61 <= total_value <= 120:
        ducks_count["Thor Ducky"] += 1
    elif 121 <= total_value <= 180:
        ducks_count["Big Blue Rubber Ducky"] += 1
    elif 181 <= total_value <= 240:
        ducks_count["Small Yellow Rubber Ducky"] += 1
    else:
        if total_value > 240:
            given_tasks -= 2
            programmers_time.append(given_time)
            tasks_num.append(given_tasks)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
[print(f"{duck}: {count}") for (duck, count) in ducks_count.items()]
