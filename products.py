class Product:
    """
    Represents a specific type of product available in the store.
    It encapsulates information about the product, including its name, price, and quantity.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initiator (constructor) method.
        Creates the instance variables (active is set to True).
        If something is invalid (empty name / negative price or quantity), raises an exception.
        """
        # Ensure name is a non-empty string.
        if not isinstance(name, str) or not name:
            raise TypeError('Name must be a non-empty string')

        # Ensure price is a non-negative number.
        if not isinstance(price, (int, float)) or price < 0:
            raise TypeError('Invalid price: a non-negative number is expected.')

        # Ensure quantity is a non-negative integer.
        if not isinstance(quantity, int) or quantity < 0:
            raise TypeError('Invalid quantity: a non-negative number is expected')

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """
        Getter function for quantity. Returns the quantity (int).
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Setter function for quantity. If quantity reaches 0, deactivates the product.
        """
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Getter function for active. Returns True if the product is active, otherwise False.
        """
        return self.active

    def activate(self):
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False

    def show(self):
        """
        Prints a string that represents the product.
        """
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        Raises an Exception in case of a problem.
        """
        # Check if the product is currently active.
        if not self.active:
            raise Exception(
                "This product is currently unavailable for purchase.")

        # Ensure a valid quantity is provided.
        if not isinstance(quantity, int) or quantity <= 0:
            raise TypeError(
                "Please ensure you've entered a valid quantity for your purchase.")

        # Check if there is enough stock.
        if quantity > self.quantity:
            raise ValueError("Insufficient quantity in stock.")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)

        return total_price

def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()
if __name__ == '__main__':
    main()