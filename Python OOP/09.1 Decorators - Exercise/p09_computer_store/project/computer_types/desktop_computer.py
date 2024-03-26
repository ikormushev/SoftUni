from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    AVAILABLE_PROCESSORS_WITH_PRICES = {
        "AMD Ryzen 7 5700G": 500,
        "Intel Core i5-12600K": 600,
        "Apple M1 Max": 1800
    }
    MAX_RAM = 128
    VALID_RAM_WITH_PRICES = {2 ** x: x * 100 for x in range(1, 8)}

    def __int__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.AVAILABLE_PROCESSORS_WITH_PRICES:
            raise ValueError(f"{processor} is not compatible with "
                             f"desktop computer {self.manufacturer} {self.model}!")

        if ram not in self.VALID_RAM_WITH_PRICES or ram > self.MAX_RAM:
            raise ValueError(f"{ram}GB RAM is not compatible with "
                             f"desktop computer {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram

        self.price += self.AVAILABLE_PROCESSORS_WITH_PRICES[processor]
        self.price += self.VALID_RAM_WITH_PRICES[ram]
        return (f"Created {self.manufacturer} {self.model} with {self.processor} "
                f"and {self.ram}GB RAM for {self.price}$.")