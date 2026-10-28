from file_handling import load_inventory, save_inventory
from product_class import Product


def get_valid_name(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Product name cannot be empty.")


def get_valid_price(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            if value >= 0:
                return value
            print("Negative prices rejected.")
        except ValueError:
            print("Error. Please enter a valid price.")


def get_valid_stock(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        if value.startswith("-"):
            print("Negative numbers rejected. Please enter a valid number.")
        else:
            print("Error. Please enter a valid positive number.")


def add_product(inventory):
    print("\n--- Add New Product ---")
    name = get_valid_name("Enter Product Name: ")
    price = get_valid_price("Enter Price: ")
    stock = get_valid_stock("Enter Stock Quantity: ")
    product = Product(inventory.get_next_id(), name, price, stock)
    inventory.add_product(product)
    print(f"\nSuccessfully added: ID: {product.product_id}, "
          f"Name: {product.name}, Stock: {product.stock}")


def update_stock(inventory):
    print("\n--- Update Product Stock ---")
    product = inventory.find_by_id(input("Enter Product ID to update: "))
    if product is None:
        print("Product ID not found.")
        return
    print(f"Current Stock for {product.name}: {product.stock}")
    product.update_stock(get_valid_stock("Enter New Stock Quantity: "))
    print(f"Stock updated successfully for {product.name}.")


def search_product(inventory):
    print("\n--- Search Product ---")
    results = inventory.search_product(input("Enter product name to search: "))
    if results:
        inventory.display_products(results)
    else:
        print("No matching products found.")


def main():
    inventory = load_inventory()

    while True:
        print("\n=========================")
        print("    INVENTORY SYSTEM     ")
        print("=========================")
        print("1. Display All Products")
        print("2. Add New Product")
        print("3. Update Product Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")

        choice = input("\nSelect an option (1-6): ").strip()

        match choice:
            case "1":
                print("\n--- Current Inventory ---")
                inventory.display_all()
            case "2":
                add_product(inventory)
            case "3":
                update_stock(inventory)
            case "4":
                search_product(inventory)
            case "5":
                save_inventory(inventory)
            case "6":
                print("Exiting system. Goodbye!")
                break
            case _:
                print("Invalid selection. Please choose an option between 1 and 6.")


if __name__ == "__main__":
    main()