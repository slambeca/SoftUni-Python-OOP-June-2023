from project.services.base_service import BaseService


class MainService(BaseService):
    DEFAULT_CAPACITY = 30

    def __init__(self, name):
        super().__init__(name, capacity=self.DEFAULT_CAPACITY)

    def details(self):
        if self.robots:
            return f"{self.name} Main Service:\nRobots: {' '.join(robot.name for robot in self.robots)}"

        return f"{self.name} Main Service:\nRobots: none"