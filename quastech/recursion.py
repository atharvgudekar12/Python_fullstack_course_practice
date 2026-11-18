# Recursion is a programming and problem-solving technique where a function calls itself to solve smaller pieces of the same problem.

# • Base Case: The stopping condition that tells the function when to stop calling itself. Without a base case, the program enters an infinite loop and crashes with a stack overflow.

# • Recursive Case: The part of the function where it breaks the problem down and calls itself with a simpler or smaller input.

# • Call Stack: The internal memory structure that keeps track of each function call until the base case is reached, after which the results are resolved step-by-step.

def factorial(n):
    if n == 1 or n == 0:
        return 1

    else:
        return n * factorial(n - 1)
print(factorial(5))

# execution of code 
# 5 * factorial(5-1)
# 5 * 4 * factorial(4-1)
# 5 * 4 * 3 * factorial(3-1)
# 5 * 4 * 3 * 2 * factorial(2-1)
# 5 * 4 * 3 * 2 * 1
# after that print(factorial(5 = 120))