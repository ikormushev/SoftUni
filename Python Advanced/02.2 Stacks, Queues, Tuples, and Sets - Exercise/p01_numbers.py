first_sequence = set([int(x) for x in set(input().split())])
second_sequence = set([int(x) for x in set(input().split())])
number = int(input())

for _ in range(number):
    command = input().split()
    if command[0] == "Check":
        if first_sequence < second_sequence or second_sequence < first_sequence:
            print("True")
        else:
            print("False")
        continue

    numbers = set([int(x) for x in command[2:]])
    if command[0] == "Add":
        if command[1] == "First":
            first_sequence.update(numbers)
        elif command[1] == "Second":
            second_sequence.update(numbers)
    elif command[0] == "Remove":
        if command[1] == "First":
            first_sequence -= numbers
        elif command[1] == "Second":
            second_sequence -= numbers

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
