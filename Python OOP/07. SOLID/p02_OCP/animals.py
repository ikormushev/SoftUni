from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    def get_species(self):
        return self.__class__.__name__

    @staticmethod
    @abstractmethod
    def make_sound():
        pass


class Cat(Animal):
    @staticmethod
    def make_sound():
        return f"meow"


class Dog(Animal):
    @staticmethod
    def make_sound():
        return f"woof-woof"


class Chicken(Animal):
    @staticmethod
    def make_sound():
        return f"cluck-cluck"


def animal_sounds(animals: List[Animal]):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Chicken()]
animal_sounds(animals)
