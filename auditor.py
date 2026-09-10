inventory = 0 #Initialize the inventory to zero in the start

while True: #Run in a continuous loop asking user to enter a stock quantity.
    stock_quantity = (input("Enter Stock Quantity (Enter 'quit' to quit): "))
    if stock_quantity.lower() == "quit": #Until the user types quit.
        print("Quit. Total inventory:", inventory) #Reporting
        break
    elif stock_quantity.isdigit(): #Handle invalid input
        stock_value = int(stock_quantity) #Accept stock values as integers
        inventory += stock_value #Manage State
        print ("Inventory:",inventory)
    elif not stock_quantity.isdigit():
        if stock_quantity.startswith("-"): #Enforce business rules
            print ("Negative numbers rejected. Please enter a valid number")
        else:
            print("Error. Please enter a valid number")