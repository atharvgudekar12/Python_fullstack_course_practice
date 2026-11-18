marks = [58,89,74,25,48,25,59,69,46]

for mark in marks:
    print(mark)

print("print 1 to 10 numbers ")
for i in range(11):
    print(i)

print("print even numbers")
for enven in range(0,10,2):
    print(enven)

print("print odd numbers")

for odd in range(1,10,2):
    print(odd)


count = 0
# Loop from 2 to 100 (1 is not a prime number)
for num in range(2, 101):
    # Check if num is divisible by any number up to its half
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            break  # Not a prime, exit the inner loop
    else:
        # If the loop finished without breaking, it's prime
         print(num, end=" ")
         count+=1
print("count is ", count)

# num = int(input("Enter the number to print the square upto that number: "))

for i in range(1, num+1):
    print(i**2)

for i in range(num, 1, -1):
    print(i)


# continue and break

print("---------Continue & Break--------------")
for i in range(1, 10, 1):
    if i == 6:
        continue
    print(i)

print("-----------Break------------")
for i in range(1, 10, 1):
    if i == 6:
        break
    print(i)

print("-----------else------------")
for i in range(1, 10, 1):
    if i == 11: #out of range value means the value is 11 is out of 10 in above range function
        break
    print(i)
else:
    print("loop was't interrupted")


num = 1

while num <= 101:
    if num  % 2 == 0:
     print(num)
    num += 1
