#this is a default constuctor example 
class Animal:#parent class
    def speak(self):#self is a reference keyword
        print("Animal is speaking")
class Dog(Animal):#child class
    def bark(self):#parent class cant able to access child class 
        print("dog is barking")       
d=Dog()###in all single inheritance child class must be create object
d.speak()
d.bark()        