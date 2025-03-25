import os
import re
CUSTOMERS_FILE = os.path.join("database", "customers.txt")
MENU_FILE = os.path.join("database", "menu_data.txt")
INGREDIENTS_FILE = os.path.join("database", "ingredients_data.txt")
Staff_FILE = os.path.join("database", "staff_data.txt")
User_FILE = os.path.join("database", "users_data.txt")
LOGIN_USER_DATA = os.path.join("cookies", "login_User_data.txt")
REQUEST_Ingredient  = os.path.join("database" , "Req_ingredients_data.txt" )
from OurRestaurant import main
from tabulate import tabulate
 
 
def manager_menu():
    print("\n-------------------- Manager Menu --------------------\n")
    while True:
        print("\nManager Menu:")
        print("1. Manage Customers")
        print("2. Manage Menu")
        print("3. Ingredients Management")
        print("4. Update Profile")
        print("5. Logout")
        choice = input("Enter choice: ")

        if choice == "1":
            manage_customers()
        elif choice == "2":
            manage_menu()
        elif choice == "3":
            manage_ingredients()
        elif choice == "4":
             Update_own_profile()
        elif choice == "5":
             logOut()
        else:
            print("Invalid choice.")
 
def manage_customers():
    while True:
        print("\n-------------Manage Customers:------------\n")
        print("1. Add Customer")
        print("2. Edit Customer")
        print("3. Delete Customer")
        print("4. View All Customers")
        print("5. Back to Manager Menu")
        choice = input("Enter choice: ") 

        if choice == "1":
            add_customer()
        elif choice == "2":
            Edit_customer()
        elif choice == "3":
            Delete_customer()
        elif choice == "4":
            View_customers()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def get_next_user_id():
    if not os.path.exists( ):
        return 100  # Start with ID 100 if the file doesn't exist
    with open(Staff_FILE, "r") as f:
        lines = f.readlines()
        if not lines:
            return 100  # Start with ID 100 if the file is empty
        last_line = lines[-1]
        last_id = int(last_line.split(",")[0])  # Extract the last ID
        return last_id + 1  # Increment the last ID by 1

def get_next_user_id():
    """Generate a new user ID based on the last recorded user."""
    if not os.path.exists(User_FILE):
        return 1  # If file doesn't exist, start with user ID 1

    with open(User_FILE, "r") as f:
        lines = f.readlines()
        if not lines:
            return 1  # If file is empty, start with user ID 1

        last_line = lines[-1].strip().split(",")[0]
        return int(last_line) + 1  # Increment last user ID by 1

def add_customer():
    print("\n------------------------------- Registration -------------------------------------\n")
    
    full_Name = input("Enter your Full Name: ")
    username = input("Enter a username: ")

    # Check if file exists before reading
    if os.path.exists(User_FILE):
        with open(User_FILE, "r") as f:
            for line in f:
                existing_username = line.strip().split(",")[2]  # Username is the 3rd field
                if existing_username == username:
                    print("Username already exists. Please go to login.")
                    return
    
    email = input("Enter your email: ")
    password = input("Enter a password: ")
    role = "Customer"
    user_id = get_next_user_id()

    # Ensure the data directory exists
    os.makedirs(os.path.dirname(User_FILE), exist_ok=True)

    with open(User_FILE, "a") as f:
        f.write(f"{user_id},{full_Name},{username},{email},{password},{role}\n")

    print(f"Registration successful! Your unique ID is {user_id}. You can now log in.")

def Edit_customer():
    print("\n-------------------- Edit Customer --------------------\n")
    Customer_List = []

    if not os.path.exists(User_FILE) or os.stat(User_FILE).st_size == 0:
        print("No customers found.")
        return

    with open(User_FILE, "r") as f:
        for line in f:
            Customer_List.append(line.strip().split(","))

    if not Customer_List:
        print("No customers found.")
        return

    # Display customers in table format
    print("\n--------- Current Customers ----------\n")
    headers = ["No", "ID", "Full Name", "Username", "Email", "Password", "Role"]
    table_data = [[i + 1] + customer for i, customer in enumerate(Customer_List)]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

    try:
        customer_index = int(input("\nEnter the number of the customer to edit: ")) - 1
        if customer_index < 0 or customer_index >= len(Customer_List):
            print("Invalid selection.")
            return

        # Get the selected customer
        selected_customer = Customer_List[customer_index]

        # Edit Name
        if input("Do you want to update the customer's name? (y/n): ").strip().lower() == "y":
            selected_customer[1] = input("Enter new name: ")

        # Edit Username
        if input("Do you want to update the customer's username? (y/n): ").strip().lower() == "y":
            selected_customer[2] = input("Enter new username: ")

        # Edit Email
        if input("Do you want to update the customer's email? (y/n): ").strip().lower() == "y":
            selected_customer[3] = input("Enter new email: ")

        # Edit Password
        if input("Do you want to update the customer's password? (y/n): ").strip().lower() == "y":
            selected_customer[4] = input("Enter new password: ")

        # Save the updated list back to the file
        with open(User_FILE, "w") as f:
            for customer in Customer_List:
                f.write(",".join(customer) + "\n")

        print("\nCustomer updated successfully!")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

