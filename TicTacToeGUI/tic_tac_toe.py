"""
    This program gleaned from the following article
    Build a Tic-Tac-Toe Game With Python and Tkinter
    at the following URL:

    https://realpython.com/tic-tac-toe-python/

    In this tutorial, you’ll learn how to:

    1.  Program the classic tic-tac-toe game using Python.

    2.  Create the game's graphical user interface (GUI) 
        using Tkinter.
      
    3.  Integrate the game's logic and GUI into a fully 
        functional computer game.

    Your tic-tac-toe game will have an interface that reproduces 
    the classic three-by-three game board. The players will take 
    turns making their moves on a shared device. The game display 
    at the top of the window will show the name of the player who 
    gets to go next.

    If a player wins, then the game display will show a winning 
    message with the player's name or mark (X or O). At the same 
    time, the winning combination of cells will be highlighted 
    on the board.

    Finally, the game's File menu will have options to reset the 
    game if you want to play again or to exit the game when you're 
    done playing.

    With these rules in mind, you'll need to put together the 
    following game components:

    1.  The game's board, which you'll build with a class called 
        TicTacToeBoard.

    2.  The game's logic, which you'll manage using a class called 
        TicTacToeGame.
"""

import tkinter as tk
from tkinter import font
from typing import NamedTuple
from itertools import cycle

class Player(NamedTuple):
    label: str
    color: str

#   Define the Move class. The .row and .col 
#   attributes will hold the coordinates that identify the 
#   move's target cell. The .label attribute will hold the 
#   sign that identifies the player, X or O. Note that .label 
#   defaults to the empty string, "", which means that this 
#   specific move hasn’t been played yet.
#   We first instantiate TicTacToeBoard and then run 
#   its main loop by calling .mainloop().
class Move(NamedTuple):
    row: int
    col: int
    label: str = ""

BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="gold"),
    Player(label="O", color="green")
)
    
#   Here we define TicTacToeGame, whose initializer takes 
#   two arguments, players and board_size. The players 
#   argument will hold a tuple of two Player objects, 
#   representing players X and O. This argument defaults 
#   to DEFAULT_PLAYERS, a constant that you'll define.
class TicTacToeGame:
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self._players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self._players)
        self.winner_combo = []
        self._current_moves = []
        self._has_winner = False
        self._winning_combos = []
        self._setup_board()
    
    #   In ._setup_board(), you use a list comprehension 
    #   to provide an initial list of values for ._current_moves. 
    #   The comprehension creates a list of lists. Each inner list 
    #   will contain empty Move objects. An empty move stores the 
    #   coordinates of its containing cell and an empty string as 
    #   the initial player's label.
    #
    #   The last line of this method calls ._get_winning_combos() 
    #   and assigns its return value to ._winning_combos.
    def _setup_board(self):
        self._current_moves = [
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]
        self._winning_combos = self._get_winning_combos()

    #   On a classic tic-tac-toe board, you'll have eight 
    #   possible winning combinations. They’re essentially the 
    #   rows, columns, and diagonals of the board.
    #
    #   We use four list comprehensions to get all the possible 
    #   winning combinations 
    def _get_winning_combos(self):
        rows = [
            [(move.row, move.col) for move in row]
            for row in self._current_moves
        ]
        columns = [list(col) for col in zip(*rows)]
        first_diagonal = [row[i] for i, row in enumerate(rows)]
        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
        return rows + columns + [first_diagonal, second_diagonal]
    
    #   Every player's move will trigger a bunch of operations on
    #   the TicTacToeGame class. These operations include:
    #
    #   Validating the move
    def is_valid_move(self, move):
        """Return True if move is valid, and False otherwise."""
        row, col = move.row, move.col
        move_was_not_played = self._current_moves[row][col].label == ""
        no_winner = not self._has_winner
        return no_winner and move_was_not_played
    
    #   Checking for a winner
    def process_move(self, move):
        """Process the current move and check if it's a win."""
        row, col = move.row, move.col
        self._current_moves[row][col] = move
        for combo in self._winning_combos:
            results = set(
                self._current_moves[n][m].label
                for n, m in combo
            )
            is_win = (len(results) == 1) and ("" not in results)
            if is_win:
                self._has_winner = True
                self.winner_combo = combo
                break

    def has_winner(self):
        """Return True if the game has a winner, and False otherwise."""
        return self._has_winner
    
    #   Checking for a tied game
    def is_tied(self):
        """Return True if the game is tied, and False otherwise."""
        no_winner = not self._has_winner
        played_moves = (
            move.label for row in self._current_moves for move in row
        )
        return no_winner and all(played_moves)
    
    #   Toggling the player for the next move
    def toggle_player(self):
        """Return a toggled player."""
        self.current_player = next(self._players)
    
    #   The code that asks the players if they wish to
    #   play another game of TicTacToe or not.
    def reset_game(self):
        """Reset the game state to play again."""
        for row, row_content in enumerate(self._current_moves):
            for col, _ in enumerate(row_content):
                row_content[col] = Move(row, col)
        self._has_winner = False
        self.winner_combo = []

