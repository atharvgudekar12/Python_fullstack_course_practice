try:
    number = int(input("Enter the number :"))
    result = 10 / number
except ValueError as e:
    print("Please enter the valid value")
    print(e)
except ZeroDivisionError as e:
    print("value canot be divide by zero")
    print(e)
else:
    print(result)
finally:
    print("Execution completed")


# giving the name for the error

print("above 16 allowed")

age = int(input("Enter age: "))

if age <= 16:
    raise ValueError("age must be above 16")