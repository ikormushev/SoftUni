numbers = input().split(" ")

numbers_list = list(numbers)
opposite_numbers = []

for i in range(len(numbers_list)):
    opposite_numbers.append(int(numbers_list[i]) * -1)

print(opposite_numbers)
