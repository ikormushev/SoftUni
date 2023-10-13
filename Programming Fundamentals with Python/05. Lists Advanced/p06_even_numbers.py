numbers = list(map(int, input().split(", ")))

even_numbers_indexes = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_numbers_indexes.append(i)

print(even_numbers_indexes)
