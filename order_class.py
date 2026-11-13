from discount_strategy import DiscountStrategy, NoDiscount
from order_line_class import OrderLine
from product_class import Product


class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
        self.discount: DiscountStrategy = discount if discount is not None else NoDiscount()

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        self.order_lines.append(OrderLine(product, quantity))

    def remove_order_line(self, product_id: str) -> bool:
        for order_line in self.order_lines:
            if order_line.product.product_id.lower() == str(product_id).strip().lower():
                self.order_lines.remove(order_line)
                return True
        return False

    def calculate_total(self) -> float:
        total = sum(line.calculate_subtotal() for line in self.order_lines)
        return self.discount.apply(total)

    def display_order(self) -> None:
        print(f"\nOrder {self.order_id}")
        print(f"{'ID':<10}{'Name':<20}{'Qty':<10}{'Price':<10}{'Subtotal':<10}")
        print("-" * 60)
        for order_line in self.order_lines:
            order_line.display_information()
        print("-" * 60)
        print(f"{'Total:':<50}${self.calculate_total():.2f}")