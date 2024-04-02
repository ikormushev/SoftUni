from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    VEHICLE_MAX_MILEAGE = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.VEHICLE_MAX_MILEAGE)

    def drive(self, mileage: float):
        percentage_reduction = round(mileage / self.max_mileage * 100)
        self.battery_level -= percentage_reduction
