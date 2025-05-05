class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_items(self, item_name: str, qty: int, unit_price: float):
        self.items.append((item_name, qty, unit_price))

    def remove_item(self, item_name: str):

        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self) -> float:
        total = 0.0

        for name, qty, price in self.items:
            total += qty * price

        return  total

    def summary(self):

        print("Cart Contents")
        for name, qty, price in self.items:
            print(f"{name}: {qty} @ Ksh {price:.2f} each")

        print(f"Total: Ksh {self.calculate_total():.2f}\n")

def checkout(cart: ShoppingCart):
    cart.summary()
    print(f"Final amount: Ksh{cart.calculate_total():.2f}\n")

#Usage
if __name__ == "__main__":

    cart: ShoppingCart = ShoppingCart()
    cart.add_items("Kiwi", 50, 79.2)
    cart.add_items("Papaya", 30, 40.1)
    cart.add_items("Guava", 10, 30.3)

    print(">>> Regular Cart <<<")

    checkout(cart)