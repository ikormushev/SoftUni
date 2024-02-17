def binary_search(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        mid_element = array[mid]

        if mid_element == target:
            return mid
        elif mid_element < target:
            start = mid + 1
        elif mid_element > target:
            end = mid - 1

    return -1


given_array = sorted([int(x) for x in input().split()])
wanted_element = int(input())

element_index = binary_search(given_array, wanted_element)
print(element_index)
