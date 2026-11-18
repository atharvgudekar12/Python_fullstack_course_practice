employees = []

def getEmployees():
    return employees

# def save_employees(employees_data):
#     print('inside save employee')
#     employees.clear()
#     employees.extend(employees_data)

def add(employess):

    employee = {}

    if len(employees) == 0:
        id = 1
    else:
        id = employees[-1]['id'] + 1

    name = input("Enter employee name")
    age = int(input("Enter employee age"))
    department = input("Enter employee Department")
    salary = float(input("Enter employee salary"))

    employee['id'] = id
    employee['name'] = name
    employee['age'] = age
    employee['department'] = department
    employee['salary'] = salary

    employees.append(employee)

    # save_employees(employees)


def delete(employees):
    # name = input("Enter the name ")

    # for emp in employees:
    #     if emp['name'] == name:
    #      employees.remove(emp)
    # print('emp delete successfully')

    id = int(input("Enter the id "))
    for emp in employees:
        if emp['id'] == id:
         employees.remove(emp)
    print('emp delete successfully')

# def update_emp(employees):

#     id = int(input("enter the emp id to update the employee: "))

#     for emp in employees:
#         if emp['id'] == id:
#             featch_employees(employees)
#         choice = int(input("""========what u want to update========
#             1. name
#             2. age
#             3. department
#             4. salary
#         """))

#         if choice == 1:
#             name = input("Enter employee name")

#             for emp in employees:
#                 if emp['name'] == name:
#                     employees['name'] = name
#                     featch_employees(employees)

#         elif choice == 2:
#             age = int(input("Enter employee age"))
#             employees['age'] = age
#             break
#         elif choice == 3:
#             department = input("Enter employee Department")
#             employees['department'] = department
#             break
#         elif choice == 2:
#             salary = int(input("Enter employee salary"))
#             employees['salary'] = salary
#             break


def update_emp(employees):
    id = int(input('Enter employees id to update: '))

    print('Leave empty to not updating')

    name = input("Enter employee name")
    age = input("Enter employee age")
    department = input("Enter employee Department")
    salary = input("Enter employee salary")

    for emp in employees:
        if emp['id'] == id:
            
            if not(name == '' or name == " "):
                emp['name'] = name

            if age:
                age = int(age)
                emp['age'] = age

            if department:
                emp['department'] = department

            if salary:
                age = float(age)
                emp['salary'] = salary

        else:
            print('Employee not found')
 
def featch_employees(employees):
    print('inside employees view')
    for employee in employees:
        print(employee)

while True:
    print("""========Employee Management System===========
        1. Veiw Employees
        2. add Employee
        3. update Employee
        4. Delete Employee
        5. Exit 
    """)

    choice = int(input("Enter your choice 1,2,3,4,5 : "))

    if choice <=0 or choice > 5:
        print('Invalid Choice')
    elif choice == 1:
        featch_employees(employees)
    elif choice == 2:
        add(employees)
    elif choice == 3:
        update_emp(employees)
    elif choice == 4:
        delete(employees)
    else:
        print('Thank You')
        break
