from abc import ABC, abstractmethod
from typing import Any

from supplier_class import Supplier


class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, supplier: Supplier) -> None:
        self.__product_id: str = str(product_id)
        self.__name: str = name
        self.__price: float = float(price)
        self.__stock: int = 0
        self.update_stock(stock)
        self.supplier: Supplier = supplier

    @property
    def product_id(self) -> str:
        return self.__product_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def stock(self) -> int:
        return self.__stock

    def update_stock(self, quantity: int) -> None:
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Stock must be a non-negative integer")
        self.__stock = quantity

    def display_information(self) -> None:
        print(f"{self.__product_id:<10}{self.__name:<20}"
              f"${self.__price:<9.2f}{self.__stock:<10}")

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

    @abstractmethod
    def to_dict(self) -> dict[str, Any]:
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict[str, Any]) -> "Product":
        pass