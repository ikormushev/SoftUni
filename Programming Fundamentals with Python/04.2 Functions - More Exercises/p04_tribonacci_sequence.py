number = int(input())


def tribonacci_sequence(x):
    previous_numbers_sum = [0, 0, 0]
    for _ in range(x):
        if sum(previous_numbers_sum) == 0 or sum(previous_numbers_sum) == 1:
            number_sum = 1
        else:
            number_sum = sum(previous_numbers_sum)
        previous_numbers_sum.pop(0)
        previous_numbers_sum.append(number_sum)
        print(number_sum, end=" ")


tribonacci_sequence(number)
