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
    Board_Size = 3
    Default_Players = (
        Player(pick="X", color="#FF3131"),
        Player(pick="Y", color="#004AAD"),
    )

    def __init__(self, parent, controller, players=Default_Players, board=Board_Size):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        homeview.interface(self)

        # Top Title
        self.text = "Multiplayer Mode"
        self.mainmode = customtkinter.CTkLabel(
            self.mainframe, text=self.text, font=self.font2, text_color=self.black
        )
        self.mainmode.place(relx=0.5, rely=0.09, anchor="center")
        
        #Start the Game
        self.start_game()
        
        
    def start_game(self):
        #initialization
        self.player1 = 0
        self.player2 = 0
        self._cells = {}
        
        scoreboard.scoreinterface(self)  # Create ScoreBoard
        tboard.TTBoard(self)  # Create Board
        roundlabel.Round(self)  # Create RoundBoard

        self.player1 += 9
        self.
        self.player1 += 2
        self.roundnumber = 1
        roundlabel.Round(self)

    def reset_progress():
        pass
