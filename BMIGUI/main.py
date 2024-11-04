'''
    Write a Python GUI TKinter program to calculate
    and display a person's body mass index (BMI).  BMI
    is used to determine whether a person is underweight, 
    optimal weight, overweight or obese for his or her 
    height using the following formula:

    bmi = weight * 703 / (height * height)

    Weight is inputted in lbs. (int) and height is
    inputted in inches (int). For valid input, the
    program should calculate and display the BMI and
    a message indicating whether a person is underweight,
    optimal weight, overweight, or obese for their height
    using these metrics:

    a)	A BMI <  18.5 is considered underweight.
    b)	A BMI >= 18.5 and < 25.0 is considered optimal weight.
    c)	A BMI >= 25.0 and < 30.0 is considered overweight.
    d)	A BMI >= 30.0 is considered obese.  Use constants!

    In addition to above, make sure the program also:

    1.	Assures a valid numeric height between 12 (MINHEIGHT)
        and 96 (MAXHEIGHT) is inputted or an error message is
        displayed. Note: These are arbitrary values.

    2.	Assures a valid numeric weight between 1 (MINWEIGHT)
        and 777 (MAXWEIGHT) is inputted or an error message is
        displayed. Note: These are arbitrary values.

    3.	Lets the user run the program multiple times if/as
        desired.  Keep track of the total number of underweight,
        the total number of optimal weight, the total number of
        overweight, and the total number of obese weight BMIs.
        Output these totals at the end of the program.
'''
import tkinter as tk
from tkinter import messagebox

# Constants
MINHEIGHT   =  12   # inches
MAXHEIGHT   =  96   # inches
MINWEIGHT   =   1   # pounds
MAXWEIGHT   = 777   # inches
MINOPTIMAL  = 18.5  # Minimum BMI for an optimal weight person
MINOVER     = 25.0  # Minimum BMI for an overweight person
MINOBESE    = 30.0  # Minimum BMI for an obese person

# Accumulators
totalUnderweight    = 0
totalOptimalWeight  = 0
totalOverweight     = 0
totalObese          = 0

class BMIApp:
  def __init__(self, root):
    self.root = root
    self.root.title("BMI Calculator")

    # Set widgets (labels, entry fields, and buttons)
    # for the application
    # Height label and entry field
    lblHeight = tk.Label(root, text ="Height (in inches): ").grid(row=0, column=0, padx=5, pady=5, stick="e")
    self.efHeight = tk.Entry(root)
    self.efHeight.grid(row=0, column=1, padx=5, pady=5)

    # Weight label and entry field
    lblWeight = tk.Label(root, text ="Weight (in lbs): ").grid(row=1, column=0, padx=5, pady=5, stick="e")
    self.efWeight = tk.Entry(root)
    self.efWeight.grid(row=1, column=1, padx=5, pady=5)

    # Buttons
    tk.Button(root, text="Calculate BMI", command=self.calculateBMI).grid(row=2, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Show Totals",   command=self.showTotals).grid(row=3, column=0, columnspan=2, pady=10)

  def calculateBMI(self):
    try:
      height = int(self.efHeight.get())
      weight = int(self.efWeight.get())

      # Height range check (must be between 12 and 96)
      if not (MINHEIGHT <= height <= MAXHEIGHT):
        raise ValueError(f"Height Must Be Between {MINHEIGHT} And {MAXHEIGHT} Inches.")

      # Weight range check (must be between 1 and 777)
      if not (MINWEIGHT <= weight <= MAXWEIGHT):
        raise ValueError(f"Weight Must Be Between {MINWEIGHT} And {MAXWEIGHT} Pounds.")

      # Height and Weight inputs both valid.
      # So calculate BMI using formula above
      bmi = weight * 703 / (height * height)

      bmiStatus = self.determineBMIStatus(bmi)

      messagebox.showinfo("CURRENT BMI STATS:", f"BMI: {round(bmi, 2)}\nStatus: {bmiStatus}")

    except ValueError as e:
      messagebox.showerror("INVALID INPUT", str(e))

  def determineBMIStatus(self, bmi):
    global totalUnderweight, totalOptimalWeight, totalOverweight, totalObese

    if (bmi < MINOPTIMAL):      # Calculated BMI < 18.5
      # Increment total underweight counter
      totalUnderweight += 1
      return "Underweight"
    elif (bmi < MINOVER):       # Calculated BMI >= 18.5 and < 25.0
      # Increment total optimal weight counter
      totalOptimalWeight += 1
      return "Optimal Weight"
    elif (bmi < MINOBESE):      # Calculated BMI >= 25.0 and < 30.0
      # Increment total overweight counter
      totalOverweight += 1
      return "Overweight"
    else:                       # Calculated BMI >= 30.0
      # Increment total obese counter
      totalObese += 1
      return "Obese"

  def showTotals(self):
    global totalUnderweight, totalOptimalWeight, totalOverweight, totalObese

    messagebox.showinfo("TOTALS", f"Total Underweight:    {totalUnderweight}\n"
                                  f"Total Optimal weight: {totalOptimalWeight}\n"
                                  f"Total Overweight:     {totalOverweight}\n"
                                  f"Total Obese:          {totalObese}")

# Main Program
root = tk.Tk()
root.geometry("300x500")
app = BMIApp(root)
root.mainloop()
    