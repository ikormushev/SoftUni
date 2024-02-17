# recursive way
def find_sum(numbers, index):
    if index == len(numbers) - 1:
        return numbers[index]

    return numbers[index] + find_sum(numbers, index + 1)


given_array = [int(x) for x in input().split()]

array_sum = find_sum(given_array, 0)

""" iterative way
for num in given_array:
    array_sum += num
"""

print(array_sum)
