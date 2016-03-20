"""
Created on Feb 20, 2012
"""

import unittest
from ship import Ship
from Board import Board


class ShipTest(unittest.TestCase):
    """Test Case for Ship."""

    def setUp(self):
        """setUp for ship."""
        self.b = Board(4)
        self.piece = Ship(3, self.b)
        self.position = [(0, 1), (0, 2), (0, 3)]

    def tearDown(self):
        """Clean Up."""
        self.b = None
        self.piece = None

    def testSunk(self):
        """Test cases for Sunk"""

        self.b.board[0][1] = 2
        self.b.board[0][2] = 2
        self.assertTrue(self.piece.is_sunk(), "Ship not sunk when sunk")
        self.b.board[0][3] = 2
        self.assertTrue(self.piece.ship_sunk(), "Ship not set to sunk")


def ship_suite():
    """Return a test suite for the computer."""
    return unittest.TestLoader().loadTestsFromTestCase(ShipTest)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(ship_suite())
