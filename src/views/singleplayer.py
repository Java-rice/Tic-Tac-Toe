import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
from game import tboard, scoreboard, roundlabel
from views import welcome, homeview


class main_game(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        # interface
        self.text = "Single Player Mode"
        homeview.interface(self)
        self.mainmode = customtkinter.CTkLabel(
            self.mainframe, text=self.text, font=self.font2, text_color=self.black
        )
        self.mainmode.place(relx=0.5, rely=0.09, anchor="center")


    def reset_progress():
        pass
