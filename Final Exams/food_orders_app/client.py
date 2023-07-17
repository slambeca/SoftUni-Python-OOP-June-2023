class Client:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.shopping_cart = []    # Will contain meal objects
        self.bill = 0.0
        self.ordered_meals = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if len(value) != 10 or not value.startswith("0") or not value.isdigit():
            raise ValueError("Invalid phone number!")
        self.__phone_number = value