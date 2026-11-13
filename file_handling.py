import csv
import json
import os

from inventory_class import Inventory
from physical_product_class import Physical_product
from digital_product_class import Digital_product
from supplier_class import Supplier
from product_class import Product
from product_factory import ProductFactory

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
        inventory.add_product(ProductFactory.create("physical", "P001", "Laptop", 1200.00, 15, 2, example))
        inventory.add_product(ProductFactory.create("physical", "P002", "Mouse", 25.50, 50, 0.10, example))
        inventory.add_product(ProductFactory.create("physical", "P003", "Keyboard", 45.00, 30, 0.25, example))
    return inventory


def save_inventory(inventory: Inventory, filename: str = FILENAME) -> None:
    with open(filename, "w") as file:
        json.dump([p.to_dict() for p in inventory.get_products()], file, indent=4)
    print(f"Inventory successfully saved to '{filename}'.")


def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        loaded = 0
        with file:
            reader = csv.reader(file)
            next(reader, None)  # skip header row
            for line_number, row in enumerate(reader, start=2):
                try:
                    product_type, product_id, name, price, stock = row
                    product = ProductFactory.create(product_type.strip(), product_id.strip(),
                                                    name.strip(), float(price), int(stock),
                                                    0.0, supplier)
                    inventory.add_product(product)
                    loaded += 1
                except ValueError as error:
                    print(f"Skipping row {line_number}: {error}")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")