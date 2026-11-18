student = {
    "name" : "Atharv",
    "age" : 22,
    "city" : "Mumbai",
    "course" : "Python"
    }

# print only  the keys 

print(student.keys())
print(student.values())

# Explain the difference between: 
# dict[key]  when the key is not present in the dictionary it will throw the key error
# dict.get(key)  when the key is not present in the dictinary it will return "None"
# print(student['location'])
print(student.get('location'))

# update student 

student["city"] = 'pune'
student["marks"] = 90
print(student)

stud_info = {"college" : "ICS"}

student.update(stud_info)
print(student)

print("extract dictionary using the for loop",'\n')
# print(student.items())
print("student information")
for key,value in student.items():
    print(key,":",value)


student1 = {
    "name": "Rahul",
    "marks": 80
}

print(student1.get("age"))
# print(student1["age"]) it gives the key error

# Print the names of students who scored more than 80.
marks = {
    "Rahul": 85,
    "Amit": 72,
    "Sneha": 91,
    "Priya": 64
}

# for key in marks(isinstance(marks, int))> 80:
#     print(key)


d = {}

d["a"] = 10
d["a"] = 20

print(d)


# print the students who score more than 80.

print("print the students who score more than 80.")
marks_2 = {
    "Rahul": 85,
    "Amit": 72,
    "Sneha": 91,
    "Priya": 64
}

for i in marks_2.items():
    if isinstance( i, dict) and i <= 10:
        i =  marks_2.items()
print(i)

print("Print the cube of each number from 1 to n")

n = 10

for i in range(1, n + 1):
    cube = i**3
    print(cube)

print("prime numbers")

for i in range(1, 101):
    if i/i == 1 and i/i != 0:
        print(i)