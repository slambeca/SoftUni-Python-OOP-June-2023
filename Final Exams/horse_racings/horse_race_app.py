from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    HORSE_RACES_CREATED = []

    VALID_HORSES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred,
    }

    def __init__(self):
        self.horses = []    # Will contain horse objects
        self.jockeys = []    # Will contain jockey objects
        self.horse_races = []    # Will contain horse races

    def add_horse(self, horse_type, horse_name, horse_speed):
        horse = self.__find_horse_by_name(horse_name)

        if horse:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.VALID_HORSES.keys():
            new_horse = self.VALID_HORSES[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name, age):
        jockey = self.__find_jockey_by_name(jockey_name)

        if jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type):
        if race_type in self.HORSE_RACES_CREATED:
            raise Exception(f"Race {race_type} has been already created!")

        new_horse_race = HorseRace(race_type)
        self.HORSE_RACES_CREATED.append(race_type)
        self.horse_races.append(new_horse_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name, horse_type):
        jockey = self.__find_jockey_by_name(jockey_name)
        horse = self.__find_horse_by_type(horse_type)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type, jockey_name):
        horse_race = self.__find_horse_race(race_type)
        jockey = self.__find_jockey_by_name(jockey_name)

        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type):
        horse_race = self.__find_horse_race(race_type)

        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        fastest_jockey = None
        fastest_horse = None
        fastest_speed = 0

        for jockey in horse_race.jockeys:
            if jockey.horse.speed > fastest_speed:
                fastest_jockey = jockey
                fastest_horse = jockey.horse
                fastest_speed = jockey.horse.speed

        return f"The winner of the {race_type} race, with a speed of {fastest_speed}km/h is {fastest_jockey.name}! " \
               f"Winner's horse: {fastest_horse.name}."

    def __find_horse_by_name(self, horse_name):
        for horse in self.horses:
            if horse.name == horse_name:
                return horse

        return None

    def __find_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey

        return None

    def __find_horse_by_type(self, horse_type):
        for horse in self.horses[::-1]:
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                return horse

    def __find_horse_race(self, race_type):
        for horse_race in self.horse_races:
            if horse_race.race_type == race_type:
                return horse_race

        return None