s = "Python"
print(s[0], s[-1], s[1:4])

# Write code to reverse a string.
st = "Atharv"
print(st[::-1])

# Write code to count the vowels in a string.
count = 0
for i in st.lower():
    print(i)
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
     count += 1
print(count)

print(st.strip()) #remove the extra space

# Check if a string is a palindrome (e.g. “madam”).

palindrome = "ayh"
rev = palindrome[::-1]
if palindrome == rev:
    print('it is palindrome')
else:
    print('it is not palindrome')

reverse = ''
for i in palindrome:
    reverse = i + reverse

print(reverse)

# num =  212

# if num:
#    num(reversed= True)
#    print('it is palindrome')
# else:
#    print('it is not palindrome')


my_list = [12,25,3,4,647,5,47]

large_num = my_list[0]

for i in my_list:
   if i > large_num:
      large_num = i
print(large_num)

stri = "Atharvsanika"
vovels = 'aeiou'
count2 = 0
for i in stri.lower():
 if i in vovels:
   count2 +=1
print(count2)

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

# check the number is palindrome or not 
print('---------------------------------------')
num = 122
original = num
reverse = 0
while num > 0:
    digit = num % 10 
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print('is palindrome')
else:
    print('is not a palindrome')


for num in range(2,101):
    for i in range(2,num):
        if num % i == 0:
            break 
    else:
        print(num, end=' ')

