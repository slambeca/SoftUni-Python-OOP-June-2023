from unittest import TestCase, main


class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat("Misha")

    def test_correct_initializing_of_cat(self):
        self.assertEqual("Misha", self.cat.name)
        self.assertFalse(self.cat.fed)    # We use assertFalse instead of assertEqual(False, ...)
        self.assertEqual(False, self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_valid_cat_eating(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_feeding_already_fed_cat_expect_raise_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_if_cat_is_sleepy_after_sleeping(self):
        self.cat.sleepy = True
        self.cat.fed = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

    def test_if_cat_is_not_fed_expect_raise_exception(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))


if __name__ == "__main__":
    main()