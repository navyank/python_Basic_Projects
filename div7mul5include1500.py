num=int(input("enter the number"))
if num>=1500 and num<=2700:  # can also use while loop insted of if statement as "while num>=1500 and num<=2700:"
    if (num%7==0 and num%5==0):
      print("number is mul of 5 and div of 7")
    else:
      print("not mul of 5 and div of 7") 
                                          # as using while loop it must be decrement the number as "num=num-1500" 
                                          # other wise it will excute the block of code until the condition is true. 
else:      
    print("must be in the range of 1500 and 2700")      