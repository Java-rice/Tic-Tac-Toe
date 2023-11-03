import tkinter as tk
import customtkinter
from itertools import cycle

class TicTacToe(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Tic Tac Toe")

        self.current_player = cycle([['Player 1', 'X'], ['Player 2', 'O']])
        self.game_board = [['' for _ in range(3)] for _ in range(3)]

        self.create_board()

    def create_board(self):
        board_frame = tk.Frame(self)
        board_frame.pack()

        for row in range(3):
            self.rowconfigure(row, weight=1)
            for col in range(3):
                self.columnconfigure(col, weight=1)
                btn = tk.Button(
                    board_frame, text='', font=('Arial', 20), width=4, height=2,
                    command=lambda row1=row, col1=col: self.on_button_click(row1, col1)
                )
                btn.grid(row=row, column=col)
                self.game_board[row][col] = btn

    def on_button_click(self, row, col):
        current_player = next(self.current_player)
        if self.game_board[row][col]['text'] == '':
            self.game_board[row][col]['text'] = current_player[1]
            self.game_board[row][col]['state'] = 'disabled'  # Prevent changing the button's value
            if self.check_winner(row, col, current_player[1]):
                self.show_winner(current_player[0])
            elif all(self.game_board[i][j]['text'] != '' for i in range(3) for j in range(3)):
                self.show_winner('Draw')

    def check_winner(self, row, col, player):
        # Function to check the winner - Implement your winning logic here
        pass

    def show_winner(self, player):
        winner = f"{player} wins!" if player != 'Draw' else "It's a draw!"
        tk.messagebox.showinfo("Game Over", winner)
        self.parent.quit()


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    game.pack()
    root.mainloop()