#MUDIT BHALLA
#VBMS SOFTWARE - ONLINE STORE MANAGEMNT
#YEARLONG PROJECT


import pickle

# Global variables
I = []  # List to store product information
L = []  # List to store employee IDs
CNT = 0  # Counter for added products

currency_symbols = {
    '1': '₹',  # Indian Rupee
    '2': '$',  # US Dollar
    '3': '€',  # Euro
    '4': 'د.إ'  # UAE Dirham
}

def welcome_function():
    """Welcome function to record employee ID."""
    print("\nWelcome to Virtual Bazaar Management Software (VBMS)\n")
    emp_ID = int(input("Please enter your 6-Digit numeric Employee ID: "))
    L.append(emp_ID)
    with open("punch_in.dat", 'wb') as f:
        pickle.dump(L, f)

def add_product():
    """Function to add a product to the inventory."""
    global CNT
    CNT += 1
    print("\nOh JOLLY! Here to add another product!\nPlease fill in the details below:")
    product_id = int(input("Enter Product ID: "))
    product_name = input("Enter Product Name: ")
    
    # Get currency choice
    print("\nSelect the currency for the product price:")
    print("1) Indian Rupee (₹)")
    print("2) US Dollar ($)")
    print("3) Euro (€)")
    print("4) UAE Dirham (د.إ)")
    currency_choice = input("Enter the number corresponding to the currency: ").strip()
    currency_symbol = currency_symbols.get(currency_choice, '$')  # Default to US Dollar if invalid choice
    
    product_price = float(input(f"Enter Product Price ({currency_symbol}): "))
    product_quantity = int(input("Enter Product Quantity: "))
    
    product_record = {
        "product_id": product_id,
        "product_name": product_name,
        "price": product_price,
        "currency": currency_symbol,
        "quantity": product_quantity
    }
    I.append(product_record)

    with open("inventory.dat", "wb") as f:  # Open in binary write mode
        pickle.dump(I, f)
    print("\nProduct added successfully!\n")

def update_product():
    """Function to update a product in the inventory."""
    name = input("Enter the name of the product you want to update: ")
    found = False

    for product in I:
        if product['product_name'].lower() == name.lower():
            found = True
            print("\nProduct Found!")
            
            # Ask how many attributes the user wants to change
            num_attributes = int(input("How many attributes of the product would you like to change? (1-4): "))
            
            for _ in range(num_attributes):
                print("\nWhich attribute would you like to update?")
                print("1) Product ID")
                print("2) Product Name")
                print("3) Product Price")
                print("4) Product Quantity")
                
                attribute_choice = input("Enter the number corresponding to the attribute: ").strip()

                # Update based on the choice
                if attribute_choice == '1':
                    product['product_id'] = int(input("Enter the new Product ID: "))
                    print("Product ID updated!\n")
                elif attribute_choice == '2':
                    product['product_name'] = input("Enter the new Product Name: ")
                    print("Product Name updated!\n")
                elif attribute_choice == '3':
                    # Get new currency choice
                    print("\nSelect the new currency for the product price:")
                    print("1) Indian Rupee (₹)")
                    print("2) US Dollar ($)")
                    print("3) Euro (€)")
                    print("4) UAE Dirham (د.إ)")
                    currency_choice = input("Enter the number corresponding to the currency: ").strip()
                    product['currency'] = currency_symbols.get(currency_choice, product['currency'])
                    product['price'] = float(input(f"Enter the new Product Price ({product['currency']}): "))
                    print("Product Price updated!\n")
                elif attribute_choice == '4':
                    product['quantity'] = int(input("Enter the new Product Quantity: "))
                    print("Product Quantity updated!\n")
                else:
                    print("Invalid choice. Please try again.")

            print("Your record has been updated successfully!\n")
            break
    
    if not found:
        print("Product not found in the inventory.\n")

def display_selective_record():
    """Function to display a selective product from the inventory."""
    sr = input("\nPlease enter the product name you would like to search for: ").lower()
    found = False
    for product in I:
        if sr in product['product_name'].lower():
            print("\nProduct Found!")
            print(f"{'Product ID:':<20} {product['product_id']}")
            print(f"{'Product Name:':<20} {product['product_name']}")
            print(f"{'Product Price:':<20} {product['currency']}{product['price']:.2f}")
            print(f"{'Product Quantity:':<20} {product['quantity']}")
            print("-" * 40)
            found = True
            break
    if not found:
        print("No matching product found.\n")

def display_complete_record():
    """Function to display the complete inventory."""
    if not I:
        print("No products in the inventory.\n")
    else:
        print("\nComplete Inventory:")
        print("-" * 40)
        for idx, product in enumerate(I, 1):
            print(f"PRODUCT NUMBER {idx}")
            print(f"{'Product ID:':<20} {product['product_id']}")
            print(f"{'Product Name:':<20} {product['product_name']}")
            print(f"{'Product Price:':<20} {product['currency']}{product['price']:.2f}")
            print(f"{'Product Quantity:':<20} {product['quantity']}")
            print("-" * 40)
        print("\n")

def delete_product():
    """Function to delete a product selectively or completely."""
    print("\nWould you like to delete a selective product or the complete inventory?")
    print("1) Selective Deletion")
    print("2) Complete Deletion")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        # Selective Deletion
        product_id = int(input("Enter the Product ID of the item you want to delete: "))
        found = False
        
        for product in I:
            if product['product_id'] == product_id:
                I.remove(product)
                found = True
                print("Product deleted successfully!\n")
                break
        
        if not found:
            print("Product with the given ID not found.\n")
        
        # Save updated list to the file
        with open("inventory.dat", "wb") as f:
            pickle.dump(I, f)

    elif choice == '2':
        # Complete Deletion
        confirm = input("Are you sure you want to delete the entire inventory? (yes/no): ").strip().lower()
        if confirm == 'yes':
            I.clear()  # Clear the entire inventory list
            with open("inventory.dat", "wb") as f:
                pickle.dump(I, f)  # Save the cleared list to the file
            print("All products have been deleted from the inventory.\n")
        else:
            print("Complete deletion canceled.\n")
    else:
        print("Invalid choice. Please try again.\n")

def exit_program():
    """Function to exit the program."""
    print("\nBYE\nSee You Soon!")
    return CNT

def menudriven():
    """Main menu-driven function."""
    global CNT
    while True:
        print('''\n1) Add Product
2) Update Product
3) Display Selective Record
4) Display Complete Record
5) Delete Product
6) Exit''')
        
        choice = input("Enter your choice from the above: ").strip().lower()

        if choice == '1' or "add" in choice:
            add_product()
        elif choice == '2' or "update" in choice:
            update_product()
        elif choice == '3' or "selective" in choice:
            display_selective_record()
        elif choice == '4' or "complete" in choice:
            display_complete_record()
        elif choice == '5' or "delete" in choice:
            delete_product()
        elif choice == '6' or "exit" in choice:
            return exit_program()
        else:
            print("Invalid choice, please try again.\n")

# Running the program
welcome_function()
CNT1 = menudriven()
print(f"\nYou added {CNT1} products today.")

