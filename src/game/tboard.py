import customtkinter
import tkinter as tk
from views import multiplayer


def TTBoard(self):
    boardframe = customtkinter.CTkFrame(master=self, fg_color=self.bg)
    boardframe.place(relx=0.5, rely=0.5, anchor="center")
    for row in range(self.start_round.board_size):
        self.rowconfigure(row, weight=1, minsize=50)
        self.columnconfigure(row, weight=1, minsize=75)
        for col in range(self.start_round.board_size):
            button = customtkinter.CTkButton(
                master=boardframe,
                text="",
                font=self.font1,
                fg_color=self.black,
                width=100,
                height=100,
                bg_color=self.black,
            )
            self._cells[button] = (row, col)
            button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
