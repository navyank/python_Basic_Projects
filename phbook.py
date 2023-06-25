phbook={}
def add():
    name=input("enter the name")
    phno=int(input("enter your phone number"))
    phbook[name]=phno
    print("your details are stored successfully!")
    print("The stored details",phbook)
def edit():
    f=input("which one you want to edit(name/phno)")
    if f=='phno':
        name=input("enter the name ")
        if name in phbook:
           phno=int(input("enter the new phno"))
           phbook[name]=phno
        #    print(phbook)
           print("your phone number is edited successfully")
        else:
            print("contact not found")   
    elif f=='name':
        phno=int(input("enter the phone number"))  
        if phno in phbook.values():
            name=input("enter the new name") 
            phbook[name]=phno
            # print(phbook)
            print("your name is edited successfully")
    else:
        pass  
  
def search():
     name=input("enter the name to search")
     if name in phbook:
         print('phone number for',name,'is',phbook[name])
     else:
         print("searched item is not present ")    
def display():
    l=len(phbook)
    if l==0:
        print("contact not found")  
    else:
        print(phbook.keys(),'=',phbook.values())           
def delete():
    name=input("enter the name to delete")#####
    if name in phbook:
        del phbook[name]
        # print(phbook)
        print("deleted sucessfully")
    else:
        print('contact not found')    
