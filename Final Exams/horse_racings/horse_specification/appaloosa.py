from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    HORSE_MAX_SPEED = 120

    def train(self):
        self.speed = min(self.speed + 2, self.HORSE_MAX_SPEED)