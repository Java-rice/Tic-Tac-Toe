def current_board(self):
    self.current_move = [
        [move(row, col) for col in range(self.board_size)]
        for row in range(self.board_size)
    ]
    self.combo_move = self.winning_combo()


def get_winning_combo(self):
    pass
