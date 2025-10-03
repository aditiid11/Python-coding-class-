class Donut:
    def __init__(self, flavor, flower, price):
        self.flavor=flavor
        self.flower=flower
        self.price=price
    
    #TODO: function to calculate the price

    def ToString(self):
        print("This is the flavor",self.flavor)
        print("This is the flower",self.flower)
        print("This is the price",self.price)

if __name__ == "__main__":
    flavor = str(input("What flavor do you want (Chocolate, vanila, strawbery):"))
    flour=str(input("What kind of flour do you want (glutan, keto,wheat)"))
    price = 0

    d1=Donut(flavor,flour,price)
    d1.ToString()