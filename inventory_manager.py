import json
import os

# --- 1. Data Persistence & File Handling ---

def load_inventory():
    if os.path.exists("inventory.json"):
        try:
            with open("inventory.json", "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error reading inventory file. Starting with an empty inventory.")
            return []
    else:
        return [
            {"id": 1001, "name": "Laptop", "stock": 15},
            {"id": 1002, "name": "Mouse", "stock": 50},
            {"id": 1003, "name": "Keyboard", "stock": 30}
        ]

def save_inventory(inventory):
        with open("inventory.json", "w") as file:
            json.dump(inventory, file, indent=4)
        print("Inventory successfully saved to 'inventory.json'.")

# --- 2. Input Validation Functions ---

def get_valid_name(valid_name):
    while True:
        name_input = input(valid_name).strip()
        if name_input:
            return name_input
        print("Error: Product name cannot be empty.")

def get_valid_stock(valid_stock):
    while True:
        stock_quantity = input(valid_stock).strip()
        if stock_quantity.isdigit():
            return int(stock_quantity)
        elif stock_quantity.startswith("-"):
            print("Negative numbers rejected. Please enter a valid number.")
        else:
            print("Error. Please enter a valid positive number.")
        return None


# --- 3. Data Manipulation Functions ---

def get_next_id(inventory):
    if not inventory:
        return 1000
    return max(item["id"] for item in inventory) + 1

def add_product(inventory):
    print("\n--- Add New Product ---")
    name = get_valid_name("Enter Product Name: ")
    stock = get_valid_stock("Enter Stock Quantity: ")
    
    if stock is None:
        print("Failed to add product. Try again.")
        return

    new_id = get_next_id(inventory)
    new_product = {"id": new_id, "name": name, "stock": stock}
    inventory.append(new_product)
    
    print(f"\nSuccessfully added: ID: {new_id}, Name: {name}, Stock: {stock}")

def update_stock(inventory):
    print("\n--- Update Product Stock ---")
    try:
        prod_id = int(input("Enter Product ID to update: "))
    except ValueError:
        print("Invalid ID format.")
        return

    for item in inventory:
        if item["id"] == prod_id:
            print(f"Current Stock for {item['name']}: {item['stock']}")
            new_stock = get_valid_stock("Enter New Stock Quantity: ")
            if new_stock is not None:
                item["stock"] = new_stock
                print(f"Stock updated successfully for {item['name']}.")
            return
    print("Product ID not found.")

def search_product(inventory):
    print("\n--- Search Product ---")
    search_term = input("Enter product name to search: ").lower()
    found = [item for item in inventory if search_term in item["name"].lower()]

    if found:
        print(f"\n{'ID':<10}{'Name':<20}{'Stock':<10}")
        print("-" * 40)
        for item in found:
            print(f"{item['id']:<10}{item['name']:<20}{item['stock']:<10}")
    else:
        print("No matching products found.")

def display_all(inventory):
    print("\n--- Current Inventory ---")
    if not inventory:
        print("Inventory is currently empty.")
        return
        
    print(f"{'ID':<10}{'Name':<20}{'Stock':<10}")
    print("-" * 40)
    for item in inventory:
        print(f"{item['id']:<10}{item['name']:<20}{item['stock']:<10}")

# --- 4. Main Menu System ---

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
                display_all(inventory)
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
                print("Invalid selection. Please choose a option between 1 and 6.")

if __name__ == "__main__":
    main()