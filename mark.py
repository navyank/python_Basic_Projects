maths=int(input("enter your mark in maths out of 100"))
cs=int(input("enter your mark in computer science  out of 100"))
phy=int(input("enter your mark in physics out of 100"))
total=maths+cs+phy
print("total mark =",total)
avg=total/3
print("average of these mark =",avg)
if avg>=90 and avg<100:
   print("your grade=A+")
elif avg>=80 and avg<90:
   print("your grade=A") 
elif avg>=70 and avg<80:
   print("your grade=B+")
elif avg>=60 and avg<70:
   print("your grade=B")
elif avg>=50 and avg<60:
   print("your grade=C+")
elif avg>=40 and avg<50:
   print("your grade=C")
elif avg>=30 and avg<40:
   print("your grade=D+")
else:
   print("you are failed!")                   