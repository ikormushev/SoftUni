def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for y in range(i + 1, len(array)):
            if array[y] < array[min_index]:
                min_index = y

        array[i], array[min_index] = array[min_index], array[i]

    return array


given_array = [int(x) for x in input().split()]

selection_sort(given_array)
print(*given_array)
