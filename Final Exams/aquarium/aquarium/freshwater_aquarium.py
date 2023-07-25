from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    SUITABLE_FOR = "FreshwaterFish"
    INITIAL_CAPACITY = 50

    def __init__(self, name):
        super().__init__(name, self.INITIAL_CAPACITY)

    def add_fish(self, fish):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."

        self.fish.append(fish)
        return f"Successfully added {self.SUITABLE_FOR} to {self.name}."