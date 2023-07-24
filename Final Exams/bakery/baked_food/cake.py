from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    INITIAL_SIZE = 245

    def __init__(self, name, price):
        super().__init__(name, self.INITIAL_SIZE, price)