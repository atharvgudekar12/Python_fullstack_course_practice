numbers = [1,2,3,4,5,6,7,8,9,10]

empty = []

print('\n','----------Using loop------------')
for i in numbers:
    empty.append(i ** 2)

print(empty)

print('\n','----------Using function traditional way------------')
def square(x):
    return x ** 2

square_list = map(square, numbers)
print(list(square_list))

print('\n','----------Using lambda function------------')

square_list = map(lambda x: x ** 2, numbers)
print(list(square_list))

