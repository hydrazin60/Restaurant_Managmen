import os
import re
from tabulate import tabulate
MENU_FILE = os.path.join("database", "menu_data.txt")
ORDERS_FILE = os.path.join("database", "orders_data.txt")
FEEDBACK_FILE = os.path.join("database", "feedback_data.txt")
LOGIN_USER_DATA = os.path.join("cookies", "login_User_data.txt")
USER_FILE_Data = os.path.join("database", "users_data.txt")
from OurRestaurant import main


# def clear_screen():
#     """Clears the terminal screen."""
#     os.system("cls" if os.name == "nt" else "clear")

# Customer menu
def customer_menu():
    while True:
        print("\nCustomer Menu:")
        print("1. View Menu")
        print("2. Order Menu")
        print("3. Send Feedback")
        print("4. Update Profile")
        print("5. Logout")
        choice = input("Enter choice: ")
        if choice == "1":
             view_menu()
        elif choice == "2":
            order()
        elif choice == "3":
            send_feedback()
        elif choice == "4":
             Update_own_profile()
        elif choice == "5":
            logOut()
        else:
            print("Invalid choice.")


def view_menu():
    print("\nMenu:")
    menu_items = [] 
    with open(MENU_FILE, "r") as f:
        for index, line in enumerate(f, start=1):
            item_details = line.strip().split(",")    
            if len(item_details) == 4:
                item_id, item_name, item_price, item_category = item_details
                menu_items.append([index, item_id, item_name, item_price, item_category])  # Add details as a row
            else:
                print(f"Skipping invalid line (line {index}): {line.strip()}")
    print(tabulate(menu_items, headers=["No.", "Item ID", "Item Name", "Price", "Category"], tablefmt="grid"))
view_menu()


# Place order
def order():
    print("\n-------- Order Menu: --------:")
    print("1. Place Order")
    print("2. Update Order")
    print("3. Cancel Order")
    print("4. View All Orders")
    print("5. Back to Customer Menu")
    choice = input("Enter choice: ")

    if choice == "1":
        place_order()
    elif choice == "2":
        update_order()
    elif choice == "3":
        order_cancel()
    elif choice == "4":
         View_All_Orders()
    elif choice == "5":
        customer_menu()
    else:
        print("Invalid choice.")    

def get_customer_name():
    # Reading the customer name from the LOGIN_USER_DATA file
    if os.path.exists(LOGIN_USER_DATA):
        with open(LOGIN_USER_DATA, "r") as f:
            # Assuming the customer name is saved in the first line of the file
            customer_name = f.readline().strip()  # Get the first line as the customer name
            return customer_name
    else:
        print("Login data file not found.")
        return None


# def place_order():
#     print("\n-------- Place Order --------\n")
#     menu_items = []
    
#     # Read menu items from the MENU_FILE
#     with open(MENU_FILE, "r") as f:
#         for index, line in enumerate(f, start=1):
#             item_details = line.strip().split(",")  
#             menu_items.append(item_details)
    
#     # Display the menu
#     table_data = [[index+1, item[0], item[1], item[2]] for index, item in enumerate(menu_items)]
#     print(tabulate(table_data, headers=["No.", "Item ID", "Item Name", "Price", "Category"], tablefmt="grid"))
    
#     # Get the customer name and role from login data
#     customer_name, role = get_customer_name_and_role()
#     if not customer_name:
#         print("No customer name found in login data.")
#         return
    
#     continue_ordering = True

#     while continue_ordering:
#         try:
#             # Ask the customer to select an item by its menu number
#             item_number = int(input("\nEnter the menu number of the item you want to order: ")) - 1  # Select item by its number
#             if item_number < 0 or item_number >= len(menu_items):
#                 print("Invalid selection. Please choose a valid number from the menu.")
#                 continue

#             # Fetch item details
#             selected_item_name = menu_items[item_number][1]  # Item Name
#             selected_item_price = menu_items[item_number][2]  # Item Price
#             selected_item_category = menu_items[item_number][3]  # Item Category
#             item_id = menu_items[item_number][0]  # Item ID
            
