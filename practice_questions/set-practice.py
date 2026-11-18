numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique = set(numbers)
result = list(unique)
print(unique)
print(type(result))

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))


a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)
print(b)

a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(5)

print(a)
print(b)