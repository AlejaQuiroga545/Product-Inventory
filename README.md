# Product Inventory 🛒

Hello everyone, welcome to the system I have created to manage the inventory of a store in a dynamic way. ☺️

The objective of our program is to efficiently track available products, their quantity and updated prices, as well as calculate the total inventory value.
Ideal for practicing functions and collections in Python such as:


- Lists
- Tuples
- Dictionaries

## 📦 What does the system do?

<b>✅ 1. Add products to the inventory  |</b> As program administrators, we have previously added 5 products to the inventory, and also allows the user to add products with attributes such as name, price and quantity available.

<b>✅ 2. Browse products in stock  |</b> Allows us to search for a product by its name and show your details (name, price, quantity).

<b>✅ 3. Update product prices  |</b> Allows us to change the price of a specific product in the inventory.

<b>✅ 4. Remove products from the inventory  |</b> Allow the removal of a product that is no longer available. 

<b>✅ 5. Calculate the total value of the inventory  |</b> It allows us to know the value of our inventory by multiplying the price by the quantity of each product and show the cumulative total.

---
## ⚡ Input and output data

Our input data will be captured through the menu, and will be executed as output data thanks to the functions we have previously created and assigned.

For example, in our function to <b>SEARCH FOR PRODUCTS</b> we have first shown the user what are in our inventory, once seen, the user will decide which one he wants to search (entering his name in the console trough the menu) . The program will bring all the information that this product contains and show it to you in the console.

```python
# 2. FUNCTION | Search products

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

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# Option in menu
elif op == 2: # Search product
            if not inventory: # We check if the inventory is empty
                print("\nThere are no products in your inventory ✳️")
                continue # We return to the beginning of the loop

            print("\nAvailable products 📌\n")
            for name in inventory:
                print(f"✅  {name.capitalize()}")

            search = input("\nProduct that you want to search 🔎 ").lower().strip()
            search_products(inventory, search)
```
This is only a very, very small part of the exercise but you can get an idea of how our program works. So below I leave you the complete exercise for you to run it

## ▶️ Result
- Run it in [Google Colab](https://colab.research.google.com/drive/1gqbJksszqpIho_iXozcnBCSsaBOcnsC4?usp=sharing)
