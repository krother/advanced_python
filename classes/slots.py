
class Fruit:

    #__slots__ = ["name", "price"]

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} costs {self.price}"


f = Fruit("banana", 1.23)
f.pprice = 4.56
print(f)
