

class User:
    def __init__(self, uid, pwd, name, address, mobileNum, pinCode, city):
        self.userId = uid
        self.pwd = pwd
        self.name = name
        self.address = address
        self.mobileNum = mobileNum
        self.pinCode = pinCode
        self.city = city

    def userDetails(self):
        return "<User('%s', '%s', '%s', '%s', '%s', '%s')>" % (
                                                                self.userId,
                                                                self.name,
                                                                self.address,
                                                                self.mobileNum,
                                                                self.pinCode,
                                                                self.city)

    def acceptDelivery(self):
        print("Order Accepted!")

    def rejectDelivery(self):
        print("Order Rejected!")