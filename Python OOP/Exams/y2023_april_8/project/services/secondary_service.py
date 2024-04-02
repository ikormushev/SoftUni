from project.services.base_service import BaseService


class SecondaryService(BaseService):
    AVAILABLE_CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, self.AVAILABLE_CAPACITY)

    def details(self):
        robots = "none" if not self.robots else " ".join(x.name for x in self.robots)
        return f"{self.name} Secondary Service:\nRobots: {robots}"
