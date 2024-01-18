import os

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task.strip()}")

def add_task(tasks, new_task):
    tasks.append(f"[ ] {new_task}\n")
    save_tasks(tasks)
    print("Task added successfully!")

def delete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        del tasks[task_index - 1]
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")

def mark_completed(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1] = tasks[task_index - 1].replace("[ ]", "[X]", 1)
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        file.writelines(tasks)

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            return file.readlines()
    else:
        return []

def main():
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List Application =====")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
        elif choice == "3":
            task_index = int(input("Enter the task index to delete: "))
            delete_task(tasks, task_index)
        elif choice == "4":
            task_index = int(input("Enter the task index to mark as completed: "))
            mark_completed(tasks, task_index)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
