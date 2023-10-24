import tkinter as tk
from tkinter import simpledialog

def edit_task(task_label):
    edited_task = simpledialog.askstring("Edit Task", "Edit Task:", initialvalue=task_label["text"])
    if edited_task is not None:
        task_label.config(text=edited_task)

def delete_task(task_label, task_buttons, task_dots):
    task_label.destroy()
    for button in task_buttons:
        button.destroy()
    for dot in task_dots:
        dot.destroy()
    task_items.remove(task_label)

def add_task():
    task_text = task_entry.get()
    if task_text:
        task_frame = tk.Frame(task_listbox, bg="lightblue")
        task_label = tk.Label(task_listbox, text=task_text, anchor="w",bg="lightblue", wraplength=150, font=("Helvetica", 12, "bold"))
        edit_button = tk.Button(task_listbox, text="Edit", command=lambda: edit_task(task_label), bg="blue", fg="white")
        delete_button = tk.Button(task_listbox, text="Delete", command=lambda: delete_task(task_label, [edit_button, delete_button], [task_dot]), bg="red", fg="white")
        task_dot = tk.Label(task_listbox, text="•", font=("Helvetica", 12), bg=task_listbox.cget("bg"), padx=5)

        task_frame.grid(row=len(task_items), column=0, columnspan=4, padx=5, pady=5, sticky="w")
        task_label.grid(row=len(task_items), column=1, padx=5, pady=5, sticky="w")
        edit_button.grid(row=len(task_items), column=2, padx=(0, 5))
        delete_button.grid(row=len(task_items), column=3)
        task_dot.grid(row=len(task_items), column=0, padx=(0, 5))

        task_items.append(task_label)
        task_entry.delete(0, tk.END)


app = tk.Tk()


app.configure(bg="aliceblue")

app.title("To Do List")

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

x = (screen_width - app.winfo_reqwidth()) // 2
y = (screen_height - app.winfo_reqheight()) // 2

app.geometry("+%d+%d" % (x, y))

header_label = tk.Label(app, text="My To-Do List", font=("Times New Roman", 18, "italic", "bold",), bg="goldenrod")
header_label.grid(row=0, column=0, columnspan=100, padx=10, pady=10)

label = tk.Label(app, text="Add Task :",font=("Times New Roman",14,"bold"))
label.grid(row=1, column=0, padx=(10, 5), pady=10)

task_entry = tk.Entry(app)
task_entry.grid(row=1, column=1, padx=5, pady=10)

add_button = tk.Button(app, text="Submit", command=add_task, bg="green", fg="white")
add_button.grid(row=1, column=2, padx=(5, 10), pady=10)

task_listbox_frame = tk.Frame(app)
task_listbox_frame.grid(row=3, column=0, columnspan=4, padx=10, pady=(0, 10))
task_listbox_frame.configure(bg="lightgreen")

saved_tasks_label = tk.Label(task_listbox_frame, text="Tasks To Complete",font=("Times New Roman",14,"bold"), bg="lightgreen")
saved_tasks_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

task_listbox = tk.Frame(task_listbox_frame, bg="lightblue")
task_listbox.grid(row=4, column=0, columnspan=4, padx=10, pady=10)



task_items = []

app.mainloop()
