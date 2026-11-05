from product_class import Product

class Digital_product(Product):
    def __init__(self, product_id, name, price, stock, size):
        super().__init__(product_id, name, price, stock)
        self.__size = float(size)

    @property
    def size(self):
        return self.__size

    def display_information(self):
        print(f"{self.product_id:<10}{self.name:<20}"
          f"${self.price:<9.2f}{self.stock:<10}{self.size:<10}")

    def get_fulfilment_info(self):
        print (f"{self.name} is a digital product. No shipping is needed; "
                f"it is delivered electronically ({self.size} GB download).")

    def to_dict(self):
        return {"type": "digital", "id": self.product_id, "name": self.name,
                "price": self.price, "stock": self.stock, "size": self.size}

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["name"], data.get("price", 0.0), data["stock"], data["size"])