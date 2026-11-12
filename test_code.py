from typing import Any
from digital_product_class import Digital_product
from inventory_class import Inventory
from order_class import Order
from physical_product_class import Physical_product
from product_class import Product
from supplier_class import Supplier


def make_products() -> tuple[Supplier, Physical_product, Digital_product]:
    supplier = Supplier("S001", "Acme Ltd", "sales@acme.com")
    laptop = Physical_product("P001", "Laptop", 1200.00, 15, 2, supplier)
    game = Digital_product("P002", "Game", 60.00, 100, 45, supplier)
    return supplier, laptop, game


# Section 2
def test_association() -> None:
    """Supplier and Product: a reference, but independent objects."""
    supplier, laptop, game = make_products()

    assert laptop.supplier is supplier        # Product stores the reference
    assert game.supplier is supplier
    assert laptop is not supplier             # separate objects

    del supplier                              # delete the variable, not the object
    laptop.supplier.display_information()     # products can still show supplier info
    game.supplier.display_information()
    assert laptop.supplier is game.supplier   # one Supplier shared by both products


# Section 3
def test_aggregation() -> None:
    """Inventory aggregates Products: removal does not destroy them."""
    _, laptop, _ = make_products()
    inventory_a, inventory_b = Inventory(), Inventory()

    inventory_a.add_product(laptop)
    assert inventory_a.find_product("P001") is laptop

    assert inventory_a.remove_product("P001") is True
    assert inventory_a.find_product("P001") is None
    assert inventory_a.remove_product("P001") is False      # already gone

    laptop.update_stock(10)                                  # product still works
    assert laptop.stock == 10
    laptop.display_information()

    inventory_b.add_product(laptop)                          # same object, new inventory
    assert inventory_b.find_product("P001") is laptop

    inventory_b.remove_product("P001")                       # empty the inventory
    assert len(inventory_b.get_products()) == 0
    assert laptop.name == "Laptop"                           # product lives on


# Section 4
def test_composition() -> None:
    """Order creates and manages its own OrderLines."""
    _, laptop, game = make_products()

    order1 = Order("O001")
    order1.add_order_line(laptop, 2)
    order1.add_order_line(game, 3)
    order1.display_order()
    assert order1.calculate_total() == 1200.00 * 2 + 60.00 * 3

    order2 = Order("O002")
    order2.add_order_line(laptop, 1)

    line1, line2 = order1.order_lines[0], order2.order_lines[0]
    assert line1 is not line2                 # each Order made its own OrderLine
    assert line1.product is line2.product     # one shared Product
    assert line1.product is laptop

    assert order1.remove_order_line("P002") is True
    assert len(order1.order_lines) == 1
    assert game.name == "Game"                # Product unaffected by line removal
    assert order2.calculate_total() == 1200.00


# Section 6
def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


def test_lsp() -> None:
    """Both subclasses can stand in for Product."""
    _, laptop, game = make_products()

    for product in (laptop, game):            # same function, both subclasses
        show_product_details(product)

    inventory = Inventory()
    inventory.add_product(laptop)
    inventory.add_product(game)
    inventory.display_all()
    assert inventory.find_product("P001") is laptop
    assert inventory.find_product("P002") is game
    assert inventory.search_product("game") == [game]

    bad_values: list[Any] = [-1, 2.5, "3"]
    for product in (laptop, game):            # update_stock means the same for both
        product.update_stock(7)
        assert product.stock == 7
        for bad in bad_values:
            try:
                product.update_stock(bad)
                raise AssertionError("invalid stock was accepted")
            except ValueError:
                pass
        assert product.stock == 7             # a rejected update changes nothing


# Section 7
def test_polymorphism() -> None:
    """One loop over Products; each object supplies its own behaviour."""
    supplier = Supplier("S001", "Acme Ltd", "sales@acme.com")
    inventory = Inventory()
    inventory.add_product(Physical_product("P001", "Laptop", 1200.00, 15, 2, supplier))
    inventory.add_product(Digital_product("P002", "Game", 60.00, 100, 45, supplier))
    inventory.add_product(Physical_product("P003", "Mouse", 25.50, 50, 0.10, supplier))

    expected = {
        "P001": "requires shipping",
        "P002": "delivered electronically",
        "P003": "requires shipping",
    }
    for product in inventory.get_products():  # no isinstance, no separate loops
        product.display_information()
        info = product.get_fulfilment_info()
        print(info)
        assert expected[product.product_id] in info


# Runner
def main() -> None:
    tests = [
        ("2. Association (Supplier - Product)", test_association),
        ("3. Aggregation (Inventory - Product)", test_aggregation),
        ("4. Composition (Order - OrderLine)", test_composition),
        ("6. Liskov Substitution", test_lsp),
        ("7. Polymorphism", test_polymorphism),
    ]
    for title, test in tests:
        print(f"\n=== {title} ===")
        test()
        print(f"PASSED: {title}")
    print("\nAll tests passed.")


if __name__ == "__main__":
    main()
