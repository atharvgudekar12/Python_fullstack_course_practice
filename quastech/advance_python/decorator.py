# import calculator as c

# def message(func):
#     def wrapper():
#         print("The process is starting...")
#         func()
#         print("function execution compeleted")
#     return wrapper

# @message
# def call():
#     print("function is being executed")

# call()


def message(func):
    def wrapper(*args):
        print("The process is starting...")
        result = func(*args)
        print("function execution compeleted")
        return result
    return wrapper

@message
def call():
    print("function is being executed")

@message
def add(a, b):
    return a + b

call()
print(add(15, 10))