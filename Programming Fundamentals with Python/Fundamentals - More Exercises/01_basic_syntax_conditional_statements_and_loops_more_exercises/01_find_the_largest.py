number = int(input())

numbers_list = []

for i in range(len(str(number))):
    numbers_list.append(str(number)[i])

numbers_list.sort(reverse=True)
print("".join(numbers_list))
