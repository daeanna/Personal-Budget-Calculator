#! /usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from plyer import notification

# Define color theme
COLOR_THEME = "#393646"
BUTTON_COLOR = "#4F4557"
LABEL_COLOR = "#6D5D6E"
ENTRY_COLOR = "#F4EEE0"

# Function to calculate total expenses
def calculate_total():
    total_expenses = sum(item[1] for item in expenses)
    total_label.config(text=f"Total Expenses: ${total_expenses:.2f}")

# Function to add expense
def add_expense():
    item = item_entry.get()
    cost = float(cost_entry.get())
    expenses.append((item, cost))
    update_expense_list()
    calculate_total()
    # Save expenses as a notification event
    notification_title = "New Expense Added"
    notification_text = f"{item}: ${cost:.2f}"
    notification.notify(title=notification_title, message=notification_text)

# Function to update expense list
def update_expense_list():
    expense_list.delete(0, tk.END)
    for item, cost in expenses:
        expense_list.insert(tk.END, f"{item}: ${cost:.2f}")

# Initialize expenses list
expenses = []

# Create main window
root = tk.Tk()
root.title("Budget Calculator")
root.configure(background=COLOR_THEME)

# Set custom font
font_style = ("Helvetica", 12)

# Set font globally
style = ttk.Style()
style.configure('.', font=font_style)

# Create labels
item_label = ttk.Label(root, text="Item:", background=COLOR_THEME, foreground=LABEL_COLOR)
item_label.grid(row=0, column=0, padx=10, pady=5)
cost_label = ttk.Label(root, text="Cost ($):", background=COLOR_THEME, foreground=LABEL_COLOR)
cost_label.grid(row=1, column=0, padx=10, pady=5)
total_label = ttk.Label(root, text="Total Expenses: $0.00", background=COLOR_THEME, foreground=LABEL_COLOR)
total_label.grid(row=3, column=0, padx=10, pady=5)

# Create entry fields
item_entry = ttk.Entry(root, style="EntryStyle.TEntry")
item_entry.grid(row=0, column=1, padx=10, pady=5)
cost_entry = ttk.Entry(root, style="EntryStyle.TEntry")
cost_entry.grid(row=1, column=1, padx=10, pady=5)

# Create buttons
add_button = ttk.Button(root, text="Add Expense", style="ButtonStyle.TButton", command=add_expense)
add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="WE")
quit_button = ttk.Button(root, text="Quit", style="ButtonStyle.TButton", command=root.quit)
quit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

# Create expense list
expense_list = tk.Listbox(root, bg=ENTRY_COLOR, fg=COLOR_THEME)
expense_list.grid(row=0, column=2, rowspan=5, padx=10, pady=5, sticky="NSWE")

# Configure grid
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(2, weight=1)

# Styling
style = ttk.Style()
style.configure("TEntry", foreground=COLOR_THEME, background=ENTRY_COLOR)
style.configure("TButton", foreground=COLOR_THEME, background=BUTTON_COLOR)
style.map("TButton", background=[("active", "#695C75")])

# Run the application
root.mainloop()
