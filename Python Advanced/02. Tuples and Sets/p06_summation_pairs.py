from collections import deque

numbers = deque([int(x) for x in input().split()])
target_num = int(input())

for _ in range(len(numbers)):
    if numbers:
        number = numbers.popleft()
        for _ in range(len(numbers)):
            if numbers:
                new_number = numbers.popleft()
                if number + new_number == target_num:
                    print(f"{number} + {new_number} = {target_num}")
                else:
                    numbers.append(new_number)
