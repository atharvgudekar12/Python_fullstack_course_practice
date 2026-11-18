# def return_value():
#     yield 1 
#     yield 2 

# obj = return_value()

# print(obj.__next__())
# print("After first call")
# print(obj.__next__())

def sqr(list_value):
    for i in list_value:
        yield i * i

num_list = [1,2,3,4,5,6,7,8,9,10]

gen_obj = sqr(num_list)

print(gen_obj.__next__())
print(gen_obj.__next__())
print(gen_obj.__next__())

square_list = [x * x for x in range(5)]
print(square_list)

square_gen = (x * x for x in range(5))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))

def get_numbers():
    for i in range(1, 6):
        yield i

numbers = get_numbers()

for num in numbers:
    print(num)