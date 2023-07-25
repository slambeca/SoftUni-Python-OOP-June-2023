from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    SUITABLE_FOR = "SaltwaterFish"
    INITIAL_CAPACITY = 25

    def __init__(self, name):
        super().__init__(name, self.INITIAL_CAPACITY)

    def add_fish(self, fish):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."

        self.fish.append(fish)
        return f"Successfully added {self.SUITABLE_FOR} to {self.name}."