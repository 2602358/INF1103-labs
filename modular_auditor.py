inventory = 0 #Initialize the inventory to zero in the start
failed_enteries = 0 #Number of Failed/Rejected Entries
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
         

while True: #Run in a continuous loop asking user to enter a stock quantity.
        stock_input = get_valid_input("Enter Stock Quantity (Enter 'quit' to quit): ")
        if stock_input == "quit": #Until the user types quit.
            print("Quit. Total inventory:", inventory) #Reporting
            print("Number of failed/rejected enteries: ", failed_enteries)
            break
        elif stock_input == "failed":
                failed_enteries += 1
        else:
            inventory += stock_input #Manage State
            print ("Inventory:",inventory)
            if inventory > 500: #Trigger Overstock Alert
                print("Overstock Alert! 500 units reached")
                break