from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

total_matches = 0
is_male_special = False

while males and females:
    male = males.pop()
    is_male_special = False
    female = females.popleft()
    is_female_special = False

    if male <= 0 and not (female <= 0):
        females.appendleft(female)

    if female <= 0 and not (male <= 0):
        males.append(male)

    if male <= 0 or female <= 0:
        continue

    if male % 25 == 0:
        if len(males):
            is_male_special = True
            males.pop()

    if female % 25 == 0:
        if len(females):
            is_female_special = True
            females.popleft()

    if is_male_special or is_female_special:
        if not is_male_special:
            males.append(male)
        if not is_female_special:
            females.appendleft(female)
        continue

    if male == female:
        total_matches += 1
    else:
        male -= 2
        males.append(male)

print(f"Matches: {total_matches}")
print("Males left:", end=" ")
if males:
    while males:
        if len(males) == 1:
            print(males.pop())
        else:
            print(males.pop(), end=", ")
else:
    print(f"none")

print("Females left:", end=" ")
if females:
    print(*females, sep=", ")
else:
    print(f"none")
