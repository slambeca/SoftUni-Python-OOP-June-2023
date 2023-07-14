from abc import ABC, abstractmethod


class Worker(ABC):
    @staticmethod
    @abstractmethod
    def work():
        pass


class BaseWorker(Worker):
    @staticmethod
    def work():
        print("I'm barely working!!")


class SuperWorker(Worker):
    @staticmethod
    def work():
        print("I'm working very, very hard!!!")


class SensationalWorker(Worker):
    @staticmethod
    def work():
        print("I know I am the best at working!")


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, Worker):
            raise AssertionError(f'`worker` must be of type {Worker}')

        self.worker = worker

    def manage(self):
        if self.worker:
            self.worker.work()


worker = BaseWorker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
sensational_worker = SensationalWorker()

try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")

manager.set_worker(sensational_worker)
manager.manage()