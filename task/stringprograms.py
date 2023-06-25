# check for palindrome 
s1=' bob' 
if s1[1]==s1[-1]:
        print("palindrom") ####################palindrom not get properly
else:
        print("not palindrom")
# reverse of string 
s2='navya'
print(s2[::-1])    
# remove ith character in the string
for i in s2:
        s=s2[:1]+s2[3:]
print(s)
# find length of string in 4 different ways
print(len(s2))
count=0
for i in s2:
       count+=1 
print(count)  
i=0
c=0
while s2[c:]:
         c+=1    
print(c)
# Avoid Spaces in string & print its length
s3="navya nk"
print(len(s3))
d=list(s3)
l1=[]
for i in s3:
        if i==' ':
                continue
        else:
             l1.append(i)                      
print(len(l1))           
# Python program to print even length words in a string
s4='This is a very good day'
n=s4.split( )
for i in n:
     if len(i)%2==0:
            print(i)
# uppercase half string
s5='navya'
l=len(s5)
h=l//2
w=''
for i in range(l):
       if i>=h:
             w+=s5[i].upper()
       else:
              w+=s5[i]    
print(w)                
# capitalize frist and last letter in the given string
s6="navya"
t=s6[0].capitalize()+s6[1:-1].lower()+s6[-1].capitalize()
print(t)
# check if a string has at least one letter and one number
s7='navya2345'
print(s7.isalnum())
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
       print("not accepted")            
# Count the Number of matching characters in a pair of string  
st1="karshmor"
st2="kavya"
count=0
for i in st1:
       if i in st2:
            count+=1
print(count)                         
# count number of vowels using sets in given string
strin='navya'
v={'a','e','i','o','u'}
cunt=0
for i in strin:
       if i in v:
              cunt+=1
print(cunt)  
# Remove all duplicates from a given string in Python 
# ###########################################not get  
# program to find special characters in the string
lo={'!','@','#','$','%','&','*','()',',','.'}
cv=0
for i in strin: 
       if i in lo:
              cv+=1
       else:
              pass 
if cv>0:
       print("special characters are not allowed")
else:
       print(strin)                    

# Execute a String of Code in Python
sum='6+9'
print(eval(sum))
#  Check for URL in a String
# Permutation of a given string using inbuilt function
# Swap commas and dots in a String
st1='12.605.500, 002'
st2=',. '
st3=[]
st4='1234567890'
for i in st1:
    if i in st4:
        st3.append(i)
    elif i in st2:
        st3.append(i)#################################not get
    else:
        pass
print(st3) 
print(''.join(st3))
                
# find uncommon words from two Strings
st3="navya"
st4='kavya'
for i in st3:
       if i not in st4:
              print(i)
for i in st4:
       if i not in st3:
              print(i)              
#  Find all close matches of input string from a list
# Check if a given string is binary string or not
# program to split and join a string
st5='navya is very good girl'
l=st5.split()
print(l)
print('-'.join(l))
# program for removing i-th character from a string
st6="navya"
i=input("enter the value to be delete")
s=st6.replace(i,'')
print(s)
# Find words which are greater than given length k
# Generating random strings until a given string is generated
#  Frequency of numbers in String##############################18
# Specific Characters Frequency in String List
#  Odd Frequency Characters
# Maximum frequency character in String
# Least Frequent Character in String       