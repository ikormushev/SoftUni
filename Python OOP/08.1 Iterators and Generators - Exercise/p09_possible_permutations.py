from itertools import permutations


def possible_permutations(numbers: list):
    for num in permutations(numbers):
        yield list(num)
