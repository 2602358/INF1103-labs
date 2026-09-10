inventory = 0

while True:
    stock_quantity = (input("Enter Stock Quantity (Enter 'quit' to quit): "))
    if stock_quantity.lower() == "quit":
        print("Quit. Total inventory:", inventory)
        break
    elif stock_quantity.isdigit():
        stock_value = int(stock_quantity)
        inventory += stock_value
        print ("Inventory:",inventory)
    else:
            print("Error. Please enter a valid number")