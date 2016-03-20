"""
Created on Feb 1, 2012
"""
from ship import Ship


class Board(object):
    '''
    Board class used to make the game
    '''

    def __init__(self, size):
        """(int) -> board"""

        self.size = size
        self.board = []
        self.user_pieces = []
        for x in range(size):
            self.board.append([])
            for y in range(size):
                self.board[x].append(0)

    def draw(self, player):
        """(Board) -> None
        Draw the Game Board using text"""

        for x in range(self.size):
            for y in range(self.size):
                if self.board[y][x] == 1 and player == "self":
                    print "S ",
                elif self.board[y][x] == 2:
                    print 'X ',
                elif self.board[y][x] == 3:
                    print 'O ',
                else:
                    print "~ ",
            print ""

    def move(self, coord):
        """(Board, tuple) -> True or false
        Makes a move on the board given a tuple, by adjusting the
        board and user_pieces, return if the move sunk a ship."""

        col = coord[0]
        row = coord[1]
        initial = 0

        for x in self.user_pieces:
            if x.is_sunk() == True:
                initial += 1
        if self.board[col][row] == 1:
            self.board[col][row] = 2
        elif self.board[col][row] == 0:
            self.board[col][row] = 3
        final = 0
        for x in self.user_pieces:
            if x.is_sunk() == True:
                final += 1
        return final > initial

    def game_over(self):
        """(Board) - > True/False
        Return True if the game is over for the player"""

        sunk_count = 0
        for x in self.user_pieces:
            if x.is_sunk() == True:
                sunk_count += 1
        return sunk_count == len(self.user_pieces)
