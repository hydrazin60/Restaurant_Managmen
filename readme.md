# Restaurant Management System - Documentation

## Project Overview
The Restaurant Management System is a Python-based application designed to handle various restaurant operations, such as order management, ingredient requests, and user authentication. The project uses text files (.txt) for data storage and retrieval.

# Project Start Instructions

## Steps to Start the Project

1. **Go to the `Restruen_management` Directory**  
   cd path/to/Restruen_management
2. **Enter the command**
   python OurRestaurant.py  //
   python3 OurRestaurant.py   
  ( OurRestaurant is the main file in our project )
2. **Login/Register Page show**
-  **Registration Process
If you’re not registered:
Username: Choose a unique username.
Password: Select a secure password.
Role: Choose one of the following roles:
Administrator
Manager
Chef
Customer
After completing the registration, you will be redirected to the login page**


## Role-Based Login
Staff Login:
If you choose Staff, you will be asked to select your role (Manager, Chef, or Administrator).
Once authenticated, you will be directed to your role-specific dashboard with features relevant to your role.
Customer Login:
If you choose Customer, you will be logged in and redirected to the customer dashboard, where you can place orders, view order status, and provide feedback.

## For Administrator:
Manage staff members (add/edit/delete managers and chefs).
View sales reports.
View customer feedback.
Update own profile.

## For Manager:
Manage customers.
Manage menu categories and pricing.
View orders and update their status.
Request ingredients.
Update own profile.

##  For Chef :
View and manage ingredients.
View and update order status.
Request ingredients.
Update own profil.


## For Customer:
Place and manage orders.
View order status.
Provide feedback to the administrator.
Update own profile.



## Project Structure

### 1. Main Files
- **OurRestaurant.py** → Entry point of the application, managing user authentication and navigation.
- **admin.py** → Handle Admin Functions related Fitures
- **chef.py** → Contains functions related to the chef, such as updating order status and requesting ingredients.
- **manager.py** → Handles manager functionalities, including ingredient approvals.
- **customer.py** → Handle the Customer related fitures ( Place order , View menu , update order , order cancle , give feadback)

### 2. Data Storage Files (.txt)
- **login_data.txt** → Stores user login information in the format:
  ```plaintext
  username, password, role
  ```
- **orders.txt** → Stores customer orders in the format:
  ```plaintext
  customer_name, order_id, item_name, quantity, unit_price, total_price, status
  ```
- **ingredients.txt** → Stores requested ingredients in the format:
  ```plaintext
  ingredient_name, quantity, unit, category
  ```
   **staff.txt** → Stores  staff data in the format:
  ```plaintext
  104,pawan pandey,jiban2060,pandeyjiban2060@gmail.com,password,Admin
  ```
    **users.txt** → Stores   customer data in the format:
  ```plaintext
   106,rich dulal,roch20,richa@gmail.com,password,Customer
  ```
- **requested_ingredients.txt** → Stores chef's requested ingredients before approval.

## 3. Key Features & Functions

### 3.1. User Authentication (OurRestaurant.py)
✅ `get_next_user_id()` → The function checks the logged-in user ID and returns the next ID..  
✅ `register()` → Registers a new user (Chef, Manager, Admin).  
✅ `login()` → Registers a new user (Chef, Manager, Admin). 
✅ `loginCustomer()` → Registers a new user (Customer).   
✅ `logOut()` → Fetches the currently logged-in user.  
✅ `remove_login_data_on_exit()` → WHen user logout or progran not run this time login user data auto delete.  


### 3.2. Admin (admin.py)  

✅ **`admin_menu()`** → Displays admin options to manage staff, sales, feedback, and profile.  
✅ **`manage_staff()`** → Provides options to add, edit, delete, and view staff.  
✅ **`get_next_staff_id()`** → Generates the next available staff ID from the file.  
✅ **`add_staff()`** → Adds a new staff member after checking for duplicate usernames and emails.  
✅ **`delete_staff()`** → Removes a staff member after selecting from the displayed list.  
✅ **`view_staff()`** → Displays all staff details in a formatted table.  
✅ **`Update_own_profile()`** → Allows logged-in users to update their own profile details.  
✅ **`edit_staff()`** → Updates staff details like name, username, email, password, and role.  

