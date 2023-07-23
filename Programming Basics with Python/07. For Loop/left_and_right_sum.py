n = int(input())

left_sum = 0
right_sum = 0

for i in range(1, n + 1):
    new_number = int(input())
    left_sum += new_number

for i in range(1, n + 1):
    new_number = int(input())
    right_sum += new_number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    subtraction = abs(left_sum - right_sum)
    print(f"No, diff = {subtraction}")
