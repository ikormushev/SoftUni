number = int(input())

numbers_sum = 0
for _ in range(number):
    new_number = int(input())
    numbers_sum += new_number

average_sum = numbers_sum / number
print(f"{average_sum:.2f}")