#   The TicTacToeBoard class inherits from Tk, which 
#   makes it a full-fledged GUI window. This window 
#   will represent the game board. Inside .__init__(), 
#   you first call the superclass's .__init__() method 
#   to properly initialize the parent class. To do this, 
#   you use the built-in super() function.
#
#   The .title attribute of Tk defines the text to show 
#   on the window'’'s title bar. In this example, you 
#   set the title to "Tic-Tac-Toe Game".
#
#   The ._cells non-public attribute holds an initially
#   empty dictionary. This dictionary will map the buttons
#   or cells on the game board to their corresponding 
#   coordinates—row and column—on the grid. These 
#   coordinates will be integer numbers reflecting the 
#   row and column where a given button will appear.
class TicTacToeBoard(tk.Tk):
    #   The "constructor" called when a TicTacToeBoard
    #   object is created (a.k.a. instantiated).
    def __init__(self, game):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self._cells = {}
        self._game = game
        self._create_menu()
        self._create_board_display()
        self._create_board_grid()

    #   To continue with the game board, you need 
    #   to create a display where you can provide info
    #   about the game's state and result. For this 
    #   display, you'll use a Frame widget as the 
    #   display panel and a Label widget to show the 
    # required information.
    def _create_board_display(self):
        #   Create a Frame object to hold the 
        #   game display. Note that the master argument 
        #   is set to self, which means that the game's 
        #   main window will be the frame's parent.
        display_frame = tk.Frame(master=self)

        #   Use the .pack() geometry manager 
        #   to place the frame object on the main window's
        #   top border. By setting the fill argument to tk.X, 
        #   you ensure that when the user resizes the window, 
        #   the frame will fill its entire width.
        display_frame.pack(fill=tk.X)

        #   Create a Label object. 
        #   This label needs to live inside the frame 
        #   object, so you set its master argument to 
        #   the actual frame. The label will initially 
        #   show the text "Ready?", which indicates that 
        #   the game is ready to go, and the players can 
        #   start a new match. Finally, you change the 
        #   label's font size to 28 pixels and make it bold.
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
        )

        #   Pack the display label inside the 
        #   frame using the .pack() geometry manager.
        self.display.pack()
    
    #   Create the actual TicTacToe board as a 3x3 grid
    #   of cells.
    def _create_board_grid(self):
        #   Create a Frame object to hold the game's
        #   grid of cells. You set the master argument to self, 
        #   which again means that the game's main window will 
        # be the parent of this frame object.
        grid_frame = tk.Frame(master=self)

        #   Use the .pack() geometry manager to place
        #   the frame object on the main window. This frame 
        #   will occupy the area under the game display, all 
        #   the way to the bottom of the window.
        grid_frame.pack()

        #   Start a loop that iterates from 0 to 2.
        #   These numbers represent the row coordinates of 
        #   each cell in the grid. For now, you'll have 3
        #   rows on the grid. However, you can change this 
        #   magic number later and provide the option of 
        #   using a different grid size, such as four by four.
        for row in range(self._game.board_size):
            #   Configure the width and minimum
            #   size of every cell on the grid.
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)

            #   Loop over the three column coordinates. 
            #   Again you use three columns, but you can change
            #   the number later to provide more flexibility and
            #   get rid of magic numbers.
            for col in range(self._game.board_size):
                #   Ccreate a Button object for 
                #   every cell on the grid. Note that you set 
                #   several attributes.
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                )
                #   Add every new button to the ._cells
                #   dictionary. The buttons work as keys, and their 
                #   coordinates—expressed as (row, col)—work as values.
                self._cells[button] = (row, col)

                #   The highlighted line binds the click event of 
                #   every button on the game board with the .play() 
                #   method. This way, whenever a player clicks a given 
                #   button, the method will run to process the move and 
                #   update the game state.
                button.bind("<ButtonPress-1>", self.play)

                #   Add every button to the main
                #   window using the .grid() geometry manager.
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )
    
    #   This method is fundamental in your tic-tac-toe game 
    #   because it puts together almost all the game logic 
    #   and GUI behavior.
    def play(self, event):
        """Handle a player's move."""
        clicked_btn = event.widget
        row, col = self._cells[clicked_btn]
        move = Move(row, col, self._game.current_player.label)
        if self._game.is_valid_move(move):
            self._update_button(clicked_btn)
            self._game.process_move(move)
            if self._game.is_tied():
                self._update_display(msg="Tied game!", color="red")
            elif self._game.has_winner():
                self._highlight_cells()
                msg = f'Player "{self._game.current_player.label}" won!'
                color = self._game.current_player.color
                self._update_display(msg, color)
            else:
                self._game.toggle_player()
                msg = f"{self._game.current_player.label}'s turn"
                self._update_display(msg)

    #   To complete the code for processing the players' 
    #   moves on the game board, you need to write three helper 
    #   methods. These methods will complete the following actions:
    #
    #   Update the clicked button
    def _update_button(self, clicked_btn):
        clicked_btn.config(text=self._game.current_player.label)
        clicked_btn.config(fg=self._game.current_player.color)

    #   Update the game display
    def _update_display(self, msg, color="black"):
        self.display["text"] = msg
        self.display["fg"] = color

    #   Highlight the winning cells
    def _highlight_cells(self):
        for button, coordinates in self._cells.items():
            if coordinates in self._game.winner_combo:
                button.config(highlightbackground="red")

    #   To add a main menu to a Tkinter application, you 
    #   can use the tkinter.Menu class. This class allows you 
    #   to create a menu bar on top of your Tkinter window.
    #   It also allows you to add dropdown menus to the menu bar.
    #
    #   Shown below is the code that creates and adds a main menu
    #   to your tic-tac-toe game:
    def _create_menu(self):
        menu_bar = tk.Menu(master=self)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(master=menu_bar)
        file_menu.add_command(
            label="Play Again",
            command=self.reset_board
        )
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    #   .reset_game() will reset the board's abstract representation.
    #
    #   Update the board display to hold the initial text, "Ready?".
    #
    #   Start a loop over the buttons on the board grid.
    #
    #   Restore every button's highlightbackground, text, and 
    #   fg properties to their initial state.
    def reset_board(self):
        """Reset the game's board to play again."""
        self._game.reset_game()
        self._update_display(msg="Ready?")
        for button in self._cells.keys():
            button.config(highlightbackground="lightblue")
            button.config(text="")
            button.config(fg="black")

#   Now we need to think of how to deal with the game's 
#   logic. This logic will consist of code that processes a 
#   player's move and determines if this player has won the 
#   game or not.

#   Define the Player class. The .label attribute 
#   will store the classic player signs, X and O. The .color 
#   attribute will hold a string with a Tkinter color. You'll 
#   use this color to identify the target player on the game board.
class Player(NamedTuple):
    label: str
    color: str

def main():
    """Create the game's board and run its main loop."""
    game = TicTacToeGame()
    board = TicTacToeBoard(game)
    board.mainloop()

#   The if __name__ == "__main__": construct is a common 
#   pattern in Python applications. It allows you to control 
#   the execution of your code. In this case, the call to 
#   main() will only happen if you run the .py file as an 
#   executable program, as opposed to an importable module.
if __name__ == "__main__":
    main()

