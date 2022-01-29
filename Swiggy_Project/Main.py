from rest import Restaurant
from bucket import Cart
from order import Order
from user import User


class Swiggy:
    def __init__(self):
        self.restaurants = {}
        self.carts = {}
        self.orders = {}
        self.users = {}
        self.pay = {}
        self.odHistory = {}
        self.currentUser = None

    def addMenuItemToRestaurant(self, resId, name, price):
        if resId in self.restaurants:
            rest = self.restaurants[resId]
            rest.addMenuItems(name, price)
        else:
            print("Invalid restaurant Id")

    def SearchFood(self, n):
        for key, rest in self.restaurants.items():
            print(key, rest)
            for i, val in rest.menu.items():
                print(i, val)
                print("please Signup")
                if i == n:
                    print("Found", rest.name, val.name, val.price)
                    return
        print("NotFound")

    def signUp(self, userId, pwd, name, address, mobileNum, pinCode, city):
        if userId not in self.users:
            self.users[userId] = User(userId, pwd, name, address,
                                      mobileNum, pinCode, city)
            print("successfully signup!")
            print("Please LogIn")
        else:
            print("User already exist")

    def logIn(self, userId, pwd):

        if userId not in self.users:
            print("Please signup")
        else:
            user = self.users[userId]
            if user.pwd == pwd:
                self.currentUser = user
                print("login successfully, Welcome {}!".format(user.name))
                print("Please Select the Menu")
            else:
                print("password is not matching!")

    def logOut(self):
        print("Logout successful, Good Bye {}".format(self.currentUser.name))
        self.currentUser = None
        exit()

    def selectFood(self, cartId, name, qty):
        cart = self.getCart(cartId)
        cart.addFoodItems(name, qty)
        return cart

    def getCart(self, cartid):
        if cartid in self.carts:
            return self.carts[cartid]
        else:
            cart = Cart(cartid)
            self.carts[cartid] = cart
            return cart

    def placeOrder(self, cartId):
        if self.currentUser is None:
            print("Please login to place order")
            return
        cart = self.carts[cartId]
        missing = None
        order = Order()
        order.userId = self.currentUser.userId
        for i, rest in self.restaurants.items():
            total = 0
            missing = False
            currPrice = [None]*len(cart.items)
            for i in range(len(cart.items)):
                food = cart.items[i]
                qty = cart.quantities[i]
                if food.name not in rest.menu:
                    missing = True
                    break
                food = rest.menu[food.name]
                currPrice[i] = food.price
                total += (int(qty) * float(rest.menu[food.name].price))
            if not missing:
                if order.totalAmount is None or order.totalAmount > total:
                    order.resId = rest.resId
                    order.totalAmount = total
                    order.prices = currPrice
        if not missing:
            order.payStatus = "pending"
            order.odrStatus = "created"
            order.fName = cart.items
            order.fQty = cart.quantities
            self.orders[order.odId] = order
            order.print()
            print("Order created successfull Please Note your order ID!")
            print("Please Make Payment")
        else:
            print("Order failed, all prodts not avlbl in a restaurant(s)")
        return order

    def getOrderDetails(self, odId):
        if odId in self.orders:
            temp = self.orders[odId]
            temp.printDetails()
        else:
            print("odId is not match")

    def addRestaurant(self, resId, name, address, mobileNum, city):
        res = Restaurant(resId, name, address, mobileNum, city)
        print("Resturant Added Sucessfully Please Add Menu")
        if resId not in self.restaurants:
            self.restaurants[resId] = res
        else:
            print("ERROR - Restaurant with same id already exists")

    def deleteRestaurant(self, resId):
        self.restaurants.pop(resId)

    def PaymentStatus(self, odId, x):
        if odId not in self.pay:
            self.pay[odId] = x
            print("payment successfully!")
            print("Your Order is processing Please Wait")
        else:
            print("Failed!")

    def orderHistory(self, odId):
        if odId not in self.odHistory:
            self.odHistory = self.orders
            print("All order details:", self.odHistory)
        else:
            print("Already recorded exit!")

    def deliverOrder(self, odId):
        if odId in self.orders:
            order = self.orders[odId]
            order.payStatus = "Delivered"
            print("Delivered succesfully!")
            print("Please Give Your Valuable Feedback")
        else:
            print("Invalid Id!")

    def feedback(self, odrId, comment):
        order = self.orders[odrId]
        if order is None:
            print("Invalid order Id")
        else:
            order.comment = comment
            self.orders[odrId] = order



if __name__ == "__main__":
    s = Swiggy()
    tc = int(input("Enter Any Two Digit No. : "))
    print("Add Resturant")
    for i in range(tc):
        tokens = input().split("|")
        if (len(tokens[0]) <= 0):
            break
        if tokens[0] == "CRR_REST":
            s.addRestaurant(tokens[1].strip(), tokens[2].strip(),
                            tokens[3].strip(), tokens[4].strip(),
                            tokens[5].strip())
        elif tokens[0].strip() == "ADD_MENU":
            s.addMenuItemToRestaurant(tokens[1].strip(), tokens[2].strip(),
                                      tokens[3].strip())
        elif tokens[0].strip() == "SEARCH":
            s.SearchFood(tokens[1])
        elif tokens[0].strip() == "SIGNUP":
            s.signUp(tokens[1].strip(), tokens[2].strip(), tokens[3].strip(),
                     tokens[4].strip(), tokens[5].strip(), tokens[6].strip(),
                     tokens[7].strip())
        elif tokens[0].strip() == "LOGIN":
            s.logIn(tokens[1].strip(), tokens[2].strip())
        elif tokens[0].strip() == "SELECT":
            s.selectFood(tokens[1].strip(), tokens[2].strip(),
                         tokens[3].strip())
        elif tokens[0].strip() == "GETCART":
            s.getCart(tokens[1].strip())
        elif tokens[0].strip() == "PLACEORDER":
            s.placeOrder(tokens[1].strip())
        elif tokens[0].strip() == "LOGOUT":
            s.logOut()
        elif tokens[0].strip() == "GETORDERDETAILS":
            s.getOrderDetails(tokens[1].strip())
        elif tokens[0].strip() == "DELETERESTAURANT":
            s.deleteRestaurant(tokens[1].strip())
        elif tokens[0].strip() == "PAYMENT":
            s.PaymentStatus(tokens[1].strip(), tokens[2].strip())
        elif tokens[0].strip() == "ORDERHISTORY":
            s.orderHistory(tokens[1].strip())
        elif tokens[0].strip() == "DELIVERORDER":
            s.deliverOrder(tokens[1].strip())
        elif tokens[0].strip() == "FEEDBACK":
            s.feedback(tokens[1].strip(), tokens[2].strip())
        else:
            print("ERROR - Unsupported instruction")


# Running Procedure
"""
14
CRR_REST| 1|Hotel Nandan|BAM| 9348588819|BAM
CRR_REST| 2|Desi Tadka| BAM|8895279327|BAM
CRR_REST| 3|Punjabi_Dhaba| BAM|9861933067|CD
ADD_MENU | 1 | Dal|25
ADD_MENU | 1 | Tea|20
ADD_MENU | 1 | Roti|20
SEARCH|Dal
SIGNUP|Kanhu|123|Kanhu|BAM-OD|9658279327|761027|BAM
LOGIN|Kanhu|123
SELECT|1|Dal|2
GETCART | 1
PLACEORDER | 1
PAYMENT |Current Order Id|50
DELIVERORDER|Current Order Id
FEEDBACK |Current Order Id|Good food !
DELETERESTAURANT|1
LOGOUT
"""