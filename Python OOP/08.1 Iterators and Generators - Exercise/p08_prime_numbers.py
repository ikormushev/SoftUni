def get_primes(numbers: list):
    prime_numbers = [x for x in numbers if len([d for d in range(1, x + 1) if x % d == 0]) == 2]
    yield from prime_numbers  # this is just like a normal for loop
