import pytest

import main
from discount_strategy import (BulkDiscount, DiscountStrategy, NoDiscount, PercentageDiscount, StudentDiscount)
from file_handling import load_products
from inventory_class import Inventory
from order_class import Order
from order_line_class import OrderLine
from physical_product_class import Physical_product
from digital_product_class import Digital_product
from product_factory import ProductFactory
from supplier_class import Supplier


@pytest.fixture
def supplier() -> Supplier:
    return Supplier("S001", "Acme Ltd", "sales@acme.com")


@pytest.fixture
def order_250(supplier):
    order = Order("O1")
    order.add_order_line(ProductFactory.create("physical", "P1", "Box", 50.0, 10, 1, supplier), 5)
    return order


# Strategy
def test_default_is_no_discount(order_250):
    assert order_250.calculate_total() == 250


def test_bulk_then_set_percentage(order_250):
    order_250.set_discount(BulkDiscount(200, 20))
    assert order_250.calculate_total() == 230
    order_250.set_discount(PercentageDiscount(10))
    assert order_250.calculate_total() == pytest.approx(225)


def test_bulk_below_threshold(order_250):
    order_250.set_discount(BulkDiscount(300, 20))
    assert order_250.calculate_total() == 250


def test_new_strategy_needs_no_order_change(order_250):
    order_250.set_discount(StudentDiscount())
    assert order_250.calculate_total() == pytest.approx(237.5)

    class HalfPrice(DiscountStrategy):          # defined outside Order entirely
        def apply(self, total: float) -> float:
            return total / 2
    order_250.set_discount(HalfPrice())
    assert order_250.calculate_total() == 125


def test_order_accepts_strategy_in_constructor():
    assert isinstance(Order("O2").discount, NoDiscount)
    assert isinstance(Order("O2", PercentageDiscount(5)).discount, PercentageDiscount)


def test_invalid_percentage():
    with pytest.raises(ValueError):
        PercentageDiscount(150)


# Factory
def test_factory_types(supplier):
    assert isinstance(ProductFactory.create("physical", "P1", "A", 1, 1, 1, supplier), Physical_product)
    assert isinstance(ProductFactory.create("digital", "D1", "B", 1, 1, 1, supplier), Digital_product)


def test_factory_unknown_type(supplier):
    with pytest.raises(ValueError, match="Unknown product type: service"):
        ProductFactory.create("service", "S1", "Install", 30, 1, 0, supplier)


# Validation
@pytest.mark.parametrize("price", [0, -5])
def test_invalid_price(supplier, price):
    with pytest.raises(ValueError):
        ProductFactory.create("physical", "P1", "A", price, 1, 1, supplier)


def test_invalid_stock(supplier):
    with pytest.raises(ValueError):
        ProductFactory.create("digital", "D1", "A", 5, -1, 1, supplier)


@pytest.mark.parametrize("qty", [0, -2])
def test_invalid_order_quantity(supplier, qty):
    product = ProductFactory.create("physical", "P1", "A", 5, 1, 1, supplier)
    with pytest.raises(ValueError):
        OrderLine(product, qty)


# Input helper
def test_get_positive_float_retries(monkeypatch, capsys):
    answers = iter(["abc", "-5", "12.50"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    assert main.get_positive_float("Price: ") == 12.5
    out = capsys.readouterr().out.splitlines()
    assert out == ["Please enter a valid number, e.g. 12.50",
                   "Please enter a number greater than zero."]


# File loading
CSV = """product_type,product_id,name,price,stock_quantity
physical,P001,Desk Lamp,25.00,10
digital,D001,Photo Editor,49.90,100
service,S001,Installation,30.00,5
physical,P002,Office Chair,abc,3
physical,P003,Monitor Stand,39.50,7
"""


def test_load_products_skips_bad_rows(tmp_path, supplier, capsys):
    path = tmp_path / "products.csv"
    path.write_text(CSV)
    inventory = Inventory()
    load_products(str(path), inventory, supplier)
    out = capsys.readouterr().out
    assert [p.product_id for p in inventory.get_products()] == ["P001", "D001", "P003"]
    assert "Unknown product type: service" in out
    assert "3 products loaded." in out
    assert out.strip().endswith("Load attempt finished.")


def test_load_products_missing_file(tmp_path, supplier, capsys):
    inventory = Inventory()
    load_products(str(tmp_path / "nope.csv"), inventory, supplier)
    out = capsys.readouterr().out
    assert "not found" in out
    assert "products loaded" not in out
    assert "Load attempt finished." in out
    assert inventory.get_products() == []