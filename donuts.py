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
    #TODO: function to calculate the price
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
            price=price+4
            rice=0
    
        if (flavor == 1):
            print("+3 on price ")
            price=price+3
        elif (flavor == 2):
            print("+2 on price ")
            price=price+2
        elif (flavor == 3):
            print("+1 on price ")
            price=price+4
        self.set_price(price)
        print("final price is ",self.get_price())
        
    
            
    def ToString(self):
        print("This is the flavor",self.flavor)
        print("This is the flour",self.flour)
        print("This is the price",self.price)


if __name__ == "__main__":
    flavor = str(input("What flavor do you want (Chocolate[1], vanila[2], strawbery[3]):"))
    flour=str(input("What kind of flour do you want (glutan [1], keto[2],wheat[3])"))
    price = 0

    d1=Donut(flavor,flour,price)
    d1.ToString()
    d1.caculate_price()