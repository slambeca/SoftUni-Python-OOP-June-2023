from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CARS = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar,
    }

    def __init__(self):
        self.cars = []    # Will contain Car objects
        self.drivers = []    # Will contain Driver objects
        self.races = []    # Will contain Race objects

    def create_car(self, car_type, model, speed_limit):
        car = self.__find_car_by_model(model)

        if car in self.cars:
            raise Exception(f"Car {model} is already created!")

        if car_type in self.VALID_CARS.keys():
            new_car = self.VALID_CARS[car_type](model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name):
        driver = self.__find_driver_by_name(driver_name)

        if driver:
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        race = self.__find_race_by_name(race_name)

        if race:
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        driver = next((driver for driver in self.drivers if driver.name == driver_name), None)
        car = self.__find_car_by_type(car_type)

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not car:
            raise Exception(f"Car {car_type} could not be found!")

        if car and driver.car:
            driver.car.is_taken = False
            old_car = driver.car
            driver.car = car
            car.is_taken = True
            return f"Driver {driver.name} changed his car from {old_car.model} to {car.model}."

        if car and not driver.car:
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name, driver_name):
        race = self.__find_race_by_name(race_name)
        driver = self.__find_driver_by_name(driver_name)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):
        race = self.__find_race_by_name(race_name)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(self.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        sorted_drivers = sorted(race.drivers, key=lambda driver: driver.car.speed_limit, reverse=True)

        result = ""

        for i in range(3):
            driver = sorted_drivers[i]
            driver.number_of_wins += 1
            speed_limit = driver.car.speed_limit
            result += f"Driver {driver.name} wins the {race_name} race with a speed of {speed_limit}.\n"

        return result.strip()

    def __find_car_by_model(self, model):
        for car in self.cars:
            if car.model == model:
                return car

        return None

    def __find_driver_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver

        return None

    def __find_race_by_name(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race

        return None

    def __find_car_by_type(self, car_type):
        for car in self.cars[::-1]:
            if car.__class__.__name__ == car_type and not car.is_taken:
                return car

        return None