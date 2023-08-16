class Basic:
    def __init__(self,name,age):#parameterised constuctor
        self.name=name
        self.age=age
obj1=Basic("kavya",20)
print(obj1.name)
print(obj1.age)        
obj2=Basic("jacki",28)
print("my name is:",obj2.name)
print("my age is:",obj2.age)
print(obj1.name,obj1.age)