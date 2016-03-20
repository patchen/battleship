"""
Created on Feb 1, 2012
"""
import unittest
from AI import ComputerAI
import Board


class CoordinateTestCase(unittest.TestCase):
    """Test Coordinates of AI."""

    def setUp(self):
        """Set up a AI."""

        self.board = Board.Board(3)
        self.computer = ComputerAI(self.board)

    def tearDown(self):
        """Clean up."""

        self.board = None
        self.computer = ComputerAI(self.board)

    def testRandom(self):
        """Test to see if returns all possible random."""

        correct_list = []
        random_list = []
        for x in range(3):
            for y in range(3):
                correct_list.append((x, y))
        for x in range(9):
            random_list.append(self.computer.computer_random())
        for x in range(len(correct_list)):
            for y in range(len(random_list)):
                if correct_list[x] == random_list[y]:
                    correct_list[x] = 0
                    random_list[y] = 0
                    break
        self.assertEqual(correct_list, [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                                        'Not all random given for AI')
        self.assertEqual(random_list, [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                                        'Extra coordinates provided')

    def testBuild(self):
        """Test build move"""
        self.computer.guessed.append((2, 2))
        self.computer.build_move(1, 2)

        self.assertEqual(self.computer.north.dequeue(), (1, 1), \
                                            'North coord Broken')
        self.assertEqual(self.computer.north.dequeue(), (1, 0), \
                                            'North coord Broken')
        self.assertTrue(self.computer.east.is_empty(), \
                        'Already guessed does not return empty')
        self.assertTrue(self.computer.south.is_empty(), \
                        'Boarder limit does not return empty')
        self.assertEqual(self.computer.west.dequeue(), (0, 2),\
                                         'West coord broken')

    def testSmart(self):
        """Test the Smart Computer"""
        self.computer.guessed.append((2, 2))
        self.computer.build_move(1, 2)
        move_list = []
        for x in range(2):
            move_list.append(self.computer.computer_smart())
        self.assertEqual(move_list, [(1, 1), (0, 2)], \
                         'Smart computer does not return correct move')


def computer_suite():
    """Return a test suite for the computer."""
    return unittest.TestLoader().loadTestsFromTestCase(CoordinateTestCase)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(computer_suite())
