class Zoo:
    animals = 0

    def __init__(self, name):
        self.zoo_name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self, species):
        if species == "mammal":
            return (f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}"
                    f"\nTotal animals: {Zoo.animals}")
        elif species == "fish":
            return (f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}"
                    f"\nTotal animals: {Zoo.animals}")
        elif species == "bird":
            return (f"Birds in {self.zoo_name}: {', '.join(self.birds)}"
                    f"\nTotal animals: {Zoo.animals}")


zoo_name = input()
zoo = Zoo(zoo_name)
number = int(input())

for _ in range(number):
    animal_info = input().split(" ")
    animal_type = animal_info[0]
    animal_name = animal_info[1]
    Zoo.animals += 1
    zoo.add_animal(animal_type, animal_name)

info = input()
print(zoo.get_info(info))
