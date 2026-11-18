x = [1,2,3,4,5]
print(id(x))

y =  x
print(id(y) == id(x))  # This will print True because y is referencing the same list as x


# immutable 
a = 10
b = a
b = b + 2
print(a)
print(b)

print(id(x))
print(id(y))

# muttable 

list1 = [1,2,3]
list2 = list1   

list2.append(4)  # This will modify the list that both m and n reference
print(list1)
print(list2)
print(id(list1))
print(id(list2))

text = "Hello, World!"
for char in text:
    print(char)


list = ["Atharv","Vedant",1,6,8,7,9,"harsh"]
x = list
for x in list:
    if isinstance(x, int):

        print(max(x))

