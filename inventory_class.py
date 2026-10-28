from product_class import Product

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if self.find_by_id(product.product_id) is not None:
            raise ValueError(f"Product ID {product.product_id} already exists.")
        self.__products.append(product)

    def find_by_id(self, product_id):
        for product in self.__products:
            if product.product_id.lower() == str(product_id).strip().lower():
                return product
        return None

    def search_product(self, search_term):
        term = search_term.lower()
        return [p for p in self.__products if term in p.name.lower()]

    def get_next_id(self):
        numbers = [int(p.product_id[1:]) for p in self.__products if p.product_id[1:].isdigit()]
        return f"P{max(numbers, default=0) + 1:03d}"

    def get_products(self):
        return list(self.__products) 

    def display_all(self):
        self.display_products(self.__products)

    def display_products(self, products):
        if not products:
            print("No products to display.")
            return
        
        print(f"{'ID':<10}{'Name':<20}{'Price':<10}{'Stock':<10}")
        print("-" * 50)
        for product in products:
            product.display_information()
