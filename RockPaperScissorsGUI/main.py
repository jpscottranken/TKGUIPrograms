"""
    Rock paper scissors is hand game, usually played between two people.
    Each player forms one of three shapes with an outstretched hand. 
    These shapes are "rock" (a closed fist), "paper" (a flat hand), and 
    "scissors" (a fist with the index finger and middle finger, 
    extended, forming a V).

  The game has three possible outcomes for player  and Computer:

  1.	A draw, where Player and Computer both choose Rock or both 
      choosePaper or both choose Scissors.

  2.	A win for Player where either:

    a.	Player chooses Rock and Computer chooses Scissors,
        as "Rock breaks Scissors".
    b.	Player chooses Paper and Computer chooses Rock,
        as "Paper covers Rock".
    c.	Player chooses Scissors and Computer 2 chooses Paper,
        as "Scissors cuts Paper".

  3.	A loss for Player where either:

    a.	Computer chooses Rock and Player chooses Scissors,
        as "Rock breaks Scissors".
    b.	Computer chooses Paper and Player chooses Rock,
        as "Paper covers Rock".
    c.	Computer chooses Scissors and Player chooses Paper,
        as "Scissors cuts Paper".

  Create a Python GUI Rock Paper Scissors game. Include:

  1.  What option each Player and Computer choose (Rock, Paper, or Scissors)
  
  2.  The result of the current game (Player/Computer wins, loses, or ties)

  3.  Total number of wins and losses for Player/Computer. And total ties.
"""

import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

# Constants
ROCK      = 1
PAPER     = 2
SCISSORS  = 3
BCR       = "Both Chose Rock" 
BCP       = "Both Chose Paper"
BCS       = "Both Chose Scissors"
PCR       = "Paper Covers Rock"
RBS       = "Rock Breaks Scissors"
SCP       = "Scissors Cuts Paper"
TG        = "TIE GAME"
CW        = "COMPUTER WINS"
PW        = "PLAYER WINS"

# Create a Python dictionary that will hold the result messages.
# First entry will be Computer. Second entry will be the Player.
RESULTMESSAGES = {
  (ROCK, ROCK):         (BCR, TG),
  (ROCK, PAPER):        (PCR, PW),
  (ROCK, SCISSORS):     (RBS, CW),
  (PAPER, ROCK):        (PCR, CW),
  (PAPER, PAPER):       (BCP, TG),
  (PAPER, SCISSORS):    (SCP, PW),
  (SCISSORS, ROCK):     (RBS, PW),
  (SCISSORS, PAPER):    (SCP, CW),
  (SCISSORS, SCISSORS): (BCS, TG)
}

class RockPaperScissorsApp:
  def __init__(self, root):
    self.root = root
    self.root.title("Rock/Paper/Scissors Game")
    self.root.eval('tk::PlaceWindow . center')
    self.root.geometry("600x400")
    self.fontSettings = ("Arial", 16, "bold")

    # Scores
    self.computerWins = 0
    self.playerWins   = 0
    self.tieGames     = 0

    # Load images
    self.imgRock      = tk.PhotoImage(file="rock.png")
    self.imgPaper     = tk.PhotoImage(file="paper.png")
    self.imgScissors  = tk.PhotoImage(file="scissors.png") 
 
     # Call function to set up the GUI
    self.createGUI()

  def createGUI(self):
    # Row 0 - Title
    lblTitle = tk.Label(self.root, text="Rock, Paper, Scissors", font=self.fontSettings)
    lblTitle.grid(row=0, column=2, padx=20, pady=20)

    # Row 1 - Rock/Paper/Scissors Buttons
    btnRock = tk.Button(self.root, image=self.imgRock, font=self.fontSettings, command=lambda: self.playGame(ROCK), width=75)
    btnRock.grid(row= 1, column=0, padx=10, pady=10)

    btnPaper = tk.Button(self.root, image=self.imgPaper, font=self.fontSettings, command=lambda: self.playGame(PAPER), width=75)
    btnPaper.grid(row= 1, column=2, padx=10, pady=10)

    btnScissors = tk.Button(self.root, image=self.imgScissors, font=self.fontSettings, command=lambda: self.playGame(SCISSORS), width=75)
    btnScissors.grid(row= 1, column=4, padx=10, pady=10)

    # Score Info
    tk.Label(self.root, text="Computer Wins", font=self.fontSettings).grid(row=2, column=0, pady=(20, 10), sticky="e")
    self.lblComputerWins = tk.Label(self.root, text="0", font=self.fontSettings)
    self.lblComputerWins.grid(row=2, column=2, pady=(20, 10), sticky="w")

    tk.Label(self.root, text="Player Wins", font=self.fontSettings).grid(row=3, column=0, pady=(5, 10), sticky="e")
    self.lblPlayerWins = tk.Label(self.root, text="0", font=self.fontSettings)
    self.lblPlayerWins.grid(row=3, column=2, pady=(5, 10), sticky="w")

    tk.Label(self.root, text="Tie Games", font=self.fontSettings).grid(row=4, column=0, pady=(5, 10), sticky="e")
    self.lblTieGames = tk.Label(self.root, text="0", font=self.fontSettings)
    self.lblTieGames.grid(row=4, column=2, pady=(5, 10), sticky="w")

  def playGame(self, playerChoice):
    computerChoice = random.randint(1, 3)
    resultMsg, resultTitle = RESULTMESSAGES[(computerChoice, playerChoice)]

    if(resultTitle == "COMPUTER WINS"):
      self.computerWins += 1
    elif(resultTitle == "PLAYER WINS"):
      self.playerWins += 1
    else:
      self.tieGames += 1
    
    # Update scores in the GUI
    self.updateScores()

    # Show results of the current game
    messagebox.showinfo(resultTitle, resultMsg)

  def updateScores(self):
    self.lblComputerWins.config(text=str(self.computerWins))
    self.lblPlayerWins.config(text=str(self.playerWins))
    self.lblTieGames.config(text=str(self.tieGames))

# Create main window and start the game
root = tk.Tk()
app  = RockPaperScissorsApp(root)
root.mainloop()