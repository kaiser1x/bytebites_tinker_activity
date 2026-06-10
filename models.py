# ByteBites Models
#
# Customer:
#   Stores customer information including name and purchase history.
#
# FoodItem:
#   Represents a menu item with a name, price, category, and popularity rating.
#
# Menu:
#   Stores a collection of FoodItem objects and supports filtering/sorting.
#
# Transaction:
#   Stores selected FoodItem objects and calculates the total order cost.


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []


class FoodItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def filter_by_category(self, category):
        return [item for item in self.items if item.category == category]

    def sort_by_popularity(self):
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)


class Transaction:
    def __init__(self, selected_items=None):
        self.selected_items = selected_items if selected_items is not None else []

    def calculate_total(self):
        return sum(item.price for item in self.selected_items)
