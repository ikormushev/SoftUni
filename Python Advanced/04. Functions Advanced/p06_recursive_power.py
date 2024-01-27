def recursive_power(number, power):
    multiplication = 1
    if power == 0:
        return multiplication
    multiplication = number * recursive_power(number, power - 1)
    return multiplication
