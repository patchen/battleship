import random
import Board
import Ship


def check_size(b, ship, s, d):
    """Return True if a ship of size, ship (int), will fit on Board, b,
    starting from coordinate s (tuple) in direction d (string)"""

    i = 0
    while i < ship:
        if ((s[0] + i) >= b.size) or ((s[1] + i) >= b.size):
            return False
        elif d == 'right' and b.board[s[0] + i][s[1]] == 1:
            return False
        elif d == 'down' and b.board[s[0]][s[1] + i] == 1:
            return False
        i += 1
    return True


def find_spaces(b, ship):
    """Return a list that contains all possible placement locations for
    a given ship size, ship (int), on the Board, b."""

    acceptable = []
    for col in range(b.size):
        for row in range(b.size):
            if check_size(b, ship, (col, row), 'right'):
                current = []
                for i in range(ship):
                    current.append((col + i, row))
                acceptable.append(current)
            if check_size(b, ship, (col, row), 'down'):
                current = []
                for i in range(ship):
                    current.append((col, row + i))
                acceptable.append(current)
    return acceptable

def place_ship(b, ship):
    """Randomly place Ship, ship, on Board, b."""
    

    available = find_spaces(b, ship.size)
    coordinates = random.randint(0,len(available) - 1)
    for coor in available[coordinates]:
        b.board[coor[0]][coor[1]] = 1
    ship.position = available[coordinates]