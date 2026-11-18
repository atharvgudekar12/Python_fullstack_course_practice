# A customer add products to a shopping cart 
cart = ["Laptop", "Mouse", "Keyboard", "Mouse"]
# Tasks:
# - Add "Headphones" to the cart.
# - Remove one "Mouse".
# - Print the total number of products.
# - Check whether "Laptop" is in the cart.

cart.append("Headphone")
print(cart)

cart.remove("Mouse")
print(cart)

total_products = len(cart)
print(total_products)

for i in cart:
 if i  == "Laptop":
    print(True)


marks = [45, 78, 32, 90, 56, 28, 67,4]

# Tasks:
# - Find all marks greater than 50.
# - Count how many students passed (passing marks = 35).
# - Find the highest and lowest marks.
# - Calculate the average marks.

count = 0
for i in marks:
  if i > 50:
    print(i)
    count += 1
print(count)

pass_student = 0 

for i in marks:
  if i >= 35:
    pass_student += 1
print(pass_student)


highest_mark = marks[0]

for i in marks:
  if i > highest_mark:
    highest_mark = i
print(highest_mark)

lower_marks = marks[0]

for i in marks:
  if i < lower_marks:
    lower_marks = i
print(lower_marks)

# avg = 0
sum_marks = 0
for i in marks:
  sum_marks += i
  avg = sum_marks/len(marks)
print(sum_marks)
print(avg)


attendance = ["Present", "Absent", "Present","Present", "Absent", "Present"]

# Tasks:
# - Count present and absent employees.
# - Calculate the attendance percentage.
# - Print "Warning" if attendance is below 75%.

count_present = 0
count_absent = 0
for i in attendance:
  if i.lower() == "present":
    count_present += 1
  else:
    count_absent += 1
    
print(count_present)
print(count_absent)


sum_attendance = int(len(attendance))
count_pre = 0
for i in attendance:
  if i.lower() == "present":
    count_pre += 1
    percentage = count_pre/sum_attendance*100
print("Attendance percentage : ",percentage)
print(sum_attendance)
print(count_pre)


if percentage <= 75:
    print("Warning")
else:
  print("Great")


expenses = [120, 250, 80, 400, 150]

# Tasks:
# - Calculate the total expenses.
# - Find expenses greater than ₹150.
# - Add a new expense of ₹300.
# - Find the second-highest expense.

total_expenses = 0
for i in expenses:
  total_expenses += i
print(f"Total Expense : {total_expenses}")

for i in expenses:
  if i > 150:
    print(i)

expenses.append(300)
print(expenses)

highest_expense = max(expenses)
second_high = expenses[0]

for i in expenses:
  if i > second_high and i < highest_expense:
    second_high = i
print(second_high)

expenses.sort()
print(expenses[-2])


usernames = ["rahul", "amit", "priya", "rohan", "atharv"]

# Tasks:
# - Check if a username already exists.
# - Add a new username only if it is not already present.
# - Make the username check case-insensitive.

# find_name = input("enter user name to check it exists or not : ")
# for i in usernames:
#   if i == find_name:
#     print(f"user '{i}' found in the list")
#     break
# else:
#     print("user is not exists")

# for i in usernames:
#   if i != i:
#     i.append("sanika")
# print(i)
  

# add() is only use when the value is not in the list 
new_user = "atharv"

if new_user not in usernames:
  usernames.append(new_user)
  print(usernames)
else:
  print("user is already found")


customer_ids = [101, 102, 101, 103, 102, 104, 101]
# Remove duplicates while preserving the original order.
unique_list = []
unique = set()
for x in customer_ids:
  if x not in unique:
   unique_list.append(x)
   unique.add(x)
print(unique_list)

# 2nd method using dict 
unique_ids = list(dict.fromkeys(customer_ids))
print(unique_ids)

# 8. Separate Even and Odd Numbers
numbers = [12, 7, 9, 20, 33, 44, 51, 60]

even_num = list()
odd_num = list()

for i in numbers:
  if i % 2 == 0:
    even_num.append(i)
  else:
    odd_num.append(i)
print(even_num)
print(odd_num)


transactions = [500, -200, 1000, -150, 300]
# Create a new reversed list without modifying the original.
original_list = transactions
reversed_list = list()
copy_list = transactions.copy()
copy_list.reverse()
reversed_list.append(copy_list)

print(original_list)
print(reversed_list)


candidate1 = ["Python", "SQL", "HTML", "Git"]
candidate2 = ["Python", "JavaScript", "SQL", "CSS"]
# Find the skills common to both candidates using lists and loops, without converting the lists into sets.

# skills_match = list()
# for i in candidate1 and x in candidate2:
#   if i in x:
#     skills_match.append(i)
# print(skills_match)