import os


def load_tasks():
    if os.path.exists("filename.txt"):
        with open("filename.txt", 'r') as file:
            tasks = file.readlines()
            tasks = [task.strip() for task in tasks]
    else:
        tasks = []
    return tasks


def save_tasks(tasks):
    with open("filename.txt", 'w') as file:
        for task in tasks:
            file.write(task + '\n')


def show_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"Deleted: {removed}")
        else:
            print("Invalid task number!")
    except:
        print("Please enter a valid task number!")


# Main program

tasks = load_tasks()

while True:
    print("\n---- To-Do List Menu ----")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose your choice (1-4): ")
    if choice == '1':
        show_tasks(tasks)

    elif choice == '2':
        add_task(tasks)
        save_tasks(tasks)

    elif choice == '3':
        delete_task(tasks)
        save_tasks(tasks)
    elif choice == '4':
        print("Good Bye👋")

    else:
        print("Invalid choice!")
