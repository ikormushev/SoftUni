first_numbers = input().split(", ")
beggars_count = int(input())

numbers_list = list(first_numbers)
number_index = 0

beggars_collections = []
beggar_index = 0

for _ in range(beggars_count):
    beggars_collections.append(0)

while True:
    if beggar_index + 1 > beggars_count:
        beggar_index = 0

    if number_index == len(numbers_list):
        break
    beggars_collections[beggar_index] = (int(beggars_collections[beggar_index])
                                         + int(numbers_list[number_index]))
    beggar_index += 1
    number_index += 1

print(beggars_collections)
