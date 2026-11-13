from file_handling import load_inventory, save_inventory
from product_factory import ProductFactory
from discount_strategy import (DiscountStrategy, NoDiscount, PercentageDiscount, BulkDiscount, StudentDiscount)
from supplier_class import Supplier
from order_class import Order
from inventory_class import Inventory

def get_valid_p_or_d(prompt: str) -> str:
    while True:
        reply = input(prompt).strip().lower()
        if reply.strip() == "p":
            return reply
        elif reply.strip() == "d":
            return reply
        else:
            print("Error")

def get_valid_name(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Product name cannot be empty.")


def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")


def get_valid_stock(prompt: str) -> int:
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        if value.startswith("-"):
            print("Negative numbers rejected. Please enter a valid number.")
        else:
            print("Error. Please enter a valid positive number.")

def get_valid_weight(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt).strip())
            if value >= 0:
                return value
            print("Negative weight rejected.")
        except ValueError:
            print("Error. Please enter a valid weight.")

def get_valid_size(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt).strip())
            if value >= 0:
                return value
            print("Negative size rejected.")
        except ValueError:
            print("Error. Please enter a valid size.")

def get_valid_supplier(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: This field cannot be empty.")

def get_supplier() -> Supplier:
    supplier_id = get_valid_supplier("Enter Supplier ID: ")
    supplier_name = get_valid_supplier("Enter Supplier Name: ")
    contact_email = get_valid_supplier("Enter Supplier Email: ")
    return Supplier(supplier_id, supplier_name, contact_email)

def add_product(inventory: Inventory) -> None:
    reply = get_valid_p_or_d("Enter p or d to add a physical or digital product respectively: ")
    print("\n--- Add New Product ---")
    name = get_valid_name("Enter Product Name: ")
    price = get_positive_float("Enter Price: ")
    stock = get_valid_stock("Enter Stock Quantity: ")
    if reply == "p":
        product_type = "physical"
        weight_or_size = get_valid_weight("Enter Weight(kg): ")
    else:
        product_type = "digital"
        weight_or_size = get_valid_size("Enter size(gb): ")
    supplier = get_supplier()
    product = ProductFactory.create(product_type, inventory.get_next_id(), name,
                                    price, stock, weight_or_size, supplier)
    inventory.add_product(product)
    print(f"\nSuccessfully added: ID: {product.product_id}, "
          f"Name: {product.name}, Stock: {product.stock}")
    print(product.get_fulfilment_info())


def update_stock(inventory: Inventory) -> None:
    print("\n--- Update Product Stock ---")
    product = inventory.find_product(input("Enter Product ID to update: "))
    if product is None:
        print("Product ID not found.")
        return
    print(f"Current Stock for {product.name}: {product.stock}")
    product.update_stock(get_valid_stock("Enter New Stock Quantity: "))
    print(f"Stock updated successfully for {product.name}.")

def remove_product(inventory: Inventory) -> None:
    print("\n--- Remove Product ---")
    if inventory.remove_product(input("Enter Product ID to remove: ")):
        print("Product removed from inventory.")
    else:
        print("Product ID not found.")

def search_product(inventory: Inventory) -> None:
    print("\n--- Search Product ---")
    results = inventory.search_product(input("Enter product name to search: "))
    if results:
        inventory.display_products(results)
    else:
        print("No matching products found.")

DISCOUNT_OPTIONS: dict[str, tuple[str, DiscountStrategy]] = {
    "1": ("No discount", NoDiscount()),
    "2": ("10% off", PercentageDiscount(10)),
    "3": ("20 off orders of 200 or more", BulkDiscount(200, 20)),
    "4": ("Student (5% off)", StudentDiscount()),
}

def get_discount() -> DiscountStrategy:
    while True:
        for key, (label, _) in DISCOUNT_OPTIONS.items():
            print(f"  {key}. {label}")
        choice = input("Select a discount: ").strip()
        if choice in DISCOUNT_OPTIONS:
            return DISCOUNT_OPTIONS[choice][1]
        print("Invalid selection.")

def create_order(inventory: Inventory) -> None:
    print("\n--- Create Order ---")
    order = Order(input("Enter Order ID: ").strip(), get_discount())

    while True:
        product_id = input("Enter Product ID to add (or press Enter to finish): ").strip()
        if not product_id:
            break
        product = inventory.find_product(product_id)
        if product is None:
            print("Product ID not found.")
            continue
        quantity = get_valid_stock("Enter quantity: ")
        if quantity == 0:
            print("Quantity must be at least 1.")
            continue
        order.add_order_line(product, quantity)
        print(f"Added {quantity} x {product.name}.")

    if order.order_lines:
        order.display_order()
    else:
        print("Order is empty.")

def main() -> None:
    inventory = load_inventory()

    while True:
        print("\n=========================")
        print("    INVENTORY SYSTEM     ")
        print("=========================")
        print("1. Display All Products")
        print("2. Add New Product")
        print("3. Update Product Stock")
        print("4. Remove Product")
        print("5. Search Product")
        print("6. Save Inventory")
        print("7. Create Order")
        print("8. Exit")

        choice = input("\nSelect an option (1-8): ").strip()

        match choice:
            case "1":
                print("\n--- Current Inventory ---")
                inventory.display_all()
            case "2":
                add_product(inventory)
            case "3":
                update_stock(inventory)
            case "4":
                remove_product(inventory)
            case "5":
                search_product(inventory)
            case "6":
                save_inventory(inventory)
            case "7":
                create_order(inventory)
            case "8":
                print("Exiting system. Goodbye!")
                break
            case _:
                print("Invalid selection. Please choose an option between 1 and 8.")


if __name__ == "__main__":
    main()