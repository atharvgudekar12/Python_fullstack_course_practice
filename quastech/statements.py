a = int(input("Enter 1st no: "))
b = int(input("Enter 2nd no: "))

if a > b:
    print("A is greater")

if a < b:
    print("B is greater")

if a > b:
    print("A is greater")
elif a == b:
    print("Both are equal")
else:
    print("B is greater")


# shorthand property

result = "A is greater" if a > b else "B is greater"
print(result)