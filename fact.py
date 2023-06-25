num=int(input("enter the number"))
try:
 if num==0 or num==1:
    print("fact =",1)
 else:
    fact=1
    i=1
    while(i<=num):
        fact=i*fact
        i+=1
    print(fact)  
except:
       print("number must be greater than zero")       
     
# a=10
# b='navya'
# try:
#    print(a+b)
# except:
#    print("error")   