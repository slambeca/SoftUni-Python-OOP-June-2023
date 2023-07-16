from project.services.base_service import BaseService


class SecondaryService(BaseService):
    DEFAULT_CAPACITY = 15

    def __init__(self, name):
        super().__init__(name, capacity=self.DEFAULT_CAPACITY)

    def details(self):
        if self.robots:
            return f"{self.name} Secondary Service:\nRobots: {' '.join(robot.name for robot in self.robots)}"

        return f"{self.name} Secondary Service:\nRobots: none"