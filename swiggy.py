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
class Restursnt:
    def __init__(self,id,name,address,mobNum,city) :
        self.resid = id
        self.res_name = name
        self.res_add = address
        self.res_num = mobNum
        self.city = city
        self.open = True
        self.menu = {}
    def Details_Res(self):
        return self.resid,self.res_name,self.res_add,self.res_num,self.city
    
    def Open_status(self):
        return self.open
     
    
        
        