def solution():
    def integers():
        number = 1
        while True:
            yield number
            number += 1


    def halves():
        for i in integers():
            yield i / 2

    def take(n, generator):
        return [next(generator) for _ in range(n)]

    return (take, halves, integers)