def Delete_customer():
    print("\n-------------------- Delete Customer --------------------\n")
    Customer_List = []

    if not os.path.exists(User_FILE) or os.stat(User_FILE).st_size == 0:
        print("No customers found.")
        return

    with open(User_FILE, "r") as f:
        for line in f:
            Customer_List.append(line.strip().split(","))

    if not Customer_List:
        print("No customers found.")
        return

    # Display customers in a table format
    print("\n--------- Current Customers ----------\n")
    headers = ["No", "ID", "Full Name", "Username", "Email", "Password", "Role"]
    table_data = [[i + 1] + customer for i, customer in enumerate(Customer_List)]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

    try:
        customer_index = int(input("\nEnter the number of the customer to delete: ")) - 1
        if customer_index < 0 or customer_index >= len(Customer_List):
            print("Invalid selection.")
            return

        # Confirm deletion
        confirm = input(f"Are you sure you want to delete {Customer_List[customer_index][1]}? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Deletion canceled.")
            return

        # Delete the customer
        del Customer_List[customer_index]

        # Save the updated list back to the file
        with open(User_FILE, "w") as f:
            for customer in Customer_List:
                f.write(",".join(customer) + "\n")

        print("\nCustomer deleted successfully!")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
 
def View_customers():
    print("\n-------------------- Customer List --------------------\n")
    
    if not os.path.exists(User_FILE) or os.stat(User_FILE).st_size == 0:
        print("No customers found.")
        return
    
    customers = []
    
    with open(User_FILE, "r") as f:
        for line in f:
            user_data = line.strip().split(",")
            customers.append(user_data)

    headers = ["ID", "Full Name", "Username", "Email", "Password", "Role"]
    print(tabulate(customers, headers=headers, tablefmt="grid"))  # Display as a table

