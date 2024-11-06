"""
    This Python TKinter GUI program should create
    a simple calculator with the following:

    1.  Row 1 with a label that says "Number1"
        Row 1 with an entry field for number1
        Row 1 with a button for addition
        Row 1 with a button for subtraction
        
    2.  Row 2 with a label that says "Number2"
        Row 2 with an entry field for number2
        Row 2 with a button for multiplication
        Row 2 with a button for division
        
    3.  Row 3 with a label that says "Answer"
        Row 3 with an readonly entry field for answer
        Row 3 with a button for modulo (remainder)
        Row 3 with a button for integer division
        
    4.  Row 4 with the following working buttons:
        Row 4 with a working button that says Clear
        Row 4 with a working button that says Exit
        Row 4 with a button for exponentiation
        
    Do not allow for non-numeric input, except for
    a "-" sign for a negative number and/or one
    decimal point.
"""
import tkinter as tk
from tkinter import messagebox

# Function to perform any/all calculations
def calculate(operation):
  try:
    # Convert the value in the efNumber1 entry field to a float
    num1 = float(efNumber1.get())
    # Convert the value in the efNumber2 entry field to a float
    num2 = float(efNumber2.get())

    match (operation):
      case "+":                 # Addition
        result = num1 + num2
        
      case "-":                 # Subtraction
        result = num1 - num2
        
      case "*":                 # Multiplication
        result = num1 * num2
        
      case "/":                 # Divison
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        
      case "%":                 # Modulo
        result = num1 % num2 if num2 != 0 else "Error: Division by zero"
        
      case "//":                # Integer Division
        result = num1 // num2 if num2 != 0 else "Error: Division by zero"
        
      case "**":                # Exponentiation
        result = num1 ** num2
      
      case "_":
        messagebox("INVALID OPERATION", "This operation cannot be performed.")
        return

    efAnswer.config(state=tk.NORMAL)    # Change readonly efAnswer to non-readonly
    efAnswer.delete(0, tk.END)          # Remove anything currently in efAnswer
    efAnswer.insert(0, str(result))     # Put answer into efAnswer
    efAnswer.config(state='readonly')   # Change non-readonly efAnswer to readonly
  except ValueError:
    messagebox.showerror("INPUT ERROR", "Please enter valid numbers")

# Function to clear any/all entry fields
def clearEntryFields():
  efNumber1.delete(0, tk.END)
  efNumber2.delete(0, tk.END)
  efAnswer.delete(0, tk.END)

# Function to validate input
def validateInput(action, value_if_allowed, prior_value):
  if (action == "1"):         # Insertion
    if (value_if_allowed in ["", "-", ".", "-."]):
      return True
    try:
      float(value_if_allowed)
      return True
    except ValueError:
      return False
  return True

def exitProgramOrNot():
  if (messagebox.askyesno("EXIT PROGRAM NOW?", "Do you want to exit")):
    root.quit()

# Main application window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("800x350")
fontSettings = ("Arial", 16, "bold")

# Row 1 (Number1)
lblNumber1 = tk.Label(root, text="Number1", font=fontSettings).grid(row=0, column=0, padx=10, pady=10)
efNumber1  = tk.Entry(root,  font=fontSettings, justify='center' )
efNumber1.grid(row=0, column=1, padx=10, pady=10)

# Row 2 (Number2)
lblNumber2 = tk.Label(root, text="Number2", font=fontSettings).grid(row=1, column=0, padx=10, pady=10)
efNumber2  = tk.Entry(root, font=fontSettings, justify='center')
efNumber2.grid(row=1, column=1, padx=10, pady=10)

# Row 3 (Answer)
lblAnswer = tk.Label(root, text="Answer", font=fontSettings).grid(row=2, column=0, padx=10, pady=10)
efAnswer  = tk.Entry(root, font=fontSettings, justify='center')
efAnswer.grid(row=2, column=1, padx=10, pady=10)

# Row 4 (Validation)
validateCmd = (root.register(validateInput), "%d", "%P", "%s")
efNumber1.config(validate="key", validatecommand=validateCmd)
efNumber2.config(validate="key", validatecommand=validateCmd)

# Row 5 (Operations Buttons)
btnAdd  = tk.Button(root, text="+",  font=fontSettings, width = 10, command=lambda: calculate("+")).grid(row=0,   column=3, padx=10, pady=10)
btnSub  = tk.Button(root, text="-",  font=fontSettings, width = 10, command=lambda: calculate("-")).grid(row=0,   column=4, padx=10, pady=10)
btnMul  = tk.Button(root, text="*",  font=fontSettings, width = 10, command=lambda: calculate("*")).grid(row=1,   column=3, padx=10, pady=10)
btnDiv  = tk.Button(root, text="/",  font=fontSettings, width = 10, command=lambda: calculate("/")).grid(row=1,   column=4, padx=10, pady=10)
btnMod  = tk.Button(root, text="%",  font=fontSettings, width = 10, command=lambda: calculate("%")).grid(row=2,   column=3, padx=10, pady=10)
btnIDiv = tk.Button(root, text="//", font=fontSettings, width = 10, command=lambda: calculate("//")).grid(row=2,  column=4, padx=10, pady=10)
btnExp  = tk.Button(root, text="**", font=fontSettings, width = 10, command=lambda: calculate("**")).grid(row=3,  column=3, padx=10, pady=10)

# Row 6 (Clear and Exit Buttons)
btnClear = tk.Button(root, text="Clear", font=fontSettings, width=10, command=clearEntryFields).grid(row=4, column=0, padx=10, pady=10)
btnExit  = tk.Button(root, text="Exit",  font=fontSettings, width=10, command=exitProgramOrNot).grid(row=4, column=1, padx=10, pady=10)

# Start the Tkinter loop
root.mainloop()