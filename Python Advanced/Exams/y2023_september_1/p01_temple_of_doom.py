from collections import deque

tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = deque([int(x) for x in input().split()])

while tools and substances and challenges:
    current_challenges = challenges
    tool = tools.popleft()
    substance = substances.pop()
    result = tool * substance
    challenge_passed = False

    for _ in range(len(challenges)):
        challenge = current_challenges.popleft()
        if result == challenge:
            challenge_passed = True
            break
        current_challenges.append(challenge)

    if not challenge_passed:
        tool += 1
        tools.append(tool)
        substance -= 1
        if substance:
            substances.append(substance)

    challenges = current_challenges

if challenges and (not tools or not substances):
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join([str(x) for x in tools])}")

if substances:
    print(f"Substances: {', '.join([str(x) for x in substances])}")

if challenges:
    print(f"Challenges: {', '.join([str(x) for x in challenges])}")
