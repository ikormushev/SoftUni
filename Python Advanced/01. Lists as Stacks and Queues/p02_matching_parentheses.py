expression = input()

stack_brackets_indexes = []

for i in range(len(expression)):
    if expression[i] == "(":
        stack_brackets_indexes.append(i)
    elif expression[i] == ")":
        start_index = stack_brackets_indexes.pop()
        print(expression[start_index:i+1])
