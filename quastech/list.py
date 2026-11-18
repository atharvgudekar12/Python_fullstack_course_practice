my_list = ['Atharv',21,874,12.2, True, "sanika"]

print(my_list)
print(type(my_list))
print(len(my_list))

# empty list 

empty_list = []
empty_set = set()
print(len(empty_list))
print(type(empty_list))
print(type(empty_set))

this_list = list(("banana", 'Apple', 'mango'))
print(type(this_list))
print(this_list)


# Accesing the items 
print("Accessing Friends in list :")
friends = ['Atharv', 'Sanika', 'Vedant', 'Harsh', 'Paras', 'Tanish', 'Prakash']

print(friends[1])
print(friends[-1])
print(friends[:5])
print(friends[1:5])
print(friends[::5])
print(friends[::-1])
print(friends[::-2])
print(friends[-4:-1:2])
print(friends[1:6:3])
print(friends[-1:-6:-2])

# changing item value
# 1. changing one value 
friends[5] = 'Ramesh'
print(friends)

# 2. changing multiplr value 
friends[4:6] = ['Suresh']
friends[4:6] = ['Shree', 'Ram']
print(friends)

# inser item 

friends.insert(2, 'She is best frined')
print(friends)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

list_friends = ['Atharv', 'Sanika', 'Vedant', 'Harsh', 'Paras', 'Tanish', 'Prakash']
print('remove in list')
print(list_friends)
# list_friends.remove("Paras")
list_friends.pop(2)
list_friends.pop()
del list_friends[0]
print(list_friends)

nums = [1,2,45,3,6,8,7,9,1,2]
nums.sort()
print(nums)

# sets unions 

setA = {1,3,5,7,9,11,12,13}
setB = {2,4,6,8,10,12,13}

print(setA.union(setB))
print(setA.intersection(setB)) # retuns common values in the set a and b
print(setA.difference(setB)) # returns the values which are in set a but not in set b
print(setA.symmetric_difference(setB)) # returns the values which are in set a and b but not in both