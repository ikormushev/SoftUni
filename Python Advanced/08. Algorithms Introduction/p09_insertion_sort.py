def insertion_sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        index = i
        while index > 0 and array[index - 1] >= current_value:
            array[index] = array[index - 1]
            index -= 1
        array[index] = current_value


given_array = [int(x) for x in input().split()]
insertion_sort(given_array)

print(*given_array)
