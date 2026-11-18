list_1 = [10,20,30,40,50]

# print first last and middle element
start, *value, end = list_1
print(start)
print(value)
print(end)

print(list_1[0])
print()
print(list_1[-1])

list_1.append(60)
print(list_1)

list_1.insert(1, 100)
print(list_1)

list_2 = [10,1000,2000,3000,4000]
list_1.extend(list_2)
print(list_1)

# add 60 remove 30 and reverse the list 
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
print(numbers)
numbers.remove(30)
print(numbers)
numbers.reverse()
print(numbers)
print("reverse", numbers[::-1])

str ="ATHARV"
if str[::-1] == str:
 print(True)
else:
 print(False)

a = [1, 2, 3]
a.append([4, 5])

print(a)
print(len(a))

a.append(20)
print(a)

a = [1, 2, 3]
b = a
b.append(4)

print(a)
print(b)

# find the 2nd largest number in list 

list_largest  = [10,45,20,67,34,67,12]
list_largest.sort()
print(list_largest[-2])


marks = [45, 78, 32, 90, 56, 89, 40,50]

print(max(marks))
print(min(marks))
print(len(marks))
print(sum(marks)/len(marks))
print(marks.count(50))

# find how many marks are greater than or equal to 50 in the list

# count = 0
# for mark in marks:
#  if mark >=50:
#   count+=1
# print("count of marks is greater than equal to 50 is ", count)




count = 0
print(marks)

for mark in marks:
 if mark >=50:
  count+=1
print(count)

print("--------------------------")

list_num = [11,51,51,6,15,61,54,59,259,35,81]

middle = int(len(list_num)/2)
print(middle, middle+1)
print(middle, middle+1)
print(list_num[middle], list_num[middle - 1])