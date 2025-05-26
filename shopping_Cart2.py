class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_items(self, item_name: str, qty: int, unit_price: float):
        self.items.append((item_name, qty, unit_price))

    def remove_items(self, item_name: str):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self) -> float:
        total = 0.0
        for name, qty, price in self.items:
            total += qty * price
        return total

    def summary(self):
        print("Cart Contents:")
        for name, qty, price in self.items:
            print(f"{name}: {qty} @ Ksh {price:.2f} each")
        print(f"Total before discount/tax: Ksh {self.calculate_total():.2f}")

    def checkout(self):
        self.summary()
        print(f"Final Amount: Ksh {self.calculate_total():.2f}\n")


class DiscountedCart(ShoppingCart):
    def __init__(self, discount_rate: float):
        super().__init__()
        self.discount_rate = discount_rate

    def calculate_total(self) -> float:
        initial_total = super().calculate_total()
        discount = initial_total * self.discount_rate
        print(f"Discount: -Ksh {discount:.2f}")
        return initial_total - discount


class TaxedCart(ShoppingCart):
    def __init__(self, tax_rate: float):
        super().__init__()
        self.tax_rate = tax_rate

    def calculate_total(self) -> float:
        initial_total = super().calculate_total()
        tax = initial_total * self.tax_rate
        print(f"Tax: +Ksh {tax:.2f}")
        return initial_total + tax


if __name__ == "__main__":
    print(">>> Regular Cart <<<")
    cart = ShoppingCart()
    cart.add_items("Kiwi", 50, 79.2)
    cart.add_items("Papaya", 30, 40.3)
    cart.add_items("Guava", 20, 20.1)
    cart.checkout()

    print(">>> Discounted Cart (15%) <<<")
    disc_cart = DiscountedCart(discount_rate=0.15)
    disc_cart.add_items("Kiwi", 50, 79.2)
    disc_cart.add_items("Papaya", 30, 40.3)
    disc_cart.add_items("Guava", 20, 20.1)
    disc_cart.checkout()

    print(">>> Taxed Cart (12%) <<<")
    tax_cart = TaxedCart(tax_rate=0.12)
    tax_cart.add_items("Kiwi", 50, 79.2)
    tax_cart.add_items("Papaya", 30, 40.3)
    tax_cart.add_items("Guava", 20, 20.1)
    tax_cart.checkout()
