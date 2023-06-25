a=[]
n=int(input("enter the number of elements:"))
print("enter the elements:")
for i in range(0,n):
    k=int(input())
    a.append(k)
index=int(input("enter the index:"))
for i in range(index,n-1):
    a[i]=a[i+1]    
n=n-1
print("list element are:")
for i in range(0,n):
    print(a[i])    