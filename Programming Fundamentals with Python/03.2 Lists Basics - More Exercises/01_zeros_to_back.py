numbers = input().split(", ")

zeros_num = numbers.count("0")
new_numbers_list = []

for _ in range(zeros_num):
    numbers.remove("0")

for i in range(len(numbers)):
    new_numbers_list.append(int(numbers[i]))

for _ in range(zeros_num):
    new_numbers_list.append(0)

print(new_numbers_list)
