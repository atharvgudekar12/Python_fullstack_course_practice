# num = 153
# sum = 0
# for i in str(num):
#     i = int(i)
#     cube = i ** 3
#     sum = sum + cube
#     print(i)
# print(sum)



# digit = 0
# for i in str(num):
#     i = int(i)
#     power = i ** len(str(num)) 
#     digit = digit + power
#     print(i)
# print(digit)

# if digit == num:
#     print("it's armstrong number")
# else:
#     print("it's not a armstrong number")

# def armstrong(num):
#     digit = 0
#     for i in str(num):
#       i = int(i)
#       power = i ** len(str(num)) 
#       digit = digit + power
#     #   print(i)
#     print(digit)

#     if digit == num:
#         print("it's armstrong number")
#     else:
#        print("it's not a armstrong number")

# armstrong(153)


num = 1634

temp = num

sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** len(str(num))
    temp //= 10
print(sum)
 
if digit == num:
    print("it's armstrong number")
else:
    print("it's not a armstrong number")


# reversed a number and check a number is palindrome or not
reverse = 121
reverse_num = 0
original = reverse
while reverse > 0:
    digit = reverse % 10
    reverse_num = reverse_num * 10 + digit
    reverse //= 10
print(reverse_num)

if original == reverse_num:
    print("It's palindrome")
else:
    print("It's not a palindrome")