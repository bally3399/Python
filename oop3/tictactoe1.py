from oop3.board import Board
from oop3.player import Player
from oop3.board import Cell


class TicTacToe1:
    def __init__(self):
        self.player = Player("player", Cell.EMPTY)
        self.board = Board()
        self.tic_tac_toe = TicTacToe()

    def main(self):
        print("Welcome to My Tic_Tac_Toe Game")
        player1 = Player("first_player", Cell.X)
        player2 = Player("second_player", Cell.O)
        self.board = Board()

        while True:
            if self.tic_tac_toe.validate(self, self.board, player1): break
            if self.tic_tac_toe.validate(self, self.board, player2): break

    def validate(self, board, player):
        self.display_board(board)
        self.get_move(self, board, player)
        if self.check_win(board, player):
            print(player.get_name() + " wins!")
            return True
        if board.is_full():
            print("Board is full")
            return True
        if self.check_draw(board):
            print("It's a draw!")
            return True
        return False

    def display_board(self, board):
         print("Current Board: ")
         self.board.display_board(board)

    def check_draw(self, board):
        return board.is_full() and not board.check_winner(Cell.X) and not board.check_winner(Cell.O)

    def check_win(self, board, player):
        return board.check_winner(player.get_cell())

    def display_board(self, board):
        print("current Board: ")
        board.display_board(board)

    def get_move(self, board, player):
        print(player.get_name() + "'s turn:")
        print("Enter a number from 1 to 9 to place your symbol: ")
        position = int(input())

        if position < 1 or position > 9:
            raise ValueError("Invalid position. Please enter a number from 1 to 9.")

        row = (position - 1) // 3
        column = (position - 1) % 3

        if self.board.valid_move(row, column):
            self.board.move(position, self.player.cell())
        else:
            print("Invalid move. Please choose another position.")
            self.get_move(board, player)



if __name__ == "__main__":
    main()

