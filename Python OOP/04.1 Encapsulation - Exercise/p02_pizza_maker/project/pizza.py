from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name_value: str):
        if name_value == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = name_value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, dough_value: Dough):
        if dough_value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = dough_value

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, max_toppings: int):
        if max_toppings <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = max_toppings

    def add_topping(self, topping: Topping):
        if len(self.toppings) + 1 > self.__max_number_of_toppings:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = 0
        self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        return self.dough.weight + sum(self.toppings.values())