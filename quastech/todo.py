tasks = []

def featch_tasks(tasks):
    for index,i in enumerate(tasks, start= 1):
        print(f"{i['id']} {i['task']} -> {i['status']}")

    # for i in tasks:
    #     print(i)

def add_task(tasks):
    task ={}
    inp_task = input("Enter your task: ")
    status = "Pending..."

    if len(tasks) == 0:
        id = 1
    else:
        id = tasks[-1]['id'] + 1

    task['id'] = id
    task['task'] = inp_task
    task['status'] = status

    tasks.append(task)

def update_status(tasks):
    id = int(input('Enter the number of task to edit the status: '))

    status = input("Enter the status: ")

    for task in tasks:
        if task['id'] == id:
            if status:
                task['status'] = status
        else:
            print('task not found')



while True:
    print("""
        To-Do App
        1. Add Task
        2. View Task
        3. Update Status
        4. Exit""")

    choice = int(input("Enter Your Choice (1,2,3): "))

    if choice == 1:
        add_task(tasks)
        print('Task added successfully')
    elif choice == 2:
        print('All Tasks')
        featch_tasks(tasks)
    elif choice == 3:
        update_status(tasks)
        print('Task update successfully')
    elif choice == 4:
        print('Thank You')
        break
    else:
        print("Invalid choice")