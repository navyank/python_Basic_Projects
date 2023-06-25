num=int(input("enter the number:"))
print("Menu")
print("1.automorphic")
print("2.Trimorphic")
choice=int(input("enter yor choice:"))
l=len(str(num))
if choice==1:
    sq=num**2
    if sq%(10**l)==num:
        print(num,"is automorphic")
    else:
        print(num,'is not automorphic')#############not 
elif choice==2:
    cb=num**3
    if cb%(10**l)==num:
        print(num,'is trimorphic')
    else:
        print(num,'is not trimorphic')#########not
else:
    print("invalid choice")                                