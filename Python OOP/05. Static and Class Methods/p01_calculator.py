class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for el in args:
            result *= el
        return result

    @staticmethod
    def divide(*args):
        first_el = args[0]
        for i in range(1, len(args)):
            first_el /= args[i]
        return first_el

    @staticmethod
    def subtract(*args):
        first_el = args[0]
        for i in range(1, len(args)):
            first_el -= args[i]
        return first_el
