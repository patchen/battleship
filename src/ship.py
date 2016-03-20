"""
Created on Feb 1, 2012
"""


class Ship(object):
    '''
    Ship Class for board
    '''
    def __init__(self, size, b):
        """(int, Board) -> None"""

        self.size = size
        self.sunk = False
        self.position = []
        self.board = b

    def is_sunk(self):
        """(Ship) -> bool
        Return True if the ship is sunk, and sets sunk to True.
        """

        for coord in self.position:
            print self.board.board[coord[0]][coord[1]]
            if self.board.board[coord[0]][coord[1]] == 1:
                return False
        self.sunk = True
        return True

    def ship_sunk(self):
        """Return value of self.sunk"""

        return self.sunk