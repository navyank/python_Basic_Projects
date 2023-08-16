class Vehicle:
    def __init__(self,name,color,price):
        self.color=color
        self.price=price
        self.name=name
    def display(self):
        print("The colour of vehicle",self.color)
        print("The price of vehicle",self.price)     
        print("The name of vehicle",self.name)
class Bus:
    def __init__(self,name,color,price):
        Vehicle.__init__(self,name,color,price)       
    def display(self):
        print("The colour of vehicle is",self.color,", The price of vehicle is",self.price," and The name of vehicle is",self.name)     
v=Bus('bus','black','2022022') 
v.display()       