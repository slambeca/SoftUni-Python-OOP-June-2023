from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_ASTRONAUTS = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist,
    }

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type, name):
        if astronaut_type not in self.VALID_ASTRONAUTS.keys():
            raise Exception("Astronaut type is not valid!")

        astronaut = self.astronaut_repository.find_by_name(name)

        if astronaut:
            return f"{name} is already added."

        new_astronaut = self.VALID_ASTRONAUTS[astronaut_type](name)
        self.astronaut_repository.add(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name, items):
        planet = self.planet_repository.find_by_name(name)

        if planet:
            return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.items = items.split(", ")
        self.planet_repository.add(new_planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astronaut = self.astronaut_repository.find_by_name(name)

        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name):
        planet = self.planet_repository.find_by_name(planet_name)

        if not planet:
            raise Exception("Invalid planet name!")

        suitable_astronauts = [astronaut for astronaut in self.astronaut_repository.astronauts if astronaut.oxygen > 30]
        suitable_astronauts.sort(key=lambda x: -x.oxygen)

        if len(suitable_astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        astronauts_participated = 0
        for astronaut in suitable_astronauts[:5]:
            for item in planet.items[::-1]:
                if astronaut.oxygen <= 0:
                    break
                astronaut.breathe()
                astronaut.backpack.append(item)
                planet.items.remove(item)
            if not planet.items:
                astronauts_participated += 1
                break

        if not planet.items:
            return f"Planet: {planet_name} was explored. {astronauts_participated} astronauts participated in collecting items."

        return "Mission is not completed."

    def report(self):
        successful_missions = 0
        not_completed_missions = 0
        astronauts_info = ""

        for planet in self.planet_repository.planets:
            if not planet.items:
                successful_missions += 1
            else:
                not_completed_missions += 1

        for astronaut in self.astronaut_repository.astronauts:
            backpack_items = astronaut.backpack
            if not backpack_items:
                astronauts_info += f"Name: {astronaut.name}\nOxygen: {astronaut.oxygen}\n" \
                                   f"Backpack items: none\n"
                continue
            astronauts_info += f"Name: {astronaut.name}\nOxygen: {astronaut.oxygen}\n" \
                               f"Backpack items: {', '.join(backpack_items)}\n"

        return f"{successful_missions} successful missions!\n{not_completed_missions} missions were not completed!\n" \
               f"Astronauts' info:\n{astronauts_info}"
