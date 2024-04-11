from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAXIMUM_SPEED = 140
    TRAIN_SPEED_INCREASE = 3

    def train(self):
        if self.speed + self.TRAIN_SPEED_INCREASE > self.MAXIMUM_SPEED:
            self.speed = self.MAXIMUM_SPEED
        else:
            self.speed += self.TRAIN_SPEED_INCREASE
