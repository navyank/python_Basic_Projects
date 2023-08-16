# sample class program
class Basic:#class is created
    def __init__(self,name,age):#CONSTUCTOR is created
        self.name=name#self is a reference keyword
        self.age=age
    def sample(self):
        print("my name is:",self.name) 
        print("my age is:",self.age)   

obj=Basic('navya',21)
obj.sample()         
        # 
