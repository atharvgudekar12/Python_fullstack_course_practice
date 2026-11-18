user = {
    'id' : 1,
    'user_name' : 'Atharv',
}

print(user)
print(user['id'])
print(user.get('user_name'))

# print(""" Selct what you want
#     id 
#     user_name""")

# user_input = input()

# print(user[user_input])
# print(user.get(user_input))

# get method advantages is that it will not throw an error if the key does not exist, instead it will return None or a default value if provided.

print(user.get('email'))  # This will return None since 'email' key does not exist
print(['age', 16])
print(user.get('age', 18))  # This will return 18 since 'age' key does not exist and we provided a default value of 18

print(user['user_name'])

user['age'] = 25
print(user)

# update dictionary with another dictionary
employee = {
    'user_name': 'Atharv',
    'location': 'mumbai',
    'course': 'python'
}
user.update(employee)
print(user)

# deleting in dictionary 

# remove_age = user.pop('age') # This will remove the 'age' key from the dictionary and return its value
# print(f"Removed age: {remove_age}")
# last_item = user.popitem()  # This will remove the last inserted item in the dictionary
# del user['location']  # This will delete the 'location' key from the dictionary
# print(user)


# user.clear()  # This will remove all items from the dictionary
# print(user)



print(user.keys())  # This will print all the keys in the dictionary
print(user.values())  # This will print all the values in the dictionary
print(user.items())  # This will print all the key-value pairs in the dictionary


# accesing using for loop

for key in user.keys():
    print(key)

for value in user.values():
    print(value)

for key,value in user.items():
    print(key, ":", value)

# emp = {
#     'emp1' : {'id' : 1,'name' : 'Atharv'},
#     'emp2' : {'id' : 2,'name' : 'Vedant'},
#     'emp3' : {'id' : 3,'name' : 'Harsh'},
#     'emp4' : {'id' : 4,'name' : 'Paras'}
# }

# emp['emp1']['name'] = 'Atharv Gudekar'
# print(emp)

# print(emp['emp1'].keys())  # This will print all the keys in the emp1 dictionary