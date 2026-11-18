initial_num = 1
count = 0
# while initial_num <= 10: 
#     print(initial_num)
#     initial_num+=1

# while initial_num<=50:
#     # print(initial_num)
#     if initial_num % 2 == 0:
#         print(initial_num)
#         count+=1
#     initial_num+=1
# print(count)

print("---------- print reverse numbers-----------")
# final_val = 10
# while final_val != 0:
#     print(final_val)
#     final_val -=1

print("---------- find the sum of numbers from 1 To 10-----------")

# sum = 0
# while initial_num <=10:
#     sum+=initial_num
#     initial_num+=1
# print(sum)


print("---------- print the table gives the value from the user-----------")

# val = int(input("Enter the value to print the table: "))

# while initial_num <=10:
#     print(initial_num, "*", val, "=", initial_num*val)
#     initial_num+=1


print("---------- calculate the fatorial of a number-----------")

# fact = 1
# num = int(input("fimd factorial: "))


# while initial_num <= num:
#     fact *= initial_num
#     initial_num +=1
# print(fact)

i = 5
while i > 0:
    print(i)
    i-=1

str = 'madam'

reverse = ''

reverse = ''
for i in str:
   reverse = i + reverse
if str == reverse:
       print("is a palindrome")
else:
       print("is not a palindrome")
       

# print(reverse)

for num in range(2,101):
     for i in range(2, int(num/2)+1):
        if num % i == 0:
          break
     else:
            print(num)

# for num in range(2, 101):
#     # Check if num is divisible by any number up to its half
#     for i in range(2, int(num / 2) + 1):
#         if num % i == 0:
#             break  # Not a prime, exit the inner loop
#     else:
#         # If the loop finished without breaking, it's prime
#          print(num, end=" ")

number = int(input('enter the number to check is prime or not'))

if number <=1:
     print('enter the positive numberes')
else:
     for i in range(2, number):
          if number % i == 0:
               print('not prime number')
               break
     else:
        print('is prime')

for num in range(2, 101):
     for i in range(2, num):
          if num % i == 0:
               break
     else:
          print(num, end=' ')

