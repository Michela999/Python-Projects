def display_tasks(tasks):
    if tasks:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\nYour to-do list is empty.")

def add_task(tasks):
    task = input("\nEnter a task to add: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def remove_task(tasks):
    display_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the number of the task to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}' removed from the list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks to remove.")

def main():
    tasks = []
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ")
        
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please choose a valid option (1-4).")

# Run the program
if __name__ == "__main__":
    main()
print("Try programiz.pro")