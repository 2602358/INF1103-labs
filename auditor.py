inventory = 0

while True:
    stock_quantity = (input("Enter Stock Quantity (Enter 'quit' to quit): "))
    if stock_quantity.lower() == "quit":
        print("Quit. Total inventory:", inventory)
        break
    else:
        stock_value = int(stock_quantity)
        inventory += stock_value
        print ("Inventory:",inventory)