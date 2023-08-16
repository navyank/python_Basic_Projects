# Sum of digit until sum becomes a single digit
# num = int(input("Enter a number: "))
# while num > 9:
#     temp = num
#     sum_of_digits = 0
#     while temp > 0:
#         sum_of_digits += temp % 10
#         temp //= 10
#     num = sum_of_digits
# print("The sum of digits until it became a single digit is:", num)

num = input("Enter a number: ")
sum = 0
while len(num) > 1:
    for i in num:
        sum += int(i)
    num = str(sum)
    sum = 0
print("The sum of digits until it becomes a single digit is:", num)