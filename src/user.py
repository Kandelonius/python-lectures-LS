class User:
    def __init__(self, money):
        self.money = money
        self.cart = []

    def __str__(self):
        return f"Money: ${self.money} Cart: ${self.cart}"
    def add_to_car(self, product):
        self.cart.append(product)
        print(f"added {product.name}")