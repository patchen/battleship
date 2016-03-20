"""
Created on Feb 17, 2012
queue.py from lecture
"""
import random
import queue


class ComputerAI(object):
    """
    Computer AI class for moves
    """

    def __init__(self, board):
        '''
        Constructor
        '''
        self.opp_board = board
        self.guessed = []
        self.north = queue.Queue()
        self.east = queue.Queue()
        self.south = queue.Queue()
        self.west = queue.Queue()

    def build_move(self, col, row):
        """(int, int) -> None
        Build the computers next move given the column and row"""

        north_valid = True
        east_valid = True
        south_valid = True
        west_valid = True
        for x in range(1, 5):
            if north_valid == True and row - x >= 0 and not ((col, row - x) in\
                                                             self.guessed):
                self.north.enqueue((col, row - x))
            else:
                north_valid = False

            if south_valid == True and row + x < len(self.opp_board.board) and\
               not ((col, row + x) in self.guessed):
                self.south.enqueue((col, row + x))
            else:
                south_valid = False

            if west_valid == True and col - x >= 0 and not ((col - x, row) in \
                                                            self.guessed):
                self.west.enqueue((col - x, row))
            else:
                west_valid = False

            if east_valid == True and col + x < len(self.opp_board.board) and\
               not ((col + x, row) in self.guessed):
                self.east.enqueue((col + x, row))
            else:
                east_valid = False

    def computer_random(self):
        """(None) - > tuple
        Simulate a human by returning a valid random coordinate(tuple). Also
        will build the next possible coordinates if it is a hit."""

        col = random.randint(0, self.opp_board.size - 1)
        row = random.randint(0, self.opp_board.size - 1)
        while (col, row) in self.guessed:
            col = random.randint(0, self.opp_board.size - 1)
            row = random.randint(0, self.opp_board.size - 1)
        self.guessed.append((col, row))

        if self.opp_board.board[col][row] == 1:
            self.build_move(col, row)
        return (col, row)

    def computer_smart(self):
        """(None) - > tuple
        Simualte a human by returning the best valid coordinate(tuple)."""

        if not self.north.is_empty():
            coord = self.north.dequeue()
            self.guessed.append(coord)
            if self.opp_board.board[coord[0]][coord[1]] == 0:
                self.north.queue_del()
            return coord
        elif not self.east.is_empty():
            coord = self.east.dequeue()
            self.guessed.append(coord)
            if self.opp_board.board[coord[0]][coord[1]] == 0:
                self.east.queue_del()
            return coord
        elif not self.south.is_empty():
            coord = self.south.dequeue()
            self.guessed.append(coord)
            if self.opp_board.board[coord[0]][coord[1]] == 0:
                self.south.queue_del()
            return coord
        elif not self.west.is_empty():
            coord = self.west.dequeue()
            self.guessed.append(coord)
            if self.opp_board.board[coord[0]][coord[1]] == 0:
                self.west.queue_del()
            return coord
        return self.computer_random()

