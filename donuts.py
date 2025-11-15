class Donut:
    def __init__(self, flavor, flour, price):
        self.flavor=flavor
        self.flour=flour
        self.price=price
    
    def get_flavor(self):
        return self.flavor
    def set_flavor(self, flavor):
        self.flavor=flavor
    def get_flour(self):
        return self.flour
    def set_flour(self,flour):
        self.flour=flour
    def get_price(self):
        return self.price
    def set_price(self,price):
        self.price=price
    def caculate_price(self):
        print("cauclate 1")
        flour= int(self.get_flour())
        flavor=int(self.get_flavor())
        price=int(self.get_price())
    
        price=0
    
        if (flour == 1):
            print("+3 on price ")
            price=price+3
        elif (flour == 2):
            print("+2 on price ")
            price=price+2
        elif (flour == 3):
            print("+1 on price ")
            price=price+1
            
    
        if (flavor == 1):
            print("+3 on price ")
            price=price+3
        elif (flavor == 2):
            print("+2 on price ")
            price=price+2
        elif (flavor == 3):
            print("+1 on price ")
            price=price+1
        self.set_price(price)
        print("final price is ",self.get_price())
        
    
            
    def ToString(self):
        print("This is the flavor",self.flavor)
        print("This is the flour",self.flour)
        print("This is the price",self.price)

    
class Store (Donut):
    def __init__(self, flavor, flour, price,advertisment,payment):
        self.advertisement=advertisement
        self.payment=payment
        Donut.__init__(self, flavor, flour, price)
    def get_advertisement(self):
        return self.advertisement
    def set_advertiment(self,advertisement):
        self.advertisement=advertisement
    def get_payment(self):
        return self.payment
    def set_payment(self,payment):
        self.payment=payment
        
    def dount_advertisement(self):
        user_click=(int(input("Did the user click yes or not (1/2)")))
        if user_click ==1:
            self.caculate_price()
        else: print("Please check advertisment!")
    

if __name__ == "__main__":
    #flavor = str(input("What flavor do you want (Chocolate[1], vanila[2], strawbery[3]):"))
    #flour=str(input("What kind of flour do you want (glutan [1], keto[2],wheat[3])"))
    #price = 0

    #d1=Donut(flavor,flour,price)
    #d1.ToString()
    #d1.caculate_price()
    flavor=1
    flour=0
    price=0
    advertisement=0
    payment=0    
    s1=Store(flavor,flour,price,advertisement,payment)
    s1.ToString()
    s1.dount_advertisement()


print("this is the final adversisment:")
    
    
    