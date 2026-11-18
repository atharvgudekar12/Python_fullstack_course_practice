# print("Calculator")
# num_1 = int(input("Enter the 1st number: "))
# num_2 = int(input("Enter the 2nd number: "))
# operator = str(input("Enter the operator: "))

# if operator == "+":
#     print(num_1 + num_2)
# elif operator == "-":
#     print(num_1 - num_2)
# elif operator == "*":
#     print(num_1 * num_2)
# elif num_1 == 0 or num_2 == 0:
#     print("Invalid Value")
# elif operator == "/":
#     print(num_1 / num_2)
# elif operator == "%":
#     print(num_1 % num_2)
# else :
#     print("Invalid Operator")


# match operator:
#     case "+":
#         print(num_1 + num_2)
#     case "-":
#         print(num_1 - num_2)
#     case "*":
#         print(num_1 * num_2)
#     case "/":
#         print(num_1 / num_2)
#     case "%":
#         print(num_1 % num_2)

# multiple value matxh 

match "Mp".lower():
    case "jpg" | "jpeg" | "png":
        print("Image File")
    case "mp4" | "avi" | "mkv":
        print("Video File")
    case _ :
        print("Unknown file type")


# empty_list = []
empty_list = [52]

if empty_list:
    print("list is not empty")
else:
    print("list is empty")



name = input("Enter your name :")

if name :
    print(name)
else:
    print("please provide the name")