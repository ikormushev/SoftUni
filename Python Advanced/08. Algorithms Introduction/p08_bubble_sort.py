def bubble_sort(array):
    is_array_sorted = False

    while not is_array_sorted:
        is_array_sorted = True
        for i in range(1, len(array)):
            if array[i] < array[i - 1]:
                is_array_sorted = False
                array[i], array[i - 1] = array[i - 1], array[i]


given_array = [int(x) for x in input().split()]
bubble_sort(given_array)

print(*given_array)
