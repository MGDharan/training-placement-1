# Filename:  inventory_management.py
class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.quantity}"

inventory = []
inventory.append(Item("Shirt", 10))
inventory.append(Item("Pants", 5))
inventory.append(Item("Shoes", 12))

for item in inventory:
    print(item)

def add_item(inventory, name, quantity):
    inventory.append(Item(name, quantity))

add_item(inventory, "Hat", 8)

for item in inventory:
    print(item)