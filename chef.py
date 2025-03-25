import os
from tabulate import tabulate
import re
ORDERS_FILE = os.path.join("database", "orders_data.txt")
INGREDIENTS_FILE = os.path.join("database", "ingredients_data.txt")
CUSTOMER_DATA = os.path.join("database", "users_data.txt")
STAFF_DATA = os.path.join("database", "staff_data.txt")
REQUEST_Ingredient = os.path.join("database" , "Req_ingredients_data.txt")
LOGIN_USER_DATA = os.path.join("cookies" , "login_User_data.txt")
from OurRestaurant import main


def chef_menu():
    while True:
        print("\nChef Menu:")
        print("1. Orders Management")
        print("2. Ingredient Managemnt ")
        print("3. Update Profile")
        print("4. Logout")
        choice = input("Enter choice: ")

        if choice == "1":
            order()
        elif choice == "2":
             ingredients()   
        elif choice == "3":
             Update_own_profile()
        elif choice == "4":
            logout()
        else:
            print("Invalid choice.")


def order():
    print("\n------------Order sections----------\n")
    print("1. View All orders")
    print("2. Update order status")
    print("3. Go Back to Chef Menu")
    choice = input("Enter Choice :")
    if choice == "1":
        view_all_orders()
    elif choice == "2":
        update_order_status()
    elif choice == "3":
        chef_menu()
    else :
        print(" Invalid choice")        
     

def ingredients ():
    print("\n-------------- ingredients Menu ----------\n")
    print("1. View Alll ingredients ")
    print("2. requist ingredients")
    print("3. Go Back to Chef Menu")
    choice = input("Enter Choice :")

    if choice == "1":
        view_all_ingredients()
    elif choice == "2":
        request_ingredients()
    elif choice == "3":
        chef_menu()
    else:
        print("Invalid choice")        

def ingredients():
    print("\n------------------ ingredients Menu ----------\n")
    print("1. View all ingredients")
    print("2. Request ingredients ")
    choice = int(input("Enter Choice. "))
    if choice == 1:
        view_all_ingredients()
    elif choice == 2:
        request_ingredients()
    else:
        print("Invalid choice")
 
def view_all_orders():
    """Fetch and display only relevant fields (Customer, Item Name, Item Price, Total Price, Status) in a table format."""
    if not os.path.exists(ORDERS_FILE):
        print("No orders found.")
        return
    
    with open(ORDERS_FILE, "r") as f:
        orders = f.readlines()

    if not orders:
        print("No orders found.")
        return
    
    order_data_list = []
    for order in orders:
        order_data = order.strip().split(",")   
        if len(order_data) == 9:   
            customer_name = order_data[0]
            item_name = order_data[3]
            item_price = order_data[4]
            total_price = order_data[7]
            status = order_data[8]
            order_data_list.append([customer_name, item_name, item_price, total_price, status])
     
    headers = ["Customer", "Item Name", "Item Price", "Total Price", "Status"]
     
    print(tabulate(order_data_list, headers=headers, tablefmt="grid"))
view_all_orders()

