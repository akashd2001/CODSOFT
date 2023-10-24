import tkinter as tk
import math

app = tk.Tk()
app.title("Simple Calculator")


input_entry = tk.Entry(app, state='readonly', font=('Helvetica', 20), bg='white')
input_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)


def button_click(value):
    current_input = input_entry.get()
    input_entry.config(state='normal')
    if current_input == "Invalid input":
        input_entry.delete(0, tk.END)
    if value == 'C':
        input_entry.delete(0, tk.END)
    elif value == 'x^2':
        try:
            result = eval(current_input) ** 2
            input_entry.delete(0, tk.END)
            input_entry.insert(tk.END, result)
        except:
            input_entry.delete(0, tk.END)
            input_entry.insert(tk.END, "Invalid input")
    elif value == '√':
        try:
            result = math.sqrt(float(current_input))
            input_entry.delete(0, tk.END)
            input_entry.insert(tk.END, result)
        except:
            input_entry.delete(0, tk.END)
            input_entry.insert(tk.END, "Invalid input")
    elif value == '=':
        try:
            result = eval(current_input)
            input_entry.delete(0, tk.END)
            input_entry.insert(tk.END, result)
        except:
            input_entry.delete(0, tk.END)
            input_entry.insert(tk.END, "Invalid input")
    else:
        input_entry.insert(tk.END, value)
    input_entry.config(state='readonly')


button_texts = [
    ['C', 'x^2', '√', '+'],
    ['9', '8', '7', '-'],
    ['6', '5', '4', '*'],
    ['3', '2', '1', '/'],
    ['.', '0', '%', '=']
]

for i, row_texts in enumerate(button_texts):
    for j, button_text in enumerate(row_texts):
        tk.Button(app, text=button_text, width=7, height=2, command=lambda button_text=button_text: button_click(button_text)).grid(row=i+1, column=j)

app.mainloop()
