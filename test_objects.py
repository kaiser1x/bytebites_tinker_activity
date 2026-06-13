from models import Customer, FoodItem, Menu, Transaction

customer = Customer("John Doe")

burger = FoodItem(
"Spicy Burger",
8.99,
"Entree",
4.7
)

soda = FoodItem(
"Large Soda",
2.49,
"Drinks",
4.3
)

menu = Menu()
transaction = Transaction()

print(customer.name)
print(customer.purchase_history)

print(burger.name)
print(burger.price)

print(menu.items)
print(transaction.selected_items)