def update_order_status():
    """Allow Chef to update the status of orders."""

    while True:
        orders = []
        with open(ORDERS_FILE, "r") as f:
            for line in f:
                orders.append(line.strip().split(",")) 
        pending_orders = [order for order in orders if order[8].lower() == "pending"]

        if not pending_orders:
            print("No pending orders found.")
            return
 
        table_headers = ["#", "Order ID", "Customer", "Item", "Quantity", "Unit Price", "Total Price", "Status"]
        table_data = []
 
        for i, order in enumerate(pending_orders): 
            order_data = [
                i + 1,   
                order[2],   
                order[0],  
                order[3],  
                order[6],   
                order[4],   
                order[7],   
                order[8]    
            ]
            table_data.append(order_data)
 
        print("\n-------- Pending Orders --------")
        print(tabulate(table_data, headers=table_headers, tablefmt="grid"))

        try: 
            order_index = int(input("\nEnter the number of the order to update: ")) - 1
            if order_index < 0 or order_index >= len(pending_orders):
                print("Invalid selection.")
                return
 
            selected_order = pending_orders[order_index]
            
            new_status = input("Enter new status (Cancelled/Completed): ").capitalize()
            if new_status not in ["Cancelled", "Completed"]:
                print("Invalid status. Please enter 'Cancelled' or 'Completed'.")
                return
            selected_order[8] = new_status
            with open(ORDERS_FILE, "w") as f:
                for order in orders:
                    f.write(",".join(order) + "\n")
            print("Order status updated successfully.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        continue_update = input("\nDo you want to update more orders? (y/n): ").lower()
        if continue_update != 'y':
            break


from tabulate import tabulate

def view_all_ingredients():
    """View all ingredient requests in table format."""
    print("\n-------- Ingredient Requests --------")

    try:
        with open(INGREDIENTS_FILE, "r") as f:
            ingredients = [line.strip().split(",") for line in f.readlines()]

        if not ingredients:
            print("No ingredient requests found.")
            return
        print(ingredients)
        max_columns = max(len(row) for row in ingredients)
        headers = ["ID", "Ingredient", "Quantity", "Unit", "Category"]
        if max_columns > len(headers):
            headers.extend([f"Extra_{i}" for i in range(1, max_columns - len(headers) + 1)])
        formatted_data = [row + ["N/A"] * (max_columns - len(row)) for row in ingredients]
        print(tabulate(formatted_data, headers=headers, tablefmt="grid"))

    except FileNotFoundError:
        print("Ingredient file not found.")


def request_ingredients():
    """Allow Chef to request ingredients."""

    print("\n-------- Request Ingredients --------")
    ingredient = input("Enter ingredient name: ").strip()
    if not ingredient:
        print("Ingredient name cannot be empty.")
        return

    # Prompt for quantity and ensure it's a valid positive integer
    try:
        quantity = int(input("Enter quantity: ").strip())
        if quantity <= 0:
            print("Quantity must be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Quantity must be a number.")
        return

    # Prompt for unit
    unit = input("Enter unit (e.g., kg, liter, pieces): ").strip()
    if not unit:
        print("Unit cannot be empty.")
        return

    # Save the ingredient request (ingredient name, quantity, and unit) to the file
    try:
        with open(REQUEST_Ingredient, "a") as f:
            f.write(f"{ingredient},{quantity},{unit}\n")
        print(f"Ingredient request for {ingredient} (Quantity: {quantity}, Unit: {unit}) added successfully.")
    except IOError:
        print("Error saving ingredient request. Please try again.")


def validate_username(new_username, staff_list):
    """Validate if the username already exists in the staff list."""
    for staff in staff_list:
        if staff[2] == new_username:  # Compare with existing usernames
            return False
    return True

def validate_email(new_email):
    """Validate email format (basic check)."""
    return "@" in new_email and "." in new_email


def validate_password(new_password):
    """Validate if password is at least 6 characters."""
    return len(new_password) >= 6


def Update_own_profile():
    """Allow customers to update their profile (name, username, password)."""
    if not os.path.exists(LOGIN_USER_DATA):
        print("You are not logged in.")
        return

    with open(LOGIN_USER_DATA, "r") as f:
        login_data = f.read().strip().split(",")
        logged_username = login_data[0]
        logged_role = login_data[2]

    staff_list = []
    with open(STAFF_DATA, "r") as f:
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

    # Customers cannot update their role
    if logged_role != "Admin":
        print("You cannot update your role.")
    else:
        is_update_role = input("Do you want to update your role (y/n): ").strip().lower()
        if is_update_role == "y":
            role = input("Enter new role (Manager/Chef): ").capitalize()

    staff_list[staff_list.index(staff_to_edit)] = [staff_id, name, username, email, password, role]

    with open(STAFF_DATA, "w") as f:
        for staff in staff_list:
            f.write(f"{staff[0]},{staff[1]},{staff[2]},{staff[3]},{staff[4]},{staff[5]}\n")

    print("\nProfile updated successfully.")


def logout():
    if os.path.exists(LOGIN_USER_DATA):
        os.remove(LOGIN_USER_DATA)
        print("Logged out successfully.")
        main()
    else:
        print("You are not logged in.")

    
   