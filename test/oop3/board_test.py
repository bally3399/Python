from oop3.board import Board
from unittest import TestCase

from oop3.board import Cell


class TestBoardFunction(TestCase):
    def setUp(self):
        self.board = Board()

    def test_valid_move(self):
        self.assertTrue(self.board.valid_move(0, 0))

    def test_check_winner(self):
        self.board.move(1, Cell.O)
        self.board.move(5, Cell.O)
        self.board.move(9, Cell.O)
        self.assertTrue(self.board.check_winner(Cell.O))

    def test_check_if_game_is_over_GameIsNotOver(self):
        self.assertFalse(self.board.game_is_over())

    def test_that_game_is_over(self):
        self.assertFalse(self.board.game_is_over())

        self.board.move(1, Cell.O)
        self.board.move(2, Cell.X)
        self.board.move(3, Cell.O)
        self.board.move(4, Cell.O)
        self.board.move(5, Cell.X)
        self.board.move(6, Cell.O)
        self.board.move(7, Cell.X)
        self.board.move(8, Cell.O)
        self.board.move(9, Cell.X)
        self.assertTrue(self.board.game_is_over())

    def test_check_if_board_is_full(self):
        self.assertFalse(self.board.game_is_over())

        self.board.move(1, Cell.O)
        self.board.move(2, Cell.X)
        self.board.move(3, Cell.O)
        self.board.move(4, Cell.O)
        self.board.move(5, Cell.X)
        self.board.move(6, Cell.O)
        self.board.move(7, Cell.X)
        self.board.move(8, Cell.O)
        self.board.move(9, Cell.X)
        self.assertTrue(self.board.is_full())

    def test_that_board_can_be_reset(self):
        self.assertFalse(self.board.game_is_over())

        self.board.move(1, Cell.O)
        self.board.move(2, Cell.X)
        self.board.move(3, Cell.O)
        self.board.move(4, Cell.O)
        self.board.move(5, Cell.X)
        self.board.move(6, Cell.O)
        self.board.move(7, Cell.X)
        self.board.move(8, Cell.O)
        self.board.move(9, Cell.X)
        self.assertTrue(self.board.game_is_over())

        self.board.reset_board()
        self.assertFalse(self.board.is_full())

    def test_if_game_is_draw(self):
        self.board.move(1, Cell.O)
        self.board.move(2, Cell.X)
        self.board.move(3, Cell.O)
        self.board.move(4, Cell.O)
        self.board.move(5, Cell.X)
        self.board.move(6, Cell.O)
        self.board.move(7, Cell.X)
        self.board.move(8, Cell.O)
        self.board.move(9, Cell.X)

        self.assertTrue(self.board.check_draw())

