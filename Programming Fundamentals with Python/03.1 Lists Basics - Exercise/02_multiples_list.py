factor = int(input())
count = int(input())

integers_list = []
number = factor

for _ in range(count):
    integers_list.append(number)
    number += factor

print(integers_list)
