numbers = input().split(" ")

new_numbers = []

for i in range(len(numbers)):
    new_numbers.append(float(numbers[i]))


def absolute_values():
    for y in range(len(new_numbers)):
        new_numbers[y] = abs(new_numbers[y])
    return new_numbers


print(absolute_values())
