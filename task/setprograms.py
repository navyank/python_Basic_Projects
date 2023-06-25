# Find the size of a Set in Python
s1={1,2,3,4}
print(len(s1))
# Iterate over a set in Python
for i in s1:
    print(i)
# Maximum and Minimum in a Set
print(max(s1))    
print(min(s1))
#  Remove items from Set
s1.pop()
print(s1)
s1.remove(3)
print(s1)
# Check if two lists have at-least one element common
l1=[1,2,3,4]
l2=[5,3,5,2]
l3=[]
for i in l1:
    if i in l2:
       l3.append(i)
print(l3,'are common in both lists')
# program to find common elements in three lists using sets
l4=[1,2,3,4,5]
l5=[7,8,5,4,7,8,9,2]
l6=[1,4,5,6]
s2=set(l4)
s3=set(l5)
s4=set(l6)
k=s2.intersection(s3,s4)
print(k)
l=list(k)
print(l)
#  Find missing and additional values in two lists
q=s2.difference(s3)
l=s3.difference(s2)
p=list(q)
w=list(l)
print(p,'is the missing values in',l5)
print(w,'is the additional values in',l4)
# Difference between two lists
print(p,'is the missing values in',l5,'according to ',l4)
# Convert a set into dictionary
s6={'navya'}
for i in s6:
    r={i:18 }
    print(r)    
# program to convert String to Set
string='navya'
s=set(string)
print(s)
#  program to convert Set to String
s7={1,2,3,4,5}
st=str(s7)
print(st)
print(type(st))
# program to convert set into a list
li=list(s7)
print(li)
# program to convert Set into Tuple and Tuple into Set
tu=tuple(s7)
print(tu)
s8=set(tu)
print(s8)
# program to check whether a given string is Heterogram or not
st1='aaCdefGh ijkL mno'
v=sorted(st1.lower())
c=0
for i in range(1, len(v)):
        if v[i] == v[i-1] and v[i].isalpha():
            c+=1
if c>0:
     print("no")
else:
     print("yes")     
# Pairs of complete strings in two sets  
###############################################
# Python set to check if string is pangram
st2="abcdefghijklmnopqvwxyz"   
r=st2.replace(" ",'')
print(r)
d=r.lower()
co=0
alp={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
for i in alp:
     if i not in d:
          co+=1
     else:
          co=0
        #   print("panagram")
        #   co+=1
if co>0:
     print(" not pangram")              
else:#####################################not completed##################################
     print("panagram")    

# Set difference to find lost element from a duplicated array     
l10=[1,2,3,4]
l11=[1,2,3]
s=set(l10)
s12=set(l11)
if len(l10)!=len(l11):
     h=s.difference(s12)
print(h)     
# program to count number of vowels using sets in given string
st1='aeiou'
l=set(st1)
print(l)     
hu="navya"
count=0
for i in hu:
     if i in l:
          count+=1         
print('number of vowels = ',count)
# Concatenated string with uncommon characters in Python
st3="navya"
st4='kavya'
ss=set(st3)
ss1=set(st4)
n=ss.intersection(ss1)
print(n)
ss5=[]
for i in ss:
    if i not in n:
       ss5.append(i)
 
for i in ss1:        
    if i not in n:
        ss5.append(i) 
print(ss5)   
print(''.join(ss5)) 
# print(type(f))
# Program to accept the strings which contains all vowels
vow={'a','e','i','o','u'}
sen='aeion'#input("enter the sentence")
s8=set()
for i in sen:
       if i in vow:
              s8.add(i)
       else:
             pass
if len(s8)==len(vow):
       print("accepted") 
else:
       print("not accepted")  ############################6

# Python – Check if a given string is binary string or not##################################
s9={0,1}
sd='10'
k=set(sd)
for i in s9:
     if i not in k:
          print("yes")
     else:
          print("no")     



