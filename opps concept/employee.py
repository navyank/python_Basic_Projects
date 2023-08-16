class Employee:
    def __init__(self,empname,empcode):
        self.empname=empname
        self.empcode=empcode
    def details(self):
        print(self.empname)
        print(self.empcode)
class Manager(Employee):
    def __init__(self,empname,empcode,bsalary):###pic name and code from parent class
       Employee.__init__(self,empname,empcode)
       self.bsalary=bsalary
    def calculate(self):
        self.netsalary=self.bsalary+self.bsalary*0.2
        print("basic salary:",self.bsalary)
        print("net salary:",self.netsalary)
m=Manager("navya",101,25000)
m.details()
m.calculate()           