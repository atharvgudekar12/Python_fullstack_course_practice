# data = ["atharv", "python",2,3,5,6,9,"RPA"]

# numbers = []

# for item in data :
#     if isinstance(item, int):
#         numbers.append(item)
#         max_num = max(numbers)
#         min_num = min(numbers)
#         sum_num = sum(numbers)
# print(max_num)
# print(min_num)
# print(sum_num)


# # to find first and last name in 
# # email = 'atharv.gudekar@gmail.com'

# # name = email.split("@")[0]
# # first_name, last_name = name.split(".")

# # # print(name)
# # print(first_name)
# # print(last_name)

mail = 'rahul.sharma@gmail.com'

# name, domain = mail.split("@")
# first_name, last_name = name.split(".")
# print(domain)
# print(name)
# print(first_name)
# print(last_name)

# highest = [10,25,7,40,15]

# highest.sort()
# print(highest)
# print(highest[-2])
# print(highest.pop(-2))

name, surname = mail.split("@")[0].split(".")
domain = mail.split("@")[1]
print(domain)
print(name, surname)


x = "10"
y = 5

print(int(x) + y)
print(type(x + str(y)))
e = None
print(type(e))

print(10/3)
print(10//3)
print(10%3)
print(10**3)
print(10*3)

print(10 == '10')
print(bool(0))
print(bool(1))

# num_1 = float(input("enter the number 1:"))
# num_2 = int(input("enter the number 2:"))

# print(num_1 + num_2)
# print(num_1 - num_2)
# print(num_1 * num_2)
# print(num_1 % num_2)
# print(num_1 / num_2)

# if num_1 % 2 == 0:
#     print(f"numner is even : {num_1}")
# else :
#     print(f"number is odd {num_1}")

# age = int(input('enter your age'))

# if age >= 18 and age <=100:
#     print("eligible to vote")
# else:
#     print("not eligible")

num_2 = int(input("enter the number 2:"))
num_3 = int(input("enter the number 2:"))

