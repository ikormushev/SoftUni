from sys import maxsize

n = int(input())

numbers_sum = 0
max_num = -maxsize

for _ in range(n):
    new_number = int(input())
    if new_number > max_num:
        max_num = new_number
    numbers_sum += new_number

if max_num == numbers_sum - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    numbers_sum -= max_num
    subtraction = abs(max_num - numbers_sum)
    print("No")
    print(f"Diff = {subtraction}")
