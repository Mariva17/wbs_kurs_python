"""
Discounts Beispiel
"""

import abc
import enum

class Discounts(enum.Enum):
    DEFAULT = 1.0
    SUMMER = 0.1
    WINTER = 0.14


class Discount(abc.ABC):
    @abc.abstractmethod
    def get_percentage(self) -> float:
        pass


class DefaultDiscount(Discount):
    def get_percentage(self) -> float:
        return Discounts.DEFAULT.value


class SummerDiscount(Discount):
    def get_percentage(self) -> float:
        return Discounts.SUMMER.value


class WinterDiscount(Discount):
    def get_percentage(self) -> float:
        return Discounts.WINTER.value


class DiscountCalculator:
    """Calculate discount based on choosen Strategy."""

    def __init__(self, price: float, discount: Discount):
        self.discount = discount
        self.price = price

    def calculate(self) -> float:
        return self.price * self.discount.get_percentage()


price = 200
new_price = DiscountCalculator(price=price, discount=DefaultDiscount()).calculate()
print(f"alter Preis: {price}, neuer Preis: {new_price}")

new_price = DiscountCalculator(price=price, discount=SummerDiscount()).calculate()
print(f"alter Preis: {price}, neuer Summerpreis: {new_price}")


# isinstance liefert True, wenn Objrkt Instanz einer Klasse oder Kindklasse
a = SummerDiscount()
print(isinstance(a, SummerDiscount))  # True
print(isinstance(a, Discount))  # True
print(isinstance(1.0, int))  # False
print(isinstance(1, float))  # False
print(isinstance(True, int))  # True
