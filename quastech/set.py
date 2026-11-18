set_1 = {1,2,3,5,3,4,5,5,6,7,8,9,10}
empty_set = set()
empty_set_dict = {}

print(set_1)
print(type(empty_set))
print(type(empty_set_dict))

# methods in set

# set_1.add(11)
set_1.update([1298,1,1415,1556])
set_1.remove(5)
# set_1.discard(1556)
set_1.pop()
# set_1.clear()

print(set_1)

list_1 = [1,2,3,4,5,6,7,59,6,48,41]

print(list_1.pop())