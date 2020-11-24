class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.qoh = 0

    def purchase(self, qty):
        self.qoh += qty

    def sell(self, qty):
        self.qoh -= qty

    def netprice(self):
        return self.price


class DiscountProduct(Product):
    def __init__(self, name, price, disrate):
        super().__init__(name, price)
        self.disrate = disrate

    # Overriding
    def netprice(self):
        return self.price - (self.price * self.disrate / 100)


p = DiscountProduct('Dell Laptop', 56000, 20)
p.purchase(10)
p.sell(3)
print(p.qoh)
print(p.netprice())
