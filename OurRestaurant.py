import os
import atexit
 
DATA_DIRECTORY = "./database"
Cookies_FILE = "./cookies"
USER_FILE = os.path.join(DATA_DIRECTORY, "users_data.txt")
STAFF_FILE = os.path.join(DATA_DIRECTORY,  "staff_data.txt")
LOGIN_USER_DATA = os.path.join(Cookies_FILE, "login_User_data.txt")

def initialize_files():
    if not os.path.exists(DATA_DIRECTORY):
        os.makedirs(DATA_DIRECTORY)
    if not os.path.exists(STAFF_FILE):
        with open(STAFF_FILE, "w") as f:
            f.write("1,admin,admin123,Admin\n")   
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as f:
            f.write("")  

def get_next_user_id(file_path):
    if not os.path.exists(file_path):
        return 100   
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]   # list comprehension
    if not lines:
        return 100   
    last_line = lines[-1]  
    last_id_str = last_line.split(",")[0].strip()  
    if not last_id_str.isdigit():   
        return 100   
    return int(last_id_str) + 1  

def register():
    print("\n------------------------------- Registration form -------------------------------------\n")
    full_name = input("Enter your Full Name: ")
    username = input("Enter a username: ")
    email = input("Enter your email: ")

    # Check in staff file
    if os.path.exists(STAFF_FILE):
        with open(STAFF_FILE, "r") as f:
            for line in f:
                existing_data = line.strip().split(",")
                if len(existing_data) < 4:  # Ensure the line has enough values
                    continue
                existing_username = existing_data[2]   
                existing_email = existing_data[3]  
                if existing_username == username or existing_email == email:
                    print("Username or email already exists. Please use a different username or email.")
                    return

    # Check in user file
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            for line in f:
                existing_data = line.strip().split(",")
                if len(existing_data) < 3:  # Ensure the line has enough values
                    continue
                existing_username = existing_data[1]   
                existing_email = existing_data[2]   
                if existing_username == username or existing_email == email:
                    print("Username or email already exists. Please use a different username or email.")
                    return

    password = input("Enter a password: ")
    role = input("Enter your role (Admin/Manager/Chef/Customer): ").capitalize()
    
    if role in ["Admin", "Manager", "Chef"]:
        user_id = get_next_user_id(STAFF_FILE)
        with open(STAFF_FILE, "a") as f:
            f.write(f"{user_id},{full_name},{username},{email},{password},{role}\n")
    else:
        user_id = get_next_user_id(USER_FILE)
        with open(USER_FILE, "a") as f:
            f.write(f"{user_id},{full_name},{username},{email},{password},{role}\n")

    print(f"Registration successful! Your unique ID is {user_id}. You can now log in.")  

def login():
    login_attempts = 3
    while login_attempts > 0:
        print("\n-------- Staff Login --------\n")
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        if not os.path.exists(STAFF_FILE):
            print("No staff records found. Please register first.")
            return None

        with open(STAFF_FILE, "r") as f:
            for line in f:
                user_data = line.strip().split(",")
                if len(user_data) >= 6:
                    stored_username = user_data[2]  # Username
                    stored_password = user_data[4]  # Password
                    role = user_data[5]  # Role

                    if stored_username == username and stored_password == password:
                        print(f"Login successful! Role: {role}")
                        # Save login data
                        with open(LOGIN_USER_DATA, "w") as f:
                            f.write(f"{username},{password},{role}")
                        return role  
        
        login_attempts -= 1
        print(f"Invalid username or password. You have {login_attempts} attempts remaining.")

    print("Maximum login attempts reached. Please try again later.")
    return None

def loginCustomer():
    login_attempts = 3
    
    while login_attempts > 0:
        print("\n--------  Customer Login --------\n")
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        
        if not os.path.exists(USER_FILE):  
            print("No customer records found. Please register first.")
            return None

        with open(USER_FILE, "r") as f:
            for line in f:
                user_data = line.strip().split(",")
                if len(user_data) >= 6:
                    stored_username = user_data[2].strip()  # Username
                    stored_password = user_data[4].strip()  # Password
                    role = user_data[5].strip()  # Role
                    if stored_username == username and stored_password == password:
                        print(f"Login successful! Role: {role}")
                        with open(LOGIN_USER_DATA, "w") as f:
                            f.write(f"{username},{password},{role}")
                        
                        return role  

        login_attempts -= 1
        print(f"Invalid username or password. You have {login_attempts} attempts remaining.")

    print("Maximum login attempts reached. Please try again later.")
    return None


def logOut():
    if os.path.exists(LOGIN_USER_DATA):
        os.remove(LOGIN_USER_DATA)
        print("Logged out successfully.")
    else:
        print("You are not logged in.")   
 
def remove_login_data_on_exit():
    if os.path.exists(LOGIN_USER_DATA):
        os.remove(LOGIN_USER_DATA)
        print("Login data removed upon program exit.")
 
atexit.register(remove_login_data_on_exit)

def main():
    initialize_files() 
    while True:
        print("\n------------ Welcome to Delicious Restaurant ------------------- \n")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            register()
        elif choice == "2": 
            user_type = input("Are you a staff or customer? (Enter 'staff' or 'customer'): ").strip().lower()
            if user_type == "staff":
                role = login()  
                if role:
                    if role == "Admin":
                        import admin
                        admin.admin_menu()
                    elif role == "Manager":
                        from manager import manager_menu
                        manager_menu()
                    elif role == "Chef":
                        import chef
                        chef.chef_menu()
                    else:
                        print("Invalid role. Please try again.")
            elif user_type == "customer":
                role = loginCustomer()   
                if role == "Customer":
                    import customer
                    customer.customer_menu()
                else:
                    print("Invalid role. Please try again.")
            else:
                print("Invalid input. Please enter 'staff' or 'customer'.")
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  

 