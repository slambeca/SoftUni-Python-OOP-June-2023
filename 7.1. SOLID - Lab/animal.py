class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Making sound"


class Dog(Animal):
    def make_sound(self):
        return super().make_sound() + " Woof woof"


class Cat(Animal):
    def make_sound(self):
        return super().make_sound() + " Meow meow"


class Monkey(Animal):
    def make_sound(self):
        return super().make_sound() + " Ua ua ua"


def animal_sound(some_animals: list):
    for animal in some_animals:
        print(animal.make_sound())


animals = [Dog('Sharo'), Cat('Lady'), Monkey("Monk")]
animal_sound(animals)