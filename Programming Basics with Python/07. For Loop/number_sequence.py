from sys import maxsize

n = int(input())

max_n = -maxsize
min_n = maxsize

for _ in range(n):
    new_number = int(input())
    if new_number > max_n:
        max_n = new_number
    if new_number < min_n:
        min_n = new_number

print(f"Max number: {max_n}")
print(f"Min number: {min_n}")
