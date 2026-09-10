inventory = 0
stock_quantity = ""

while stock_quantity != "quit":
    stock_quantity = (input("Enter Stock Quantity (Enter 'quit' to quit): "))    
    if stock_quantity.isdigit():
        print("Valid Number")
    else:
        print("Error")
