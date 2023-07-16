from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    FEMALE_ROBOT_WEIGHT = 9
    POSSIBLE_SERVICE = "MainService"

    def __init__(self, name, kind, price):
        super().__init__(name, kind, price, self.FEMALE_ROBOT_WEIGHT)

    def eating(self):
        self.weight += 3