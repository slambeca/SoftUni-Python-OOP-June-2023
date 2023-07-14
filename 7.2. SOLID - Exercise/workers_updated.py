from abc import ABC, abstractmethod
import time


class Work(ABC):
    @abstractmethod
    def work(self):
        pass


class Eat(ABC):
    @abstractmethod
    def eat(self):
        pass


class BaseWorker(Work, Eat):
    def work(self):
        print("I'm a normal worker. I'm working, but only when the managers are watching.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Work, Eat):
    def work(self):
        print("My name is Tobby. I'm a super worker! I work very hard! I am the hardest worker!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(Work):
    def work(self):
        print("I'm a robot. I'm working. I don't need to eat, "
              "therefore I am more productive than the delusional Tobby.")


class Manager(ABC):
    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass


class WorkManager(Manager):
    def set_worker(self, worker):
        if not isinstance(worker, Work):
            raise AssertionError(f'`worker` must be able to work.')

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(Manager):
    def set_worker(self, worker):
        if not isinstance(worker, Eat):
            raise AssertionError(f'`worker` should be able to eat.')

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


work_manager = WorkManager()
break_manager = BreakManager()

work_manager.set_worker(BaseWorker())
break_manager.set_worker(BaseWorker())

work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())

work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()

try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass