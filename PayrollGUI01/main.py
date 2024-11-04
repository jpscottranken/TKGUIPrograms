"""
    Create a simple Python GUI Payroll program
    using TKinter set up in the following way:

    1.  Row 1 with a label for First Name
        Row 1 with an entry field for first name    (Cannot be blank)

    2.  Row 2 with a label for Last Name
        Row 2 with an entry field for last name     (Cannot be blank)

    3.  Row 3 with a label for Hours Worked
        Row 3 with an entry field for hours worked  (Must be between 0.00 - 84.00)

    4.  Row 4 with a label for Hourly Rate
        Row 4 with an entry field for hourly rate   (Must be between 0.00 - 99.99)

    5.  Row 5 with a label for Gross Pay
        Row 5 with an entry field for gross pay     (With OT for hw > 40)

    6.  Row 6 with a working button text Calculate  (Calculate the gross pay)
        Row 6 with a working button text Clear      (Set focus to First Name)
        Row 6 with a working button text Exit       (Let user end pgm or not)
"""
import tkinter as tk
from   tkinter import messagebox

# Constants
MINHOURS =  0.00
MAXHOURS = 84.00
MINHRATE =  0.00
MAXHRATE = 99.99
MAXNONOT = 40.00
OVERRATE =  1.50

def calculateGrossPay():
  try:
    # FirstName Error Handling
    if (efFirstName.index)("end") == 0:
      raise ValueError("First Name CANNOT Be Empty")

    # LastName Error Handling
    if (efLastName.index)("end") == 0:
      raise ValueError("Last Name CANNOT Be Empty")
    
    # HoursWorked Error Handling
    if (efHoursWorked.index)("end") == 0:
      raise ValueError("Hours Worked CANNOT Be Empty")
    
    # Get the value from hoursWorked entry field
    hoursWorked = float(efHoursWorked.get())

    # HoursWorked range check (>= 0.00 and <= 84.00)
    if (hoursWorked < MINHOURS or hoursWorked > MAXHOURS):
      raise ValueError(f"Hours Worked MUST BE BETWEEN {MINHOURS} And {MAXHOURS}")

    # HourlyRate Error Handling
    if (efHourHourlyRate.index)("end") == 0:
      raise ValueError("Hourly Rate CANNOT Be Empty")

    # Get the value from hoursWorked entry field
    hourlyRate = float(efHourHourlyRate.get())
    
    # HourlyRate range check (>= 0.00 and <= 99.99)
    if (hourlyRate < MINHRATE or hourlyRate > MAXHRATE):
      raise ValueError(f"Hourly Rate MUST BE BETWEEN {MINHRATE} And {MAXHRATE}")

    # Both hoursWorked and hourlyRate were valid
    # Calculate grossPay, including OT for hoursWorked > 40
    if (hoursWorked > MAXNONOT):   # Person has OT coming
      otHours = hoursWorked - MAXNONOT
      grossPay = (MAXNONOT * hourlyRate) + (otHours * hourlyRate * OVERRATE)
    # Otherwise, no OT worked. gross is hoursWorked * hourlyRate
    else:
      grossPay = hoursWorked * hourlyRate

    # Put the grossPay variable value into the efGrossPay entry field
    efGrossPay.config(state="normal")
    efGrossPay.delete(0, tk.END)
    efGrossPay.insert(0, f"${grossPay: .2f}")
    efGrossPay.config(state="readonly")

  except ValueError as e:
    messagebox.showerror("Invalid Input: ", str(e))

def clearFields():
  efFirstName.delete(0, tk.END)
  efLastName.delete(0, tk.END)
  efHoursWorked.delete(0, tk.END)
  efHourHourlyRate.delete(0, tk.END)
  efGrossPay.config(state="normal")
  efGrossPay.delete(0, tk.END)
  efGrossPay.config(state="readonly")
  efFirstName.focus_set()

def exitProgramOrNot():
  if messagebox.askyesno("Exit", "Are You Sure You Want To Exit Program?"):
    root.destroy()

# Set up program interface
# Create the main window
root = tk.Tk()

# Set the window title
root.title("Payroll Calculator 01")

# Set a variable for global font setting
fontSettings = ("Arial", 16, "bold")

# Set the window size
root.geometry("515x350")

# Row 0 (First Name label and entry field)
tk.Label(root, text="First Name", font=fontSettings, width=12).grid(row=0, column=0, padx=10, pady=10, sticky="e")
efFirstName = tk.Entry(root, font=fontSettings, width=10)
efFirstName.grid(row=0, column=1, padx=10, pady=10)

# Row 1 (Last Name label and entry field)
tk.Label(root, text="Last Name", font=fontSettings, width=12).grid(row=1, column=0, padx=10, pady=10, sticky="e")
efLastName = tk.Entry(root, font=fontSettings, width=10)
efLastName.grid(row=1, column=1, padx=10, pady=10)

# Row 2 (Hours Worked label and entry field)
tk.Label(root, text="Hours Worked", font=fontSettings, width=12).grid(row=2, column=0, padx=10, pady=10, sticky="e")
efHoursWorked = tk.Entry(root, font=fontSettings, width=10)
efHoursWorked.grid(row=2, column=1, padx=10, pady=10)

# Row 3 (Hourly Rate label and entry field)
tk.Label(root, text="Hourly Rate", font=fontSettings, width=12).grid(row=3, column=0, padx=10, pady=10, sticky="e")
efHourHourlyRate = tk.Entry(root, font=fontSettings, width=10)
efHourHourlyRate.grid(row=3, column=1, padx=10, pady=10)

# Row 4 (Gross Pay label and entry field)
tk.Label(root, text="Gross Pay", font=fontSettings, width=12).grid(row=4, column=0, padx=10, pady=10, sticky="e")
efGrossPay = tk.Entry(root, font=fontSettings, width=10, state="readonly")
efGrossPay.grid(row=4, column=1, padx=10, pady=10)

# Row 5 (Buttons)
btnCalculate = tk.Button(root, text="Calculate", font=fontSettings, width=10, command=calculateGrossPay)
btnCalculate.grid(row=5, column=0, padx=10, pady=20)

btnClear = tk.Button(root, text="Clear", font=fontSettings, width=10, command=clearFields)
btnClear.grid(row=5, column=1, padx=10, pady=20)

btnExit = tk.Button(root, text="Exit", font=fontSettings, width=10, command=exitProgramOrNot)
btnExit.grid(row=5, column=2, padx=10, pady=20)

root.mainloop()
