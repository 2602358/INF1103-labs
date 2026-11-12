class Supplier:
    def __init__(self, supplier_id: str, supplier_name: str, contact_email: str) -> None:
        self.__supplier_id: str = str(supplier_id)
        self.__supplier_name: str = str(supplier_name)
        self.__contact_email: str = str(contact_email)

    @property
    def supplier_id(self) -> str:
        return self.__supplier_id

    @property
    def supplier_name(self) -> str:
        return self.__supplier_name

    @property
    def contact_email(self) -> str:
        return self.__contact_email

    def display_information(self) -> None:
        print(f"{self.supplier_id:<10}{self.supplier_name:<20}{self.contact_email:<25}")

    def to_dict(self) -> dict[str, str]:
        return {"id": self.supplier_id, "name": self.supplier_name,
                "email": self.contact_email}

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> "Supplier":
        return cls(data["id"], data["name"], data["email"])