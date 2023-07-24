from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    VALID_FOOD_TYPES = {
        "Bread": Bread,
        "Cake": Cake,
    }

    VALID_DRINK_TYPES = {
        "Tea": Tea,
        "Water": Water,
    }

    VALID_TABLE_TYPES = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable,
    }

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        if self.__find_food_by_name(name):
            raise Exception(f"{food_type} {name} is already in the menu!")

        new_food = self.VALID_FOOD_TYPES[food_type](name, price)
        self.food_menu.append(new_food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        if self.__find_drink_by_name(name):
            raise Exception(f"{drink_type} {name} is already in the menu!")

        new_drink = self.VALID_DRINK_TYPES[drink_type](name, portion, brand)
        self.drinks_menu.append(new_drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        if self.__find_table_by_table_number(table_number):
            raise Exception(f"Table {table_number} is already in the bakery!")

        new_table = self.VALID_TABLE_TYPES[table_type](table_number, capacity)
        self.tables_repository.append(new_table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number, *food_names):
        table = self.__find_table_by_table_number(table_number)

        if not table:
            return f"Could not find table {table_number}"

        ordered_food = []
        not_in_menu_food = []

        for food_name in food_names:
            food = self.__find_food_by_name(food_name)
            if food:
                ordered_food.append(food)
                table.order_food(food)
            else:
                not_in_menu_food.append(food_name)

        order_info = "\n".join(repr(food) for food in ordered_food)
        not_in_menu_info = "\n".join(not_in_menu_food)

        result = f"Table {table_number} ordered:\n{order_info}"

        if not_in_menu_info:
            result += f"\n{self.name} does not have in the menu:\n{not_in_menu_info}"

        return result

    def order_drink(self, table_number, *drink_names):
        table = self.__find_table_by_table_number(table_number)

        if not table:
            return f"Could not find table {table_number}"

        ordered_drinks = []
        not_in_menu_drinks = []

        for drink_name in drink_names:
            drink = self.__find_drink_by_name(drink_name)
            if drink:
                ordered_drinks.append(drink)
                table.order_drink(drink)
            else:
                not_in_menu_drinks.append(drink_name)

        order_info = "\n".join(repr(drink) for drink in ordered_drinks)
        not_in_menu_info = "\n".join(not_in_menu_drinks)

        result = f"Table {table_number} ordered:\n{order_info}"

        if not_in_menu_info:
            result += f"\n{self.name} does not have in the menu:\n{not_in_menu_info}"

        return result

    def leave_table(self, table_number):
        table = self.__find_table_by_table_number(table_number)

        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        return "\n".join(table.free_table_info() for table in self.tables_repository)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def __find_table_by_table_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

        return None

    def __find_food_by_name(self, food_name):
        for food in self.food_menu:
            if food.name == food_name:
                return food

        return None

    def __find_drink_by_name(self, drink_name):
        for drink in self.drinks_menu:
            if drink.name == drink_name:
                return drink

        return None