class Store:
    def __init__(self, clicked, advertisment):
        self.clicked=clicked
        self.advertisment=advertisment 
    def get_clicked(self):
        return self.clicked 
    def set_clicked(self,clicked):
        self.clicked =clicked
    def get_advertisment(self):
        return self.advertisment
    def set_advertisment (self,advertisment):
        elf.advertisment=advertisment
    def populate_advertsiment(self):
        clickedd=int(input("Did the user click the box?[1 yes/2 no]"))
        if (clickedd == 1):
            print("Good job here",self.get_advertisment())
        elif (clickedd == 2):
            print("Oh no go back and click it! ")
    def ToString(self):
        print("this advertisment",self.get_advertisment())
        print("this clicked",self.get_clicked()) 
        
if __name__ == "__main__":
    s1= Store("happy",1)
    s1.ToString()
    s1.populate_advertsiment()