import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Atharv@12",
    database = "college"
)

mycursor = mydb.cursor()

query = "SELECT * FROM students ORDER BY id DESC"

mycursor.execute(query)

result = mycursor.fetchall()

for row in result:
    print("ID:", row[0])
    print("Name:", row[1])
    print("Age:", row[2])
    print("Course:", row[3])
    print("-------------------")

print("======================================")


query2 = "SELECT * FROM students WHERE course = %s"
value2 = input("Enter the course to get data of students: ")

val = (value2,)
# val= tuple(value2,)

mycursor.execute(query2, val)

result = mycursor.fetchall()

for record in result:
    print(record)


print("=================Display the oldest students first=====================")
print("=================fetch only one student record using fetchone=====================")

query3 = "SELECT * FROM students"

mycursor.execute(query3)
result = mycursor.fetchone()

print(result)