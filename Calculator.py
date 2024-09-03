import tkinter as tk

print("% =  reminder value")

# Function to update the expression in the entry box
def update_expression(symbol):
    current_text = expression.get()
    expression.set(current_text + str(symbol))

# Function to evaluate the final expression
def evaluate_expression():
    try:
        result = str(eval(expression.get()))
        expression.set(result)
    except:
        expression.set("Error")

# Function to clear the entry box
def clear_expression():
    expression.set("")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Variable to store the expression
expression = tk.StringVar()

# Create an entry box for the expression
entry_box = tk.Entry(window, textvariable=expression, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
entry_box.grid(row=0, column=0, columnspan=4)

# Create buttons for the calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),('%', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),('00', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),('000', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),('C', 4, 4),
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 18), command=evaluate_expression)
    else:
        btn = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda t=text: update_expression(t))
    btn.grid(row=row, column=col)

# Add a clear button
clear_btn = tk.Button(window, text='C', padx=20, pady=20, font=('Arial', 18), command=clear_expression)
clear_btn.grid(row=4, column=4)

# Start the GUI event loop
window.mainloop()
