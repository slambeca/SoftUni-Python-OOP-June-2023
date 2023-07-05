from unittest import TestCase, main


class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(TestCase):
    # The setUp() is called before every test
    def setUp(self):
        self.worker = Worker("Borislav Ivanov", 2500, 100)    # First we set up our worker object

    def test_correct_initializing_of_worker(self):    # Then we test if the __init__ works correctly, all attributes
        self.assertEqual("Borislav Ivanov", self.worker.name)
        self.assertEqual(2500, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_increment_money_on_worker_when_working(self):
        self.worker.work()
        self.assertEqual(2500, self.worker.money)    # The worker gained one salary

    def test_decrease_energy_on_worker_when_working(self):
        self.worker.work()
        self.assertEqual(99, self.worker.energy)    # The energy is decreased by one point

    def test_raise_exception_when_worker_is_working_with_zero_or_negative_energy(self):
        # We can create new worker, or we can set the energy of our worker to 0 or less
        self.worker.energy = 0    # Arrange

        with self.assertRaises(Exception) as ex:
            self.worker.work()    # Act

        self.assertEqual(str(ex.exception), "Not enough energy.")    # Assert

    def test_increase_worker_energy_after_resting(self):
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_get_worker_info(self):
        result = self.worker.get_info()
        expected_result = "Borislav Ivanov has saved 0 money."
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()