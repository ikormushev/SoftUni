from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    INITIAL_WEIGHT_KG = 9
    WEIGHT_INCREASE_AFTER_EATING_KG = 3

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.INITIAL_WEIGHT_KG)

    def eating(self):
        self.weight += self.WEIGHT_INCREASE_AFTER_EATING_KG