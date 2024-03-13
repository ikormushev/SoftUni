from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    WEIGHT_INCREASE_BY_FOOD = 0.10
    FOODS_TO_EAT = [Vegetable, Fruit]

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):
    WEIGHT_INCREASE_BY_FOOD = 0.40
    FOODS_TO_EAT = [Meat]

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):
    WEIGHT_INCREASE_BY_FOOD = 0.30
    FOODS_TO_EAT = [Meat, Vegetable]

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    WEIGHT_INCREASE_BY_FOOD = 1.00
    FOODS_TO_EAT = [Meat]

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "ROAR!!!"
