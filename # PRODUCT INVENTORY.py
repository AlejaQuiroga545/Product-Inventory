# PRODUCT INVENTORY
# GitHUb | https://github.com/AlejaQuiroga545/Product-Inventory

# Let's create our inventory with 5 products already defined
inventory = {
    "apple": {"Price": 1300, "Available_quantity": 5},
    "bananas": {"Price": 6000, "Available_quantity": 4},
    "potato": {"Price": 3500, "Available_quantity": 10},
    "water": {"Price": 15000, "Available_quantity": 15},
    "spaguetti": {"Price": 6000, "Available_quantity": 3}
}



# 1. Add products

def add_products(inventory):
    name = input("Name: ").lower()

    while True:  # Let's create a loop to ensure a valid price
        price_str = input("Price: ")
        try:
            price = float(price_str.replace(".", ""))  # Allows periods as separators and removes them for floats
            if price > 0:
                break  # We exit the loop if the price is valid
            else:
                print("\nOops, the price must be a valid number")
        except ValueError:
            print("\nPlease enter a valid number for the price.")

    while True:  # Let's create another loop to ensure a valid quantity
        try:
            quantity = int(input("Available quantity: "))
            if quantity >= 0:
                break
            else:
                print("Oops, the quantity must be a valid number")
        except ValueError:
            print("Please enter a valid number")

    inventory[name] = {"Price": price, "Available_quantity": quantity}  # Let's add the product to our dictionary
    print(f"\nYour product {name.capitalize()} has been added successfully. 🥳")



# 2. Search products

def search_products(inventory, name):
    if name in inventory: # Verify if the name of the product exist in the inventory
        product = inventory[name]  # Search the inventory dictionary for the name and the values ​​associated with it, and save them in the variable
        price = product["Price"]
        quantity = product["Available_quantity"]

        print(f"\n⚜️  Product: {name.capitalize()}") # Show us the information of the product
        print(f"Price: {price:,}")
        print(f"Available quantity: {quantity}")
    else:
        print(f"\nOops, the product {name} is not in your inventory. 👀")



# 3. Update prices

def update_prices(inventory, name):
    if name not in inventory: # Verify if the name of the product exist in the inventory
        print(f"\nOops, the product {name} is not in your inventory. 👀")
        return

    last_price = inventory[name]["Price"] # We create some variables that show us both the price and the current quantity in the inventory.
    last_quantity = inventory[name]["Available_quantity"]

    print(f"\n⏪ Last price of {name}: {last_price}")

    while True: # We create a loop to ensure a new valid price
        new_price_str = input("\n⏩ Enter the new price: ")
        try:
            new_price = float(new_price_str.replace(".", "")) # Allows periods as separators and removes them for floats
            if new_price > 0:
                break # We exit the loop if the price is valid
            else:
                print("Oops 🫢... You must enter a valid price.")
        except ValueError:
            print("Please enter a valid number for the price.")

    inventory[name]["Price"] = new_price # We update that specific value
    print(f"\n〽️  The new price for {name} is ${new_price:,}.")



# 4. Remove products for the inventory

def remove_products(inventory, name):
    if name in inventory: # If the product name is in the inventory, we remove all values ​​associated with it
        del inventory[name]
        print(f"\nThe product {name} has been successfully removed from your inventory. ✅")
    else:
        print(f"The product {name} is not in your inventory. 👀")



# 5. Calculate the total value of the inventory

def total_inventory(inventory):
    
    total_value = 0 # We start the count at 0
    for values_p in inventory.values(): # I only take these specific values ​​from my dictionary
        price = values_p["Price"]
        quantity = values_p["Available_quantity"]
        total_value += price * quantity # These values ​​are multiplied for each product, and then their results are added
        
    print(f"\n〽️ The total value of your inventory is {total_value:,.2f}")



# Let's create the menu

def menu():
    
    print("\nHi coder, welcome to your Product Inventory! 🚀. What do you want to do?")

    while True: # Main menu loop
        print("-" * 20)
        print("1. Add products")
        print("2. Search products")
        print("3. Update prices")
        print("4. Remove products from inventory")
        print("5. Total inventory value")
        print("6. Leave the system")

        op_str = input("\n✳️  Choose a option (1-6): ")

        if not op_str.isdigit(): # We check if the input is a number (.isdigit() is used to check if all characters within a string are digits (0-6)
            print("\nOops, you must enter a number between 1 and 6 🫢. Please try again.")
            continue # We return to the beginning of the loop

        op = int(op_str) # We convert the input to an integer

        if op == 1: # Add product
            print("\nAdd the new product ⚜️\n")
            add_products(inventory)

        elif op == 2: # Search product
            if not inventory: # We check if the inventory is empty
                print("\nThere are no products in your inventory ✳️")
                continue # We return to the beginning of the loop

            print("\nAvailable products 📌\n")
            for name in inventory:
                print(f"✅  {name.capitalize()}")

            search = input("\nProduct that you want to search 🔎 ").lower().strip()
            search_products(inventory, search)

        elif op == 3: # Update prices
            if not inventory: # We check if the inventory is empty
                print("\nThere are no products in your inventory. ✳️")
                continue # We return to the beginning of the loop

            print("\nAvailable products 📌\n")
            for name in inventory:
                print(f"✅  {name.capitalize()}")

            name_to_update = input("\nName of the product that you want to update its price 💱 ").lower()
            update_prices(inventory, name_to_update)

        elif op == 4: # Remove products
            if not inventory: # We check if the inventory is empty
                print("\nThere are no products in your inventory to remove. ✳️")
                continue # We return to the beginning of the loop

            print("\nAvailable products 📌\n")
            for name in inventory:
                print(f"✅  {name.capitalize()}")

            name_to_remove = input("\n🗑️  Name of the product that you want to remove: ").lower()
            remove_products(inventory, name_to_remove)

        elif op == 5: # Total value
            total_inventory(inventory)

        elif op == 6: # Exit option
            print("See you soon coder! 🚀")
            break # We exit the main loop

        else: # Invalid option
            print("Oops, you must enter a number between 1 and 6 🫢. Please try again.")

# Run the main menu
menu()