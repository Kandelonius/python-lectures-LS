class User:
    def __init__(self, money):
        self.money = money
        self.cart = []

    def __str__(self):
        return f"Money: ${self.money} Cart: ${self.cart}"

    def add_to_car(self, product):
        self.cart.append(product)
        print(f"added {product.name}")


# dict = {0: 1, 1: 1,2: 2}
# def fact(n):
#     index = 2
#     # if n in dict:
#     #     return n
#     for num in range(index, n + 1):
#         dict[num] = dict[index - 1] * dict[index - 2]
#         index += 1
#     return dict[n]
# print(fact(5))

print(3 ** (-0))
