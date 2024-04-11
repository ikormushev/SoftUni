from abc import ABC, abstractmethod


class Supply(ABC):
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value == "":
            raise ValueError("Name cannot be an empty string.")
        self.__name = value

    @property
    def energy(self):
        return self.__value

    @energy.setter
    def energy(self, value: int):
        if value < 0:
            raise ValueError("Energy cannot be less than zero.")
        self.__value = value

    @abstractmethod
    def details(self):
        pass