class Product: 

    def __init__(self, product_id, name, price, stock):
        self.__product_id = str(product_id)
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)
        self.update_stock(stock)

    def product_id(self):
        return self.__product_id

    def name(self):
        return self.__name

    def price(self):
        return self.__price

    def stock(self):
        return self.__stock

    def update_stock(self, quantity):
        if not isinstance (quantity, int) or quantity < 0:
            raise ValueError ("Stock must be an integer bigger than 0")
        self.__stock = quantity

        def display_information(self):
            print(f"{self.__product_id:<10}{self.__name:<20}"
              f"${self.__price:<9.2f}{self.__stock:<10}")