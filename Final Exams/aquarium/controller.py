from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    VALID_AQUARIUM_TYPES = {
        "FreshwaterAquarium": FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium,
    }

    VALID_DECORATIONS = {
        "Ornament": Ornament,
        "Plant": Plant,
    }

    VALID_FISH_TYPES = {
        "FreshwaterFish": FreshwaterFish,
        "SaltwaterFish": SaltwaterFish,
    }

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type not in self.VALID_AQUARIUM_TYPES.keys():
            return "Invalid aquarium type."

        new_aquarium = self.VALID_AQUARIUM_TYPES[aquarium_type](aquarium_name)
        self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        if decoration_type not in self.VALID_DECORATIONS.keys():
            return "Invalid decoration type."

        new_decoration = self.VALID_DECORATIONS[decoration_type]()
        self.decorations_repository.add(new_decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        aquarium = self.__find_aquarium_by_name(aquarium_name)

        if decoration == "None" or not aquarium:
            return f"There isn't a decoration of type {decoration_type}."

        if decoration and aquarium:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        if fish_type not in self.VALID_FISH_TYPES.keys():
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.__find_aquarium_by_name(aquarium_name)

        if aquarium.SUITABLE_FOR != fish_type:
            return "Water not suitable."

        new_fish = self.VALID_FISH_TYPES[fish_type](fish_name, fish_species, price)
        return aquarium.add_fish(new_fish)

    def feed_fish(self, aquarium_name):
        aquarium = self.__find_aquarium_by_name(aquarium_name)

        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        total_sum = sum([fish.price for fish in aquarium.fish]) + \
                    sum([decoration.price for decoration in aquarium.decorations])

        return f"The value of Aquarium {aquarium_name} is {total_sum:.2f}."

    def report(self):
        return '\n'.join(str(aquarium) for aquarium in self.aquariums)

    def __find_aquarium_by_name(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium

        return None