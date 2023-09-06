import customtkinter
import tkinter as tk 

def SCBoard(self):
    self.scoreboard = customtkinter.CTkFrame(master=self, width=400, height=75, border_width=2, border_color=self.black, fg_color=self.bg, bg_color=self.bg)
    self.scoreboard.place(relx=0.5, rely=0.8, anchor="center")
    