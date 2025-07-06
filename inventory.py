# Step 1: Initialize inventory
inventory = {}

num_items = int(input("How many different products to start with? "))

for i in range(num_items):
    product = input(f"Enter name of product {i+1}: ")
    quantity = int(input(f"Enter quantity for {product}: "))
    inventory[product] = quantity

# Step 2: Menu loop to manage inventory
while True:
    print("\nChoose an option:")
    print("1. View Inventory")
    print("2. Add Stock")
    print("3. Remove Stock")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("\nCurrent Inventory:")
        for product, qty in inventory.items():
            print(f"{product}: {qty}")

    elif choice == "2":
        product = input("Enter product name to add: ")
        quantity = int(input("Enter quantity to add: "))
        if product in inventory:
            inventory[product] += quantity
        else:
            inventory[product] = quantity
        print(f"Added {quantity} to {product}")

    elif choice == "3":
        product = input("Enter product name to remove: ")
        if product in inventory:
            quantity = int(input("Enter quantity to remove: "))
            if quantity <= inventory[product]:
                inventory[product] -= quantity
                print(f"Removed {quantity} from {product}")
            else:
                print(f"Not enough stock to remove {quantity}. Only {inventory[product]} available.")
        else:
            print("Product not found in inventory.")

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")