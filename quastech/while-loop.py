val = 1

while val <= 10:
    print(val)
    val +=1

# name = input("Enter your name: ")

# while True:
#     name = input("Enter your name: ")
#     if name:
#         print(name)
#         break

# val = int(input("Enter the number to print the table "))
# start = 1

# while start <= 10:
#     product = start *val
#     print(product)
#     start += 1

# table_number = int(input("Enter the number to print the table: "))
# i = 1

# while i <=10:
#     print(table_number, "*", i, "=", table_number*i)
#     i += 1


while True:
    password = input("Enter the secret password: ")
    if password == "Python12":
        print("Access Gurrented")
        break
    else:
        print("Wrong Password. try again.")