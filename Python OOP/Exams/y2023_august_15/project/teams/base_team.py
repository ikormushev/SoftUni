from abc import ABC, abstractmethod


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value == "" or not value.strip():
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value: str):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value: int):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        result = (f"Name: {self.name}\n"
                  f"Country: {self.country}\n"
                  f"Advantage: {self.advantage} points\n"
                  f"Budget: {self.budget:.2f}EUR\n"
                  f"Wins: {self.wins}\n"
                  f"Total Equipment Price: {sum([eq.price for eq in self.equipment]):.2f}")

        average_protection = 0
        try:
            average_protection = sum([eq.protection for eq in self.equipment]) / len(self.equipment)
        except ZeroDivisionError:
            pass
        result += f"\nAverage Protection: {int(average_protection)}"
        return result
