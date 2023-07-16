from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    FEMALE_ROBOT_WEIGHT = 7
    POSSIBLE_SERVICE = "SecondaryService"

    def __init__(self, name, kind, price):
        super().__init__(name, kind, price, self.FEMALE_ROBOT_WEIGHT)

    def eating(self):
        self.weight += 1