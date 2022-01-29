from food import Food


class Cart:
    def __init__(self, cartid):
        self.cartId = cartid
        self.restaurant = None
        self.items = []
        self.quantities = []
        self.price = []
        self.count = 0

    def addFoodItems(self, name, qty):
        self.items.append((Food(name)))
        self.quantities.append(qty)
        self.count += int(qty)
        print("INFO : Food item {} * {} added to your cart[{}]"
              .format(name, qty, self.cartId))

    def removeFoodItems(self, food):
        missing = True
        for i in range(len(self.foods)):
            if self.foods[i].name == food:
                self.items.pop(i)
                self.items.quantities(i)
                missing = False
                print("INFO : Food Item {} removed from your cart[{}]"
                      .format(food, self.cartId))
        if missing:
            print("ERROR : This food item [{}] is not in your cart[{}]"
                  .format(food, self.cartId))

    def modifiyQuantity(self, qty, food):
        missing = True
        for i in range(len(self.items)):
            if food.name == self.foods[i].name:
                self.quantities[i] = qty
                missing = False
                print("INFO : Food quantity updated successfully in cart")
        if missing:
            print("ERROR : This food item [{}] is not in your cart[{}]"
                  .format(food, self.cartId))