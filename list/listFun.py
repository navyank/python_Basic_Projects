mylist=[1,2,3,4,4,5,6,10]
print(mylist[0]) #44
print(len(mylist)) #45
mylist[0]=9
print(mylist)#46
print(mylist[-1]) #47
mylist.append(11)#48
print(mylist)
mylist.reverse()#49
print(mylist)
print(max(mylist))#50
print(mylist.index(5))#51
print(mylist.count(4))#52
# 53

fru=['apple','banana','cherry','kiwi','mango'] #55
l1=[]
for i in fru:
    if i!='kiwi':
        l1.append(i)
print(l1)

fruit=['apple','banana','cherry','kiwi','mango'] #54
li=[]
for i in fruit:
    if 'a' in i:
        li.append(i)
print(li)        

fruits=['apple','banana','cherry','kiwi','mango']   #55
list=[]
for x in fruits:
    u=x.upper()
    list.append(u)
print(list)  

u=[]
l=[]
str='NavYa nK'
for i in str:
    if i.isupper():
      u.append(i)
    elif i.islower():
       l.append(i)
    else:
        print('nothing')   
        

print('list of uppercase letter',u) 
print('list of lowercase letters',l)  

