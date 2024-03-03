class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight

    @property
    def flour_type(self):
        return self.__flour_type

    @flour_type.setter
    def flour_type(self, flour: str):
        if flour == "":
            raise ValueError("The flour type cannot be an empty string")
        self.__flour_type = flour

    @property
    def baking_technique(self):
        return self.__baking_technique

    @baking_technique.setter
    def baking_technique(self, technique: str):
        if technique == "":
            raise ValueError("The baking technique cannot be an empty string")
        self.__baking_technique = technique

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight_value: float):
        if weight_value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight = weight_value
