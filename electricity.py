bill=int(input("enter the unit of charge "))
if bill<=100:
    d=bill*0.50
    print(d)
elif bill>100 and bill<=150:
    d=((bill-100)*0.75)+(100*0.50)
    print(d)   
elif bill>150 and bill<=200:
    d=((bill-150)*1)+(50*0.75)+(100*0.50)
    print(d)    
elif bill>200:
      d=(50*0.75)+(100*0.50)+(50*1)+((bill-200)*2)
      print(d)
else:
    pass     