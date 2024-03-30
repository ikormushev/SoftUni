from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    BASE_OXYGEN_LEVEL = 120
    MISS_DECREASE_VALUE = 0.6

    def __init__(self, name: str):
        super().__init__(name, self.BASE_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        decrease_value = self.MISS_DECREASE_VALUE * time_to_catch
        if self.oxygen_level - decrease_value < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= decrease_value
            self.oxygen_level = round(self.oxygen_level)

    def renew_oxy(self):
        self.oxygen_level = self.BASE_OXYGEN_LEVEL
