import tkinter as tk
from functools import partial
from tkinter import messagebox
import commands

def handle_update(id, title, app):
    if not title:
        messagebox.showerror(title="Edit task", message="Cannot update with an empty task!", parent=app)
    else:
        commands.update_task(id, {"title": title})
        show_all_tasks_frame(app)

def handle_delete(id, app):
    commands.delete_task(id)
    show_all_tasks_frame(app)

def submit_task(title, app):
    if not title:
        messagebox.showerror(
            title="Add Task",
            message="Cannot add empty task!",
            parent=app
        )
    else:
        commands.save_task({"title": title})
        show_all_tasks_frame(app)
    
def show_edit_task_frame(task, app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    label = tk.Label(master=frame, text="Edit task", font=("Arial", 14, "bold"))
    label.grid(row=0, column=0, columnspan=2, pady=10)
    # Add an entry widget and show the task title
    # Add a button with text Update for saving the changes
    # Add a button with text Back / Cancel for remove the frame

    task_entry = tk.Entry(master=frame)
    task_entry.insert(0, task["title"])
    task_entry.grid(column=0)

    
    update_btn = tk.Button(
        master=frame,
        text = "Update",
        width=8,
        command=lambda: handle_update(task["_id"], task_entry.get(), app))
    update_btn.grid(row=2, column=0, pady=10, sticky="e")

    cancel_btn = tk.Button(
        master=frame,
        text = "Back",
        width=8,
        command=lambda: frame.destroy())
    cancel_btn.grid(row=2, column=1, pady=10, sticky="w")

    frame.tkraise()


def show_add_ask_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    label = tk.Label(master=frame, text="What do you want to do?")
    label.grid()
    entry = tk.Entry(master=frame)
    entry.grid()
    btn = tk.Button(master=frame, text="Submit", command=lambda: submit_task(entry.get(), app))
    btn.grid(pady=10)

    cancel_btn = tk.Button(
        master=frame,
        text = "Back",
        width=8,
        command=lambda: frame.destroy())
    cancel_btn.grid(row=2, column=1, pady=10, sticky="w")

    frame.tkraise()

def show_all_tasks_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    tasks = commands.get_tasks().to_list()
    for task in tasks:
        checkbtn = tk.Checkbutton(master=frame, text=task["title"])
        checkbtn.grid(row=tasks.index(task), column=0, sticky="w", padx=5, pady=5)

        edit_btn = tk.Button(
            master=frame,
            text="Edit",
            command=partial(show_edit_task_frame, task, app))
        edit_btn.grid(row=tasks.index(task), column=1)

        delete_btn = tk.Button(
            master=frame,
            text="Delete",
            command=partial(handle_delete, task["_id"], app))
        delete_btn.grid(row=tasks.index(task), column=2)
        
    add_btn = tk.Button(master=frame, 
            text="Add Task",
            command=lambda: show_add_ask_frame(app))
    add_btn.grid(row=len(tasks) +1, column=1)

    frame.tkraise()