inventory = 0 #Initialize the inventory to zero in the start
failed_enteries = 0 #Number of Failed/Rejected Entries
total_tax = 0 #Total Amount Taxed
deliveries_processed = 0 #Record Tracking   
history = []
def get_valid_input(valid_input):
    stock_quantity = input(valid_input)  
    if stock_quantity.lower() == "quit": #Until the user types quit.
        return "quit"
    elif stock_quantity.isdigit():
        return int(stock_quantity)
    else:
        if stock_quantity.startswith("-"): #Enforce business rules
                print ("Negative numbers rejected. Please enter a valid number")
        else:
                print("Error. Please enter a valid number")
        return "failed"

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.10

def generate_report(inventory, total_tax, deliveries_processed, failed_enteries):
    print("Quit. Total Units: ", inventory)
    print("Total Tax: ", total_tax)
    print("Deliveries Processed: ", deliveries_processed)
    print("Failed attempts: ", failed_enteries)

def load_inventory():
    with open("inventory.txt", "r") as file:
        lines = file.readlines()
        inventory_read = lines[0].strip()
        history_read = lines[1].strip()
        total_tax_read = lines[2].strip()
        for line in lines:
            print(line.strip())
    return inventory_read, history_read, total_tax_read

inventory_read, history_read, total_tax_read = load_inventory()

def save_inventory(inventory, history, total_tax):
    with open("inventory.txt", "a") as file:
        file.write ("Inventory: ")
        file.write (str(inventory) + "\n")
        file.write ("total_tax: ")
        file.write (str(history) + "\n")
        file.write ("Total_tax: ")
        file.write (str(total_tax) + "\n")

while True: #Run in a continuous loop asking user to enter a stock quantity.
        stock_input = get_valid_input("Enter Stock Quantity (Enter 'quit' to quit): ")
        if stock_input == "quit": #Until the user types quit.
            generate_report(inventory, total_tax, deliveries_processed, failed_enteries)
            break
        elif stock_input == "failed":
                failed_enteries += 1
        else:
            inventory = process_delivery(inventory, stock_input) #Manage State
            print ("Inventory:", inventory)

            delivery_tax = calculate_tax(stock_input)
            total_tax += delivery_tax
            print ("Total Tax: ", total_tax)

            deliveries_processed += 1

            history.append(stock_input)

            if inventory > 500: #Trigger Overstock Alert
                print("Overstock Alert! 500 units reached")
                break

save_inventory (inventory, history, total_tax)