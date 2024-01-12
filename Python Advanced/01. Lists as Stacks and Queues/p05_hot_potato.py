from collections import deque

kids = input().split(" ")
toss = int(input())

kids_tossing_potato = deque(kids)
tosses = 0

while len(kids_tossing_potato) > 1:
    tosses += 1
    moving_kid = kids_tossing_potato.popleft()
    if tosses % toss == 0:
        print(f"Removed {moving_kid}")
        continue
    else:
        kids_tossing_potato.append(moving_kid)

print(f"Last is {''.join(kids_tossing_potato)}")
