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
        Product.__init__(self, name, price)
        self.disrate = disrate

    # Overriding
    def netprice(self):
        return self.price - (self.price * self.disrate / 100)


class TaxableProduct(Product):
    def __init__(self, name, price, taxrate):
        Product.__init__(self, name, price)
        self.taxrate = taxrate

    # Overriding
    def netprice(self):
        return self.price + (self.price * self.taxrate / 100)


# Multiple Inheritance
class TaxableDiscountProduct(DiscountProduct, TaxableProduct):
    def __init__(self, name, price, disrate, taxrate):
        DiscountProduct.__init__(self, name, price, disrate)
        TaxableProduct.__init__(self, name, price, taxrate)

    def netprice(self):
        discounted_price = DiscountProduct.netprice(self)
        return discounted_price + (discounted_price * self.taxrate / 100)


p = DiscountProduct('Dell Laptop', 56000, 20)
p.purchase(10)
p.sell(3)
print(p.qoh)
print(p.netprice())

td = TaxableDiscountProduct('iPhone 11', 100000, 30, 15)
td.purchase(10)
print(td.netprice())
