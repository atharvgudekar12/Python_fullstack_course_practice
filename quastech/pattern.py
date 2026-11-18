# ******
# ******
# ******
# ******
# print the square


for i in range(1, 5 +1):
    print(i * '*')

for i in range(5, 0, -1):
    print(i * '*')

num = 1

while num <= 5:
    count = 1
    while count <= num:
        print(count , num)
        count += 1
    print()
    num +=1