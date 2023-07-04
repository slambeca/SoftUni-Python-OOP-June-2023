from abc import ABC, abstractmethod
from math import log2, ceil, floor


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == "":
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == "":
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        pass

    # @staticmethod
    # def log2(x):
    #     # return log10(x) / log10(2)
    #     return log2(x)

    @staticmethod
    def power_of_two(ram: int):
        result = log2(ram)
        return floor(result) == ceil(result)    # we check if the result is 1.0, 2.0, 3.0, etc...

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"