import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Conticazino Interest Rate Calculator")

# Define the function to calculate the interest rate
def interest_calculator():
    try:
        # Get the deposit from the entry fields
        deposit = float(entry1.get())
        
        # Perform the calculations
        interest_sum = deposit - ((deposit*19.6)/20)
        actual_deposit_value = (deposit*19.6)/20
        
        # Update the labels
        interest_label.config(text=f"Interest: {interest_sum}")
        actual_deposit_label.config(text=f"Actual Deposit: {actual_deposit_value}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers!")

# Create the deposit number input field
label1 = tk.Label(root, text="Enter deposit number:")
label1.pack(pady=5)

entry1 = tk.Entry(root)
entry1.pack(pady=5)

# Create the button to calculate
add_button = tk.Button(root, text="Calculate", command=interest_calculator)
add_button.pack(pady=10)

# Create the label to display the interest
interest_label = tk.Label(root, text="Interest: ")
interest_label.pack(pady=10)

# Create the label to display the actual deposit
actual_deposit_label = tk.Label(root, text="Actual Deposit: ")
actual_deposit_label.pack(pady=10)

# Run the main event loop
root.mainloop()