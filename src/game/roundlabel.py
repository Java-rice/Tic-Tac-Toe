import customtkinter
import tkinter as tk 

def Round(self):
    self.roundnumber = ""
    self.roundturn = ""
    
    self.roundlabel = customtkinter.CTkLabel(self,text="Round" + self.roundnumber, font=self.font2, text_color=self.black,bg_color=self.bg, fg_color=self.bg)
    self.turnlabel = customtkinter.CTkLabel(self,text=self.roundturn + "Turn", font=self.font2, text_color=self.black,bg_color=self.bg, fg_color=self.bg)
    self.roundlabel.place(relx = 0.5, rely = 0.19, anchor = "center")
    self.turnlabel.place(relx = 0.5, rely = 0.24, anchor = "center")
