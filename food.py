
class Food:
    def __init__(self, name, price=None):
        self.name = name
        self.price = price

    def getprice(self):
        return self.price

    def __str__(self):
        return self.name + ' : ' + str(self.getprice())