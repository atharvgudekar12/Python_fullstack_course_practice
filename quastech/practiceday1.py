# find largest number in the list without max function

find_largest = [10,25,7,40,15,50,100,38] 

# print(max(find_largest))

# find_largest.sort()
# print(find_largest[-1])

# print(find_largest)
# find_largest.reverse()
# print(find_largest[0])

# print(find_largest)

# using for loop 

large_num = max(find_largest)

for i in find_largest:
   if i > large_num:
      large_num = i
print(large_num)

# to find second maximum value 
print("second max")
second_max = find_largest[0]
for i in find_largest:
    if i > second_max and i < large_num :
     second_max = i
print(second_max)


list_2 = [12,34,45,3,32,234,5,5,56,90,6]
list_3 = [12,34,45,3,324,24,5,95,56,64,86,12]

middle_num = int(len(list_2)/2)
print('middle value present on index num', middle_num)
print(list_2[middle_num])

# to find even value list 
middle_num2 = int(len(list_3)/2)
print('middle value present on index num', middle_num2, middle_num2-1)
print("Middle value of even list is : ", list_3[middle_num2],'&', list_3[middle_num2 -1])

# print(3**3)
# print(15//3)

student_marks = [78,39,49,50,97,"Vedant",86,83,'atharv.gudekar@gmail.com',50,36,47,45,90,"Atharv","Gudekar"]

count = 0

for marks in student_marks:
   if isinstance(marks, int) and marks >= 50:
      count+=1
print(count)

# print(isinstance(student_marks, int))                                   