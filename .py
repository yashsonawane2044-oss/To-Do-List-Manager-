import json
import os

FILE_NAME = "tasks.json"


# ---------- File Handling ---------- #

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        print("Error loading tasks. Starting fresh.")
        return []


def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except:
        print("Error saving tasks.")


# ---------- Task Functions ---------- #

def add_task(tasks):
    title = input("Enter task title: ")
    tag = input("Enter tag (optional): ")
    due = input("Enter due date (optional): ")

    tasks.append({
        "title": title,
        "done": False,
        "tag": tag,
        "due": due
    })

    save_tasks(tasks)
    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. [{status}] {task['title']} | Tag: {task['tag']} | Due: {task['due']}")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: "))
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted.")
    except:
        print("Invalid input.")


def mark_done(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: "))
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task marked as done.")
    except:
        print("Invalid input.")


# ---------- Menu ---------- #

def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            mark_done(tasks)
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# ---------- Run Program ---------- #

if __name__ == "__main__":
    main()