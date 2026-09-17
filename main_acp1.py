import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        # Get the numbers from the entry fields
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        # Calculate the product
        result = num1 * num2
        
        # Update the result label
        lbl_result.config(text=f"Product: {result}")
    except ValueError:
        # Show an error box if the user types something that isn't a number
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Set up the main window
window = tk.Tk()
window.title("Product Calculator")
window.geometry("300x250")

# Create and place the first number input
lbl_num1 = tk.Label(window, text="Enter first number:")
lbl_num1.pack(pady=5)
entry1 = tk.Entry(window)
entry1.pack(pady=5)

# Create and place the second number input
lbl_num2 = tk.Label(window, text="Enter second number:")
lbl_num2.pack(pady=5)
entry2 = tk.Entry(window)
entry2.pack(pady=5)

# Create and place the calculation button
btn_calculate = tk.Button(window, text="Calculate Product", command=calculate_product)
btn_calculate.pack(pady=15)

# Create and place the result label
lbl_result = tk.Label(window, text="Product: ", font=("Arial", 12, "bold"))
lbl_result.pack(pady=5)

# Run the Tkinter event loop
window.mainloop()