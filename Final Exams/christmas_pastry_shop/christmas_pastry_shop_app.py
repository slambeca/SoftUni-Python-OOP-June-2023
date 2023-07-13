from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACIES = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen,
    }

    VALID_BOOTHS = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth,
    }

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy, name, price):
        delicacy = [delicacy for delicacy in self.delicacies if delicacy.name == name]

        if delicacy:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.VALID_DELICACIES.keys():
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.VALID_DELICACIES[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth, booth_number, capacity):
        booth = [booth for booth in self.booths if booth.booth_number == booth_number]

        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.VALID_BOOTHS.keys():
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.VALID_BOOTHS[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people):
        try:
            booth = next(filter(lambda b: b.capacity >= number_of_people and not b.is_reserved, self.booths))
        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number, delicacy_name):
        try:
            booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies))
        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        if booth and delicacy:
            booth.delicacy_orders.append(delicacy)
            return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number):
        booth = [booth for booth in self.booths if booth.booth_number == booth_number][0]
        total_sum = booth.price_for_reservation + sum(d.price for d in booth.delicacy_orders)
        self.income += total_sum
        booth.is_reserved = False
        booth.delicacy_orders = []
        # booth.delicacy_orders.clear()
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\nBill: {total_sum:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."