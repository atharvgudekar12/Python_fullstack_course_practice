user_info = []
admin_info = {"role": "Admin", "password": "admin12"}

def admin_pannel(admin_info):
    role = input("enter user name:")
    password = input("enter user password:")
    for key, value in admin_info.items():
        # print(f"{key} : {value}")
        if key == role and value == password:
            print("Login as Admin")
        else:
            print("Login as Admin unsuccessfully")


def register_user(user_info):
    user = {}
    name = input("Enter Your name:")
    email = input("Enter Your Email: ")
    mob = input("Enter Your mobile number: ")
    create_pass = input("Create Strong Password: ")

    user['name'] = name
    user['email'] = email
    user['mob'] = mob
    user['create_pass'] = create_pass

    user_info.append(user)

def view_all_users(user_info):
    for user in user_info:
        print(user)

def login_user(user_info):
    email = input("Enter Your Email: ")
    enter_pass = input("Enter Your Password: ")

    for user in user_info:
        if user['email'] == email and user['create_pass'] == enter_pass:
            print(f"Login as {user['name']}")
            break
    else: 
        print("login unsuccessfully") 


while True:
    print("""
    Register u are new user and login if un have already an account
    1. For Register
    2. For Login
    3. For View All Users
    4. For Admin Login Only
    5. For Exit
    """)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        register_user(user_info)
        print('Register Successfully')
    elif choice == 2:
        login_user(user_info)
    elif choice == 3:
        view_all_users(user_info)
    elif choice == 4:
        admin_pannel(admin_info)
    elif choice == 5:
        print("Thank You")
        break
    else:
        print("invalid choice")