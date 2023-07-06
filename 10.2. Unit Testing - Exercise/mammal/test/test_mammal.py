from unittest import TestCase, main
from project.mammal import Mammal


class MammalTests(TestCase):
    def setUp(self):
        self.mammal = Mammal("some name", "some type", "some sound")

    def test_proper_initializing_of_mammal(self):
        self.assertEqual("some name", self.mammal.name)
        self.assertEqual("some type", self.mammal.type)
        self.assertEqual("some sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_method(self):
        self.assertEqual("some name makes some sound", self.mammal.make_sound())

    def test_check_kingdom_type(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_get_info_method(self):
        self.assertEqual("some name is of type some type", self.mammal.info())


if __name__ == "__main__":
    main()