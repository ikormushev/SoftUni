def modifying_stack(given_query: str, given_stack: list):
    split_query = given_query.split()
    if split_query[0] == "1":
        given_stack.append(int(split_query[1]))
    elif split_query[0] == "2":
        if given_stack:
            given_stack.pop()
    elif split_query[0] == "3":
        if given_stack:
            print(max(given_stack))
    elif split_query[0] == "4":
        if given_stack:
            print(min(given_stack))


stack = []
number = int(input())

for _ in range(number):
    query = input()
    modifying_stack(query, stack)

while stack:
    if len(stack) == 1:
        print(stack.pop())
    else:
        print(stack.pop(), end=", ")
