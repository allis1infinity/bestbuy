import products


class Store:
    """The Store class manages products and handles orders."""

    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        """Adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all items in the store."""
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self) -> list:
        """Returns a list of all active products."""
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list) -> float:
        """Processes an order and returns the total price."""
        total_price = 0.0
        for product, quantity in shopping_list:
            if product.get_quantity() < quantity:
                raise ValueError(
                    f"Not enough quantity of {product.name} available.")

            product.set_quantity(product.get_quantity() - quantity)
            total_price += product.price * quantity

        return total_price


if __name__ == '__main__':
    # Test code from the specification
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    all_products = best_buy.get_all_products()

    print(best_buy.get_total_quantity())
    print(best_buy.order([(all_products[0], 1), (all_products[1], 2)]))
