import json
import os

from inventory_class import Inventory
from physical_product_class import Physical_product
from digital_product_class import Digital_product
from supplier_class import Supplier
from product_class import Product

FILENAME = "inventory.json"

PRODUCT_TYPES: dict[str, type[Product]] = {"physical": Physical_product,
                                           "digital": Digital_product}

def load_inventory(filename: str = FILENAME) -> Inventory:
    inventory = Inventory()
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                for data in json.load(file):
                    product_class = PRODUCT_TYPES[data.get("type", "physical")]
                    inventory.add_product(product_class.from_dict(data))
        except (json.JSONDecodeError, KeyError, ValueError):
            print("Error reading inventory file. Starting with an empty inventory.")
            return Inventory()
    else:
        example = Supplier("S001", "Example Ltd", "sales@exmaple.com")
        inventory.add_product(Physical_product("P001", "Laptop", 1200.00, 15, 2, example))
        inventory.add_product(Physical_product("P002", "Mouse", 25.50, 50, 0.10, example))
        inventory.add_product(Physical_product("P003", "Keyboard", 45.00, 30, 0.25, example))
    return inventory


def save_inventory(inventory: Inventory, filename: str = FILENAME) -> None:
    with open(filename, "w") as file:
        json.dump([p.to_dict() for p in inventory.get_products()], file, indent=4)
    print(f"Inventory successfully saved to '{filename}'.")