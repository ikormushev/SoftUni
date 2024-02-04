from collections import deque

operations = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x // y
}
sequence = deque(input().split())

current_numbers = deque()

while sequence:
    current_element = sequence.popleft()
    if current_element in ["*", "+", "-", "/"]:
        current_num = current_numbers.popleft()
        while current_numbers:
            next_num = current_numbers.popleft()
            if current_element == "/" and next_num == 0:
                continue
            else:
                current_num = operations[current_element](current_num, next_num)
        current_numbers.append(current_num)
    else:
        current_numbers.append(int(current_element))
print(current_numbers.popleft())
