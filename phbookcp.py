import phbook
while True:
    print("enter the choice")
    print("1.add")
    print("2.edit")
    print("3.search")
    print("4.display")
    print("5.delete")
    print("6.exit")
    choice=int(input("enter your choice"))
    if choice==1:
        phbook.add()
    elif choice==2:
        phbook.edit()
    elif choice==3:
        phbook.search()
    elif choice==4:
        phbook.display()
    elif choice==5:
        phbook.delete()
    elif choice==6:
        r=input("are you sure do you want to exit(y/n)")
        if r=='y':
            exit()
        else:
            continue       
    else:
        print("invalid choice")   