# unpack without using indexing 

student = ('Atharv',22,"Python")

name, age, course = student
print(name)
print(age)
print(course)

# Can a tuple contain a mutable object?
# yes we we can modify it also 
x = ([1, 2, 3], 10)
x[0].append(50)
print(x)