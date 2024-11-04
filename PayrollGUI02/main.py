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

    7.  Row 7 with a label for Total # of Employees
        Row 7 with an entry field Total # of Employees

    8.  Row 8 with a label for Lowest Paid Employee
        Row 8 with an entry field Lowest Paid Employee
    
    9.  Row 9 with a label for Highest Paid Employee
        Row 9 with an entry field Highest Paid Employee
    
    10. Row 10 with a label for Average Paid Employee
        Row 10 with an entry field Average Paid Employee
    
    11. Row 11 with a label for Total Payroll
        Row 11 with an entry field for Total Payroll
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

class Payroll02GUI:
  def __init__(self, root):
    self.root = root
    self.root.title("Payroll Calculator 02")

    # Set the window size
    root.geometry("800x800")
    self.root.configure(padx=20, pady=20)

    # Set a variable for global font setting
    self.fontSettings = ("Arial", 16, "bold")
    self.widget_width = 20

    # Initialize Payroll data
    self.totalEmployees = 0
    self.totalPayroll   = 0.00
    self.lowPay         = None
    self.highPay        = None
    self.avgPay         = None

    # Create and place widgets
    self.createWidgets()

  def createWidgets(self):
    # Row 0 (First Name label and entry field)
    tk.Label(self.root, text="First Name", font=self.fontSettings, width=12).grid(row=0, column=0, padx=10, pady=10, sticky="w")
    self.efFirstName = tk.Entry(self.root, font=self.fontSettings, width=10)
    self.efFirstName.grid(row=0, column=1, padx=10, pady=10)

    # Row 1 (Last Name label and entry field)
    tk.Label(self.root, text="Last Name", font=self.fontSettings, width=12).grid(row=1, column=0, padx=10, pady=10, sticky="w")
    self.efLastName = tk.Entry(self.root, font=self.fontSettings, width=10)
    self.efLastName.grid(row=1, column=1, padx=10, pady=10)

    # Row 2 (Hours Worked label and entry field)
    tk.Label(self.root, text="Hours Worked", font=self.fontSettings, width=12).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    self.efHoursWorked = tk.Entry(self.root, font=self.fontSettings, width=10)
    self.efHoursWorked.grid(row=2, column=1, padx=10, pady=10)

    # Row 3 (Hourly Rate label and entry field)
    tk.Label(self.root, text="Hourly Rate", font=self.fontSettings, width=12).grid(row=3, column=0, padx=10, pady=10, sticky="w")
    self.efHourlyRate = tk.Entry(self.root, font=self.fontSettings, width=10)
    self.efHourlyRate.grid(row=3, column=1, padx=10, pady=10)

    # Row 4 (Gross Pay label and entry field)
    tk.Label(self.root, text="Gross Pay", font=self.fontSettings, width=12).grid(row=4, column=0, padx=10, pady=10, sticky="w")
    self.efGrossPay = tk.Entry(self.root, font=self.fontSettings, width=10, state="readonly")
    self.efGrossPay.grid(row=4, column=1, padx=10, pady=10)

    # Row 5 (Buttons)
    self.btnCalculate = tk.Button(self.root, text="Calculate", font=self.fontSettings, width=10, command=self.calculateGrossPay)
    self.btnCalculate.grid(row=5, column=0, padx=10, pady=20)

    self.btnClear = tk.Button(self.root, text="Clear", font=self.fontSettings, width=10, command=self.clearFields)
    self.btnClear.grid(row=5, column=1, padx=10, pady=20)

    self.btnExit = tk.Button(self.root, text="Exit", font=self.fontSettings, width=10, command=self.exitProgramOrNot)
    self.btnExit.grid(row=5, column=2, padx=10, pady=20)

    # Row 6 (Total # of Employees)
    tk.Label(self.root, text="Total # Emps", font=self.fontSettings, width=20).grid(row=6, column=0, padx=10, pady=10, sticky="w")
    self.efTotalEmps = tk.Entry(self.root, font=self.fontSettings, width=10, state="readonly")
    self.efTotalEmps.grid(row=6, column=1, padx=10, pady=10)

    # Row 7 (Lowest Paid Employee)
    tk.Label(self.root, text="Lowest Paid", font=self.fontSettings, width=20).grid(row=7, column=0, padx=10, pady=10, sticky="w")
    self.efLowestEmp = tk.Entry(self.root, font=self.fontSettings, width=10, state="readonly")
    self.efLowestEmp.grid(row=7, column=1, padx=10, pady=10)

    # Row 8 (Highest Paid Employee)
    tk.Label(self.root, text="Highest Paid", font=self.fontSettings, width=20).grid(row=8, column=0, padx=10, pady=10, sticky="w")
    self.efHighestEmp = tk.Entry(self.root, font=self.fontSettings, width=10, state="readonly")
    self.efHighestEmp.grid(row=8, column=1, padx=10, pady=10)

    # Row 9 (Average Paid Employee)
    tk.Label(self.root, text="Avg Paid", font=self.fontSettings, width=20).grid(row=9, column=0, padx=10, pady=10, sticky="w")
    self.efAvgEmp = tk.Entry(self.root, font=self.fontSettings, width=10, state="readonly")
    self.efAvgEmp.grid(row=9, column=1, padx=10, pady=10)

    # Row 10 (Total Payroll)
    tk.Label(self.root, text="Tot Payroll", font=self.fontSettings, width=20).grid(row=10, column=0, padx=10, pady=10, sticky="w")
    self.efTotPayroll = tk.Entry(self.root, font=self.fontSettings, width=10, state="readonly")
    self.efTotPayroll.grid(row=10, column=1, padx=10, pady=10)

  def calculateGrossPay(self):
    try:
      firstName     = self.efFirstName.get().strip()
      lastName      = self.efLastName.get().strip()
      hoursWorked   = self.efHoursWorked.get().strip()
      hourlyRate    = self.efHourlyRate.get().strip()

      # Verify that neither firstName nor lastName are empty
      if (not firstName or not lastName):
        raise ValueError("Both FirstName and LastName are mandatory!")
      
      # Verify that neither hoursWorked nor hourlyRate are empty
      if (not hoursWorked or not hourlyRate):
        raise ValueError("Both HoursWorked and HourlyRate are mandatory!")
      
      # Attempt to convert what is in hoursWorked and
      # hourlyRate entry fields into their float equivalent
      hoursWorked = float(hoursWorked)
      hourlyRate  = float(hourlyRate)
      
      # Range check for hoursWorked (must be between 0.00 - 84.00)
      if (hoursWorked < MINHOURS or hoursWorked > MAXHOURS):
        raise ValueError(f"Hours Worked MUST BE BETWEEN {MINHOURS} and {MAXHOURS}")

      # Range check for hourlyRate (must be between .00 - 99.99)
      if (hourlyRate < MINHRATE or hourlyRate > MAXHRATE):
        raise ValueError(f"Hourly Rate MUST BE BETWEEN {MINHRATE} and {MAXHRATE}")

      # Both hoursWorked and hourlyRate were valid
      # Calculate grossPay, including OT for hoursWorked > 40
      if (hoursWorked > MAXNONOT):   # Worked > 40 hours, person has OT coming
        otHours = hoursWorked - MAXNONOT
        grossPay = (MAXNONOT * hourlyRate) + (otHours * hourlyRate * OVERRATE)
      # Otherwise, no OT worked. gross is hoursWorked * hourlyRate
      else:
        grossPay = hoursWorked * hourlyRate
      
      self.updatePayrollStats(grossPay)

      # Put the grossPay variable value into the efGrossPay entry field
      self.efGrossPay.config(state="normal")
      self.efGrossPay.delete(0, tk.END)
      self.efGrossPay.insert(0, f"${grossPay: .2f}")
      self.efGrossPay.config(state="readonly")

    except ValueError as e:
      messagebox.showerror("Invalid Input: ", str(e))

  def updatePayrollStats(self, grossPay):
    # Increment total # of employees
    self.totalEmployees += 1

    # Increment total pay accumulator
    self.totalPayroll += grossPay

    self.lowPay  = min(self.lowPay or grossPay, grossPay)
    self.highPay = max(self.highPay or grossPay, grossPay)
    self.avgPay  = self.totalPayroll / self.totalEmployees

    self.updateCurrentEntry(self.efTotalEmps,   self.totalEmployees)
    self.updateCurrentEntry(self.efLowestEmp,   self.lowPay)
    self.updateCurrentEntry(self.efHighestEmp,  self.highPay)
    self.updateCurrentEntry(self.efAvgEmp,      self.avgPay)
    self.updateCurrentEntry(self.efTotPayroll,  self.totalPayroll)

  def updateCurrentEntry(self, entry, value):
    # Make readonly current entry non-readonly
    entry.config(state="normal")

    # Delete whatever is in the current entry
    entry.delete(0, tk.END)

    # Insert current entry
    entry.insert(0, str(value))

    # Make normal current entry readonly
    entry.config(state="readonly")

  def clearFields(self):
    self.efFirstName.delete(0, tk.END)
    self.efLastName.delete(0, tk.END)
    self.efHoursWorked.delete(0, tk.END)
    self.efHourlyRate.delete(0, tk.END)
    self.efGrossPay.config(state="normal")
    self.efGrossPay.delete(0, tk.END)
    self.efGrossPay.config(state="readonly")
    self.efFirstName.focus_set()

  def exitProgramOrNot(self):
    if messagebox.askyesno("Exit", "Are You Sure You Want To Exit Program?"):
      self.root.destroy()

# Set up program interface
# Create the main window
root = tk.Tk()

# Instantiate the app
app = Payroll02GUI(root)
root.mainloop()
