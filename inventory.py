class Shoe:
    
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"Country: {self.country}\nCode: {self.code}\nProduct: {self.product}\nCost: {self.cost}\nQuantity: {self.quantity}"

# An empty list to store Shoe objects
shoe_list = []


def read_shoes_data():
    try:
        # Open the inventory.txt file
        with open('inventory.txt', 'r') as file:
            lines = file.readlines()
            for line in lines[1:]:  # Skip the first line
                data = line.strip().split(',')
                shoe = Shoe(*data)
                shoe_list.append(shoe)
        print("Data loaded successfully from inventory.txt.")
    except FileNotFoundError:
        print("File not found.")

# Prompt the user to enter shoe details
def capture_shoes():
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = input("Enter cost: ")
    quantity = input("Enter quantity: ")
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    print("Shoe data captured successfully.")

# Function to view shoes
def view_all():

    if not shoe_list:
        print("No shoes available.")
        return

    print("=== All Shoes ===")
    for shoe in shoe_list:
        print(f"Country: {shoe.country}")
        print(f"Code: {shoe.code}")
        print(f"Product: {shoe.product}")
        print(f"Cost: {shoe.cost}")
        print(f"Quantity: {shoe.quantity}")
        print("-------------------")

# Function will find the shoe object with the lowest quantity,which is the shoes that need to be re-stocked.
def re_stock():
    if not shoe_list:
        print("No shoes available.")
        return
    lowest_quantity_shoe = min(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"Shoe with code {lowest_quantity_shoe.code} needs to be restocked.")
    quantity_to_add = int(input("Enter the quantity to be added: "))
    lowest_quantity_shoe.quantity += quantity_to_add
    print("Shoe quantity updated successfully.")

    # Update the quantity in the inventory.txt file
    with open('inventory.txt', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines[1:], 1):  # Start from line 1 to skip the header
        data = line.strip().split(',')
        code = data[1]
        if code == lowest_quantity_shoe.code:
            data[-1] = str(lowest_quantity_shoe.quantity)
            lines[i] = ','.join(data) + '\n'
            break

    with open('inventory.txt', 'w') as file:
        file.writelines(lines)

    print("Shoe quantity updated in the inventory file.")

# Function to search for shoes
def search_shoe():
    if not shoe_list:
        print("No shoes available.")
        return
    code = input("Enter the shoe code: ")
    found_shoe = None
    for shoe in shoe_list:
        if shoe.code == code:
            found_shoe = shoe
            break
    if found_shoe:
        print(found_shoe)
    else:
        print("Shoe not found.")

# Function will calculate the total value for each item
def value_per_item():
    if not shoe_list:
        print("No shoes available.")
        return

    print("=== Value per Item ===")
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"Product: {shoe.product}")
        print(f"Value: {value}")
        print("-------------------")

# Function to find highest quantity
def highest_qty():
    if not shoe_list:
        print("No shoes available.")
        return

    max_quantity_shoe = max(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"The shoe with the highest quantity for sale is:\n{max_quantity_shoe}")

# Main Menu
while True:
    print("\n=== Shoe Inventory Management === Please select option 1 first to load shoe Inventory ")
    print("1. Read shoes data from file")
    print("2. Capture new shoe")
    print("3. View all shoes")
    print("4. Re-stock shoes")
    print("5. Search for a shoe")
    print("6. Calculate value per item")
    print("7. Find shoe with highest quantity")
    print("8. Exit")
    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        read_shoes_data()
    elif choice == "2":
        capture_shoes()
    elif choice == "3":
        view_all()
    elif choice == "4":
        re_stock()
    elif choice == "5":
        search_shoe()
    elif choice == "6":
        value_per_item()
    elif choice == "7":
        highest_qty()
    elif choice == "8":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
