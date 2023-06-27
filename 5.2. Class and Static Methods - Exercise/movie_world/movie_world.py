from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    # DVD_CAPACITY = 15
    # CUSTOMER_CAPACITY = 10

    def __init__(self, name):
        self.name = name
        self.customers = []    # Customer objects
        self.dvds = []    # dvd objects

    @staticmethod
    def dvd_capacity():
        # return MovieWorld.DVD_CAPACITY
        return 15

    @staticmethod
    def customer_capacity():
        # return MovieWorld.CUSTOMER_CAPACITY
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():    # MovieWorld.customer_capacity()
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():    # MovieWorld.dvd_capacity()
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = [customer for customer in self.customers if customer.id == customer_id][0]
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]

        if dvd.is_rented and dvd not in customer.rented_dvds:
            return f"DVD is already rented"

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = [customer for customer in self.customers if customer.id == customer_id][0]
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]

        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += f"{customer.__repr__()}\n"
        for dvd in self.dvds:
            result += f"{dvd.__repr__()}\n"

        return result.strip()