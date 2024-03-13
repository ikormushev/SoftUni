from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    WEIGHT_INCREASE_BY_FOOD = 0.25
    FOODS_TO_EAT = [Meat]

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    WEIGHT_INCREASE_BY_FOOD = 0.35
    FOODS_TO_EAT = [Meat, Vegetable, Fruit, Seed]

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Cluck"
