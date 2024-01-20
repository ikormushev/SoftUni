from collections import deque

expression = deque(input().split())

numbers = deque()

operations = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x // y
}

while expression:
    element = expression.popleft()
    if element in ["*", "+", "-", "/"]:
        new_number = numbers.popleft()
        while numbers:
            next_number = numbers.popleft()
            new_number = operations[element](new_number, next_number)
        numbers.append(new_number)
    else:
        numbers.append(int(element))

print(numbers.popleft())
