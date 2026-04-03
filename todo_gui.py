import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"


# ---------- FILE HANDLING ---------- #

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# ---------- FUNCTIONS ---------- #

def add_task():
    title = title_entry.get()
    tag = tag_entry.get()
    due = due_entry.get()

    if title == "":
        messagebox.showwarning("Warning", "Task title cannot be empty!")
        return

    tasks.append({
        "title": title,
        "tag": tag,
        "due": due,
        "done": False
    })

    save_tasks()
    update_list()

    title_entry.delete(0, tk.END)
    tag_entry.delete(0, tk.END)
    due_entry.delete(0, tk.END)


def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        save_tasks()
        update_list()
    except:
        messagebox.showwarning("Warning", "Select a task first!")


def mark_done():
    try:
        selected = listbox.curselection()[0]
        tasks[selected]["done"] = True
        save_tasks()
        update_list()
    except:
        messagebox.showwarning("Warning", "Select a task first!")


def update_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔" if task["done"] else "✘"
        text = f"[{status}] {task['title']} | Tag: {task['tag']} | Due: {task['due']}"
        listbox.insert(tk.END, text)


# ---------- MAIN WINDOW ---------- #

tasks = load_tasks()

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")

# Inputs
tk.Label(root, text="Task Title").pack()
title_entry = tk.Entry(root, width=40)
title_entry.pack()

tk.Label(root, text="Tag").pack()
tag_entry = tk.Entry(root, width=40)
tag_entry.pack()

tk.Label(root, text="Due Date").pack()
due_entry = tk.Entry(root, width=40)
due_entry.pack()

# Buttons
tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Mark as Done", command=mark_done).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)

# Task List
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

update_list()

# Run app
root.mainloop()
