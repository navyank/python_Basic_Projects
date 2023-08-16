
class Car:
    def __init__(self,color,name,price):
        self.color=color
        self.name=name
        self.price=price
       
    def details(self):
        print("car color is:",self.color)
        print("car price is : ",self.price)
        print("car name is:",self.name)
               
class Toyota(Car):
      def __init__(self,name,color,price):
           Car.__init__(self,color,name,price)
           
      def available(self):
        if self.price<1900000:
            print( 'not available')
        else:
            print ('available')
class Maruti(Car):
      def __init__(self,name,color,price):
           Car.__init__(self,color,name,price)
           
      def available(self):
        if self.price<1500000:
            print( 'not available')
        else:
            print( 'available')        
m=Maruti('maruthi','black',2000000)
m.available() 
t=Toyota("toyota",'white',590000)
t.available()      
m.details()
t.details()     