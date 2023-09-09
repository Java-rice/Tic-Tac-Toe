import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
from game import tboard, scoreboard, roundlabel, mainlogic
from views import welcome, homeview
from typing import NamedTuple


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
        
        self.controller = controller
        homeview.interface(self)
        
        #interface
        self.text = "Multiplayer Mode"
        self.board_size = 3
        self.default_players = (Player(pick="X", color=self.red), Player(pick="Y", color=self.blue))
        self.mainmode = customtkinter.CTkLabel(self.mainframe, text=self.text, font=self.font2, text_color=self.black)
        self.mainmode.place(relx = 0.5, rely = 0.09, anchor = "center")
        
        #logic
        self._cells = {}
        tboard.TTBoard(self)
        scoreboard.SCBoard(self)
        roundlabel.Round(self)
    
    def reset_progress():
        pass
        
        
    
    