from enum import Enum


class Cell(Enum):
    EMPTY = ' '
    X = 'X'
    O = 'O'

    def __str__(self):
        return str(self.value)


class Board:
    size = 3

    def __init__(self):
        self.cells = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.initialize_board()

    def initialize_board(self):
        for index in range(self.size):
            for idx in range(self.size):
                self.cells[index][idx] = Cell.EMPTY

    def move(self, position, player):
        row = (position - 1) // self.size
        column = (position - 1) % self.size
        if row < 0 or row >= self.size or column < 0 or column >= self.size or self.cells[row][column] != Cell.EMPTY:
            return False
        self.cells[row][column] = player
        return True

    def valid_move(self, row, column):
        return 0 <= row < self.size and 0 <= column < self.size

    def check_winner(self, player):
        for index in range(self.size):
            if self.cells[index][0] == player and self.cells[index][1] == player and self.cells[index][2] == player:
                return True
            if self.cells[0][index] == player and self.cells[1][index] == player and self.cells[2][index] == player:
                return True
        if self.cells[0][0] == player and self.cells[1][1] == player and self.cells[2][2] == player:
            return True
        if self.cells[0][2] == player and self.cells[1][1] == player and self.cells[2][0] == player:
            return True
        return False

    def game_is_over(self):
        return self.check_winner(Cell.X) or self.check_winner(Cell.O) or self.is_full()

    def is_full(self):
        for index in range(self.size):
            for count in range(self.size):
                if self.cells[index][count] == Cell.EMPTY:
                    return False
        return True

    def display_board(self):
        print("Current Board: ")
        for index in range(3):
            for idx in range(3):
                if self.cells[index][idx] == Cell.EMPTY:
                    print("-", end=" ")
                else:
                    print(self.cells[index][idx], end=" ")
            print()

    def reset_board(self):
        for index in range(self.size):
            for idx in range(self.size):
                self.cells[index][idx] = Cell.EMPTY

    def check_draw(self):
        if not self.is_full():
            return False
        return not self.check_winner(Cell.X) and not self.check_winner(Cell.O)
