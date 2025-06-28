# Filename:  inventory_manager.py
class InventoryItem:
    def __init__(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Quantity: {self.quantity}, Price: ${self.price:.2f}"

class InventoryManager:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.item_id] = item

    def update_quantity(self, item_id, quantity):
        if item_id in self.items:
            self.items[item_id].quantity += quantity

    def get_item(self, item_id):
        return self.items.get(item_id)

    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]

    def list_items(self):
        return list(self.items.values())