def get_valid_name(valid_name):
    valid_name_input = input(valid_name)
    if valid_name_input.lower() == "quit":
        return "quit"
    return valid_name_input
    
def get_valid_input(valid_input):
    stock_quantity = input(valid_input)
    if stock_quantity.isdigit():
        return int(stock_quantity)
    else:
        if stock_quantity.startswith("-"): #Enforce business rules
            print ("Negative numbers rejected. Please enter a valid number")
        else:
            print("Error. Please enter a valid number")
        return "failed"

def increment_id():
    id_count = 1000 
    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                if line.strip():
                    # Split by comma to match how we save it
                    parts = line.strip().split(",")
                    if parts:
                        file_id = int(parts[0])
                        # Track the largest ID found in the file
                        if file_id > id_count:
                            id_count = file_id
    except FileNotFoundError:
        pass
    return id_count

def save_inventory(new_id, name_input, stock_input):
    with open("inventory.txt", "a") as file:
        file.write (f"{new_id}, {name_input}, {stock_input}\n")

def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        pass
    return

load_inventory()
            
current_id = increment_id()

while True:
    name_input = get_valid_name("\nEnter Product name (Enter 'quit' to quit): ")
    if name_input == "quit": 
        break
        
    stock_input = get_valid_input("Enter Stock Quantity: ")
    if stock_input == "failed":
        print("Failed to add product. Try again.")
        continue # Skip saving and restart the loop
    
    # 3. Only increment the ID when saving a valid item
    current_id += 1 
    
    # 4. Save the item immediately inside the loop
    save_inventory(current_id, name_input, stock_input)
    print("New order add\n")
    print (f"{current_id}, {name_input}, {stock_input}")
    print("Successfully saved")