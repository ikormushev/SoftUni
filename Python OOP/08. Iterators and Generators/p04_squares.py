def squares(n: int):
    start = 1
    while start <= n:
        yield start ** 2
        start += 1
