def find_closing_parentheses(parenthesis):
    closing_parentheses = {"(": ")", "[": "]", "{": "}"}
    if parenthesis in closing_parentheses:
        return closing_parentheses[parenthesis]
    return ""


parentheses = input()
unbalanced_parentheses = False
parentheses_stack = []

for given_parenthesis in parentheses:
    if given_parenthesis in ["(", "{", "["]:
        parentheses_stack.append(given_parenthesis)
    elif given_parenthesis in [")", "}", "]"]:
        if not parentheses_stack or given_parenthesis != find_closing_parentheses(parentheses_stack.pop()):
            unbalanced_parentheses = True
            break

if unbalanced_parentheses:
    print("NO")
else:
    print("YES")
