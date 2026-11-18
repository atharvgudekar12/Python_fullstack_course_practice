students = [
    {
        "name": "Ruturaj Gayakwad",
        "id" : 101,
        "Div" : "C",
        "marks" : [67,53,46,81,60,78]
    },
    {
        "name": "Virat Kohali",
        "id" : 102,
        "Div" : "A",
        "marks" : [97,83,76,81,86,81]
    },
    {
        "name": "Stive Smit",
        "id" : 103,
        "Div" : "D",
        "marks" : [47,23,36,80,50,48]
    },
    {
        "name": "Rajat Patidar",
        "id" : 104,
        "Div" : "B",
        "marks" : [97,93,76,81,80,88]
    },
    {
        "name": "David Warner",
        "id" : 105,
        "Div" : "C",
        "marks" : [87,63,86,41,90,58]
    },
    {
        "name": "MS Dhoni",
        "id" : 106,
        "Div" : "C",
        "marks" : [67,83,74,61,69,38]
    },
    {
        "name": "Rishabh Panth",
        "id" : 107,
        "Div" : "D",
        "marks" : [47,53,56,61,70,48]
    },
    {
        "name": "Jasprit Bhumara",
        "id" : 108,
        "Div" : "B",
        "marks" : [87,73,66,91,70,88]
    },
    {
        "name": "Rohit Sharma",
        "id" : 109,
        "Div" : "D",
        "marks" : [87,63,66,41,40,58]
    },
    {
        "name": "Shubhaman Gill",
        "id" : 110,
        "Div" : "A",
        "marks" : [77,93,66,31,80,68]
    }
]

#---------- Accessing the dictionary values in the list
for i in students:
     if i["Div"] == 'A':
      print(i)

for i in students:
    if isinstance(i.get("Div"), str) and i.get("Div") == 'B':
        print(i)
# for i in students:
#      if i["Div"] == 'B' and i["id"] > 105:
#       print(i)

# for student in students:
#     for mark in students:
#         if mark <= 35 :
#             print(student["name"], "Fail")
#         else:
#             print(student["name"], "Pass")
            

for student in students:
     marks = student["marks"]
     status = "Pass"
     for mark in marks:
         if mark < 35:
             status = "Fail"
            #  break
     print(student["name"], ":", status)


tup = [21,54,98,45]

print(max(tup))

min_val = min(tup)

for i in tup:
    if i < min_val :
        min_val = i 
print("is the minimum value: ",min_val)