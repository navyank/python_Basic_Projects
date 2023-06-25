a=[]
n=int(input("enter yhe limit array"))
print("enter the element")
for i in range(0,n):
    no=int(input())
    a.append(no)
big=a[0]
for i in range(1,n):
    if a[i]>big:
        big=a[i]  
if big==a[0]:
    
    sbig=a[1]
else:
    sbig=a[0] 
for i in range(0,n):
    if a[i]<big and a[i]>sbig:
        sbig=a[i]
print("Second largest is:",sbig)                         