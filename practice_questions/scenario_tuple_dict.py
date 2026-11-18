marks ={
    "Atharv": 85,
    "Rahul": 72,
    "Sneha": 91,
    "Sanika": 65
}

# prints each student name and marks

for key, values in marks.items():
    print(key, ":", values )

print("print students have marks greater than 75")
for names,mark in marks.items():
    if mark > 75:
        print(names, mark)

print("Calculate the average marks")


sum_mark = 0
for mark in marks.values():
    length = len(marks)
    sum_mark += mark
    avg = sum_mark/length
# print(sum_mark)
print(avg)

print("Product stock management")

stocks = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15,
    "Monitor": 5,
}

# A customer buy 3 mouse 
# update the mouse stock

stocks.update({"Mouse": 22})
print(stocks)

# Add webcap with an initial stock of 8
# print final stock

marks.update({"Webcap": 8})
count_stock = 0
for stock in stocks.values():
    count_stock += stock
print(count_stock)

print("Word Frequency: count how many times the each word appear")

sentence = "python is the easy and python is powerful"

# from collections import Counter 
# sli = Counter(sentence.split())

# print(sli)

# using for loop

word_count = {}

for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

print("employee")

employee = {
    "Atharv": 35000,
    "Sanika": 33000,
    "Vedant": 20000,
    "Harsh": 25000,
}

# print the emp with highest salary
print(max(employee.items()))

for name, sal in employee.items():
    if sal > 25000:
        print(name, ":", sal)