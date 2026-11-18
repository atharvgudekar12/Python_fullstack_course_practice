def make_multiplier(factor):

    def multiply(number):
        return number * factor

    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))

# modify clouser 

def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter

my_counter = make_counter()

print(my_counter())
print(my_counter())
print(my_counter())




# def reverse_list(my_list):

#     for i in range(len(my_list)-1,-1,-1):
#         print(my_list[i])
#     print()

# number = [1,2,3,4,5]
# print(reverse_list(number))

# def print_reverse(my_list):
#     for i in range(len(my_list) - 1, -1, -1):
#         print(my_list[i], end=" ")

# numbers = [10, 20, 30, 40, 50]
# print_reverse(numbers)


list_1=[1,2,3,4,5,6,7,8]
def reverse_list(list_1):
    leng_th=len(list_1)-1
    temp_list=[]
    for i in range(leng_th,-1,-1):
        temp_list.append(list_1[i])
    return temp_list
        # print(list_1[i])
    

print(list_1)
list_2=reverse_list(list_1)
print(list_2)
# reverse_list(list_1)
# print(list(reverse_list))

