# Initialize an empty list for tasks
tasks = []
def menu():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"Added task: {task}")
        elif choice == '2':
            if not tasks:
                print("No tasks in the list.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        elif choice == '3':
            if not tasks:
                print("No tasks to delete.")
            else:
                task_number = int(input("Enter the task number to delete: "))
                if 0 < task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Deleted task: {removed_task}")
                else:
                    print("Invalid task number.")
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

menu()
