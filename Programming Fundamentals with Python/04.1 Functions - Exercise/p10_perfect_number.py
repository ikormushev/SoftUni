number = int(input())


def proper_divisors(n):
    dividers_list = []
    for i in range(1, n):
        if n % i == 0:
            dividers_list.append(i)
    return dividers_list


def total_aliquot_sum(dividers):
    aliquot_sum = 0
    for j in range(len(dividers)):
        aliquot_sum += dividers[j]
    return aliquot_sum


def is_number_perfect():
    if total_aliquot_sum(proper_divisors(number)) == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


is_number_perfect()
