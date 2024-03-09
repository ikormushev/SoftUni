from math import floor


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        if type(float_value) is not float:
            return "value is not a float"
        return cls(floor(float_value))

    @classmethod
    def from_roman(cls, value: str):
        roman_numbers = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        result = 0
        skip_next = False
        for i in range(len(value)):
            if skip_next:
                skip_next = False
                continue

            if i + 1 < len(value):
                new_el = value[i] + value[i+1]
                if new_el in roman_numbers:
                    result += roman_numbers[new_el]
                    skip_next = True
                    continue
            result += roman_numbers[value[i]]
        return cls(result)

    @classmethod
    def from_string(cls, value: str):
        if type(value) is not str:
            return "wrong type"
        return cls(int(value))

