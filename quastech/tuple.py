t1 = (1,2,5,4)
t2 = 1,2,3,4,5
t3 = (1,)
t4 = (1)
print(type(t1))
print(type(t2))
print(type(t3))
print(type(t4))

std_tup = (36,89,100,"Atharv", "Gudekar", 20, 5.9, True,15, 12, 5,100,89)

# methods in tuple

print(std_tup.count(36))
print(std_tup.index(100))

# to unpacked tuple means to extract the values from tuple .
# it extract the values in the list internally

unpack_tup = (36,89,100,"Atharv", "Gudekar", 20, 5.9, True,15, 12, 5,100,89)

start, *value, end = unpack_tup

print(start)
print(value)    
print(end)
print(len(unpack_tup))
print(type(start))
print(type(value))
print(type(end))


print(unpack_tup[0])
print(unpack_tup[-2])
print(unpack_tup[1:5])
print(unpack_tup[1:8:2])
print(unpack_tup[::-1])
print(unpack_tup[:4:-1])
print(unpack_tup[-1:-5:-2])

