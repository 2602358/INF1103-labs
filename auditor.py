inventory = 0 #Initialize the inventory to zero in the start
failed_enteries = 0 #Number of Failed/Rejected Entries

while True: #Run in a continuous loop asking user to enter a stock quantity.
    stock_quantity = (input("Enter Stock Quantity (Enter 'quit' to quit): "))
    if stock_quantity.lower() == "quit": #Until the user types quit.
        print("Quit. Total inventory:", inventory) #Reporting
        print("Number of failed/rejected enteries: ", failed_enteries)
        break
    elif stock_quantity.isdigit(): #Handle invalid input
        stock_value = int(stock_quantity) #Accept stock values as integers
        inventory += stock_value #Manage State
        print ("Inventory:",inventory)
        if inventory > 500: #Trigger Overstock Alert
            print("Overstock Alert! 500 units reached")
            break
        else:
            continue
    elif not stock_quantity.isdigit():
        if stock_quantity.startswith("-"): #Enforce business rules
            print ("Negative numbers rejected. Please enter a valid number")
        else:
            print("Error. Please enter a valid number")
        failed_enteries += 1