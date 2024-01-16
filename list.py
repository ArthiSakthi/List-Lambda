todo_list=[]
add_task=lambda task: todo_list.append(task)
view_tasks=lambda: todo_list
complete_task=lambda task: todo_list.remove(task) if task in todo_list else None
delete_task=lambda task: todo_list.remove(task) if task in todo_list else None
while True:
    print("\nWelcome to Todo List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        task=input("Enter a task to add: ")
        add_task(task)
        print(f"Task '{task}' is added to the list")
    elif choice=="2":
        tasks=view_tasks()
        if tasks:
            print("Todo List:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}.{task}")
        else:
            print("Your list is empty")
    elif choice=="3":
        if not todo_list:
            print("There is no task to complete")
        else:
            task=input("Enter the task to mark as completed: ")
            complete_task(task)
            print(f"Task '{task}' marked as completed")
    elif choice=="4":
        if not todo_list:
            print("There is no task to delete")
        else:
            task=input("Enter the task to delete: ")
            delete_task(task)
            print(f"Task '{task}' removed from the list")
    elif choice=="5":
        print("Bye Bye!")
        break
    else:
        print("Invalid choice")
