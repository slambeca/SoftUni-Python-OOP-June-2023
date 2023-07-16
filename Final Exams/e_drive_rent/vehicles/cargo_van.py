from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180
    ADDITIONAL_PERCENT = 5

    def __init__(self, brand, model, license_plate_number):
        super().__init__(brand, model, license_plate_number, self.MAX_MILEAGE)

    def drive(self, mileage):
        self.battery_level -= (round(mileage / self.MAX_MILEAGE * 100) + self.ADDITIONAL_PERCENT)