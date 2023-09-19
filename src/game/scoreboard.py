import customtkinter
import tkinter as tk


def scoreinterface(self):
    self.label1 = "Player 1: "
    self.label2 = "Player 2: "
    
    # scoreboard frame and label
    self.scoreboard = customtkinter.CTkFrame(
        master=self,
        width=500,
        height=75,
        border_width=2,
        border_color=self.black,
        fg_color=self.bg,
        bg_color=self.bg,
    )
    self.scoreboard.place(relx=0.5, rely=0.8, anchor="center")
    self.scorelabel = customtkinter.CTkLabel(
        self.scoreboard,
        text="Score",
        font=self.font2,
        text_color=self.black,
        bg_color=self.bg,
        fg_color=self.bg,
    )
    self.scorelabel.place(relx=0.5, rely=0.25, anchor="center")

    # player1core
    self.player1frame = customtkinter.CTkFrame(
        self.scoreboard,
        width=180,
        corner_radius=0,
        border_width=0,
        border_color=self.bg,
        fg_color=self.bg,
        bg_color=self.bg,
    )
    self.player1frame.place(relx=0.25, rely=0.65, anchor="center")
    self.player1label = customtkinter.CTkLabel(
        self.player1frame,
        text=self.label1,
        font=self.font2,
        text_color=self.red,
        bg_color=self.bg,
        fg_color=self.bg,
    )
    self.player1label.pack(side="left", padx=2)
    self.scorebox1 = customtkinter.CTkFrame(
        self.player1frame,
        width=100,
        height=30,
        border_width=2,
        border_color=self.red,
        fg_color=self.bg,
        bg_color=self.bg,
    )
    self.scorebox1.pack(side="left", padx=3)
    self.currentscore1 = customtkinter.CTkLabel(
        self.scorebox1,
        width=75,
        height=25,
        text=self.player1,
        font=self.font6,
        text_color=self.red,
        bg_color=self.bg,
        fg_color=self.bg,
    )
    self.currentscore1.place(relx=0.5, rely=0.5, anchor="center")

    # player2core
    self.player2frame = customtkinter.CTkFrame(
        self.scoreboard,
        width=180,
        corner_radius=0,
        border_width=0,
        border_color=self.bg,
        fg_color=self.bg,
        bg_color=self.bg,
    )
    self.player2frame.place(relx=0.75, rely=0.65, anchor="center")
    self.player2label = customtkinter.CTkLabel(
        self.player2frame,
        text=self.label2,
        font=self.font2,
        text_color=self.blue,
        bg_color=self.bg,
        fg_color=self.bg,
    )
    self.player2label.pack(side="left", padx=2)
    self.scorebox2 = customtkinter.CTkFrame(
        self.player2frame,
        width=100,
        height=30,
        border_width=2,
        border_color=self.blue,
        fg_color=self.bg,
        bg_color=self.bg,
    )
    self.scorebox2.pack(side="left", padx=3)
    self.currentscore2 = customtkinter.CTkLabel(
        self.scorebox2,
        width=75,
        height=25,
        text=self.player2,
        font=self.font6,
        text_color=self.blue,
        bg_color=self.bg,
        fg_color=self.bg,
    )
    self.currentscore2.place(relx=0.5, rely=0.5, anchor="center")
