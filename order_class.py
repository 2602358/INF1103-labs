from order_line_class import OrderLine
from product_class import Product


class Order:
    def __init__(self, order_id: str) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> bool:
        for order_line in self.order_lines:
            if order_line.product.product_id.lower() == str(product_id).strip().lower():
                self.order_lines.remove(order_line)
                return True
        return False

    def calculate_total(self) -> float:
        return sum(line.calculate_subtotal() for line in self.order_lines)

    def display_order(self) -> None:
        print(f"\nOrder {self.order_id}")
        print(f"{'ID':<10}{'Name':<20}{'Qty':<10}{'Price':<10}{'Subtotal':<10}")
        print("-" * 60)
        for order_line in self.order_lines:
            order_line.display_information()
        print("-" * 60)
        print(f"{'Total:':<50}${self.calculate_total():.2f}")