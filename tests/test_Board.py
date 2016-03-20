"""
Created on Feb 20, 2012
"""

import unittest
from Board import Board
from ship import Ship


class BoardTest(unittest.TestCase):

    def setUp(self):
        """setUP of the board"""

        self.b = Board(5)
        self.ship1 = Ship(3, self.b)
        self.ship1.position.append((0, 2))
        self.ship1.position.append((1, 2))
        self.b.user_pieces.append(self.ship1)
        self.b.board[0][0][0] = 0
        self.b.board[0][1][0] = 1
        self.b.board[1][2][0] = 1
        self.b.board[0][2][0] = 1
        self.b.board[0][3][0] = 3

    def tearDown(self):
        """Clean up."""

        self.b = None
        self.ship1 = None
        self.user_pieces = []

    def boardSize(self):
        """Tests if the Board is the correct size."""

        row = 0
        area = 0
        for x in self.board.b:
            row += 1
            for y in self.board.b:
                area += 1
        self.assertEqual(row, 5, 'Not correct Row')
        self.assertEqual(area, 25, 'Not correct Col/Area')

    def testShip(self):
        """Tests if ship is added"""

        self.b.user_pieces.append(Ship(3, self.b))
        self.assertEqual(len(self.b.user_pieces), 2,\
                          "Adds ships properly to user_pieces")

    def testMove(self):
        """Tests if correct moves are made."""

        self.b.move((0, 0))
        self.assertEqual(self.b.board[0][0][0], 3, 'Water to Miss')
        self.b.move((0, 1))
        self.assertEqual(self.b.board[0][1][0], 2, 'Water to Hit')
        self.b.move((0, 2))
        self.assertEqual(self.b.board[0][2][0], 2, 'No Change to already hit')
        self.b.move((0, 3))
        self.assertEqual(self.b.board[0][3][0], 3, 'No Change to already miss')

    def testMoveSunk(self):
        """ Test is returns sunk after a hit."""

        self.assertFalse(self.b.move((1, 2)), 'Move return True when not sunk')
        self.assertTrue(self.b.move((0, 2)), 'Move return False when sunk')

    def testGameOver(self):
        """Tests if Gameover returns correct value"""
        self.assertFalse(self.b.game_over(), 'Game is over when game not done')
        self.b.user_pieces[0].sunk = True
        self.assertTrue(self.b.game_over(), \
                        'Game is not over, when game is done')


def board_suite():
    """Return a test suite for the computer."""

    return unittest.TestLoader().loadTestsFromTestCase(BoardTest)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(board_suite())
