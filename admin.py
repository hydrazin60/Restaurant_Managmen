import os

# File paths
STAFF_FILE = os.path.join("data", "staff.txt")
SALES_FILE = os.path.join("data", "sales.txt")
FEEDBACK_FILE = os.path.join("data", "feedback.txt")
USER_FILE = os.path.join( "data", "users.txt")
LOGIN_USER_DATA = os.path.join("data", "login_User_data.txt")
 
def admin_menu():
    while True:
        print("\n---------Admin Menu:---------\n")
        print("1. Manage Staff")
        print("2. View Sales Report")
        print("3. View Feedback")
        print("4. Update Profile")
        print("5. Logout")
        choice = input("Enter choice: ")

        if choice == "1":
            manage_staff()
        elif choice == "2":
            view_sales_report()
        elif choice == "3":
            view_feedback()
        elif choice == "4":
            Update_own_profile()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
 
def manage_staff():
    while True:
        print("\n-------Manage Staff:-------\n")
        print("1. Add Staff")
        print("2. Edit Staff")
        print("3. Delete Staff")
        print("4. View Staff")
        print("5. Back to Admin Menu")
        choice = input("Enter choice: ")

        if choice == "1":
            add_staff()
        elif choice == "2":
            edit_staff()
        elif choice == "3":
            delete_staff()
        elif choice == "4":
            view_staff()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
 
def get_next_staff_id():
    if not os.path.exists(STAFF_FILE):
        return 100  # Start with ID 100 if the file doesn't exist
    with open(STAFF_FILE, "r") as f:
        lines = f.readlines()
        if not lines:
            return 100  # Start with ID 100 if the file is empty
        last_line = lines[-1]
        last_id = int(last_line.split(",")[0])  # Extract the last ID
        return last_id + 1  # Increment the last ID by 1

def add_staff():
    print("\n--------Add Staff:--------\n")
    staff_id = get_next_staff_id()  # Generate a unique ID
    staff_name = input("Enter staff name: ")
    username = input("Enter staff username: ")
    email = input("Enter staff email: ")
    password = input("Enter staff password: ")
    role = input("Enter staff role (Manager/Chef): ").capitalize()
    
    # Check if the username or email already exists
    if os.path.exists(STAFF_FILE):
        with open(STAFF_FILE, "r") as f:
            for line in f:
                existing_data = line.strip().split(",")
                existing_username = existing_data[2]  # Username is the third field
                existing_email = existing_data[3]  # Email is the fourth field
                if existing_username == username:
                    print("Username already exists. Please choose a different username.")
                    return
                if existing_email == email:
                    print("Email already exists. Please use a different email.")
                    return

    # Save new staff to file
    with open(STAFF_FILE, "a") as f:
        f.write(f"{staff_id},{staff_name},{username},{email},{password},{role}\n")
    print(f"Staff added successfully. Staff ID: {staff_id}")
 

def delete_staff():
    print("\n--------- Delete Staff -------------\n")

    # Read staff data
    staff_list = []
    with open(STAFF_FILE, "r") as f:
        for line in f:
            staff_list.append(line.strip().split(","))

    if not staff_list:
        print("No staff found.")
        return

    # Display Staff List in Table Format
    print("\nCurrent Staff:")
    print(f"{'No.':<5}{'ID':<5}{'Full Name':<20}{'Username':<15}{'Email':<25}{'Role':<10}")
    print("-" * 80)

    for i, staff in enumerate(staff_list):
        if len(staff) >= 6:  # Ensure all fields are present
            print(f"{i + 1:<5}{staff[0]:<5}{staff[1]:<20}{staff[2]:<15}{staff[3]:<25}{staff[5]:<10}")

    try:
        staff_index = int(input("\nEnter the number of the staff to delete: ")) - 1
        if staff_index < 0 or staff_index >= len(staff_list):
            print("Invalid selection.")
            return

        deleted_staff = staff_list.pop(staff_index)  # Remove selected staff

        # Write updated staff list back to file
        with open(STAFF_FILE, "w") as f:
            for staff in staff_list:
                f.write(",".join(staff) + "\n")

        print(f"\nStaff '{deleted_staff[1]}' (ID: {deleted_staff[0]}) deleted successfully.")

    except ValueError:
        print("Invalid input. Please enter a number.")


