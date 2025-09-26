import products
import store

product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
]

best_buy = store.Store(product_list)


def handle_list_products(catalogue):
    """Shows all active products in the store's catalogue."""
    print("------")
    for i, product in enumerate(catalogue.get_all_products(), 1):
        print(f"{i}. ", end="")
        product.show()
    print("------")


def handle_show_total(catalogue):
    """Shows the total quantity of all items in the store's inventory."""
    print(f"Total of {catalogue.get_total_quantity()} items in store")


def handle_make_order(catalogue):
    """Handles the user input and logic for placing an order."""
    shopping_list = []
    all_products = catalogue.get_all_products()

    print("------")
    for i, product in enumerate(all_products, 1):
        print(f"{i}. ", end="")
        product.show()
    print("------")
    print("When you want to finish your order, enter empty text.")

    while True:
        product_num_str = input(
            "Enter the product number you want to order: ").strip()
        if not product_num_str:
            break

        if not product_num_str.isdigit():
            print("Error: The product number must be a digit!")
            continue

        product_index = int(product_num_str)
        if product_index < 1 or product_index > len(all_products):
            print("Error: Invalid product number.")
            continue

        quantity_str = input("Enter the quantity you want to order: ").strip()
        if not quantity_str.isdigit():
            print("Error: Please specify the quantity using numbers.")
            continue

        quantity = int(quantity_str)
        product_to_order = all_products[product_index - 1]

        if quantity <= 0 or quantity > product_to_order.get_quantity():
            print("Error: The amount requested is not available.")
            continue

        shopping_list.append((product_to_order, quantity))
        print("Product added to list!")

    if shopping_list:
        try:
            total_price = catalogue.order(shopping_list)

            # Simplified and clean output
            print("\n--- ✅ Order Successfully Processed ---")
            print("Your order includes:")

            for product, amount in shopping_list:
                print(
                    f"  - {product.name} (Qty: {amount}) @ ${product.price} each. Item Total: ${product.price * amount}"
                )

            print(f"\nTotal Price for the entire order: ${total_price}")
            print("--------------------------------------")

        except ValueError as error:
            print(f"Failed to process the order. Reason: {error}")
    else:
        print("No products selected.")


def start(catalogue):
    """Starts the interactive store menu."""
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ").strip()

        if choice == "1":
            handle_list_products(catalogue)
        elif choice == "2":
            handle_show_total(catalogue)
        elif choice == "3":
            handle_make_order(catalogue)
        elif choice == "4":
            print("Thank you for visiting! Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    start(best_buy)
