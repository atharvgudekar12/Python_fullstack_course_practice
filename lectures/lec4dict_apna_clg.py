# # Dictionary in python
# # dictionary are use to store the data values in key: pairs
# # theu are unordered mutable and dont allow duplicate keys 

# dict = {
#     "name" : "atharv",
#     "cgpa" : 8.32,
#     "marks" : 85.90,
#     "subjects" : ["python", "django"],
#     "topics" : ("dictionary", "set"),
#     "is_adult" : True
# }

# # dict("key" : value)

# dict["name"] = "shravani"

# \
# print(dict)

# dict = {}

# name = input("enter your name : ")

# dict["name"] = name

# print(dict)


# nested dictionary 

student = {
    "name" : "Atharv", 
    "info" :{
        "age" : 21,
        "CGPA" : 8.32,
        "destination" : "python developer"
    }
    
}

# print(student["info"]["CGPA"])
print(list(student.keys()))


age = 18
income = 50000

if age >= 18 and income >= 30000 :
    print("you are eligible and qualify the loan")
else :
    print("you are not eligible and not qualify the loan")

if age >= 18 :
    print("you are eligible")
    if income >= 30000:
        print("eligible for loan")
    else:
        print("you are not eligible for thr loan")
else:
    print("you are not eligible")

count = 0

while count <=5 :
    print(count)
    count +=1

fruits = ["apple","banana","grapes","pineapple","mango","orange"]


# for i in range (14, 20) :
#     print(i)
for fruit in fruits :
    print(len(fruit))

for fruit in fruits :
    print(fruit[0:])

for i in range(1,6):
    for j in range(1,6):
        print(i*j ,end= " ")
    print()

# name = input("Enter your name : ")

# def greet(hello):
#     print(f"Hello  {hello}")

# greet(name)

def add_numbers(num1, num2):
    sum = num1+num2
    return sum

result = add_numbers(5,5)
print(result)


global_var = 10
def scope():
    local_var = 20
    print(global_var)
    print(local_var)

scope()
print(global_var) 

file = open("C:\Users\ATHARVA GUDEKAR\Desktop\python Developer\lectures\demo.txt", "r")
# content = file.read()
content = file.delete()
print(content)
# file.close()