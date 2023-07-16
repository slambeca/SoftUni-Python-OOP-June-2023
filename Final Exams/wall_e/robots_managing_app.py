from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService,
    }

    VALID_ROBOT_TYPES = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot,
    }

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type, name):
        if service_type not in self.VALID_SERVICES.keys():
            raise Exception("Invalid service type!")

        new_service = self.VALID_SERVICES[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type, name, kind, price):
        if robot_type not in self.VALID_ROBOT_TYPES.keys():
            raise Exception("Invalid robot type!")

        new_robot = self.VALID_ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name, service_name):
        robot = self.__find_robot(robot_name)
        service = self.__find_service(service_name)

        if robot.POSSIBLE_SERVICE != service.__class__.__name__:
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name, service_name):
        service = self.__find_service(service_name)
        robot = [robot for robot in service.robots if robot.name == robot_name]

        if not robot:
            raise Exception("No such robot in this service!")

        robot_obj = robot[0]
        service.robots.remove(robot_obj)
        self.robots.append(robot_obj)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name):
        service = self.__find_service(service_name)
        number_of_robots_fed = len(service.robots)

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name):
        service = self.__find_service(service_name)

        total_price = sum(robot.price for robot in service.robots)
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return '\n'.join([s.details() for s in self.services])

    def __find_robot(self, robot_name):
        for robot in self.robots:
            if robot.name == robot_name:
                return robot

    def __find_service(self, service_name):
        for service in self.services:
            if service.name == service_name:
                return service