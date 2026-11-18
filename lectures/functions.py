# # Global variable
# num = int(input("Enter the first number: "))

# def calculator():
#     global num

#     while True:
#         sign = input("Enter the sign (+, -, *, /): ")

#         if sign == "+":
#             print("Addition =", num + num)

#         elif sign == "-":
#             print("Subtraction =", num - num)

#         elif sign == "*":
#             print("Multiplication =", num * num)

#         elif sign == "/":
#             print("Division =", num / 2)

#         else:
#             print("Invalid operator")

#         choice = input("Do you want to continue? (y/n): ").lower()

#         if choice == "n":
#             break

#         num = int(input("Enter next number: "))


# def max2():
#     num2 = int(input("Enter second number: "))

#     if num > num2:
#         print("Greater number is:", num)
#     else:
#         print("Greater number is:", num2)


# calculator()
# max2()

# print("Program executed successfully")

# # Write is_prime(n) returning True if n is prime else False


# stocks = {}
# balance = 10000


# def signup():
#     username = input("Create username: ")
#     password = input("Create password: ")
#     print("Signup successful!")
#     return username, password


# def login():
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     print("Login successful!")
#     return True


# def buy_stock():
#     global balance

#     stock_name = input("Enter stock name: ")
#     quantity = int(input("Enter quantity: "))
#     price = float(input("Enter price per share: "))

#     total = quantity * price

#     if total <= balance:
#         balance -= total
#         stocks[stock_name] = stocks.get(stock_name, 0) + quantity
#         print(f"Bought {quantity} shares of {stock_name}")
#         print("Remaining Balance =", balance)
#     else:
#         print("Insufficient balance!")


# def sell_stock():
#     global balance

#     stock_name = input("Enter stock name: ")

#     if stock_name in stocks:
#         quantity = int(input("Enter quantity to sell: "))
#         price = float(input("Enter selling price: "))

#         if quantity <= stocks[stock_name]:
#             stocks[stock_name] -= quantity
#             balance += quantity * price

#             print(f"Sold {quantity} shares of {stock_name}")
#             print("Updated Balance =", balance)
#         else:
#             print("Not enough shares!")
#     else:
#         print("Stock not found!")


# def calculate_profit():
#     invested = float(input("Enter invested amount: "))
#     current = float(input("Enter current value: "))

#     profit = current - invested

#     print("Profit/Loss =", profit)


# # Main Program
# signup()

# if login():

#     while True:
#         print("\n----- STOCK MENU -----")
#         print("1. Buy Stock")
#         print("2. Sell Stock")
#         print("3. Calculate Profit")
#         print("4. View Portfolio")
#         print("5. Exit")

#         choice = input("Enter choice: ")

#         if choice == "1":
#             buy_stock()

#         elif choice == "2":
#             sell_stock()

#         elif choice == "3":
#             calculate_profit()

#         elif choice == "4":
#             print("Portfolio =", stocks)
#             print("Balance =", balance)

#         elif choice == "5":
#             print("Thank You!")
#             break

#         else:
#             print("Invalid Choice")


# balance = 50000

# def check_balance():
#     global balance
#     print(f"Your balance is {balance}")
#     pass

# def deposit():
#     global balance
#     amt = int(input("enter your maount for deposit : "))
#     balance += amt
#     print(f"your amount {amt} is succesfully deposit")
#     pass

# def withdraw():
#     global balance
#     withdraw = int(input("enter your amount to withdraw :"))
#     balance -= withdraw
#     print(f"take your cash {withdraw}")
#     pass

# def exit_program():
#     print("Thank You!! Visite Again.")
#     pass

# while True:
#     print("1 : check your balance")
#     print("2 : Deposite the money")
#     print("3 : with your money")
#     print("4 : exit")

#     choise = int(input("enter your choise"))

#     if choise == 1 :
#         check_balance()
#     elif choise == 2:
#         deposit()
#     elif choise == 3:
#         withdraw()
#     elif choise == 4:
#         exit_program()
#         break

