from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLES_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        try:
            user = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
            return f"{driving_license_number} has already been registered to our platform."
        except StopIteration:
            self.users.append(User(first_name, last_name, driving_license_number))
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLES_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        try:
            vehicle = next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
            return f"{license_plate_number} belongs to another vehicle."
        except StopIteration:
            self.vehicles.append(self.VALID_VEHICLES_TYPES[vehicle_type](brand, model, license_plate_number))
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_id = len(self.routes) + 1

        route = None
        try:
            route = next(filter(lambda r: r.start_point == start_point and r.end_point == end_point, self.routes))
        except StopIteration:
            pass

        if route is not None:
            if route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            else:
                route.is_locked = True

        self.routes.append(Route(start_point, end_point, length, route_id))
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
        vehicle = next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
        route = next(filter(lambda r: r.route_id == route_id, self.routes))
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()
        return str(vehicle)

    def repair_vehicles(self, count: int):
        needed_vehicles = [x for x in self.vehicles if x.is_damaged]
        needed_vehicles = list(sorted(needed_vehicles, key=lambda v: (v.brand, v.model)))

        new_count = 0
        while new_count < count:
            if new_count == len(needed_vehicles):
                break
            needed_vehicles[new_count].recharge()
            needed_vehicles[new_count].change_status()
            new_count += 1

        return f"{new_count} vehicles were successfully repaired!"

    def users_report(self):
        ordered_users = list(sorted(self.users, key=lambda u: -u.rating))
        new_users = [str(x) for x in ordered_users]

        return "*** E-Drive-Rent ***\n" + "\n".join(new_users)