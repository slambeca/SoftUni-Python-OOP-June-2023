from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.starter import Starter


class FoodOrdersApp:
    receipt_id = 0    # The receipt_id should be incremented on each finished order

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number):
        client = self.__find_client_by_phone_number(client_phone_number)

        if client:
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if isinstance(meal, (Starter, MainDish, Dessert)):
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        result = ""
        for meal in self.menu:
            result += f"{meal.details()}\n"

        return result.strip()

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantity):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        if not self.__find_client_by_phone_number(client_phone_number):
            self.register_client(client_phone_number)

        client = self.__find_client_by_phone_number(client_phone_number)
        meals_to_order = []
        current_bill = 0

        for meal_name, meal_quantity in meal_names_and_quantity.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity >= meal_quantity:
                        meals_to_order.append(meal)
                        current_bill += meal.price * meal_quantity
                        break
                    else:
                        raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")
            else:
                raise Exception(f"{meal_name} is not on the menu!")

        client.shopping_cart.extend(meals_to_order)
        client.bill += current_bill

        for meal_name, meal_quantity in meal_names_and_quantity.items():
            if meal_name not in client.ordered_meals:
                client.ordered_meals[meal_name] = 0
            client.ordered_meals[meal_name] += meal_quantity
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity -= meal_quantity

        return f"Client {client_phone_number} " \
               f"successfully ordered {', '.join(meal.name for meal in client.shopping_cart)} " \
               f"for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number):
        client = self.__find_client_by_phone_number(client_phone_number)

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for ordered_meal, quantity in client.ordered_meals.items():
            for menu_meal in self.menu:
                if ordered_meal == menu_meal.name:
                    menu_meal.quantity += quantity

        client.shopping_cart = []
        client.bill = 0
        client.ordered_meals = {}
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):
        client = self.__find_client_by_phone_number(client_phone_number)

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        total_paid_money = f"{client.bill:.2f}"
        client.shopping_cart = []
        client.bill = 0
        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money} was successfully paid for " \
               f"{client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    def __find_client_by_phone_number(self, phone_number):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return client

        return None