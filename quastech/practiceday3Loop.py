print("Print using for loop")
for i in range(1 , 6):
    print(i * "*")

print("Print using for loop")
for i in range(1 , 6):
    print(i * "1")

print("Print using while loop")
condition = 1
while condition <=5:
    print(condition * "*")
    condition += 1

i = 1 
while i <=5:
    j = 1
    while j <= i:
        print("*", end='')
        j += 1
    print()
    i += 1

print("-----------------------------------------------")
for p in range(1 , 5):
    print(p * "1")

x= 5
for i in range(1,x+1):
    print(" " *(x-i)+ i * "*")

for i in range(1 , 11):
    print((i * "*").rjust(10))

a = 1
while a <= 10:
    b = 1
    k = 10
    while k >= a:
        print(" ", end="")
        k -= 1
    while b <= a:
        print("*", end="")
        b += 1
    print()
    a += 1

print("----------------------------------------------") 

num = 1

while num <= 5:
    num2 = 1
    while num2 <= num:
        print("a", end=" ")
        num2 +=1
    print()
    num +=1

print('----------------------------------------------')

pattern = 1
while pattern <= 5:
    pt = 1
    while pt <= pattern:
        print('','*', end='')
        pt +=1
    print()
    pattern +=1