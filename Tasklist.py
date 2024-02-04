#version 1.2

import tkinter as tk
from tkinter import simpledialog, messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
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
    else:
        messagebox.showwarning("Warning", "Please select a task to edit!")

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

# Start the main event loop
root.mainloop()