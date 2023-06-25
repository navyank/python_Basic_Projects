mydict={1:'navya',2:'kavya',3:'anu'}
print(mydict)
d=dict({1:'vardha',2:'megha',3:'ammu'})##################dict method is used to create dictionary
print(d)
print(type(d))
print(mydict[2])
print(d.get(2))
# print(d.get(9))###################this line doesnt print any error while the code doesnt contain the key 9.it will only print None
# print(d[9])#####################this line will show key error ie,the key 9 is not present in the key  
d[1]='unni'
print(d)
d[4]='anjana'
print(d)
print(d.pop(3))#############remove the value in the given key
print(d)
print(d.popitem())##############remove last keyvalue pair
print(d)
d[2]='navya'
print(d)
print(mydict.clear())##################this line doesnot delete complete dictionary it only clear all values in dictionary.
del mydict
# print(mydict)##########################this line shows error ie,mydict dictionary is already deleted using del keyword
marks={}.fromkeys(['maths','eng'],80)##############this fromkeys are used while we have keys have same values
print(marks)
for i in marks.items():#######items are used to access items in marks
    print(i)
print(list(sorted(marks.keys())))    #########to access the keys in mark in sorted order in list form

# convert two list into dictionary
l1=[1,2,3,4]
l2=['a','b','c','j','p']
d1=dict(zip(l1,l2))
print(d1)