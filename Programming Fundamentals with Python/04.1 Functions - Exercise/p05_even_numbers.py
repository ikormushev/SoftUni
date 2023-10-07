numbers = list(map(int, input().split(" ")))


def even_number(x):
    if x % 2 == 0:
        return True
    else:
        return False


even_numbers_list = []

for i in range(len(numbers)):
    if even_number(numbers[i]):
        even_numbers_list.append(numbers[i])

print(even_numbers_list)
