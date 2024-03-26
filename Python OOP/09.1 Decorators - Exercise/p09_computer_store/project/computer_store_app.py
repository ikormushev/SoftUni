from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_COMPUTER_TYPES = {"Laptop": lambda x, y: Laptop(x, y),
                            "Desktop Computer": lambda x, y: DesktopComputer(x, y)}

    def __init__(self):
        self.warehouse: list = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_COMPUTER_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        new_computer = self.VALID_COMPUTER_TYPES[type_computer](manufacturer, model)
        configuration = new_computer.configure_computer(processor, ram)
        self.warehouse.append(new_computer)

        return configuration

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        try:
            computer = next(filter(lambda comp: comp.price <= client_budget
                                                and comp.processor == wanted_processor
                                                and comp.ram >= wanted_ram, self.warehouse))
            self.profits += client_budget - computer.price
            self.warehouse.remove(computer)
            return f"{computer} sold for {client_budget}$."

        except StopIteration:
            raise Exception(f"Sorry, we don't have a computer for you.")
