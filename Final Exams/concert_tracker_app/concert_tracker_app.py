from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_TYPES = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer,
    }

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type, name, age):
        if musician_type not in self.VALID_TYPES.keys():
            raise ValueError("Invalid musician type!")

        musician = self.__find_musician_by_name(name)

        if musician:
            raise Exception(f"{name} is already a musician!")

        new_musician = self.VALID_TYPES[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name):
        band = self.__find_band_by_name(name)

        if band:
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre, audience, ticket_price, expenses, place):
        concert = self.__find_concert_by_place(place)

        if concert:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name, band_name):
        musician = self.__find_musician_by_name(musician_name)
        band = self.__find_band_by_name(band_name)

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name, band_name):
        band = self.__find_band_by_name(band_name)

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = self.__find_musician_added_to_band_by_name(band, musician_name)
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place, band_name):
        band = self.__find_band_by_name(band_name)
        singer, drummer, guitarist = 0, 0, 0

        for member in band.members:
            if isinstance(member, Singer):
                singer += 1
            elif isinstance(member, Drummer):
                drummer += 1
            elif isinstance(member, Guitarist):
                guitarist += 1

        if not all([singer, drummer, guitarist]):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = self.__find_concert_by_place(concert_place)

        if concert.genre == "Rock":
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drumsticks" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ == "Singer" and "sing high pitch notes" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ == "Guitarist" and "play rock" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
        elif concert.genre == "Metal":
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drumsticks" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ == "Singer" and "sing low pitch notes" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ == "Guitarist" and "play metal" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
        elif concert.genre == "Jazz":
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drum brushes" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ == "Singer" and ("sing high pitch notes" not in member.skills
                                                                or "sing low pitch notes" not in member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ == "Guitarist" and "play jazz" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

    def __find_musician_by_name(self, musician_name):
        for musician in self.musicians:
            if musician.name == musician_name:
                return musician

        return None

    def __find_band_by_name(self, band_name):
        for band in self.bands:
            if band.name == band_name:
                return band

        return None

    def __find_concert_by_place(self, concert_place):
        for concert in self.concerts:
            if concert.place == concert_place:
                return concert

        return None

    @staticmethod
    def __find_musician_added_to_band_by_name(band, musician_name):
        for musician in band.members:
            if musician.name == musician_name:
                return musician
        else:
            raise Exception(f"{musician_name} isn't a member of {band.name}!")
