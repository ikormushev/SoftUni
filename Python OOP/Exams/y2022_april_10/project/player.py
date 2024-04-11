class Player:
    players_names = []
    MAX_STAMINA = 100
    MIN_STAMINA = 0

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.players_names.append(name)
        self.age = age
        self.stamina = stamina

    @property
    def need_sustenance(self):
        return self.__stamina < 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value == "":
            raise ValueError("Name not valid!")
        elif value in self.players_names:
            raise Exception(f"Name {value} is already used!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value: int):
        if value < self.MIN_STAMINA or value > self.MAX_STAMINA:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
