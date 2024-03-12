from oop3.board import Board
from oop3.player import Player
from oop3.board import Cell


class TicTacToe:
    def __init__(self):
        print("Welcome to My Tic-Tac-Toe game")
        self.first_player = Player("Player 1", Cell.X)
        self.second_player = Player("Player 2", Cell.O)
        self.board = Board()

    def play(self):
        while True:
            self.board.display_board()
            self.get_move(self.first_player)
            if self.check_win(self.first_player):
                print(self.first_player.name + " wins!")
                break
            if self.check_draw():
                print("It's a draw!")
                break

            self.board.display_board()
            self.get_move(self.second_player)
            if self.check_win(self.second_player):
                print(self.second_player.name + " wins!")
                break
            if self.check_draw():
                print("It's a draw!")
                break

    def check_draw(self):
        return self.board.is_full() and not self.check_win(self.first_player) and not self.check_win(self.second_player)

    def check_win(self, player):
        return self.board.check_winner(player.cell)

    def get_move(self, player):
        print(player.name + "'s turn:")
        position = int(input("Enter a number from 1 to 9 to place your symbol: "))

        if position < 1 or position > 9:
            raise ValueError("Invalid position. Please enter a number from 1 to 9.")

        row = (position - 1) // 3
        col = (position - 1) % 3

        if self.board.valid_move(row, col):
            self.board.move(position, player.cell)
        else:
            print("Invalid move")
            self.get_move(player)

    def display_board(self):
        print("Current Board: ")
        self.board.display_board()


def main():
    tictactoe = TicTacToe()
    tictactoe.play()


if __name__ == "__main__":
    main()
