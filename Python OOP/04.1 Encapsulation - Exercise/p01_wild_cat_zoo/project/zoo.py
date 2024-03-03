from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int):
        if self.__budget - price >= 0 and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif len(self.animals) < self.__animal_capacity and self.__budget - price < 0:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries_sum = sum([worker.salary for worker in self.workers])
        if salaries_sum <= self.__budget:
            self.__budget -= salaries_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animals_money_for_care_sum = sum([animal.money_for_care for animal in self.animals])
        if animals_money_for_care_sum <= self.__budget:
            self.__budget -= animals_money_for_care_sum
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        lions = [animal for animal in self.animals if type(animal) is Lion]
        tigers = [animal for animal in self.animals if type(animal) is Tiger]
        cheetahs = [animal for animal in self.animals if type(animal) is Cheetah]

        return (f"You have {len(self.animals)} animals\n----- {len(lions)} Lions:\n" +
                '\n'.join([lion.__repr__() for lion in lions]) + f"\n----- {len(tigers)} Tigers:\n" +
                '\n'.join([tiger.__repr__() for tiger in tigers]) + f"\n----- {len(cheetahs)} Cheetahs:\n" +
                '\n'.join([cheetah.__repr__() for cheetah in cheetahs]))

    def workers_status(self):
        keepers = [worker for worker in self.workers if type(worker) is Keeper]
        caretakers = [worker for worker in self.workers if type(worker) is Caretaker]
        vets = [worker for worker in self.workers if type(worker) is Vet]

        return (f"You have {len(self.workers)} workers\n----- {len(keepers)} Keepers:\n" +
                '\n'.join([keeper.__repr__() for keeper in keepers]) + f"\n----- {len(caretakers)} Caretakers:\n" +
                '\n'.join([caretaker.__repr__() for caretaker in caretakers]) + f"\n----- {len(vets)} Vets:\n" +
                '\n'.join([vet.__repr__() for vet in vets]))
