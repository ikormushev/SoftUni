train_wagons = int(input())


def train_creation(wagons: int) -> list:
    train = []
    for _ in range(wagons):
        train.append(0)
    return train


def train_commands(t: list) -> list:
    while True:
        command = input()
        if command == "End":
            return t

        new_command = command.split(" ")
        if "add" in new_command:
            t[-1] += int(new_command[1])
        elif "insert" in new_command:
            t[int(new_command[1])] += int(new_command[2])
        elif "leave" in new_command:
            t[int(new_command[1])] -= int(new_command[2])


print(train_commands(train_creation(train_wagons)))
