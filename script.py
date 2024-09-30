import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Addition App")

# Define the function to calculate the interest rate
def interest_calculator():
    try:
        # Get the deposit from the entry fields
        deposit = float(entry1.get())
        
        # Perform the calculations
        interest_sum = deposit - ((deposit*19.6)/20)
        
        
        # Update the labels
        result_label.config(text=f"Interest: {interest_sum}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers!")

# Create the first number input field
label1 = tk.Label(root, text="Enter first number:")
label1.pack(pady=5)

entry1 = tk.Entry(root)
entry1.pack(pady=5)

# Create the second number input field
label2 = tk.Label(root, text="Enter second number:")
label2.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Create the button to add numbers
add_button = tk.Button(root, text="Add", command=add_numbers)
add_button.pack(pady=10)

# Create the label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# Run the main event loop
root.mainloop()