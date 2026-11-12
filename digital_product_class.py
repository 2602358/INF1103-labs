from typing import Any

from product_class import Product
from supplier_class import Supplier


class Digital_product(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 size: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__size: float = float(size)

    @property
    def size(self) -> float:
        return self.__size

    def display_information(self) -> None:
        print(f"{self.product_id:<10}{self.name:<20}"
              f"${self.price:<9.2f}{self.stock:<10}{self.size:<10}")

    def get_fulfilment_info(self) -> None:
        print(f"{self.name} is a digital product. No shipping is needed; "
              f"it is delivered electronically ({self.size} GB download).")

    def to_dict(self) -> dict[str, Any]:
        return {"type": "digital", "id": self.product_id, "name": self.name,
                "price": self.price, "stock": self.stock, "size": self.size,
                "supplier": self.supplier.to_dict()}

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Digital_product":
        return cls(data["id"], data["name"], data.get("price", 0.0), data["stock"],
                   data["size"], Supplier.from_dict(data["supplier"]))