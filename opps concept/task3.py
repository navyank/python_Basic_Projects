# Sum of first n even numbers
num=int(input("enter the number to count even numbers"))
sum=0
for i in range(0,num+1,2):
    sum+=i
print(sum)    