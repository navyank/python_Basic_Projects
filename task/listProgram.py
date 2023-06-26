# write a programm to interchange frist and last element in the list

l1=[1,2,3,4,5,6]
print("the original list",l1)
l1[0],l1[-1]=l1[-1],l1[0]
print("the interchanged list",l1)
# write a program to swap two elements in the list

l2=[3,5,6,9,1]
print("the original list",l2)
l2[0],l2[1]=l2[1],l2[0]   #swap two elements without temp 
print("The swaped list",l2)

# swap elements in string list
l3=['apple','orange','grapes']
print("original list",l3)  ##################this lines are to swap items in the list
l3[0],l3[1]=l3[1],l3[0]
print(l3)
l4=[]
for i in l3:
    s=i.replace('e','G') #####################this lines to swap letters in list
    l4.append(s)
print(l4)

# ways to find length of string
l5=[1,2,5,8,67]
print(len(l5)) #without loop
count=0
for i in l5:#using loop
    count+=1
print("length of list",count)    

# maximum of two values in python
a=10
b=9
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")    

# minimum of two numbers in python
if a<b:
    print("a is less than b")
else:
    print("b is less than a")    
#check if elements exit in the list 

l6=[8,9,7,6,3,1]
if 3 in l6:
        print("present")
else:
        print("not present")    
  
# clear a list
l7=[1,2,3]
print(l7)
l7.clear()
print(l7)

# reversing a list
l8=[1,2,3,4]
print(l8[::-1])
l8.reverse()
print(l8)

# cloning and coping list
l20=[1,2,3,4,5,6,10,7]
l21=l20.copy()
print(l21)
# count occurance of elements in the list
l9=[1,1,2,2,3,9,8,7,7,6]
print(l9.count(1))
# sum and avg in list
l10=[1,2,3,4,5]
su=0
i=0
while i<len(l10):
     su+=l10[i] 
     i+=1
print(su) 
avg=su//len(l10)      
print(avg)  

s=sum(l10) ############using sum function
print(s)
# sum of number digit in list
l22=[1,2,3,4,5]
print(sum(l22))
# multiply all elements in list
l11=[1,2,3,4,5]
mul=1
i=0
while i<len(l11):
     mul*=l11[i]
     i=i+1
print(mul)     
# smallest number in the list
l12=[1,6,8,34,0]
l12.sort()
print(l12[0])
print(min(l12))
# largest number in the list
print(l12[-1])
print(max(l12))
# second largest number inthe list
print(l12[-2])
# odd and even numbers in the list
l13=[1,2,3,4,5,6,7,8,9]
l14=[]
l15=[]
for i in l13:
     if i%2==0:
          l14.append(i)
     else:
          l15.append(i)     
print("even numbers",l14)
print("odd numbers",l15) 
# odd number in the range    ######################3
for i in range(1,10,2):
     print(i) 
print("loop closed")      
#even number in the range
for i in range(0,10,2):
     print(i)  
#count  even and odd numbers in the list
even=0
odd=0
for i in l13:
     if i%2==0:
          even+=1
     else:
          odd+=1
print("even",even) 
print("odd",odd) 
# print positive and negative numbers in list   
l16=[-1,-2,-3,-4,-5,9,8,7,6,5,3]
l17=[]
l18=[]
for i in l16:
     if i>0:
          l17.append(i)
     else:
          l18.append(i) 
print("podsitive",l17)  
print("negative",l18)  

# print all positive numbers in a range
for i in range(-9,10):
     if i>0:
          print(i)
print("loop closed")          
#print all negative numbers in a range
for i in range(-9,10):
     if i<0:
          print(i) 
#count number of positive and negative number in a list
pos=0
neg=0
for i in l16:
     if i>0:
          pos+=1
     else:
          neg+=1      
print("positive numbers =",pos)   
print("negative numbers=",neg)   

# remove multiple elements in the list
l19=[1,2,3,4,5,6]
for i in l19:
     if i%2==0:
          l19.remove(i)
print(l19)          
# to print list of duplicate elements
li=[1,1,2,2,3,4,4,5,6,7,7,90,90]
ss1= []  
for i in li:
      b = li.count(i)
      if b > 1:
         if ss1.count(i) == 0: 
             ss1.append(i)
print(ss1)
# remove empty tuple from a list##########################
t1= [(), ('navya','15','8'), (), ('keerthika', 'ram'),
          ('unni', 'john', '45'), ('',''),()]
tup = [t for t in t1 if t]
print(tup)
sum of digit
def sum():
   no=int(input("enter the number"))
   s=0
   while no>0:
      s=s+no%10
      no=no//10
   print(s)  
sum()

def sum(num):
    s=0
    str1=str(num)
    for i in str1:
        s=s+int(i)
    print(s)  
sum(123)     

vowels
li1=['a','e','i','o','u']
   
hu=input("enter the name")
def vowel(li1):
   count=0
   for i in hu:
     if i in li1:
          count+=1         
   print('number of vowels = ',count)
vowel(['a','e','i','o','u'])   
# palindrom

def pali(num):
    str1=str(num)
    rev=str1[::-1]
    if rev==str1:
        print("pali")
    else:
        print("not pali")   
   
pali(101)  

'''
def fun(*x):
   s=0
   for i in x:
      s=s+i
   print(s)   
    
fun(1,2,3)    '''
list=[2,3,4]

 
def add(): 
    list.append(5)
    print(list)
add()      
def avg():
     sum=0 
     for i in list:
         sum+=i 
     print(sum)    
     avg=sum//len(list) 
     print("average of numbers:",avg) 
avg()



    
 
