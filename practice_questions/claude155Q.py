# Write a function that returns the sum of two numbers.
def num_sum(a,b):
    return a + b
print(num_sum(5,15))

# Write a function to check if a number is even or odd.
def check(num):
    if num % 2 == 0:
     return 'even'
    else:
       return 'odd'
print(check(4))

# Write a function to find the factorial of a number.
def fact(num):
   if num == 1 or num == 0:
      return 1
   else:
      return num * fact(num - 1)
print(fact(5))

# Write a function to check if a number is prime.
def prime(num):
   if num <= 1:
      return False
   for i in range(2 , num):
      if num % i == 0:
         return False
   return True
# print(prime(97))
n = 7
if prime(n):
   print('prime number')
else:
   print('Not a prime number')

# Write a function that returns the largest number in a list.
def largest_num(numbers):
    largest = numbers[0]
    for i in numbers:
      if i > largest:
         largest = i
    return largest

my_list = [12,45,65,87,288]
result = largest_num(my_list)
print(result)

# Write a function to reverse a string.
def reverse_str(rev):
   reverse = ''
   for i in rev:
      reverse = i + reverse
   return reverse

str1 = "atharv"
result = reverse_str(str1)
print(result)

str2 = "sanika"
reversestr = ''
for i in str2:
   print(i)
   reversestr = i + reversestr
print(reversestr)

# Write a function to count vowels in a string.

string = "India is my country all Indians are my brothers and sisters."

def vovels_count(string):
   count = 0
   vovel = 'aeiou'
   for i in string.lower():
      if i in vovel:
         count += 1
   print(count)
vovels_count(string)