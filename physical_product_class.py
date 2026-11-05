from product_class import Product
from canbeshipped import CanBeShipped

class Physical_product(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = float(weight)

    @property
    def weight(self):
        return self.__weight

    def display_information(self):
        print(f"{self.product_id:<10}{self.name:<20}"
          f"${self.price:<9.2f}{self.stock:<10}{self.weight:<10}")

    def calculate_shipping_cost(self) -> float:
        return self.weight * 3
    
    def get_fulfilment_info(self):
        print (f"{self.name} is a physical product. It requires shipping "
                f"({self.weight} kg) and will be dispatched from the warehouse."
                f"(The shipping will cost ${self.calculate_shipping_cost():.2f})")
    
    def to_dict(self):
        return {"type": "physical", "id": self.product_id, "name": self.name,
                "price": self.price, "stock": self.stock, "weight": self.weight}

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["name"], data.get("price", 0.0), data["stock"], data["weight"])