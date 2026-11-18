# table_num = int(input("Enter the number to print the table: "))
# i = 1
# while i <=10:
#     print(f"{table_num} * {i} = {table_num*i}")
#     i+=1

# initil = 1
# num = 5
# fact = 1

# while initil <= num:
#     fact *= initil
#     initil+=1
# print(fact)

# evaluating expressions and functions 
name = "atharv"
print(f"convert the name to upper case: {name.upper()}")

age = 21
print(f"my age this year is {age} & the next year is {age + 1}")

print("dictionary lookup")
user ={"role": "Admin"}
print(f"User role is: {user['role']}")


print("Decimal Converter")

# :.2f
# :,
# :%
# :.0%

print("number and currency formatting"'\n')
print(f"Fixed decimal places: {19.598:.2f}")
print(f"thousand seperator: {1000000:,}")
print(f"percentage conversion: {0.75:%}")
print(f"percentage with no decimal: {0.75:.0%}")


print("self documenting expression")
x = 10
y= 20

print(f"{x+y}")
print(f"{x+y=}")

print("date and time")

import datetime

today = datetime.datetime.now()
print(f"Today is: {today: %b, %d, %y}")
print(f"Today is: {today: %B, %d, %y}")
print(f"Today is: {today: %B, %D, %y}")
print(f"Today is: {today: %B, %D, %Y}")
print(f"Today is: {today: %b, %d, %Y}")
print(f"Today is: {today: %d %b %Y}")
print(f"Today is: {today: %Y %b %d}")

print("Padding alignment")
print(f"{'Atharv':>10}")
print(f"{'Atharv':^10}")

# count the digit in the number 
number = 123456
count = 0
while number > 0:
    digit = number % 10
    count+= 1
    number //=10
print(count)

# formating string using .format 

# name = input("ENter ur name: ")
# qualification = input("ENter ur qualification: ")

# print("i'm {} and i have done {}" .format(name, qualification))
# print("i'm {0} and i have done {1}" .format(name, qualification))
# print("i'm {0} and i have done {1}" .format(name, qualification))
# # using keyword argument
# print("i'm {n} and i have done {q}" .format(n=name, q=qualification))

# seperators in sting

print("{:.2f}".format(3.14236887))
print("{:,}".format(10000000))
print("{:<10}".format("hi"))
print("{:>10}".format("hi"))
print("{:.1%}".format(0.7568))
print("{:.2%}".format(0.7568))
print("{:b}".format(1)) #binary conversion
print("{:b}".format(2)) #binary conversion
print("{:b}".format(3)) #binary conversion
print("{:b}".format(4)) #binary conversion
print("{:b}".format(5)) #binary conversion
print("{:b}".format(6)) #binary conversion
print("{:b}".format(7)) #binary conversion
print("{:b}".format(8)) #binary conversion
print("{:b}".format(9)) #binary conversion
print("{:b}".format(10)) #binary conversion
print("{:b}".format(11)) #binary conversion

strs = "atharv"

print(len(strs))

user = {"name": "Atharv", "role": "Admin", "age" : 21}
marks = [85,97,59,57,87,83]

print("user {u[name]} logged in as {u[role]}".format(u=user))
print("{m[0]} {m[1]} {m[2]} {m[3]} {m[4]} {m[5]}" .format(m=marks))

print("{{{}}} loggin as admin" .format("atharv"))

precision = 4
print("{:.{}}" .format(3.14159265, precision))

