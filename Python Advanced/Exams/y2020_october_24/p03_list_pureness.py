def best_list_pureness(numbers, num):
    best_pureness = sum([numbers[x] * x for x in range(len(numbers))])
    best_rotations = 0
    rotations = 0

    for _ in range(num):
        rotations += 1

        last_element = numbers.pop()
        numbers.insert(0, last_element)

        current_sum = 0
        for i in range(len(numbers)):
            current_sum += i * numbers[i]

        if current_sum > best_pureness:
            best_pureness = current_sum
            best_rotations = rotations

    return f"Best pureness {best_pureness} after {best_rotations} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)