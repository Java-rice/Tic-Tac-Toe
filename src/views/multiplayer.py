import tkinter as tk
import customtkinter
from game import tboard, scoreboard, roundlabel
from views import welcome, homeview
from typing import NamedTuple
from itertools import cycle
from PIL import Image, ImageTk

#main_game class
class main_game(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller 

        # Label Inteface
        homeview.interface(self)

        # Top Title
        self.text = "Multiplayer Mode"
        self.mainmode = customtkinter.CTkLabel(self.mainframe, text=self.text, font=self.font2, text_color=self.black)
        self.mainmode.place(relx=0.5, rely=0.09, anchor="center")

        # Game variables
        self.current_player = cycle([
            ['Player 1', "./src/Assets/X.png"],
            ['Player 2', "./src/Assets/O.png"]
        ])
        
        # Triggers start game
        self.start_game()
        
    def reset_game(self):
        self.game_board = [[None for _ in range(3)] for _ in range(3)]
        self.buttons_clicked = [[False for _ in range(3)] for _ in range(3)] # Track buttons clicked
        
    def start_game(self):
        self.reset_game()
        self.create_board()
        roundlabel.Round(self)  
    
    def create_board(self):
        boardframe = customtkinter.CTkFrame(master=self, fg_color=self.bg)
        boardframe.place(relx=0.5, rely=0.5, anchor="center")

        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)

            for col in range(3):
                button = customtkinter.CTkButton(
                    master=boardframe,
                    text="",
                    font=self.font1,
                    fg_color=self.black,
                    image="",
                    width=100,
                    height=100,
                    bg_color=self.black,
                    command=lambda row1=row, col1=col: self.on_button_click(row1, col1)
                )
                self.game_board[row][col] = button  # Store the button in the game board
                button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
                print(f"Button at ({row}, {col}): {button}")

    def on_button_click(self, row, col):
        button = self.game_board[row][col]
        if not self.buttons_clicked[row][col]:  # Check if the button has been clicked
            current_player = next(self.current_player)
            image_path = Image.open(current_player[1])
            ctk_image = customtkinter.CTkImage(light_image=image_path, dark_image=image_path, size=(50, 50))
            button.configure(image=ctk_image)
            button.image = ctk_image
            self.game_board[row][col] = current_player[0]
            self.buttons_clicked[row][col] = True  # Set the button as clicked
            if self.check_winner(row, col, current_player[0]):
                self.show_winner(current_player[0]) 
            elif all(all(cell is not None for cell in row) for row in self.game_board):
                self.show_winner('Draw')  # If all cells are filled, and no winner, declare draw
                
    #CHECK IF ELEMENTS ARE SAME ON EVERY INDEX
    def check_winner(self, row, col, player):
        # Example of winning conditions for a 3x3 tic-tac-toe game
        return (
            self.game_board[row][0] == self.game_board[row][1] == self.game_board[row][2] == player or
            self.game_board[0][col] == self.game_board[1][col] == self.game_board[2][col] == player or
            self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] == player or
            self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] == player
        )


    def show_winner(self, player):
        winner = f"{player} wins!" if player != 'Draw' else "It's a draw!"
        # Show winner or draw message - Implement as needed
        pass
    
    def reset_progress(self):
        for row in range(3):
            for col in range(3):
                button = self.game_board[row][col]
                button.configure(image="")  # Remove image from the button
                button.image = None 
                self.buttons_clicked[row][col] = False
                self.game_board[row][col] = None
