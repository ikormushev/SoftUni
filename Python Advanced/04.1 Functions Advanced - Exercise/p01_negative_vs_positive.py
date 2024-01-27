def operations(numbers):
    def sum_positives():
        return sum([x for x in numbers if x > 0])

    def sum_negatives():
        return sum([x for x in numbers if x < 0])

    def bigger_absolute_value():
        if sum_positives() > abs(sum_negatives()):
            return "The positives are stronger than the negatives"
        else:
            return "The negatives are stronger than the positives"

    print(sum_negatives())
    print(sum_positives())
    print(bigger_absolute_value())


given_numbers = [int(x) for x in input().split()]
operations(given_numbers)
