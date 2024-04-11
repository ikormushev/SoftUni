from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAXIMUM_SPEED = 120
    TRAIN_SPEED_INCREASE = 2

    def train(self):
        if self.speed + self.TRAIN_SPEED_INCREASE > self.MAXIMUM_SPEED:
            self.speed = self.MAXIMUM_SPEED
        else:
            self.speed += self.TRAIN_SPEED_INCREASE
