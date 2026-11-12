class Supplier():
    def __init__(self, supplier_id, supplier_name, contact_email):
        self.__supplier_id = str(supplier_id)
        self.__supplier_name = str(supplier_name)
        self.__contact_email = str(contact_email)

    @property
    def supplier_id(self):
        return self.__supplier_id

    @property
    def supplier_name(self):
        return self.__supplier_name

    @property
    def contact_email(self):
        return self.__contact_email

    def display_information(self):
        print(f"{self.supplier_id:<10}{self.supplier_name:<20}{self.contact_email:<25}")

    def to_dict(self):
        return {"id": self.supplier_id, "name": self.supplier_name,
                "email": self.contact_email}

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["name"], data["email"])