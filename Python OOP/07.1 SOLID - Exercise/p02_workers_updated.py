from abc import ABC, abstractmethod
import time


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Worker(Workable, Eatable):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Workable, Eatable):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class BaseManager(ABC):
    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass


class WorkManager(BaseManager):
    def set_worker(self, worker):
        assert isinstance(worker, Workable), f"`worker` must be of type {Workable}"
        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(BaseManager):
    def set_worker(self, worker):
        assert isinstance(worker, Eatable), f"`worker` must be of type {Eatable}"
        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


class Robot(Workable):
    def work(self):
        print("I'm a robot. I'm working....")
