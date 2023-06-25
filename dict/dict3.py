contactlist={}
n=int(input("enter the number of contacts :"))
for i in range(1,n+1):
      name=input("enter the contact name:")
      phno=int(input("Enter the phone number:"))
      contactlist[name]=phno##this line is used to store values in phno into key name
print(contactlist)      
print("Keys")
for x in contactlist.keys():
      print(x)
print("values")
for x in contactlist.values():
      print(x)
print("keys-value-pair")
for x,y in contactlist.items():
      print(x,"-",y)                   