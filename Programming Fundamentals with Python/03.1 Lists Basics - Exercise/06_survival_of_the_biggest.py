numbers_list = input().split(" ")
numbers_removal_count = int(input())

new_numbers = []

for i in range(len(numbers_list)):
    new_numbers.append(int(numbers_list[i]))

sorted_numbers_list = new_numbers
sorted_numbers_list.sort()

removed_numbers_list = []

for y in range(numbers_removal_count):
    removed_numbers_list.append(sorted_numbers_list[y])

final_numbers = []
for j in range(len(numbers_list)):
    if int(numbers_list[j]) not in removed_numbers_list:
        final_numbers.append(numbers_list[j])


for k in range(len(final_numbers)):
    if k < len(final_numbers) - 1:
        print(final_numbers[k], end=", ")
    else:
        print(final_numbers[k], end="")
