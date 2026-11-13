from product_class import Product
from physical_product_class import Physical_product
from digital_product_class import Digital_product
from supplier_class import Supplier


class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float, stock: int, weight_or_size: float, supplier: Supplier) -> Product:
        if product_type == "physical":
            return Physical_product(product_id, name, price, stock, weight_or_size, supplier)
        elif product_type == "digital":
            return Digital_product(product_id, name, price, stock, weight_or_size, supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type}")
