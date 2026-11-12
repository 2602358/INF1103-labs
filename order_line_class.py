from product_class import Product


class OrderLine:
    def __init__(self, product: Product, quantity: int):
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self):
        return self.product.price * self.quantity

    def display_information(self) -> None:
        print(f"{self.product.product_id:<10}{self.product.name:<20}"
              f"{self.quantity:<10}${self.product.price:<9.2f}"
              f"${self.calculate_subtotal():<10.2f}")