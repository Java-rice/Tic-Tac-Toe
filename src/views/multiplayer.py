import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
from game import tboard, scoreboard, roundlabel, mainlogic
from views import welcome, homeview
from typing import NamedTuple
from itertools import cycle

class Player(NamedTuple):
    pick: str
    color: str

class Move(NamedTuple):
    row: int
    col: int
    label: str = ""

class main_game(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        homeview.interface(self)

        # Top Title
        self.text = "Multiplayer Mode"
        self.mainmode = customtkinter.CTkLabel(self.mainframe, text=self.text, font=self.font2, text_color=self.black)
        self.mainmode.place(relx=0.5, rely=0.09, anchor="center")
        
        #Start the Game
        self.start_game()
        
    def start_game(self):
        #initialization
        self.playerX = 0
        self.playerY = 0
        Board_Size = 3
        Default_Players = (
            Player(pick="X", color="#FF3131"),
            Player(pick="Y", color="#004AAD"),
        )
        self.start_round(Board_Size,Default_Players)

    def start_round(self,board_size,players):
        self._cells = {}
        self.players = cycle(players)
        self.board_size = board_size
        self.turn_player = next(self.players)
        self.winner_combo = []
        self.current_moves = []
        self._haswinner = False
        self.winning_combo = []
        
        scoreboard.scoreinterface(self)  # Create ScoreBoard
        tboard.TTBoard(self.board_size)  # Create Board
        roundlabel.Round(self)  # Create RoundBoard
    
    def _get_winning_combos(self):
        rows = [
            [(move.row, move.col) for move in row]
            for row in self._current_moves
        ]
        columns = [list(col) for col in zip(*rows)]
        first_diagonal = [row[i] for i, row in enumerate(rows)]
        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
        return rows + columns + [first_diagonal, second_diagonal]
    
    def setup_board(self):
        self.current_moves = [
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]
        self._winning_combos = self._get_winning_combos()
    
    
    def reset_progress():
        pass
