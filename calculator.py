import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the display
display = tk.Entry(window, width=35, bg="lightgray")
display.grid(row=0, column=0, columnspan=5)

# Create the buttons
button_list = [
    "7", "8", "9", "+", "C",
    "4", "5", "6", "-", "√",
    "1", "2", "3", "*", "/",
    "0", ".", "=", "+/-", "%"
]

row = 1
col = 0
for button_text in button_list:
    def cmd(x=button_text):
        click(x)
    tk.Button(window, text=button_text, width=5, command=cmd).grid(row=row, column=col)
    col += 1
    if col > 4:
        col = 0
        row += 1

# Create the click function
def click(key):
    if key == "=":
        # Evaluate the expression and display the result
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    elif key == "C":
        # Clear the display
        display.delete(0, tk.END)
    elif key == "√":
        # Calculate the square root and display the result
        result = eval(display.get())**0.5
        display.delete(0, tk.END)
        display.insert(0, str(result))
    elif key == "+/-":
        # Change the sign of the number in the display
        if display.get()[0] == "-":
            display.delete(0)
        else:
            display.insert(0, "-")
    elif key == "%":
        # Calculate the percentage and display the result
        result = eval(display.get())/100
        display.delete(0, tk.END)
        display.insert(0, str(result))
    else:
        # Add the key to the display
        display.insert(tk.END, key)

# Run the main loop
window.mainloop()