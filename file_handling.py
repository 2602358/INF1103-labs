import json
import os

from inventory_class import Inventory
from product_class import Product

FILENAME = "inventory.json"


def load_inventory(filename=FILENAME):
    inventory = Inventory()
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                for data in json.load(file):
                    inventory.add_product(Product.from_dict(data))
        except (json.JSONDecodeError, KeyError, ValueError):
            print("Error reading inventory file. Starting with an empty inventory.")
            return Inventory()
    else:
        inventory.add_product(Product("P001", "Laptop", 1200.00, 15))
        inventory.add_product(Product("P002", "Mouse", 25.50, 50))
        inventory.add_product(Product("P003", "Keyboard", 45.00, 30))
    return inventory


def save_inventory(inventory, filename=FILENAME):
    with open(filename, "w") as file:
        json.dump([p.to_dict() for p in inventory.get_products()], file, indent=4)
    print(f"Inventory successfully saved to '{filename}'.")