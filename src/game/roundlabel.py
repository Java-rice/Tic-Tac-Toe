import customtkinter
import tkinter as tk


def Round(self):
    self.roundnumber = 1
    self.roundturn = ""

    self.roundlabel = customtkinter.CTkLabel(
        self,
        text="Round " + str(self.roundnumber),
        font=self.font2,
        text_color=self.black,
        bg_color=self.bg,
        fg_color=self.bg,
    )
    self.turnlabel = customtkinter.CTkLabel(
        self,
        text=self.roundturn + "Turn",
        font=self.font2,
        text_color=self.black,
        bg_color=self.bg,
        fg_color=self.bg,
    )
    self.roundlabel.place(relx=0.5, rely=0.20, anchor="center")
    self.turnlabel.place(relx=0.5, rely=0.24, anchor="center")
