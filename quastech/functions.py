# def function name(parameter):
#     block of codes
# function name calling(argumnets)

# A function is a reusable, named block of code designed to perform a specific task.

def greeting(name):
    print("Hello", name)
greeting("Atharv")
greeting("Vedant")
greeting("Sanika")

# 'name' is the parameter
def personalized_greet(name):
    print(f"Hello, {name}!")

# "Alice" and "Bob" are the arguments
personalized_greet("Alice") 
personalized_greet("Bob")

def addition(a,b):
    result = a + b
    return result

r = addition(87,13)
print(r)
# print(addition(84,16))

def greetings(name, age, /, salary):
    print(f"Hello {name}, your age is {age}, ur salary is {salary}")

greetings('Atharv', 21, salary = 30000)
greetings('Harsh', 21, salary = 25000)


def create_user(username, *, is_admin=False):
    print(f"User: {username}, Admin: {is_admin}")

create_user('Atharv', is_admin=True)

def add(a: int, b: int) -> int:
    return a + b

add1 = add('15','30')  #not neccesary to add only int it is use to know only that function is accepting the int values
print(add1)

# first function in python 

def sub(a: int, b: int) -> int:
    print(a - b)
    
def execute(func, a, b):
    func(a, b)

execute(sub, 50,35)


def multiplier_factory(factor):
    def multiply(number):
        return number * factor
    return multiply

double = multiplier_factory(2)
print(double(10))

double = multiplier_factory(3)
print(double(10))


# Anaonimus function 

square = lambda x: x ** 2
print(square(3))

PI = 3.14
multi_parameters = lambda x,y,z: x ** 2 + y * 2 - z
print(multi_parameters(3,4,5))

pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
print(pairs)
pairs.sort()
print(pairs)
print('-------------------------------------------------------')
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
print(pairs)
pairs.sort(key=lambda pairs:pairs[1])
print(pairs)