### 3.3.  manager (.py)  

✅ **`admin_menu()`** → Displays admin options to manage staff, sales, feedback, and profile.  
✅ **`manage_staff()`** → Provides options to add, edit, delete, and view staff.  
✅ **`get_next_staff_id()`** → Generates the next available staff ID from the file.  
✅ **`add_staff()`** → Adds a new staff member after checking for duplicate usernames and emails.  
✅ **`delete_staff()`** → Removes a staff member after selecting from the displayed list.  
✅ **`view_staff()`** → Displays all staff details in a formatted table.  
✅ **`Update_own_profile()`** → Allows logged-in users to update their own profile details.  
✅ **`edit_staff()`** → Updates staff details like name, username, email, password, and role.  
- **manage_menu()** → Displays and manages the menu options for item upload, edit, delete, and view.
- **get_next_item_id()** → Generates the next unique item ID in the format M1, M2, etc.
- **item_exists(item_name)** → Checks if an item with the given name already exists in the menu.
- **add_item()** → Adds a new item to the menu with validation and a unique ID.
- **edit_item()** → Edits an existing menu item's details.
- **delete_item()** → Deletes an item from the menu.
- **view_menu()** → Displays the menu in a formatted table.

### 2. Ingredients Management Functions
- **manage_ingredients()** → Manages ingredient-related operations like view, upload, delete, and update.
- **get_next_ingredient_id()** → Generates the next unique ingredient ID (I1, I2, etc.).
- **upload_ingredients()** → Uploads a new ingredient with a unique ID and validation.
- **view_ingredients()** → Displays all ingredients in a table format.
- **update_ingredient()** → Updates an ingredient's details after displaying them in a table.
- **delete_ingredient()** → Deletes an ingredient from the list after confirmation.

### 3. Profile Management Functions
- **Update_own_profile()** → Allows staff to update their own profile details (name, username, email, password, role).
- **validate_email(email)** → Validates if the email is in the correct format.
- **validate_password(password)** → Ensures the password is at least 6 characters long.
- **validate_username(username, staff_list)** → Ensures the new username is unique.

### 4. Utility Functions
- **logOut()** → Logs out the user by deleting login data and returning to the main menu.

### 5. Main Files
- **OurRestaurant.py** → Entry point of the application, managing user authentication and navigation.




### 3.3. Customer  (customer.py)  

✅ **`customer_menu()`** → Displays customer options to view menu, place orders, send feedback, and update profile.  
✅ **`view_menu()`** → Displays the restaurant menu in a formatted table.  
✅ **`order()`** → Provides options to place, update, cancel, or view orders.  
✅ **`place_order()`** → Allows customers to place orders by selecting items from the menu.  
✅ **`get_customer_name_and_role()`** → Retrieves the logged-in customer's name and role.  
✅ **`order_cancel()`** → Cancels a pending order after confirmation.  
✅ **`View_All_Orders()`** → Displays all orders for the logged-in customer with a total price.  
✅ **`get_logged_in_user()`** → Retrieves the username of the currently logged-in user.  
✅ **`update_order()`** → Allows customers to update the quantity or category of their orders.  
✅ **`send_feedback()`** → Enables customers to send feedback, which is saved with their username and role.  
✅ **`validate_username()`** → Checks if a username is already taken.  
✅ **`validate_email()`** → Validates the format of an email address.  
✅ **`validate_password()`** → Ensures the password is at least 6 characters long.  
✅ **`Update_own_profile()`** → Allows customers to update their profile details (name, username, email, password).  
✅ **`logOut()`** → Logs out the user by removing login data and redirects to the main menu.  


