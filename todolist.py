def display_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        for i, task in enumerate(todo_list, start=1):
            status = "Completed" if task['completed'] else "Incomplete"
            print(f"{i}. {task['name']} - {status}")

def add_task(todo_list):
    task_name = input("Enter the task's name: ")
    todo_list.append({'name': task_name, 'completed': False})
    print(f"Task '{task_name}' added to the list.")

def mark_task_completed(todo_list):
    display_todo_list(todo_list)
    task_num = int(input("Enter the task number to mark as completed: "))
    if 0 < task_num <= len(todo_list):
        todo_list[task_num - 1]['completed'] = True
        print(f"Task '{todo_list[task_num - 1]['name']}' marked as completed.")
    else:
        print("Invalid task number.")

def remove_task(todo_list):
    display_todo_list(todo_list)
    task_num = int(input("Enter the task number to remove: "))
    if 0 < task_num <= len(todo_list):
        removed_task = todo_list.pop(task_num - 1)
        print(f"Task '{removed_task['name']}' removed from the list.")
    else:
        print("Invalid task number.")

def main():
    todo_list = []

    while True:
        print("\nTo-Do List Application")
        print("1. Display To-Do List")
        print("2. Add a Task")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            mark_task_completed(todo_list)
        elif choice == '4':
            remove_task(todo_list)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if _name_ == "_main_":
    main()
