import tkinter as tk

# Define a function to perform arithmetic operations
def calculate():
    # Get the input values from the input fields
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    operator = operator_var.get()

    # Perform the selected operation
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2

    # Update the result label with the calculated result
    result_label.config(text="Result: " + str(result))

# Create a new Tkinter window
root = tk.Tk()
root.title("Calculator")

# Create input fields for the numbers and operator
num1_label = tk.Label(root, text="Number 1:")
num1_label.grid(row=0, column=0)

num1_entry = tk.Entry(root)
num1_entry.grid(row=0, column=1)

num2_label = tk.Label(root, text="Number 2:")
num2_label.grid(row=1, column=0)

num2_entry = tk.Entry(root)
num2_entry.grid(row=1, column=1)

operator_label = tk.Label(root, text="Operator:")
operator_label.grid(row=2, column=0)

operator_var = tk.StringVar(root)
operator_var.set("+")
operator_menu = tk.OptionMenu(root, operator_var, "+", "-", "*", "/")
operator_menu.grid(row=2, column=1)

# Create a button to perform the calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