**How It Works:**
- Users log in using their credentials.
- Their role is verified before accessing different functionalities.
 



**How It Works:**
- Orders are stored in `orders.txt`.
- Orders can only be updated if their status is Pending.
- Orders are displayed in a structured table format.

**Example order stored in `orders.txt`:**
```plaintext
Jiban pandey, 101, Pasta, 2, 10, 20, Pending
sital , 102, Pizza, 1, 15, 15, Completed
```

### 3.3. Chef Functions (chef.py)
✅ `update_order_status()`
- Displays all pending orders in a table format.
- Allows the chef to select an order and update its status.

✅ `request_ingredients()`
- Chef requests ingredients by specifying:
  - Ingredient name
  - Quantity
  - Unit (kg, liters, etc.)
  - Category (Vegetables, Meat, etc.)
- Requests are stored in `requested_ingredients.txt`.

**Example format:**
```plaintext
Tomatoes, 5, kg, Vegetables
Chicken, 2, kg, Meat
```

### 3.4. Manager Functions (manager.py)
✅ `view_all_ingredients()`
- Displays all requested ingredients in a table format.
- Allows the manager to approve or reject ingredient requests.

✅ `approve_ingredient_request()`
- If approved, the ingredient moves from `requested_ingredients.txt` to `ingredients.txt`.

### 3.5. Ingredient Management (ingredients.py)
✅ `view_available_ingredients()` → Displays all approved ingredients.  
✅ `add_ingredient()` → Manually adds an ingredient to `ingredients.txt`.  
✅ `remove_ingredient()` → Deletes an ingredient from the inventory.  

## 4. How Data is Stored and Retrieved

### Orders Example (`orders.txt`)
| Customer   | Order ID | Item   | Quantity | Unit Price | Total Price | Status  |
|------------|---------|--------|----------|------------|-------------|---------|
|   Jiban    | 101     | Pasta  | 2        | 10         | 20          | Pending |
|  sital     | 102     | Burger | 1        | 12         | 12          | Completed |

### Ingredient Requests Example (`requested_ingredients.txt`)
| Ingredient | Quantity | Unit | Category    |
|------------|----------|------|------------|
| Tomatoes  | 5        | kg   | Vegetables  |
| Chicken   | 2        | kg   | Meat        |

### Approved Ingredients Example (`ingredients.txt`)
| Ingredient | Quantity | Unit  | Category  |
|------------|----------|------|-----------|
| Flour     | 10       | kg   | Baking    |
| Milk      | 5        | liters | Dairy    |

## 5. User Roles and Permissions

| Role     | Can Place Orders | Can Update Orders | Can Request Ingredients | Can Approve Ingredients |
|----------|----------------|-----------------|----------------------|----------------------|
| Customer | ✅            | ❌             | ❌                   | ❌                   |
| Chef     | ❌            | ✅ (Only Pending) | ✅                   | ❌                   |
| Manager  | ❌            | ❌             | ✅ (Approve Only)     | ✅                   |

## 6. Project Flow
1️⃣ **Login/Register** → User selects their role (Chef, Manager, etc.).  
2️⃣ **Chef Operations** → Chef can update pending orders and request ingredients.  
3️⃣ **Manager Operations** → Manager can approve ingredient requests.  
4️⃣ **Order Status Updates** → Orders move from Pending → Completed or Cancelled.  
5️⃣ **Ingredient Management** → Only approved ingredients are stored for use.  

## 7. Future Enhancements
🔹 Implement a database (SQLite, MySQL) instead of text files.  
🔹 Add a GUI using Tkinter or PyQt for better usability.  
🔹 Implement a notification system for order and ingredient status updates.  

## Conclusion
This Restaurant Management System provides a basic yet effective way to manage orders, ingredients, and user roles in a restaurant environment. It uses Python and text files for data storage, making it easy to use and modify. 🚀
