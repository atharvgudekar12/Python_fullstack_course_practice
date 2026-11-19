try:
    number = int(input("Enter the number :"))
    result = 10 / number
except ValueError:
    print("Please enter the valid value")
except ZeroDivisionError:
    print("value canot be divide by zero")
else:
    print(result)
finally:
    print("Execution completed")


# giving the name for the error

print("above 16 allowed")

age = int(input("Enter age: "))

if age <= 16:
    raise ValueError("age must be above 16")