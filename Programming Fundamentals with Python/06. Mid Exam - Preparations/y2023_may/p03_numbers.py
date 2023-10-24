integers = list(map(int, input().split(" ")))
average_value = sum(integers) / len(integers)

higher_than_average_numbers = [x for x in integers if x > average_value]

if len(higher_than_average_numbers) == 0:
    print("No")
else:
    sorted_numbers = sorted(higher_than_average_numbers)
    if len(sorted_numbers) > 5:
        items_to_be_removed = len(sorted_numbers) - 5
        for _ in range(items_to_be_removed):
            sorted_numbers.pop(0)

    reverse_sorted_numbers = sorted(sorted_numbers, reverse=True)
    for i in range(len(reverse_sorted_numbers)):
        if i == len(reverse_sorted_numbers) - 1:
            print(reverse_sorted_numbers[i])
        else:
            print(reverse_sorted_numbers[i], end=" ")
