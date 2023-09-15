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
    Board_Size = 3
    Default_Players = (Player(pick="X", color="#FF3131"), Player(pick="Y", color="#004AAD"))
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        homeview.interface(self)
        
        #interface
        self.text = "Multiplayer Mode"
        self.mainmode = customtkinter.CTkLabel(self.mainframe, text=self.text, font=self.font2, text_color=self.black)
        self.mainmode.place(relx = 0.5, rely = 0.09, anchor = "center")
        self.start_game()

        
        #Function to StartGame
            #--Initial Players 0-0
            #--Restart Board
            #--Create Board
            
            #--Start Round
                #Game Proper
                #If-anyone-wins
                    #Update scoreboard
                    #Restart Board
                    #function to next round
                #clicks-reset
                    #Reset Player Scoreboard
                    #Reset Board
                    #function to StartGame            
    
    def start_game(self):
        scoreboard.SCBoard(self) #Create ScoreBoard
        
        
        
        self._cells = {}
        tboard.TTBoard(self) #Create Board
        roundlabel.Round(self) #Create RoundBoard
        
        self.player1 += 1
        
        
        
        
        
        
        
        
    def reset_progress():
        pass
        
        
    
    