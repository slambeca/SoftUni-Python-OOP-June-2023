from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_TYPES = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan,
    }

    def __init__(self):
        self.users = []    # Contains user objects
        self.vehicles = []    # Contains vehicle objects
        self.routes = []    # Contains route objects

    def register_user(self, first_name, last_name, driving_license_number):
        user = self.__find_user(driving_license_number)

        if user is None:
            new_user = User(first_name, last_name, driving_license_number)
            self.users.append(new_user)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

        return f"{driving_license_number} has already been registered to our platform."

    def upload_vehicle(self, vehicle_type, brand, model, license_plate_number):
        if vehicle_type not in self.VALID_TYPES.keys():
            return f"Vehicle type {vehicle_type} is inaccessible."

        vehicle = self.__find_vehicle(license_plate_number)

        if vehicle is None:
            new_vehicle = self.VALID_TYPES[vehicle_type](brand, model, license_plate_number)
            self.vehicles.append(new_vehicle)
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

        return f"{license_plate_number} belongs to another vehicle."

    def allow_route(self, start_point, end_point, length):
        route = self.__find_route(start_point, end_point)

        if route:
            if route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            route.is_locked = True

        idx = len(self.routes) + 1
        new_route = Route(start_point, end_point, length, idx)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number, license_plate_number, route_id, is_accident_happened):
        user = self.__find_user(driving_license_number)
        vehicle = self.__find_vehicle(license_plate_number)
        route = self.__find_route_by_id(route_id)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count):
        damaged_vehicles = [vehicle for vehicle in self.vehicles if vehicle.is_damaged]
        sorted_vehicles = sorted(damaged_vehicles, key=lambda vehicle: (vehicle.brand, vehicle.model))[:count]

        for vehicle in sorted_vehicles:
            vehicle.is_damaged = False
            vehicle.battery_level = 100

        return f"{len(sorted_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda x: x.rating, reverse=True)
        result = "*** E-Drive-Rent ***\n"

        for user in sorted_users:
            result += f"{str(user)}\n"

        return result.strip()

    def __find_user(self, driving_license_number):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return user

    def __find_vehicle(self, license_plate_number):
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return vehicle

    def __find_route(self, start_point, end_point):
        filtered_routes = [route for route in self.routes if route.start_point == start_point
                           and route.end_point == end_point]
        if filtered_routes:
            return filtered_routes[0]

        return None

    def __find_route_by_id(self, route_id):
        filtered_routes = [route for route in self.routes if route.route_id == route_id]

        if filtered_routes:
            return filtered_routes[0]

        return None
