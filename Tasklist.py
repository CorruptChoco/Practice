#version 1.3

import tkinter as tk
from tkinter import simpledialog, messagebox

def add_task():
    task = entry.get()
    if task:
        index = len(listbox.get(0,tk.END))
        listbox.insert(tk.END, str((index + 1)) + ") " + task)
        entry.delete(0, tk.END)
        save_tasks_to_file()
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
        index_tasks()
        save_tasks_to_file()
    else:
        messagebox.showwarning("Warning", "Please select a task to remove!")

def edit_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        selected_task = listbox.get(selected_task_index)
        edited_task = simpledialog.askstring("Edit Task","Edit Task", initialvalue=selected_task)
        if edited_task is not None:
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, edited_task)
            save_tasks_to_file()
    else:
        messagebox.showwarning("Warning", "Please select a task to edit!")

def index_tasks():
    tasks = listbox.get(0, tk.END)
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        blank_space = task.find(' ')
        task = task[blank_space+1:]
        task = str(i+1) + ") " + task
        listbox.insert(tk.END, task)


def save_tasks_to_file():
    with open("task_list.txt", "w") as file:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + '\n')

def load_tasks_from_file():
    try:
        with open('task_list.txt', "r") as file:
            tasks = [line.strip() for line in file.readlines()]
            # non list comprehension version for comparison of above line
            # tasks = []
            # for line in file.readlines():
            #     tasks.append(line.strip())
            listbox.delete(0, tk.END)  # Clear existing tasks in the Listbox
            for task in tasks:
                listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass  # Ignore if the file is not found (no tasks saved yet)

# Create the main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry ("600x400")

# Create and pack GUI elements
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5, side='bottom')

edit_button = tk.Button(root, text= 'Edit Task', command=edit_task)
edit_button.pack(pady=5, side = 'bottom')

listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=80, height=50)
listbox.pack(pady=10, expand= True)

# Call load_tasks_from_file at the beginning
load_tasks_from_file()

# Start the main event loop
root.mainloop()