# ########################    Menu Management  ########################
 
 
def manage_menu():
    while True:
        print("\n-------Manage Menu:-------\n")
        print("1. Item upload")
        print("2. Edit Item")
        print("3. Delete Item")
        print("4. View Menu")
        print("5. Back to Manager Menu")
        choice = input("Enter choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            edit_item()
        elif choice == "3":
            delete_item()
        elif choice == "4":
            view_menu()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
     
def get_next_item_id():
    """Generates the next item ID in the format M1, M2, M3..."""
    if not os.path.exists(MENU_FILE) or os.stat(MENU_FILE).st_size == 0:
        return "M1"  # If file is empty, start from M1

    with open(MENU_FILE, "r") as f:
        lines = f.readlines()
        if not lines:
            return "M1"

        last_line = lines[-1].strip().split(",")  # Get last entry
        last_id = last_line[0] if last_line else "M0"  # Extract ID
        next_id = f"M{int(last_id[1:]) + 1}"  # Increment numeric part

    return next_id
 
def get_next_item_id():
    """Generates the next item ID (M1, M2, M3, ...)."""
    if not os.path.exists(MENU_FILE) or os.stat(MENU_FILE).st_size == 0:
        return "M1"

    with open(MENU_FILE, "r") as f:
        lines = f.readlines()
        if not lines:
            return "M1"

        last_line = lines[-1].strip().split(",")  # Get last entry
        last_id = last_line[0] if last_line else "M0"  # Extract ID
        next_id = f"M{int(last_id[1:]) + 1}"  # Increment numeric part

    return next_id

def item_exists(item_name):
    """Checks if an item with the given name already exists."""
    if not os.path.exists(MENU_FILE):
        return False

    with open(MENU_FILE, "r") as f:
        for line in f:
            existing_name = line.strip().split(",")[1].lower()
            if existing_name == item_name.lower():
                return True
    return False

def add_item():
    """Adds a new menu item with validation and unique ID."""
    print("\n-------- Item Upload --------\n")
    
    item_id = get_next_item_id()  # Generate unique ID
    item_name = input("Enter item name: ").strip()

    if item_exists(item_name):
        print(f"Error: '{item_name}' already exists in the menu.")
        return

    while True:
        item_price = input("Enter item price (₹): ").strip()
        if item_price.isdigit():  # Ensure valid numeric price
            item_price = int(item_price)
            break
        print("Invalid price. Please enter a valid number.")

    valid_types = ["veg", "non-veg", "buffet", "drinks", "snacks"]
    
    while True:
        item_type = input(f"Enter item type {valid_types}: ").strip().lower()
        if item_type in valid_types:
            break
        print(f"Invalid item type! Choose from {valid_types}")

    with open(MENU_FILE, "a") as f:
        f.write(f"{item_id},{item_name},{item_price},{item_type}\n")

    print(f"\n✅ Item '{item_name}' added successfully with ID {item_id}!")
 
def edit_item():
    """Edits an existing menu item."""
    print("\n-------- Edit Item: --------\n")
    item_list = []

    if not os.path.exists(MENU_FILE) or os.stat(MENU_FILE).st_size == 0:
        print("No items found.")
        return

    with open(MENU_FILE, "r") as f:
        for line in f:
            item = line.strip().split(",")
            while len(item) < 4:  # Ensure all items have 4 columns
                item.append("")
            item_list.append(item)

    if not item_list:
        print("No items found.")
        return

    # Create a display list with serial numbers
    display_list = [[i + 1] + item for i, item in enumerate(item_list)]

    # Show items in a table with numbering
    print(tabulate(display_list, headers=["No.", "ID", "Name", "Price (₹)", "Type"], tablefmt="grid"))

    try:
        item_number = int(input("\nEnter the number of the item to edit: ")) - 1
        if item_number < 0 or item_number >= len(item_list):
            print("Invalid selection.")
            return

        # Extract the selected item
        selected_item = item_list[item_number]
        item_id, item_name, item_price, item_type = selected_item

        # Update item fields
        if input(f"Do you want to update item name (current: {item_name})? (y/n): ").strip().lower() == "y":
            selected_item[1] = input("Enter new item name: ").strip()

        if input(f"Do you want to update item price (current: ₹{item_price})? (y/n): ").strip().lower() == "y":
            while True:
                new_price = input("Enter new item price (₹): ").strip()
                if new_price.isdigit():
                    selected_item[2] = new_price
                    break
                print("Invalid price. Please enter a valid number.")

        if input(f"Do you want to update item type (current: {item_type})? (y/n): ").strip().lower() == "y":
            valid_types = ["veg", "non-veg", "buffet", "drinks", "snacks"]
            while True:
                new_type = input(f"Enter new item type {valid_types}: ").strip().lower()
                if new_type in valid_types:
                    selected_item[3] = new_type
                    break
                print(f"Invalid item type! Choose from {valid_types}")

        # Write updated data to file
        with open(MENU_FILE, "w") as f:
            for item in item_list:
                f.write(",".join(item) + "\n")

        print("\n Item updated successfully!")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_item():
    """Deletes an existing menu item."""
    print("\n--------- Delete Item: ---------\n")
    item_list = []

    if not os.path.exists(MENU_FILE) or os.stat(MENU_FILE).st_size == 0:
        print("No items found.")
        return

    with open(MENU_FILE, "r") as f:
        for line in f:
            item = line.strip().split(",")
            while len(item) < 4:  # Ensure each item has 4 columns
                item.append("")
            item_list.append(item)

    if not item_list:
        print("No items found.")
        return

    # Create a display list with serial numbers
    display_list = [[i + 1] + item for i, item in enumerate(item_list)]

    # Show items in a table with numbering
    print(tabulate(display_list, headers=["No.", "ID", "Name", "Price (₹)", "Type"], tablefmt="grid"))

    try:
        item_number = int(input("\nEnter the number of the item to delete: ")) - 1
        if item_number < 0 or item_number >= len(item_list):
            print("Invalid selection.")
            return

        # Confirm deletion
        confirm = input(f"Are you sure you want to delete '{item_list[item_number][1]}'? (y/n): ").strip().lower()
        if confirm != "y":
            print("Item deletion cancelled.")
            return

        # Delete the selected item
        del item_list[item_number]

        # Write the updated list back to the file
        with open(MENU_FILE, "w") as f:
            for item in item_list:
                f.write(",".join(item) + "\n")

        print(f"\n Item deleted successfully!")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

def view_menu():
    """Displays the menu in a formatted table."""
    print("\n-------------------- MENU --------------------\n")

    if not os.path.exists(MENU_FILE) or os.stat(MENU_FILE).st_size == 0:
        print("No items found in the menu.")
        return

    menu_items = []

    with open(MENU_FILE, "r") as f:
        for line in f:
            menu_items.append(line.strip().split(","))  # Convert CSV line to list

    if not menu_items:
        print("No items found in the menu.")
        return

    headers = ["ID", "Item Name", "Price (₹)", "Type"]
    print(tabulate(menu_items, headers=headers, tablefmt="grid"))
# ##################  Ingredients       ###################
def manage_ingredients():
    while True:
        print("\n-------- Manage Ingredients --------\n")
        print("1. View Ingredients")
        print("2. Upload New Ingredient")
        print("3. Delete Ingredient")
        print("4 . Update Ingredient")
        print("5. View / Update Ingredients Requests of Chef ")
        print("6. Go Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_ingredients()
        elif choice == "2":
            upload_ingredients()
        elif choice == "3":
            delete_ingredient()
        elif choice == "4":
            update_ingredient()
        elif choice == "5":
             View_AND_Update_Ingredients_Requests_of_Chef()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

def get_next_ingredient_id():
    """Generate the next unique ingredient ID (I1, I2, I3, etc.)."""
    if not os.path.exists(INGREDIENTS_FILE) or os.stat(INGREDIENTS_FILE).st_size == 0:
        return "I1"  # Start with I1 if file is empty

    with open(INGREDIENTS_FILE, "r") as f:
        lines = f.readlines()
        last_id = lines[-1].split(",")[0]  # Get last stored ID (e.g., I5)
        next_id = int(last_id[1:]) + 1  # Extract number and increment
        return f"I{next_id}"

# def upload_ingredients():
#     """Uploads a new ingredient with unique ID."""
#     print("\n-------- Upload New Ingredient --------\n")

#     ingredient_id = get_next_ingredient_id()  # Get new unique ID
#     ingredient_name = input("Enter ingredient name: ").strip().title()
    
#     while True:
#         quantity = input("Enter quantity (in kg/ltr/units): ").strip()
#         if quantity.replace(".", "", 1).isdigit():  # Allow decimals
#             break
#         print(" Invalid quantity! Please enter a number.")

#     ingredient_type = input("Enter ingredient type (e.g., vegetable, spice, dairy, meat): ").strip().lower()
#     brand_name = input("Enter brand name (if any, else type 'none'): ").strip().title()

#     # Save ingredient to file
#     with open(INGREDIENTS_FILE, "a") as f:
#         f.write(f"{ingredient_id},{ingredient_name},{quantity},{ingredient_type},{brand_name}\n")

#     print(f"\n Ingredient '{ingredient_name}' added successfully with ID {ingredient_id}!")


def extract_quantity_and_unit(quantity_input):
    """Extracts numeric value and unit separately (e.g., '2.5kg' → 2.5, 'kg')."""
    match = re.match(r"^(\d*\.?\d+)([a-zA-Z]+)$", quantity_input.strip())
    if match:
        return match.group(1), match.group(2)  # Return number & unit separately
    return None, None   
 
def get_next_ingredient_id():
    # Assuming ingredients start from 'I1' and are incremented sequentially
    with open(INGREDIENTS_FILE, "r") as f:
        lines = f.readlines()
        last_id = lines[-1].split(",")[0] if lines else "I0"
        last_num = int(last_id[1:])  # Extract number from ID (e.g., I3 -> 3)
        new_id = f"I{last_num + 1}"
    return new_id
 
def get_next_ingredient_id():
    """Generates the next unique ingredient ID."""
    if not os.path.exists(INGREDIENTS_FILE):  # Check if file exists
        # If the file does not exist, create it and return ID I1
        with open(INGREDIENTS_FILE, "w") as f:
            pass  # Just create the file
        return "I1"  # Starting ID when the file is new
    
    # If the file exists, fetch the last ID
    with open(INGREDIENTS_FILE, "r") as f:
        lines = f.readlines()
        if lines:
            last_id = lines[-1].split(",")[0]  # Get the ID from the last line
            last_num = int(last_id[1:])  # Extract number from ID (e.g., I3 -> 3)
            return f"I{last_num + 1}"  # Return next ID
        else:
            return "I1"  # If the file is empty, start from I1

def extract_quantity_and_unit(quantity_input):
    """Extracts numeric value and unit separately (e.g., '2kg' → 2, 'kg')."""
    match = re.match(r"^\s*(\d*\.?\d+)\s*([a-zA-Z]+)\s*$", quantity_input.strip())
    if match:
        return match.group(1), match.group(2)  # Number & unit separately
    return None, None  # Invalid format

def upload_ingredients():
    """Uploads a new ingredient with a unique ID."""
    print("\n-------- Upload New Ingredient --------\n")

    ingredient_id = get_next_ingredient_id() 
    ingredient_name = input("Enter ingredient name: ").strip().title()

    while True:
        quantity_input = input("Enter quantity (e.g., '2kg', '1.5ltr', '10units'): ").strip()
        quantity, unit = extract_quantity_and_unit(quantity_input)
        if quantity is not None:
            break
        print("❌ Invalid input! Please enter a number followed by a unit (e.g., '2kg', '1.5ltr').")

    ingredient_type = input("Enter ingredient type (e.g., vegetable, spice, dairy, meat): ").strip().lower()
    brand_name = input("Enter brand name (if any, else type 'none'): ").strip().title()

    # Save ingredient to file
    with open(INGREDIENTS_FILE, "a") as f:
        f.write(f"{ingredient_id},{ingredient_name},{quantity},{unit},{ingredient_type},{brand_name}\n")

    print(f"\n✅ Ingredient '{ingredient_name}' added successfully with ID {ingredient_id}!")

    # Show uploaded ingredient in a table format
    print("\n-------- Ingredient Details --------")
    print(f"| {ingredient_id} | {ingredient_name} | {quantity} | {unit} | {ingredient_type} | {brand_name} |")

def view_ingredients():
    """Displays all ingredients in a table format."""
    print("\n-------- Ingredients List --------\n")

    if not os.path.exists(INGREDIENTS_FILE) or os.stat(INGREDIENTS_FILE).st_size == 0:
        print("No ingredients found.")
        return

    ingredient_list = []
    
    with open(INGREDIENTS_FILE, "r") as f:
        for line in f:
            ingredient = line.strip().split(",")  # Split CSV data
            ingredient_list.append(ingredient)

    if not ingredient_list:
        print("No ingredients found.")
        return

    # Display in table format
    print(tabulate(ingredient_list, headers=["ID", "Name", "Quantity", "Type", "Brand"], tablefmt="grid"))


def extract_quantity_and_unit(quantity_input):
    match = re.match(r'(\d+(\.\d+)?)([a-zA-Z]+)', quantity_input)
    if match:
        quantity = match.group(1)  # Extract quantity number
        unit = match.group(3)      # Extract unit (e.g., 'kg', 'ltr')
        return quantity, unit
    return None, None


# def View_AND_Update_Ingredients_Requests_of_Chef():
#     """View and update ingredient requests for the chef in a tabular format."""
#     print("\n-------- Ingredient Requests --------")

#     try:
#         # Read all requests from the file
#         with open(REQUEST_Ingredient, "r") as file:
#             ingredient_requests = [line.strip().split(",") for line in file.readlines()]

#         if not ingredient_requests:
#             print("No ingredient requests found.")
#             return

#         # Ensure each request has exactly 5 values, fill missing fields with default values
#         cleaned_requests = []
#         for req in ingredient_requests:
#             if len(req) == 3:  # If only ingredient, quantity, unit are present
#                 req.extend(["N/A", ""])  # Add default values for status and extra_1
#             elif len(req) == 4:  # If ingredient, quantity, unit, and status are present
#                 req.append("N/A")  # Add default value for extra_1
#             elif len(req) == 5:
#                 pass  # Already has 5 values, no change needed
#             else:
#                 print(f"Warning: Skipping invalid line with {len(req)} values: {req}")
#                 continue  # Skip the line if it doesn't have 3, 4, or 5 values
#             cleaned_requests.append(req)

#         # Prepare data for tabular display
#         table_data = []
#         for idx, req in enumerate(cleaned_requests, 1):
#             ingredient, quantity, unit, status, extra_1 = req
#             table_data.append([f"{idx}", ingredient, quantity, unit, "Request"])

#         # Table headers
#         headers = ["ID", "Ingredient", "Quantity", "Unit", "Action"]

#         # Display the table
#         print(tabulate(table_data, headers=headers, tablefmt="grid"))

#         # Ask user if they want to update or delete
#         print("\nDo you want to update or delete any request? (yes/no)")
#         choice = input().lower()

#         if choice == "yes":
#             # Ask for the number of the ingredient to update or delete
#             print("Enter the number of the ingredient to update or delete (e.g., 1, 2, 3, ...):")
#             try:
#                 choice_number = int(input().strip())  # Convert the input to an integer
#                 if choice_number < 1 or choice_number > len(cleaned_requests):
#                     print(f"Invalid number. Please choose a number between 1 and {len(cleaned_requests)}.")
#                     return
                
#                 # Get the selected ingredient by number
#                 selected_ingredient = cleaned_requests[choice_number - 1]  # List is 0-indexed
#                 ingredient, quantity, unit, status, extra_1 = selected_ingredient
#                 print(f"Current details: {ingredient} - {quantity} {unit} - Status: {status}")

#                 # Ask whether to update or delete
#                 print("Would you like to update or delete this request? (update/delete):")
#                 action_choice = input().lower()

#                 if action_choice == "update":
#                     # Ask for new quantity (and validate)
#                     while True:
#                         quantity_input = input("Enter quantity (e.g., '2kg', '1.5ltr', '10units'): ").strip()
#                         quantity, unit = extract_quantity_and_unit(quantity_input)
#                         if quantity is not None:
#                             break
#                         print("❌ Invalid input! Please enter a number followed by a unit (e.g., '2kg', '1.5ltr').")

#                     # Ask for the ingredient type
#                     ingredient_type = input("Enter ingredient type (e.g., vegetable, spice, dairy, meat): ").strip().lower()

#                     # Ask for brand name
#                     brand_name = input("Enter brand name (if any, else type 'none'): ").strip().title()

#                     # Update the ingredient's quantity, unit, type, and brand name
#                     cleaned_requests[choice_number - 1][1] = quantity
#                     cleaned_requests[choice_number - 1][2] = unit
#                     cleaned_requests[choice_number - 1][4] = f"{ingredient_type}, {brand_name}"
#                     cleaned_requests[choice_number - 1][3] = "ok"  # Mark as updated/ok

#                     print(f"Updated {ingredient} to {quantity} {unit}, type: {ingredient_type}, brand: {brand_name}.")

#                     # Save the updated ingredient requests back to the file
#                     with open(REQUEST_Ingredient, "w") as file:
#                         for req in cleaned_requests:
#                             file.write(",".join(req) + "\n")

#                     # Update or add the ingredient to INGREDIENTS_FILE
#                     with open(INGREDIENTS_FILE, "a") as ingredient_file:
#                         # Check if ingredient already exists in INGREDIENTS_FILE
#                         ingredient_file.write(f"I{choice_number},{ingredient},{quantity},{unit},{ingredient_type},{brand_name}\n")

#                     print(f"Ingredient requests have been updated and uploaded to INGREDIENTS_FILE.")

#                 elif action_choice == "delete":
#                     # Delete the ingredient from the request list
#                     cleaned_requests.pop(choice_number - 1)
#                     print(f"Deleted {ingredient} from the request list.")

#                     # Save the updated ingredient requests back to the file after deletion
#                     with open(REQUEST_Ingredient, "w") as file:
#                         for req in cleaned_requests:
#                             file.write(",".join(req) + "\n")

#                     print(f"Ingredient request has been deleted.")

#                 else:
#                     print("Invalid action. Please choose either 'update' or 'delete'.")

#             except ValueError:
#                 print("Invalid input. Please enter a valid number.")

#     except FileNotFoundError:
#         print("Ingredient request file not found.")


def View_AND_Update_Ingredients_Requests_of_Chef():
    """View and update ingredient requests for the chef in a tabular format."""
    print("\n-------- Ingredient Requests --------")

    try: 
        with open(REQUEST_Ingredient, "r") as file:
            ingredient_requests = [line.strip().split(",") for line in file.readlines()]

        if not ingredient_requests:
            print("No ingredient requests found.")
            return
        cleaned_requests = []
        for req in ingredient_requests:
            if len(req) == 3:   
                req.extend(["N/A", ""])  
            elif len(req) == 4:  
                req.append("N/A")   
            elif len(req) == 5:
                pass  
            else:
                print(f"Warning: Skipping invalid line with {len(req)} values: {req}")
                continue  
            cleaned_requests.append(req)
 
        table_data = []
        for idx, req in enumerate(cleaned_requests, 1):
            ingredient, quantity, unit, status, extra_1 = req
            table_data.append([f"{idx}", ingredient, quantity, unit, "Request"])
 
        headers = ["ID", "Ingredient", "Quantity", "Unit", "Action"]
 
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
 
        print("\nDo you want to update or delete any request? (yes/no)")
        choice = input().lower()

        if choice == "yes": 
            print("Enter the number of the ingredient to update or delete (e.g., 1, 2, 3, ...):")
            try:
                choice_number = int(input().strip())   
                if choice_number < 1 or choice_number > len(cleaned_requests):
                    print(f"Invalid number. Please choose a number between 1 and {len(cleaned_requests)}.")
                    return
                 
                selected_ingredient = cleaned_requests[choice_number - 1]  # List is 0-indexed
                ingredient, quantity, unit, status, extra_1 = selected_ingredient
                print(f"Current details: {ingredient} - {quantity} {unit} - Status: {status}")
 
                print("Would you like to update or delete this request? (update/delete):")
                action_choice = input().lower()

                if action_choice == "update":
                    while True:
                        quantity_input = input("Enter quantity (e.g., '2kg', '1.5ltr', '10units'): ").strip()
                        quantity, unit = extract_quantity_and_unit(quantity_input)
                        if quantity is not None:
                            break
                        print("❌ Invalid input! Please enter a number followed by a unit (e.g., '2kg', '1.5ltr').")
 
                    ingredient_type = input("Enter ingredient type (e.g., vegetable, spice, dairy, meat): ").strip().lower()
                    brand_name = input("Enter brand name (if any, else type 'none'): ").strip().title()
                    cleaned_requests[choice_number - 1][1] = quantity
                    cleaned_requests[choice_number - 1][2] = unit
                    cleaned_requests[choice_number - 1][4] = f"{ingredient_type}, {brand_name}"
                    cleaned_requests[choice_number - 1][3] = "ok"   

                    print(f"Updated {ingredient} to {quantity} {unit}, type: {ingredient_type}, brand: {brand_name}.")
                    with open(REQUEST_Ingredient, "w") as file:
                        for req in cleaned_requests:
                            file.write(",".join(req) + "\n")
                    with open(INGREDIENTS_FILE, "a") as ingredient_file:
                        ingredient_file.write(f"I{choice_number},{ingredient},{quantity},{unit},{ingredient_type},{brand_name}\n")

                    print(f"Ingredient requests have been updated and uploaded to INGREDIENTS_FILE.")

                elif action_choice == "delete":
                    deleted_ingredient = cleaned_requests.pop(choice_number - 1)
                    print(f"Deleted {deleted_ingredient[0]} from the request list.")
                    with open(REQUEST_Ingredient, "w") as file:
                        for req in cleaned_requests:
                            file.write(",".join(req) + "\n")

                    print(f"Ingredient request has been deleted.")

                else:
                    print("Invalid action. Please choose either 'update' or 'delete'.")

            except ValueError:
                print("Invalid input. Please enter a valid number.")

    except FileNotFoundError:
        print("Ingredient request file not found.")



def update_ingredient():
    """Updates an ingredient's details after displaying them in a table format."""
    print("\n-------- Update Ingredient --------\n")
    if not os.path.exists(INGREDIENTS_FILE) or os.stat(INGREDIENTS_FILE).st_size == 0:
        print("No ingredients found.")
        return
    
    ingredient_list = []
    with open(INGREDIENTS_FILE, "r") as f:
        for line in f:
            ingredient_list.append(line.strip().split(","))   

    if not ingredient_list:
        print("No ingredients found.")
        return
 
    indexed_ingredients = [[i + 1] + ingredient for i, ingredient in enumerate(ingredient_list)]
    print(tabulate(indexed_ingredients, headers=["No.", "ID", "Name", "Quantity", "Type", "Brand"], tablefmt="grid"))

    try: 
        ingredient_index = int(input("\nEnter the number of the ingredient to update: ")) - 1
        if ingredient_index < 0 or ingredient_index >= len(ingredient_list):
            print("Invalid selection.")
            return 
        current_ingredient = ingredient_list[ingredient_index]
 
        new_name = input(f"Enter new name ({current_ingredient[1]}): ").strip() or current_ingredient[1]
        new_quantity = input(f"Enter new quantity ({current_ingredient[2]}): ").strip() or current_ingredient[2]
        new_type = input(f"Enter new type ({current_ingredient[3]}): ").strip() or current_ingredient[3]
        new_brand = input(f"Enter new brand ({current_ingredient[4]}): ").strip() or current_ingredient[4]
 
        ingredient_list[ingredient_index] = [current_ingredient[0], new_name, new_quantity, new_type, new_brand]
 
        with open(INGREDIENTS_FILE, "w") as f:
            for ingredient in ingredient_list:
                f.write(",".join(ingredient) + "\n")

        print(f"\nIngredient '{new_name}' updated successfully!")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
 




def delete_ingredient():
    """Deletes an ingredient from the list after displaying it in a table format."""
    print("\n-------- Delete Ingredient --------\n")
 
    if not os.path.exists(INGREDIENTS_FILE) or os.stat(INGREDIENTS_FILE).st_size == 0:
        print("No ingredients found.")
        return

    ingredient_list = []
 
    with open(INGREDIENTS_FILE, "r") as f:
        for line in f:
            ingredient_list.append(line.strip().split(","))   

    if not ingredient_list:
        print("No ingredients found.")
        return
 
    indexed_ingredients = [[i + 1] + ingredient for i, ingredient in enumerate(ingredient_list)]
    print(tabulate(indexed_ingredients, headers=["No.", "ID", "Name", "Quantity", "Type", "Brand"], tablefmt="grid"))

    try: 
        ingredient_index = int(input("\nEnter the number of the ingredient to delete: ")) - 1
        if ingredient_index < 0 or ingredient_index >= len(ingredient_list):
            print("Invalid selection.")
            return
 
        confirm = input(f"Are you sure you want to delete '{ingredient_list[ingredient_index][1]}'? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Ingredient deletion canceled.")
            return
 
        deleted_ingredient = ingredient_list.pop(ingredient_index)
 
        with open(INGREDIENTS_FILE, "w") as f:
            for ingredient in ingredient_list:
                f.write(",".join(ingredient) + "\n")

        print(f"\nIngredient '{deleted_ingredient[1]}' deleted successfully!")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


def validate_email(email):
    """Validate if the given email is in correct format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password(password):
    """Validate password strength (at least 6 characters)."""
    return len(password) >= 6

def validate_username(username, staff_list):
    """Ensure the new username is unique."""
    for staff in staff_list:
        if staff[2] == username:   
            return False
    return True

def Update_own_profile():
    if not os.path.exists(LOGIN_USER_DATA):
        print("You are not logged in.")
        return

    with open(LOGIN_USER_DATA, "r") as f:
        login_data = f.read().strip().split(",")
        logged_username = login_data[0]
        logged_role = login_data[2]

    staff_list = []
    with open(Staff_FILE, "r") as f:
        for line in f:
            staff_list.append(line.strip().split(","))

    staff_to_edit = None
    for staff in staff_list:
        staff_id, name, username, email, password, role = staff
        if username == logged_username:
            staff_to_edit = staff
            break

    if not staff_to_edit:
        print("Staff member not found.")
        return

    print("\n-------- Edit Your Profile: --------\n")
    staff_id, name, username, email, password, role = staff_to_edit

    # Display current details
    print(f"\nCurrent Profile Details: ")
    print(f"Name: {name}")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Role: {role}")
    
    # Ask for updates
    is_update_name = input("Do you want to update your name (y/n): ").strip().lower()
    if is_update_name == "y":
        name = input("Enter new name: ")

    is_update_username = input("Do you want to update your username (y/n): ").strip().lower()
    if is_update_username == "y":
        while True:
            new_username = input("Enter new username: ").strip()
            if validate_username(new_username, staff_list):
                username = new_username
                break
            print("Username already taken, please choose another one.")

    is_update_email = input("Do you want to update your email (y/n): ").strip().lower()
    if is_update_email == "y":
        while True:
            new_email = input("Enter new email: ").strip()
            if validate_email(new_email):
                email = new_email
                break
            print("Invalid email format. Please enter a valid email.")

    is_update_password = input("Do you want to update your password (y/n): ").strip().lower()
    if is_update_password == "y":
        while True:
            new_password = input("Enter new password: ").strip()
            if validate_password(new_password):
                password = new_password
                break
            print("Password must be at least 6 characters long.")

    # No role update option for non-admins
    if logged_role == "Admin":
        is_update_role = input("Do you want to update your role (y/n): ").strip().lower()
        if is_update_role == "y":
            role = input("Enter new role (Manager/Chef): ").capitalize()

    staff_list[staff_list.index(staff_to_edit)] = [staff_id, name, username, email, password, role]

    with open(Staff_FILE, "w") as f:
        for staff in staff_list:
            f.write(f"{staff[0]},{staff[1]},{staff[2]},{staff[3]},{staff[4]},{staff[5]}\n")

    print("\nProfile updated successfully.")
    if logged_role == "Manager":
        manager_menu()
 

    if not os.path.exists(LOGIN_USER_DATA):
        print("You are not logged in.")
        return
 
    with open(LOGIN_USER_DATA, "r") as f:
        login_data = f.read().strip().split(",")
        logged_username = login_data[0]
        logged_role = login_data[2]
 
    staff_list = []
    with open(Staff_FILE, "r") as f:
        for line in f:
            staff_list.append(line.strip().split(","))

    staff_to_edit = None
    for staff in staff_list:
        staff_id, name, username, email, password, role = staff
        if username == logged_username:
            staff_to_edit = staff
            break

    if not staff_to_edit:
        print("Staff member not found.")
        return

    print("\n-------- Edit Your Profile: --------\n")
    staff_id, name, username, email, password, role = staff_to_edit
 
    print(f"\nCurrent Profile Details: ")
    print(f"Name: {name}")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Role: {role}")
     
    is_update_name = input("Do you want to update your name (y/n): ").strip().lower()
    if is_update_name == "y":
        name = input("Enter new name: ")

    is_update_username = input("Do you want to update your username (y/n): ").strip().lower()
    if is_update_username == "y":
        while True:
            new_username = input("Enter new username: ").strip()
            if validate_username(new_username, staff_list):
                username = new_username
                break
            print("Username already taken, please choose another one.")

    is_update_email = input("Do you want to update your email (y/n): ").strip().lower()
    if is_update_email == "y":
        while True:
            new_email = input("Enter new email: ").strip()
            if validate_email(new_email):
                email = new_email
                break
            print("Invalid email format. Please enter a valid email.")

    is_update_password = input("Do you want to update your password (y/n): ").strip().lower()
    if is_update_password == "y":
        while True:
            new_password = input("Enter new password: ").strip()
            if validate_password(new_password):
                password = new_password
                break
            print("Password must be at least 6 characters long.")

 
    staff_list[staff_list.index(staff_to_edit)] = [staff_id, name, username, email, password, role]
 
    with open(Staff_FILE, "w") as f:
        for staff in staff_list:
            f.write(f"{staff[0]},{staff[1]},{staff[2]},{staff[3]},{staff[4]},{staff[5]}\n")

    print("\nProfile updated successfully.")

 
    if not os.path.exists(LOGIN_USER_DATA):
        print("You are not logged in.")
        return
 
    with open(LOGIN_USER_DATA, "r") as f:
        login_data = f.read().strip().split(",")
        logged_username = login_data[0]
        logged_role = login_data[2]
 
    staff_list = []
    with open(Staff_FILE, "r") as f:
        for line in f:
            staff_list.append(line.strip().split(","))
 
    staff_to_edit = None
    for staff in staff_list:
        staff_id, name, username, email, password, role = staff
        if username == logged_username:
            staff_to_edit = staff
            break

    if not staff_to_edit:
        print("Staff member not found.")
        return

    print("\n-------- Edit Your Profile: --------\n")
    staff_id, name, username, email, password, role = staff_to_edit

    # Display current details
    print(f"\nCurrent Profile Details: ")
    print(f"Name: {name}")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Role: {role}")
    
    # Ask for updates
    is_update_name = input("Do you want to update your name (y/n): ").strip().lower()
    if is_update_name == "y":
        name = input("Enter new name: ")

    is_update_username = input("Do you want to update your username (y/n): ").strip().lower()
    if is_update_username == "y":
        username = input("Enter new username: ")

    is_update_email = input("Do you want to update your email (y/n): ").strip().lower()
    if is_update_email == "y":
        email = input("Enter new email: ")

    is_update_password = input("Do you want to update your password (y/n): ").strip().lower()
    if is_update_password == "y":
        password = input("Enter new password: ")

    is_update_role = input("Do you want to update your role (y/n): ").strip().lower()
    if is_update_role == "y" and logged_role == "Admin":  # Admin can update role, others cannot
        role = input("Enter new role (Manager/Chef): ").capitalize()
 
    staff_list[staff_list.index(staff_to_edit)] = [staff_id, name, username, email, password, role]
 
    with open(Staff_FILE, "w") as f:
        for staff in staff_list:
            f.write(f"{staff[0]},{staff[1]},{staff[2]},{staff[3]},{staff[4]},{staff[5]}\n")

    print("\nProfile updated successfully.")

def logOut():
    if os.path.exists(LOGIN_USER_DATA):
        os.remove(LOGIN_USER_DATA)
        print("Logged out successfully.")
        main()
    else:
        print("You are not logged in.")

    

 
 

