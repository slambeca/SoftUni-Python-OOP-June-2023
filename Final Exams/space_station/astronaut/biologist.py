from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    INITIAL_OXYGEN = 70

    def __init__(self, name):
        super().__init__(name, oxygen=self.INITIAL_OXYGEN)

    def breathe(self):
        self.oxygen -= 5
