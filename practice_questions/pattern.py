digit = 123
total = 0

for i in str(digit):
    total += int(i)

print(total)

print(sum(map(int,str(digit))))

while digit > 0:
    last_digit = digit % 10
    total += last_digit
    digit //= 10
print(total)

def num_sum(a,b):
    print(a + b)

num_sum(12,10)

def greet(name="Guest"):
        print("Hello", name)

greet()
greet("Atharv")

def add(a, b):
    return a + b
    print("Done")

print(add(2, 3))

def largest(x,y):
     if x > y:
          print(f'{x} is greater')
     else:
          print(f'{y} is greater')
largest(1,5)

def square(num):
     return num ** 2
squared = square(5) 
print(squared)

def check(num):
    #  print(num % 2 == 0, 'even')
    if num % 2 == 0:
         print(f'{num} :even number')
    else:
         print(f'{num} :odd number')
check(41)

def largest_three_num(a,b,c):
    #  if a >= b and a >= c:
    #       return a
    #  if b >= a and b >= c:
    #       return b
    #  else:
    #       return c
    return max(a,b,c)

print(largest_three_num(81,8,81))

def factorial(num):
     fact = 1
     
     for i in range(1, num+1):
          fact *= i
        #   fact += 1
     print(fact)

factorial(5) 

def reverse(num):
     reverse_num = 0
     original = num
     while reverse_num > 0:
          digit = num % 10
          reverse_num *= 10 + digit
          num = num // 10

     print(reverse_num)
    # num = 122
    # original = num
    # reverse = 0
    # while num > 0:
    #     digit = num % 10 
    #     reverse = reverse * 10 + digit
    #     num = num // 10

    # print(reverse)
    # if original == reverse:
    #  print('is palindrome')
    # else:
    #  print('is not a palindrome')
reverse(121)