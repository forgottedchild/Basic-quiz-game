def todo_list():
    tasks = []
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            task = input("Enter a task: ")
            tasks.append(task)
            print("Task added!")
        elif choice == '2':
            print("Your tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == '3':
            task_no = int(input("Enter task number to remove: ")) - 1
            if 0 <= task_no < len(tasks):
                tasks.pop(task_no)
                print("Task removed!")
            else:
                print("Invalid task number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
