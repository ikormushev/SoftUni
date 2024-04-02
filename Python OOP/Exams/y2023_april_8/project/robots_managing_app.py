from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = {"MainService": {"instance": MainService, "available_robots": "MaleRobot"},
                      "SecondaryService": {"instance": SecondaryService, "available_robots": "FemaleRobot"}}
    VALID_ROBOTS = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots: list = []
        self.services: list = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")
        self.services.append(self.VALID_SERVICES[service_type]["instance"](name))
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")
        self.robots.append(self.VALID_ROBOTS[robot_type](name, kind, price))
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        wanted_robot = next(filter(lambda r: r.name == robot_name, self.robots))
        wanted_service = next(filter(lambda s: s.name == service_name, self.services))

        if (self.VALID_SERVICES[wanted_service.__class__.__name__]["available_robots"]
                != wanted_robot.__class__.__name__):
            return f"Unsuitable service."

        if len(wanted_service.robots) == wanted_service.capacity:
            raise Exception("Not enough capacity for this robot!")

        wanted_service.robots.append(wanted_robot)
        self.robots.remove(wanted_robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        try:
            wanted_service = next(filter(lambda s: s.name == service_name, self.services))
            wanted_robot = next(filter(lambda r: r.name == robot_name, wanted_service.robots))
            wanted_service.robots.remove(wanted_robot)
            self.robots.append(wanted_robot)
            return f"Successfully removed {robot_name} from {service_name}."

        except StopIteration:
            raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str):
        wanted_service = next(filter(lambda s: s.name == service_name, self.services))
        [x.eating() for x in wanted_service.robots]
        return f"Robots fed: {len(wanted_service.robots)}."

    def service_price(self, service_name: str):
        wanted_service = next(filter(lambda s: s.name == service_name, self.services))

        total_price = sum(x.price for x in wanted_service.robots)
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return "\n".join(x.details() for x in self.services)
