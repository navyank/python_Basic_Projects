
# arbitory 
def myFunction(*formal):
    print(type(formal))
    s=0
    for x in formal:
        s=s+x
    print("sum is",s)    
myFunction(10,20)  
myFunction(10,20,30,40,50)  
myFunction(10,2,15,5,26.3)
# reference

def  area(r):
    return (3.14*r**2)
def circumference(r):
    return (2*3.14*r)
radius=int(input("enter the radius:"))
print("area is",area(radius))
print("circumference is",circumference(radius))
# default
def func(x,ans):
    if(x==0):
        return 0
    else:
        return func(x-1,x+ans)###########doubt
print(func(2,66))    
def sum(*no):
    print(type(no))
    s=0
    for x in no:
        s=s+x
    return s
def add(p):
    print(p*6)
def avg(s):
    print(s/5)
sm=sum(10,20,30,40)
add(sm)
sm=sum(25,36,45,78,52) 
avg(sm)  
        #  
def interest(x,y,z):
	i=x*y*z/100
	return i
p=int(input("Enter the principle amount : "))
r=int(input("Enter the rate of interest : "))
t=int(input("Enter the period : "))
i=interest(p,r,t)
print("Simple Interest is : ",i)

def simple_interest(p,t,r=5):
	i=p*r*t/100
	return i
principle_amount=int(input("Enter the principle amount : "))
time_period=int(input("Enter the time duration : "))
rate_of_interest=int(input("Enter the rate of interest : "))
i1=simple_interest(principle_amount,time_period)
print("Interest : ",i1)
i2=simple_interest(principle_amount,time_period,rate_of_interest)
print("Interest : ",i2)
# amstrong
def amstrong():
     num=int(input("enter the number"))
     st=str(num)
     l=len(st)
     no=num    
     am=0
     while no>0:
          am+=(no%10)**(l)
          no=no//10       
     if am==num:
          print("amstrong") 
     else:
          print("not amstrong")       
amstrong()     
# binary to decimal
def binary(num):
    l1=str(num)
    st=l1[::-1]
    l=len(st)
    d=0
    for i in range(0,l):
         r=st[i]
         d+=int(r)*(2**(i))
    print(d)
binary(input("enter the binary number"))    

'''def product(a, b):
        return(a*b)

print(product(product(2,4), product(3,5)))'''
def decimal(no):
     while no>=1:
        print(no%2)
        no=no//2
decimal(int(input("enter the number")))           
      
   



