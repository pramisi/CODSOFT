import tkinter as tk

# Function to add a new task to the list
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Function to delete a selected task
def delete_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
    except IndexError:
        pass

# Create main window
root = tk.Tk()
root.title("To-Do List")

# Frame for task entry and buttons
frame = tk.Frame(root)
frame.pack(padx=10 ,pady=(40,20))

# Task entry
task_entry = tk.Entry(frame, font=('Arial', 14))
task_entry.grid(row=0, column=0, padx=5)

# Add task button
add_button = tk.Button(frame, text="Add Task", font=('Arial', 12), command=add_task)
add_button.grid(row=0, column=1, padx=10)

# Task list
task_list = tk.Listbox(root, font=('Arial', 14), width=25, height=10, bg='#C850C0', bd=0)
task_list.pack(pady=20)

# Delete task button
delete_button = tk.Button(root, text="Delete Task", font=('Arial', 12), command=delete_task)
delete_button.pack(pady=5)

# Run the application
root.mainloop()
