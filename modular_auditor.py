inventory = 0 #Initialize the inventory to zero in the start
failed_enteries = 0 #Number of Failed/Rejected Entries
total_tax = 0 #Total Amount Taxed
deliveries_processed = 0 #Record Tracking
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

            if inventory > 500: #Trigger Overstock Alert
                print("Overstock Alert! 500 units reached")
                break