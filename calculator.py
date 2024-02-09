import tkinter as tk

# Function to update the display
def button_click(symbol):
    current = display_var.get()
    if symbol == '=':
        try:
            result = eval(current)
            display_var.set(str(result))
        except:
            display_var.set("Error")
    elif symbol == 'C':
        display_var.set('')
    else:
        display_var.set(current + symbol)

# Creating main window
root = tk.Tk()
root.title("Calculator")

# Variable to hold the current display value
display_var = tk.StringVar()
display_var.set('')

# Display widget
display = tk.Entry(root, textvariable=display_var, font=('Arial', 20), bd=10, insertwidth=4, width=15, justify='right')
display.grid(row=0, column=0, columnspan=4)

# Button symbols
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Create buttons
for i in range(4):
    for j in range(4):
        btn = tk.Button(root, text=buttons[i][j], font=('Arial', 16), width=5, height=2,
                        command=lambda symbol=buttons[i][j]: button_click(symbol))
        btn.grid(row=i+1, column=j, padx=5, pady=5)

# Run the application
root.mainloop()
