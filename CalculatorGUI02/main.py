"""
    This GUI calculator was "gleaned" from
    the following URL/article:

    https://medium.com/pythonflood/learn-python-by-creating-a-calculator-3c7788c2d4fa

    The application is designed to perform basic arithmetic operations 
    and offer a user-friendly graphical interface for easy interaction.

    The primary objectives of this Python Project are:

    1.  The goal is to create a functional calculator capable of 
        performing basic arithmetic operations such as addition, 
        subtraction, multiplication, and division. In addition,
        JPS provided the following extra math operations:

        a.  %  for modulo (remainder).
        b.  // for straight integer division.
        c.  ** for exponentiation.
    
    2.  To provide a graphical user interface (GUI) that is intuitive 
        and easy to navigate.
    
    3.  To ensure that the calculator handles user inputs and errors 
        effectively.
    
    4.  Additional features like square root computation, character 
        deletion, modulo, integer division, and exponentiation are
        implemented to enhance the application's usability.
"""

# import necessary libraries
#
# Tkinter provides the necessary tools for creating the GUI, 
# allowing the development of a windowed application with 
# interactive components.
#
# The math library performs specific mathematical operations, 
# such as calculating the square root.
import tkinter as tk
import math

# Function to evaluate the expression
#
# The calculate_expression function evaluates the 
# mathematical expression input by the user.
# 
# It retrieves the text from the display and uses 
# the eval function to compute the result, which is 
# then displayed in the entry field.
# 
# If an error occurs, such as a syntax error or
# division by zero, the function catches the exception 
# and displays "Error."
def calculate_expression():
  try:
    result = eval(display.get())
    display.delete(0, tk.END)
    display.insert(tk.END, str(result))
  except Exception as e:
    display.delete(0, tk.END)
    display.insert(tk.END, "Error")

# Function to clear the entry field
#
# The clear_display function clears the display field, 
# allowing users to start a new calculation. It uses 
# the display delete method to remove any text from 
# the entry field.
def clear_display():
  display.delete(0, tk.END)

# Function to delete the last character from the entry field
#
# This function allows users to correct mistakes by deleting 
# the last character entered in the display field.
# 
# It first retrieves the current text and then deletes the
# last character if any is present.
def delete_last_character():
  current_text = display.get()
  if current_text:
    display.delete(len(current_text) - 1, tk.END)

# Function to append characters to the entry field
#
# The add_character_to_display function appends a 
# specified character to the current text in the 
# display.
# 
# This function is crucial for building mathematical
# expressions one character at a time.
def add_character_to_display(character):
  display.insert(tk.END, character)

# Function to calculate the square root
#
# This function computes the square root of the value
# in the display.
# 
# It first evaluates the current expression and then
# applies the math.sqrt function to calculate the 
# square root. The result is displayed if the 
# computation is successful; otherwise, "Error" is shown.
def calculate_square_root():
  try:
    result = math.sqrt(eval(display.get()))
    display.delete(0, tk.END)
    display.insert(tk.END, str(result))
  except Exception as e:
    display.delete(0, tk.END)
    display.insert(tk.END, "Error")

# Create the main application window
#
# Initialize the main application window using 
# tk.Tk(), which creates the root window for the 
# calculator.
# 
# The title of the window is set as well.
app_window = tk.Tk()
app_window.title("Basic Calculator From medium.com")
app_window.geometry("500x500")
fontSettings = ("Arial", 16, "bold")

# Create an entry field for displaying input and results
#
# The display is an entry widget that shows user inputs 
# and results. It has a width of 30 characters and uses
# Arial font size 14 for readability.
# 
# It is placed at the top of the window, spans five columns.
display = tk.Entry(app_window, width=30, justify='center', font=fontSettings)
display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Define the layout of the calculator buttons
#
# The buttons are arranged in a grid layout, with 
# each sublist representing a row of buttons.
# 
# This layout helps organize the buttons logically in the GUI.
buttons = [
  ['(', ')', '←', 'Clear'],
  ['7', '8', '9', '+', '√'],
  ['4', '5', '6', '-', '%'],
  ['1', '2', '3', '*', '//'],
  ['0', '.', '=', '/', '**']
]

# Create the buttons and assign them functions
#
# Buttons are created and assigned specific 
# functions based on their labels.
# 
# For instance, the equals button is linked to
# calculate_expression, and the clear button to
# clear_display.
# 
# Other buttons like numbers and operators use
# add_character_to_display with their respective text.
for r, button_row in enumerate(buttons, start=1):
  for c, button_text in enumerate(button_row):
    if button_text == '=':
      btn = tk.Button(app_window, text=button_text, font=fontSettings, width=5, command=calculate_expression)
    elif button_text == 'Clear':
      btn = tk.Button(app_window, text=button_text, font=fontSettings, width=5, command=clear_display)
    elif button_text == '←':
      btn = tk.Button(app_window, text=button_text, font=fontSettings, width=5, command=delete_last_character)
    elif button_text == '√':
      btn = tk.Button(app_window, text=button_text, font=fontSettings, width=5, command=calculate_square_root)
    else:
      btn = tk.Button(app_window, text=button_text, font=fontSettings, width=5, command=lambda char=button_text: add_character_to_display(char))
      
    btn.grid(row=r, column=c, padx=5, pady=5)

# Allow the grid to resize with the window
#
# The grid layout is configured to resize 
# proportionally with the window, ensuring that 
# the interface remains consistent and 
# user-friendly regardless of the window size.
for i in range(5):
  app_window.grid_columnconfigure(i, weight=1)
for i in range(6):
  app_window.grid_rowconfigure(i, weight=1)

# Start the Tkinter main loop
#
# The app_window.mainloop() call starts the Tkinter 
# event loop, which keeps the application running 
# and responsive to user inputs.
# 
# This loop continues until the user closes the window.
app_window.mainloop()