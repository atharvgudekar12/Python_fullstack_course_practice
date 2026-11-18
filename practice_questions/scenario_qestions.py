employees = [
    ("Rahul", "IT", 50000),
    ("Amit", "HR", 40000),
    ("Sneha", "IT", 65000),
    ("Priya", "Finance", 55000),
    ("Raj", "IT", 70000)
]

# Using Python collections, find:

# Employees working in IT
# Highest salary
# Average salary
# Unique departments
# Employee with the highest salary

# name, *dep, salary = employees
# for i in employees:
#     for dep in i :
#         if dep == "IT":
#             dep = i
#             break
# print(name, dep)

# name, *dep, salary = employees
for name, dept,salary in employees:
    print(f"Name: {name} | Department: {dept} | salary: {salary}")

# sum of first n natural number get number from user 

n = int(input("enter the number to print sum of 1 n natural number: "))

# find factorial give value from the user 
fact = 1
for i in range(1, n+1):
    fact = fact*i
print(n)

num_sum = 0
# sum of 1st n natural number using loop 

for i in range(1, n+1):
    num_sum+=i
print(num_sum)

# sum of 1st n natural number using mathematical formula 
# num = int(input("Enter n: "))
total = sum(range(1, n + 1))
print(f"Sum: {total}")

# print all the number from 1 to 10 using loop 

num = 10 

for i in range(0, num):
    print(num - i)

print("-------------------------------------------------")
num_1 = 0
while num_1 != 100:
    num_1+= 1
    # num_1+= 2
    print(num_1)


sum_n = 0
print("-----------------------------------")
for i in range(1, 11):
    if i % 2 == 0:
        # printing even numbers 
        print(i* '*')
        # printing even numbers sum
        sum_n += i
print(f"sum of n even numbers : {sum_n}")

li = [22]
print(li)
