from abc import ABC#abstraction abc=module,ABC=class
class Car(ABC):##ABC became parent class#inheritance
    def mileage(self):
        pass
class Tesla(Car):
    def mileage(self):
        print("The mileage is 30 kmph")   
class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25 kmph")
class Duster(Car):
    def mileage(self):
        print("The mileage is 24 kmph") 
class Renault(Car):
    def mileage(self):
        print("The mileage is 27 kmph")     
t=Tesla()
t.mileage()
r=Renault()
r.mileage()
s=Suzuki()
s.mileage()
d=Duster()
d.mileage()              

