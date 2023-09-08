import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
from game import tboard, scoreboard, roundlabel
from views import welcome, homeview

class main_game(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller

        #color_varibles
        self.blue = "#004AAD"
        self.red = "#FF3131"
        self.black = "#1E1E1E"
        self.bg = "#FFF9E1"
        
        #font_styles
        self.font1 = ('Inter', 14)
        self.font2 = ('Inter', 24, 'bold')
        self.font3 = ('Inter', 20, 'bold')
        self.font4 = ('Inter', 14, 'bold')
        self.font5 = ('Inter', 32, 'bold')
        self.font6 = ('Inter', 18)
        
        #interface
        self.text = "Multiplayer"
        homeview.interface(self)
        self.mainmode = customtkinter.CTkLabel(self.mainframe, text=self.text, font=self.font2, text_color=self.black)
        self.mainmode.place(relx = 0.5, rely = 0.09, anchor = "center")
        
        #logic
        self._cells = {}
        tboard.TTBoard(self)
        scoreboard.SCBoard(self)
        roundlabel.Round(self)
    
    def reset_progress():
        pass