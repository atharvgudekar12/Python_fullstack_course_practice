import datetime
expences = []

def get_expences():
    return expences

def add_expences(expences):
    expence = {}

    date = datetime.datetime.now()
    description = input("Enter the expence description: ")
    amount = int(input("Enter the expence amount: "))


    if len(expences) == 0:
        number = 1
    else:
        number = expences[-1]['number'] + 1

    expence['number'] = number
    expence['Date'] =  f"{date: %d, %b, %y}"
    expence['Description'] = description
    expence['Amount'] = amount


    expences.append(expence)


def update_expence(expences):
    number = int(input("Enter the sr. no. to update the expence: "))
    description = input("Enter the expence description: ")
    amount = input("Enter the expence amount: ")

    for expence in expences:
        if expence['number'] == number:

            if not(description == "" and description == " "):
                expence['Description'] = description

            if amount:
                int(amount)
                expence['Amount'] = amount
        else:
            print("Expence not found")

            
def view_expences(expences):
    for expence in expences:
        print(expence)

def delete_expence(expences):
    number = int(input("Enter the sr. no. to delete the expence: "))

    for expence in expences:
        if expence['number'] == number:
            expences.remove(expence)


while True:
    print("----------Expence Tracker----------")
    print("""
    1. Add Expence
    2. View Expences
    3. Update Expences
    4. Delete Expences
    5. Exit
    """)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_expences(expences)
        print("Expence Added Successfully")
    elif choice == 2:
        print("---------- All Expences ----------")
        view_expences(expences)
    elif choice == 3:
        update_expence(expences)
        print("Expence Updated Successfully")
    elif choice == 4:
        delete_expence(expences)
        print("Expence Deleted Successfully")
    elif choice == 5:
        print("Thank You")
        break
    else:
        print("Invalid Choice")
