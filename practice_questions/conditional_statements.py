# conditional problems

# grade cheaker

# below 35 fail, 35 to 50 = c grade,51 to 80 = b 81 to 100 =a.

# marks = float(input("enter the marks to check the grades of the students :"))

# if marks > 0 and marks <= 35 :
#     print("failed")
# elif marks > 35 and marks <= 50 :
#     print(f"C grade and you got {marks}%")
# elif marks > 50 and marks <= 80 :
#     print(f"B grade and you got {marks}%")
# elif marks > 80 and marks <= 100 :
#     print(f"A grade and you got {marks}%")
# else:
#     print("Invalid marks")


# names = ["Atharv", "Shravani" , "Neha", "Harsh", "Soham", "Yash", "Paras", "Tanish", "Rohit", "Affrin", "Sanika", "Ajinkya" , "Rutuja"]

# x = [name.lower() for name in names]
# print(x)

# i = "Shravani"

# if i in names :
#     print(i)
# else:
#     print("not present")
# ---- Optional ways to do the same thing ----

# 1) Using a for loop
# lower_names = []
# for name in names:
#     lower_names.append(name.lower())
# print(lower_names)

# 2) Using map() with str.lower
# lower_names = list(map(str.lower, names))
# print(lower_names)

# 3) Using map() with lambda
# lower_names = list(map(lambda name: name.lower(), names))
# print(lower_names)
# i = "s"

# if i in list :
#     print(list.index(i) , i, "is my Crush...")
# else:
#     print("not in the list")

# ============================================================
# EXTRA CONDITIONAL STATEMENTS PRACTICE PROBLEMS
# ============================================================

# 1) Positive, Negative or Zero
# Write a program that takes a number from the user and prints whether it is positive, negative, or zero.

number = int(input("enter the number to check it is positive nigative or zero : "))

# if number >= 1 :
#    print(f"{number} is positive")
# elif number == 0 :
#    print(f"{number} is zero" )
# else :
#    print(f"{number} is nigative")


# 2) Even or Odd
# Write a program that checks whether a given integer is even or odd.
# if number%2 == 0 :
#    print(f"number is even : {number}")
# elif number == 1 :
#       print(f"number is not even and odd : {number}")
# else :
#    print(f"number is odd : {number}")

# 3) Largest of Three Numbers
# Take three numbers as input and print the largest one without using max().

# 4) Leap Year Checker
# A year is a leap year if it is divisible by 4, except years divisible by 100 unless they are also divisible by 400.
# Write a program to check if a year is a leap year.

# 5) Vowel or Consonant
# Take a single character from the user and check whether it is a vowel or consonant.

# 6) Simple Calculator
# Take two numbers and an operator (+, -, *, /) as input.
# Use if-elif-else to perform the operation and print the result. Handle division by zero.

# 7) Voting Eligibility
# Take age as input and print whether the person is eligible to vote (age >= 18).

# 8) Rock Paper Scissors
# Take two inputs (player1 and player2 choices) and determine the winner or if it is a tie.

# 9) BMI Calculator with Categories
# BMI = weight(kg) / (height(m) ** 2)
# Categories: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (>=30)

# 10) Divisible by 5 and 11
# Check whether a number is divisible by both 5 and 11.

# 11) Days in a Month
# Take a month number (1-12) and print how many days it has. Consider leap year for February.

# 12) Electricity Bill Calculator
# Units consumed:
#   - First 100 units: Rs 5/unit
#   - Next 100 units (101-200): Rs 7/unit
#   - Above 200 units: Rs 10/unit
# Calculate total bill.

# 13) Temperature Converter
# Ask the user to choose: 1) Celsius to Fahrenheit  2) Fahrenheit to Celsius
# Then take the temperature and print the converted value.

# 14) Triangle Validity and Type
# Take three sides and check if they form a valid triangle (sum of any two > third).
# If valid, classify as Equilateral, Isosceles, or Scalene.

# 15) Number Range Checker
# Take a number and print which range it falls into:
#   0-20, 21-40, 41-60, 61-80, 81-100, or Out of Range.