#             # Save the order to the orders file with customer name and role, but not the password
#             with open(ORDERS_FILE, "a") as f:
#                 f.write(f"{customer_name},{role},{item_id},{selected_item_name},{selected_item_price},{selected_item_category},Pending\n")
            
#             print(f"Order placed successfully for {selected_item_name}!")

#             # Ask if the customer wants to order more items
#             another_order = input("\nDo you want to place another order? (y/n): ").strip().lower()
#             if another_order != 'y':
#                 continue_ordering = False
#                 print("Your order has been completed.")
        
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")

def place_order():
    print("\n-------- Place Order --------\n")
    menu_items = []
    
    # Read menu items from the MENU_FILE
    with open(MENU_FILE, "r") as f:
        for index, line in enumerate(f, start=1):
            item_details = line.strip().split(",")  
            menu_items.append(item_details)
    
    # Display the menu
    table_data = [[index+1, item[0], item[1], item[2]] for index, item in enumerate(menu_items)]
    print(tabulate(table_data, headers=["No.", "Item ID", "Item Name", "Price", "Category"], tablefmt="grid"))
    
    # Get the customer name and role from login data
    customer_name, role = get_customer_name_and_role()
    if not customer_name:
        print("No customer name found in login data.")
        return
    
    continue_ordering = True

    while continue_ordering:
        try:
            # Ask the customer to select an item by its menu number
            item_number = int(input("\nEnter the menu number of the item you want to order: ")) - 1  # Select item by its number
            if item_number < 0 or item_number >= len(menu_items):
                print("Invalid selection. Please choose a valid number from the menu.")
                continue

            # Fetch item details
            selected_item_name = menu_items[item_number][1]  # Item Name
            selected_item_price = menu_items[item_number][2]  # Item Price
            selected_item_category = menu_items[item_number][3]  # Item Category
            item_id = menu_items[item_number][0]  # Item ID

            # Ask for the quantity
            quantity = int(input(f"Enter the quantity for {selected_item_name}: "))
            if quantity <= 0:
                print("Please enter a valid quantity greater than 0.")
                continue
            
            # Calculate the total price
            total_price = int(selected_item_price) * quantity

            # Save the order to the orders file with customer name and role, but not the password
            with open(ORDERS_FILE, "a") as f:
                f.write(f"{customer_name},{role},{item_id},{selected_item_name},{selected_item_price},{selected_item_category},{quantity},{total_price},Pending\n")
            
            print(f"Order placed successfully for {quantity}x {selected_item_name}!")

            # Ask if the customer wants to order more items
            another_order = input("\nDo you want to place another order? (y/n): ").strip().lower()
            if another_order != 'y':
                continue_ordering = False
                print("Your order has been completed.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_customer_name_and_role():
    """Fetches the customer name and role from login data."""
    try:
        with open(LOGIN_USER_DATA, "r") as file:
            user_data = file.readline().strip()
            username, password, role = user_data.split(",")  # Assuming format: username,password,role
            return username, role  # Return only username and role
    except FileNotFoundError:
        print("Login data not found.")
        return None, None


def get_customer_name_and_role():
    """Fetches the customer name and role from login data."""
    try:
        with open(LOGIN_USER_DATA, "r") as file:
            user_data = file.readline().strip()
            username, password, role = user_data.split(",")   
            return username, role   
    except FileNotFoundError:
        print("Login data not found.")
        return None, None

 

def order_cancel():
    print("\n-------- Cancel Order --------\n")
     
    with open(ORDERS_FILE, "r") as f:
        orders = f.readlines()
    
    if not orders:
        print("No orders found.")
        return
     
    table_data = []
    for i, order in enumerate(orders):
        order_data = order.strip().split(",") 
        table_data.append([i + 1, order_data[3], order_data[4], order_data[5], order_data[6], order_data[8]])
 
    print(tabulate(table_data, headers=["No.", "Item", "Price", "Category", "Num of order", "Status"], tablefmt="grid"))
    
    try: 
        order_index = int(input("Enter the number of the order to cancel: ")) - 1
        if order_index < 0 or order_index >= len(orders):
            print("Invalid selection.")
            return 
        order_data = orders[order_index].strip().split(",")
        status = order_data[8]
         
        if status.lower() != "pending":
            print("Only orders with 'Pending' status can be cancelled.")
            return
         
        is_cancelled = input("Are you sure you want to cancel this order? (yes/no): ").lower() == "yes"
        
        if is_cancelled: 
            orders.pop(order_index)

            with open(ORDERS_FILE, "w") as f:
                f.writelines(orders)
            
            print("Order cancelled successfully.")
        else:
            print("Order not cancelled.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


# def View_All_Orders():
#     logged_in_user = get_logged_in_user()
    
#     if not logged_in_user:
#         print("No logged-in user found.")
#         return
    
#     print("\nOrder Status:\n")
    
#     # Read orders from the ORDERS_FILE
#     with open(ORDERS_FILE, "r") as f:
#         orders = f.readlines()
#         if not orders:
#             print("No orders found.")
#             return
        
#         # Prepare the data for the table
#         table_data = []
#         total_price = 0  # Initialize total price
        
#         for i, order in enumerate(orders):
#             order_data = order.strip().split(",")
            
#             # Ensure the order data has 9 relevant fields (corrected from 8 to match saved data format)
#             if len(order_data) == 9:  # 9 because it's in the format: customer_name, role, item_id, item_name, price, category, quantity, total_price, status
#                 customer_name = order_data[0]
#                 role = order_data[1]
#                 item_name = order_data[3]
#                 item_price = float(order_data[4])  # Convert price to float for calculation
#                 item_category = order_data[5]
#                 quantity = int(order_data[6])  # Quantity of items ordered
#                 total_item_price = float(order_data[7])  # Total price for the ordered quantity
#                 status = order_data[8]
                
#                 # Only show orders of the logged-in user
#                 if customer_name == logged_in_user:
#                     table_data.append([i + 1, customer_name,  item_name, item_price, item_category, quantity, total_item_price, status])
#                     total_price += total_item_price  # Add the total item price to the total price
#             else:
#                 print(f"Skipping malformed order (line {i + 1}): {order.strip()}")
        
#         # If there are valid orders, display them in a table format using tabulate
#         if table_data:
#             print(tabulate(table_data, headers=["No.", "Customer Name",  "Item Name", "Price", "Category", "Quantity", "Total Price", "Status"], tablefmt="grid"))
#             print(f"\nTotal Price: Rs {total_price:.2f}")
#         else:
#             print(f"No orders found for {logged_in_user}.")


def View_All_Orders():
    logged_in_user = get_logged_in_user()
    
    if not logged_in_user:
        print("No logged-in user found.")
        return
    
    print("\nOrder Status (Completed & Pending Orders Only):\n")
    
    if not os.path.exists(ORDERS_FILE):
        print("No orders file found.")
        return
    
    with open(ORDERS_FILE, "r") as f:
        orders = f.readlines()
        if not orders:
            print("No orders found.")
            return
        
        # Prepare the data for the table
        table_data = []
        total_price = 0  # Initialize total price
        
        for i, order in enumerate(orders):
            order_data = order.strip().split(",")
            
            # Ensure the order data has the correct number of fields
            if len(order_data) == 9:
                customer_name = order_data[0]
                role = order_data[1]
                item_name = order_data[3]
                item_price = float(order_data[4])  # Convert price to float for calculation
                item_category = order_data[5]
                quantity = int(order_data[6])  # Quantity of items ordered
                total_item_price = float(order_data[7])  # Total price for the ordered quantity
                status = order_data[8].strip().lower()  # Convert status to lowercase for consistency
                
                # **Show only "Completed" or "Pending" orders**
                if customer_name == logged_in_user and status in ["completed", "pending"]:
                    table_data.append([i + 1, customer_name, item_name, item_price, item_category, quantity, total_item_price, status.capitalize()])
                    total_price += total_item_price  # Add to total price
            else:
                print(f"Skipping malformed order (line {i + 1}): {order.strip()}")

        # Display filtered orders in a table format
        if table_data:
            print(tabulate(table_data, headers=["No.", "Customer Name", "Item Name", "Price", "Category", "Quantity", "Total Price", "Status"], tablefmt="grid"))
            print(f"\nTotal Price (Completed & Pending Orders): Rs {total_price:.2f}")
        else:
            print(f"No Completed or Pending orders found for {logged_in_user}.")

def get_logged_in_user(): 
    try:
        with open(LOGIN_USER_DATA, "r") as file:
            user_data = file.readline().strip()
            username, _, _ = user_data.split(",")   
            return username
    except FileNotFoundError:
        print("Login data not found.")
        return None
    

def update_order():
    print("\n-------- Update Order --------\n")
    
    # Read orders from the ORDERS_FILE
    order_list = []
    with open(ORDERS_FILE, "r") as f:
        for line in f:
            order_list.append(line.strip().split(","))  # Store each order as a list of details
    
    if not order_list:
        print("No orders found.")
        return
    
    # Get the logged-in user
    logged_in_user = get_logged_in_user()
    
    if not logged_in_user:
        print("No logged-in user found.")
        return
    
    # Filter the orders for the logged-in user
    user_orders = [order for order in order_list if order[0] == logged_in_user]
    
    if not user_orders:
        print(f"No orders found for {logged_in_user}.")
        return
    
    while True:
        print(f"\nCurrent Orders for {logged_in_user}:")
        table_data = []
        for i, order in enumerate(user_orders): 
            table_data.append([i + 1, order[3], order[4], order[5], order[6], order[8] , order[7]])  # Corrected fields
        print(tabulate(table_data, headers=["No.", "Item", "Price", "Category", "Num of order", "Status","Total Price"], tablefmt="grid"))
        
        try:
            order_index = int(input("Enter the number of the order to update: ")) - 1  # Get the order index
            if order_index < 0 or order_index >= len(user_orders):
                print("Invalid selection.")
                continue

            selected_order = user_orders[order_index]
            print(f"Current order details: Item: {selected_order[3]}, Price: {selected_order[4]}, Category: {selected_order[5]}, Status: {selected_order[7]}")
             
            ifUpdateOrderItems = input("Do you want to update this order (y/n): ").strip().lower()
            if ifUpdateOrderItems == "y": 
                # Update the number of items
                new_num_of_items = input(f"Current number of items: {selected_order[6]}. Enter new number of items: ").strip()
                if new_num_of_items.isdigit():
                    selected_order[6] = new_num_of_items  # Update the number of items
                else:
                    print("Invalid input. Please enter a valid number for quantity.")
                    continue
                
                # Update the item category
                new_category = input(f"Current category: {selected_order[5]}. Enter new category: ").strip()
                selected_order[5] = new_category  # Update the category

                # Update the corresponding order in the original order list
                order_list[order_index] = selected_order
                 
                # Write the updated orders back to the file
                with open(ORDERS_FILE, "w") as f:
                    for order in order_list:
                        f.write(",".join(order) + "\n")
                
                print("Order updated successfully.")
            
            else:
                print("Order not updated.")
             
            # Ask if the user wants to update another order
            another_update = input("Do you want to update another order (y/n): ").strip().lower()
            if another_update != "y":
                print("Redirecting to the main menu...")
                break  # Exit the loop and return to the main menu
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def send_feedback():
    """Send feedback with the logged-in user's username and role."""
    logged_in_user = get_logged_in_user()
    
    if not logged_in_user:
        print("No user is logged in.")
        return
    
    # Get the logged-in user's role (from LOGIN_USER_DATA)
    try:
        with open(LOGIN_USER_DATA, "r") as file:
            user_data = file.readline().strip()
            username, _, role = user_data.split(",")  # Assuming format: username,password,role
            user_role = role
    except FileNotFoundError:
        print("Login data not found.")
        return
    
    print("\nSend Feedback:")
    message = input("Enter your feedback: ")
    
    # Store feedback along with the user info in the feedback file
    try:
        with open(FEEDBACK_FILE, "a") as f:
            f.write(f"User: {logged_in_user}, Role: {user_role}, Feedback: {message}\n")
        print("Feedback sent successfully.")
    except Exception as e:
        print(f"Error saving feedback: {e}")

# ###############################################
 

 
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
    with open(USER_FILE_Data, "r") as f:
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

    with open(USER_FILE_Data, "w") as f:
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

    

 
 