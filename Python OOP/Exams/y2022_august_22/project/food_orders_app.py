from project.meals.meal import Meal
from project.client import Client


class FoodOrdersApp:
    MIN_MENU_SIZE = 5
    VALID_MEALS = ["Starter", "MainDish", "Dessert"]
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        try:
            client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
            raise Exception("The client has already been registered!")
        except StopIteration:
            self.clients_list.append(Client(client_phone_number))
            return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.VALID_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < self.MIN_MENU_SIZE:
            raise Exception("The menu is not ready!")
        return "\n".join(x.details() for x in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < self.MIN_MENU_SIZE:
            raise Exception("The menu is not ready!")

        client = None
        try:
            client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        except StopIteration:
            self.register_client(client_phone_number)
            client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        for (meal, quantity) in meal_names_and_quantities.items():
            wanted_meal = None
            try:
                wanted_meal = next(filter(lambda m: m.name == meal, self.menu))
            except StopIteration:
                raise Exception(f"{meal} is not on the menu!")

            if wanted_meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {wanted_meal.__class__.__name__}: {meal}!")

        for (meal, quantity) in meal_names_and_quantities.items():
            wanted_meal = next(filter(lambda m: m.name == meal, self.menu))
            wanted_meal.quantity -= quantity
            client.shopping_cart.append(wanted_meal)

            if wanted_meal.name not in client.current_meals:
                client.current_meals[wanted_meal.name] = 0
            client.current_meals[wanted_meal.name] += quantity
            client.bill += wanted_meal.price * quantity

        return (f"Client {client_phone_number} successfully "
                f"ordered {', '.join(x.name for x in client.shopping_cart)} for {client.bill:.2f}lv.")

    def cancel_order(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal, quantity in client.current_meals.items():
            wanted_meal = next(filter(lambda m: m.name == meal, self.menu))
            wanted_meal.quantity += quantity
        client.shopping_cart = []
        client.bill = 0
        client.current_meals = {}
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        bill = client.bill
        self.receipt_id += 1

        client.shopping_cart = []
        client.bill = 0
        client.current_meals = {}

        return (f"Receipt #{self.receipt_id} with total amount of {bill:.2f} "
                f"was successfully paid for {client_phone_number}.")

    def __str__(self):
        return (f"Food Orders App has {len(self.menu)} "
                f"meals on the menu and {len(self.clients_list)} clients.")
