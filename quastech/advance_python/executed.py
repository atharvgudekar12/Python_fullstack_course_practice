# import calculator

# print("Executed file running...")
# print(__name__)
# print(calculator.add(15,20))

# when we import the other file in the main file __name__ give the actual name for that file and the efile that we run like app.py main file it gives the name as __main__
# this is calculator file..
# calculator calculator file
# Executed file running...
# __main__

# ------------------------------------------------------------------------------------------------------------------------------------------

# from calculator import add
# from calculator import sub
# from calculator import mul
# from calculator import div


# to import all we can use * 

from calculator import *

print("Executed file running...")
print(__name__)

print(add(15, 20))
print(sub(15, 20))
print(mul(15, 20))
print(div(15, 5))

# from calculator import say_hello,name

print(say_hello(name))