def view_staff():
    print("\n-----------Staff List:-------\n")
    if not os.path.exists(STAFF_FILE):
        print("No staff found.")
        return
    print(f"{'No.':<5} {'ID':<5} {'Name':<20} {'Username':<15} {'Email':<25} {'Role':<10}")
    print("-" * 80)
    with open(STAFF_FILE, "r") as f:
        for i, line in enumerate(f, start=1):
            staff_data = line.strip().split(",")
            if len(staff_data) == 6:  # Ensure the line has all required fields
                staff_id, name, username, email, password, role = staff_data
                print(f"{i:<5} {staff_id:<5} {name:<20} {username:<15} {email:<25} {role:<10}")

def Update_own_profile():
    if not os.path.exists(LOGIN_USER_DATA):
        print("You are not logged in.")
        return
 
    with open(LOGIN_USER_DATA, "r") as f:
        login_data = f.read().strip().split(",")
        logged_username = login_data[0]
        logged_role = login_data[2]
 
    staff_list = []
    with open(STAFF_FILE, "r") as f:
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
 
    with open(STAFF_FILE, "w") as f:
        for staff in staff_list:
            f.write(f"{staff[0]},{staff[1]},{staff[2]},{staff[3]},{staff[4]},{staff[5]}\n")

    print("\nProfile updated successfully.")


def edit_staff():
    print("\n-------- Edit Staff: --------\n")
    staff_list = []

    with open(STAFF_FILE, "r") as f:
        for line in f:
            staff_list.append(line.strip().split(","))

    if not staff_list:
        print("No staff found.")
        return

    # Display current staff in table format
    print("\n--------- Current Staff: ----------\n")
    print(f"{'No.':<5} {'ID':<5} {'Name':<20} {'Username':<15} {'Email':<25} {'Role':<10}")
    print("-" * 80)
    
    for i, staff in enumerate(staff_list):
        staff_id, name, username, email, password, role = staff
        print(f"{i + 1:<5} {staff_id:<5} {name:<20} {username:<15} {email:<25} {role:<10}")

    try:
        # Ask for the staff member to edit
        staff_index = int(input("\nEnter the number of the staff to edit: ")) - 1
        if staff_index < 0 or staff_index >= len(staff_list):
            print("Invalid selection.")
            return
        # Get the current staff details
        current_staff = staff_list[staff_index]
        staff_id, name, username, email, password, role = current_staff
        # Update name
        is_update_name = input("Do you want to update staff name (y/n): ").strip().lower()
        if is_update_name == "y":
            name = input("Enter new name: ")
        # Update username
        is_update_username = input("Do you want to update username (y/n): ").strip().lower()
        if is_update_username == "y":
            username = input("Enter new username: ")
        is_update_email = input("Do you want to update email (y/n): ").strip().lower()
        if is_update_email == "y":
            email = input("Enter new email: ")
        is_update_password = input("Do you want to update password (y/n): ").strip().lower()
        if is_update_password == "y":
            password = input("Enter new password: ")
        is_update_role = input("Do you want to update role (y/n): ").strip().lower()
        if is_update_role == "y":
            role = input("Enter new role (Manager/Chef): ").capitalize()
        staff_list[staff_index] = [staff_id, name, username, email, password, role]
        with open(STAFF_FILE, "w") as f:
            for staff in staff_list:
                f.write(f"{staff[0]},{staff[1]},{staff[2]},{staff[3]},{staff[4]},{staff[5]}\n")

        print("\nStaff updated successfully.")

    except ValueError:
        print("\nInvalid input. Please enter a number.")

 