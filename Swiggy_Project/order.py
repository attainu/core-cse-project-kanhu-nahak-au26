import time
import uuid


class Order:
    def __init__(self):
        self.odId = str(uuid.uuid1()).split("-")[0]
        self.resId = None
        self.cartId = None
        self.fName = []
        self.fQty = []
        self.prices = []
        self.totalAmount = None
        self.payStatus = None
        self.odrStatus = None
        self.comment = None
        self.userId = None
        self.time = time.asctime(time.localtime(time.time()))

    def print(self):
        print("\t\t\t\t{}".format(self.time))
        print("RESTAURANT: {}\t\t\tORDER: {}".format(self.resId, self.odId))
        print("STATUS: {}\t\t\tPAYMENT: {}".format(self.odrStatus,
                                                   self.payStatus))
        print("Quantity\tName\t\t\t\tPrice\tTotal")
        for i in range(len(self.fName)):
            print("{} * {}\t\t\t\t{}\t{}".format(self.fQty[i],
                                                 self.fName[i].name,
                                                 self.prices[i],
                                                 float(self.prices[i]) *
                                                 int(self.fQty[i])))
        print("Total : {}".format(self.totalAmount))

        if self.comment:
            print("Customer feedback : {}".format(self.comment))

    def printDetails(self):
        print("<Order('%s', '%s', '%s', '%s', '%s', \
         '%s','%s','%s','%s')>" % (self.odId, self.resId, self.cartId,
                                   self.fName, self.fQty, self.totalAmount,
                                   self.payStatus, self.odrStatus, self.time))