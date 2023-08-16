class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print("Hi my name is",self.name,"and I am",self.age,'years old')
class Student(Person):
    def __init__(self,name,age,student_id):
        Person.__init__(self,name,age)
        self.student_id=student_id
    def study(self):
        print("I am studying")
    def introduce(self):
           print("Hi my name is",self.name," I am",self.age,'years old,and my student ID is',self.student_id)
class Teacher(Person):
    def __init__(self,name,age,subject):
        Person.__init__(self,name,age)
        self.subject=subject
    def teach(self):
        print("I am studying")
    def introduce(self):
              print("Hi my name is",self.name," I am",self.age,'years old,and my student ID is',self.subject)
s=Student('navya',21,101)
s.study()
s.introduce()     
t=Teacher('akhil',28,'computer science')      
t.teach()
t.introduce()                
