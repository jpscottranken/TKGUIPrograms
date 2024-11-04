"""
  Scenario: Write a Python TKinter program to generate
  a random number between either 1 - 10, 1 - 100,
  or 1 - 1000 and asks the user to guess said number.  
     
  See the following URL: https://pythonspot.com/random-numbers/

  # Generates a random integer between 1 and either 10, 100, or 1000.

                  Requirements:
                  =============
  a)	Create constants for minimum guess (1), maximum guess (10, 100,
      or 1000) and any string error text desired.

  b)	At the end of each guessing game iteration, ask 
      the user if s/he wants to run the program again and 
      let them do so indefinitely if/as desired.

  c)	Put in code to clear all variables at the beginning 
      of each program run.

  d)	Put in the code that generates a random number from 
      1 to 10, 100, or 1000 (use the constants).

  e)	Put in the code that lets the user make a guess. 

  f)	Put in the code to determine the guess status 
      (invalid, too low, too high, or correct guess).

    If a guess is non-numeric, < 1 or > 10, 100,
    or 1000, the program should display "All guesses must 
    be numbers between 1 - 10, 100, or 1000.  Please try again."
    Do not increment total guesses.

    If a guess (e.g., 67) is higher/lower than the 
    generated random number, the program should display 
    "The guess of 67 is too low/high. Please try again."  
    Do increment total guesses.

    If a guess (e.g., 67) is correct, the user should be 
    given an associated message like "The guess of 67 in 4 
    guesses was correct!"  Do increment total guesses.

  g)	The program should continue to solicit user guesses 
      until the user correctly guesses the random number 
      and then print out the message as shown above. Let 
      the user continue to "play the game" as many times 
      as desired, generating a new random number each time.
"""
import tkinter as tk
from tkinter import messagebox
from random  import randint

# Constants
MINNUMBER     =    1
MAXNUMBEREZ   =   10
MAXNUMBERMED  =  100
MAXNUMBERHARD = 1000

# Global variables
numberToGuess = 0
totalGuesses  = 0
maxNumber     = 0   # MAXNUMBEREZ or MAXNUMBERMED or MAXNUMBERHARD

# Set upper limit for the game
# based on the choice of the user.
def setUpperLimit(selection):
  global numberToGuess, maxNumber

  # Determine if maxNumber is 10, 100 or 1000.
  match selection:
    case "1":
         maxNumber = MAXNUMBEREZ    # Number between 1 - 10
    case "2":
         maxNumber = MAXNUMBERMED   # Number between 1 - 100
    case "3":
         maxNumber = MAXNUMBERHARD  # Number between 1 - 1000
    case _:
        messagebox.showerror("INVALID INPUT", "Please select an option between 1 - 3")
        return
  
  # Generate the random number
  numberToGuess = randint(MINNUMBER, maxNumber)
  startTheGame()

def startTheGame():
  global totalGuesses

  # Set totalGuesses counter to 0
  totalGuesses = 0

  # Clear out any value in the guess entry field
  efGuess.delete(0, tk.END)

  # Provide feedback to the user
  lblFeedback.config(text=f"Enter a guess between {MINNUMBER} and {maxNumber}")
  lblFeedback.pack(pady=10)
  efGuess.pack(pady=10)
  btnGuess.pack(pady=10)
  btnGuess.config(state=tk.NORMAL)

def checkCurrentGuess():
  global totalGuesses, numberToGuess

  try:
    # Grab current guess from entry field
    guess = int(efGuess.get())

    # Validate that the guess was within range.
    # If not within range, raise a ValueError.
    if (guess < MINNUMBER or guess > maxNumber):
      raise ValueError
  except ValueError:
    lblFeedback.config(text=f"All guesses must be numeric and be between {MINNUMBER} and {maxNumber}. Please try again.")
    return
    
  # Guess was valid, i.e. the guess made was
  # between 1 and the maxNumber variable value.
  # Increment totalGuesses counter
  totalGuesses += 1

  # Check to see if the current guess is either:
  #
  # 1.  Too low.
  # 2.  Too high.
  # 3.  Correct.
  if (guess < numberToGuess):     # Guess was too low
    lblFeedback.config(text=f"Your guess of {guess} was too low. Please try again.")
  elif (guess > numberToGuess):   # Guess was too high
    lblFeedback.config(text=f"Your guess of {guess} was too high. Please try again.")
  else:                           # Use guessed the correct number
    lblFeedback.config(text=f"Your guess of {guess} was correct. It took you {totalGuesses} guesses.")
    btnGuess.config(state=tk.DISABLED)
    playAnotherGame()
    
def playAnotherGame():
  if (messagebox.askyesno("ANOTHER GAME???", "Play Another Game?")):
    startGameSelectionWindow()
  else:
    root.quit()

def startGameSelectionWindow():
  for widget in root.winfo_children():
    widget.pack_forget()
    
  lblSelection = tk.Label(root, text="Chose game option:")
  lblSelection.pack(pady=10)

  btnEzGame = tk.Button(root, text="1 - 10", command=lambda: setUpperLimit("1"))
  btnEzGame.pack(pady=10)

  btnMedGame = tk.Button(root, text="1 - 100", command=lambda: setUpperLimit("2"))
  btnMedGame.pack(pady=10)

  btnHardGame = tk.Button(root, text="1 - 1000", command=lambda: setUpperLimit("3"))
  btnHardGame.pack(pady=10)

# Main app winow
root = tk.Tk()
root.title("Guessing Game GUI")
root.geometry("500x500")

# Guessing Game widgets
lblFeedback = tk.Label(root, text="")

efGuess = tk.Entry(root)

btnGuess = tk.Button(root, text="Submit Guess", command=checkCurrentGuess)
btnGuess.pack(pady=10)

# Start game selection window
startGameSelectionWindow()

root.mainloop()