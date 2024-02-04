from collections import deque

numbers = [int(x) for x in input().split(", ")]
sorted_numbers = deque(sorted(numbers))

wanted_job_index = int(input())
wanted_num = numbers[wanted_job_index]

clock_cycles = 0

while sorted_numbers:
    current_num = sorted_numbers.popleft()
    clock_cycles += current_num
    next_num = -1
    if len(sorted_numbers):
        next_num = sorted_numbers.popleft()
    if current_num == wanted_num and next_num != wanted_num:
        break
    else:
        if next_num != -1:
            sorted_numbers.appendleft(next_num)

print(clock_cycles)
