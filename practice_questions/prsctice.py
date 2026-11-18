list_num = [25,55,48,51,58,62,48,2,84,62,8,62,555,444]

large_num = list_num[0]

for i in list_num:
    if i > large_num:
        large_num = i
print(large_num)    


max_val = max(list_num)
second_max = list_num[0]

for i in list_num:
    if i < max_val and i >second_max:
        second_max = i
print(second_max)


number = [1,2,3,4,5,6,7]

# print(number[0])
# print(number[-1])

first, *all, last = number

print(first)
print(*all)
print(last)