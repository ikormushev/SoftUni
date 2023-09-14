from sys import maxsize

largest_number = -maxsize

for _ in range(3):
    number = int(input())
    if number > largest_number:
        largest_number = number

print(largest_number)
