import datetime
import os
import uuid
import time

class User:
    def __init__(self,uid,pwd,name,address,mobileNum,pincode,city) :
        self.UserId = uid
        self.pwd = pwd
        self.name = name
        self.address = address
        self.mobileNum = mobileNum
        self.pincode = pincode
        self.city = city
        #created a new user
    def userDetails(self):
        return self.UserId,self.name,self.address,self.mobileNum,self.city
    
    
    def OrderReceive(self):
        print("Dear",self.name,"You have palce order successfuly...!")
        
    def OrderDenied(self):
        print("Dear",self.name,"Your order has Rejected")
        
############################ user creation done #######################################
class Food:
    def __init__(self,name,price = None) :
        self.name = name
        self.price = price
        
    def Price(self):
        return self.price
    def __str__(self):
        return self.name + ':' + str(self.Price())
########################## Food Part is Over ###########################################
class Resturant:
    def __init__(self,id,name,address,mobNum,city) :
        self.resid = id
        self.res_name = name
        self.res_add = address
        self.res_num = mobNum
        self.city = city
        self.open = True
        self.menu = {}
    def Details_Res(self):
        return Resturant (self.resid,self.res_name,self.res_add,self.res_num,self.city)
    
    def Open_status(self):
        return self.open
    
    def Menu(self):
        for i in self.menu:
            print(i)
            
    def add_items(self,name,price):
        food = Food(name,price)
        if name not in self.menu:
            self.menu[name] = food
            print("Item added successfully")
        else:
            print("Item already exist")
            
    def menu_update(self,name,price):
        food = self.menu[name]
        if food is not None:
            food.price = price
            self.menu[name] = food
    def del_menu(self,name):
        self.menu.pop(name)
# if __name__=="__main__":
#     x = Resturant(123,"hotel","BAM",9348588819,"BAM")
#     x.Menu()
#     x.add_items("Dal",80)
#     x.add_items("Chapati",80)
#     x.menu_update("Dal",110)
#     print(x.menu)

class Order:
    def __init__(self) -> None:
        self.OrId = str(uuid.uuid1()).split("_")[0]
        self.resid = None
        self.bucketid = None
        self.Item_name = []
        self.itm_Qnt = []    
        self.prices = []
        self.total = None
        self.pay_sts = None
        self.ord_sts = None
        self.msg = None
        self.UserId = None
        self.date_time =  datetime. now(). strftime("%Y_%m_%d-%I:%M:%S_%p")
    def print(self):
        pass
    
    
    def printDetails(self):
        pass

class bucket:
    def __init__(self,bucketid):
        self.bucketId = bucketid
        self.resturant = None
        self.item = []
        self.quantities = []
        self.price = []
        self.count = 0
    
    def add_item(self,name,qty):
        self.item.append(Food(name))
        self.quantities.append(qty)
        self.count += int(qty)
        print(" Food item {} * {} added to your cart[{}]"
              .format(name, qty, self.bucketId))
    
    def remove_item(self,food):
        missing = True
        for i in range (len(self.food)):
            if self.food[i].name == food:
                self.item.pop(i)
                self.item.quantities(i)
                missing = False
                print("INFO : Food Item {} removed from your cart[{}]"
                      .format(food, self.cartId))
        if missing:
            print("ERROR : This food item [{}] is not in your cart[{}]"
                  .format(food, self.cartId))

    def modifiyQuantity(self, qty, food):
        missing = True
        for i in range(len(self.item)):
            if food.name == self.food[i].name:
                self.quantities[i] = qty
                missing = False
                print("INFO : Food quantity updated successfully in cart")
        if missing:
            print("ERROR : This food item [{}] is not in your cart[{}]"
                  .format(food, self.bucketId))
    
    
############################ End of Cart ##################################
                
                