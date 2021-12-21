from food import Food


class Restaurant:
    def __init__(self, resId, name, address, mobileNum, city):
        self.resId = resId
        self.name = name
        self.address = address
        self.mobileNum = mobileNum
        self.city = city
        self.open = True
        self.menu = {}

    def RestaurantDetails(self):
        return "<Restaurant('%s', '%s', '%s', '%s', '%s', \
                            )>" % (self.resId, self.name, self.address,
                                   self.mobileNum, self.city)

    def status(self):
        return self.open

    def getMenu(self):
        for i in self.menu:
            print(i)

    def addMenuItems(self, name, price):
        food = Food(name, price)
        if name not in self.menu:
            self.menu[name] = food
            print("INFO : Menu item successfully added")
        else:
            print("ERROR : Menu item already added")

    def updateMenu(self, name, price):
        food = self.menu[name]
        if food is not None:
            food.price = price
            self.menu[name] = food

    def deleteMenu(self, name):
        self.menu.pop(name)