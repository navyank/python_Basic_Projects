a=[]
n=int(input("enter the number of elements:"))
print("enter the element")
for i in range(0,n):
    k=int(input())
    a.append(k)
big=a[0]
for i in range(1,n):
    if a[i]>big:
        big=a[i]
print("Biggest:",big)            