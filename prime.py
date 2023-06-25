lower=int(input('enter the lowerer number'))
upper=int(input('enter the upper number'))

# def prime(num):
for num in range(lower,upper+1): 
  if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
              break
       else:
           print('prime number',num)   
# r=int(input("enter the number"))           
# prime(r)           