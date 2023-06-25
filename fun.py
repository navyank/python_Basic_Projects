# factorial
num=int(input("enter the number"))
def fact():
      if num<0:
        print("number must be greater than zero")
      elif num==0 or num==1:
        print("fact =",1)
      else:
        fact=1
        i=1
        while(i<=num):
          fact=i*fact
          i+=1
        print(fact)   
fact() 
# # area  
# a=10
# def area():
#      area=a*a
#      print(area)
# area()  
# # evenorodd
# num=int(input('enter the number'))
# def evenodd():
#     if num%2==0:
#         print("this number is a even number")
#     else:
#         print("this number is a odd number") 
# evenodd()  
# # multiplication
# def mul():
#     num=int(input("enter the number"))
#     for i in range(11):
#         t=i*num
#         print(i,'*',num,'=',t)
# mul()  
def facto():
    n=int(input("enter the number"))
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)    
facto()           