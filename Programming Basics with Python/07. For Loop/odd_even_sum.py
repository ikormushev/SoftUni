n = int(input())

even_sum = 0
odd_sum = 0

for i in range(n):
    new_number = int(input())
    if i % 2 == 0:
        even_sum += new_number
    else:
        odd_sum += new_number

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    subtraction = abs(even_sum - odd_sum)
    print("No")
    print(f"Diff = {subtraction}")
