"""
Created on Feb 15, 2012
"""

import Board
import ship
import random
import AI
import Tkinter


def draw_game(window, b1, b2, player):
    """Draw b1 and b2 (Boards) on window (Tk)."""

    window.grid()
    size = 750 / b1.size * b1.size
    board = Tkinter.Canvas(window, bg='black', height=size + 30, width=2\
                           * size + 10)
    board.grid(column=0, row=0)
    board.create_rectangle(size, 0, size + 10, size, fill='white')
    board.create_rectangle(0, 0, size, size, fill='blue')
    board.create_rectangle(size + 10, 0, 2 * size + 10, size, fill='blue')
    if player == 1:
        p2_label = Tkinter.Label(window, bg='black', fg='red',\
                                 text='Player 2', font=("Impact", 12))
        p2_label.place(x=(size / 2 - 25), y=size + 5)
        p1_label = Tkinter.Label(window, bg='black', fg='green', \
                                 text='Player 1', font=("Impact", 12))
        p1_label.place(x=(size / 2 + size - 15), y=size + 5)
    elif player == 2:
        p1_label = Tkinter.Label(window, bg='black', fg='red',\
                                 text='Player 1', font=("Impact", 12))
        p1_label.place(x=(size / 2 - 25), y=size + 5)
        p2_label = Tkinter.Label(window, bg='black', fg='green',\
                                 text='Player 2', font=("Impact", 12))
        p2_label.place(x=(size / 2 + size - 15), y=size + 5)
    for col in range(0, b1.size):
        for row in range(0, b1.size):
            if b1.board[col][row] == 1 or b1.board[col][row] == 2:
                board.create_rectangle(size / b1.size * col + size + 10,
                                       size / b1.size * row,\
                                      size / b1.size * (col + 1) + size + 10,\
                                      size / b1.size * (row + 1), fill='grey')
                if b1.board[col][row] == 2:
                    board.create_line(size / b1.size * col + size + 10, size\
                                      / b1.size * row, \
                                    size / b1.size * (col + 1) + size + 10,\
                                    size / b1.size * (row + 1), fill='red')
                    board.create_line(size / b1.size * (col + 1) + size + 10, \
                                      size / b1.size * row, \
                                    size / b1.size * col + size + 10, size /\
                                    b1.size * (row + 1), fill='red')
            elif b1.board[col][row] == 3:
                board.create_line(size / b1.size * col + size + 10, size /\
                                  b1.size * row, \
                                size / b1.size * (col + 1) + size + 10,\
                                size / b1.size * (row + 1), fill='white')
                board.create_line(size / b1.size * (col + 1) + size + 10,\
                                  size / b1.size * row, size / b1.size * col +\
                                  size + 10, size / b1.size * (row + 1),\
                                fill='white')
            if b2.board[col][row] == 2:
                board.create_rectangle(size / b1.size * col,\
                                        size / b1.size * row,\
                                        size / b1.size * (col + 1),\
                                        size / b1.size * (row + 1),\
                                        fill='grey')
                board.create_line(size / b1.size * col, size /\
                                  b1.size * row, \
                                size / b1.size * (col + 1),\
                                size / b1.size * (row + 1), fill='red')
                board.create_line(size / b1.size * (col + 1),\
                                  size / b1.size * row, size / b1.size *\
                                  col, size / b1.size * (row + 1),\
                                fill='red')
            elif b2.board[col][row] == 3:
                board.create_line(size / b1.size * col, size /\
                                  b1.size * row, \
                                size / b1.size * (col + 1),\
                                size / b1.size * (row + 1), fill='white')
                board.create_line(size / b1.size * (col + 1),\
                                  size / b1.size * row, size / b1.size * \
                                  col, size / b1.size * (row + 1),\
                                fill='white')
    for i in range(0, size, size / b1.size):
        board.create_line(i, 0, i, size)
        board.create_line(i + size + 10, 0, i + size + 10, size)
        board.create_line(0, i, size, i)
        board.create_line(size + 10, i, 2 * size + 10, i)


def window_close(window):
    window.withdraw()
    window.quit()


def end_game_prompt(winner):
    '''Create and display an end game prompt.'''

    end = Tkinter.Toplevel(bg='grey')
    end.title = "GAME OVER"
    end_label = Tkinter.Message(end, bg='grey', text="Game Over, " + winner + \
                              " wins!")
    end_label.pack()
    end_button = Tkinter.Button(end, text="End Game", bg='grey',\
                            command=end.quit)
    end_button.pack()
    end.mainloop()


def ship_sunk():
    '''Create a prompt when a ship is sunk.'''

    sunk = Tkinter.Toplevel(bg='grey')
    sunk.title("Ship Sunk!")
    sunk_label = Tkinter.Message(sunk, bg='grey',\
                text="A ship has been destroyed!")
    sunk_label.pack()
    sunk_button = Tkinter.Button(sunk, text="Click to continue.", bg='grey',\
                            command= lambda: window_close(sunk))
    sunk_button.pack()
    sunk.mainloop()

def play_single(event, b1, b2, comp):
    '''Similate a turn of a single player game and return True if there is a 
    winner.'''
    
    col = event.x / (750 / b1.size)
    row = event.y / (750 / b1.size)
    global winner
    if col < b1.size and row < b1.size and \
       b2.board[col][row] != 2 and b2.board[col][row]\
         != 3 and winner == "No One":
        if b2.move((col,row)):
            draw_game(game, b1, b2, 1)
            winner = ""
            ship_sunk()
            winner = "No One"
        if b2.game_over():
            winner = "Player 1"
            draw_game(game, b1, b2, 1)
            end_game_prompt("Player 1")
            game.destroy()
            return True
        attack = comp.computer_smart()
        if b1.move(attack):
            draw_game(game, b1, b2, 1)
            winner = ""
            ship_sunk()
            winner = "No One"
        if b1.game_over():
            winner = "Player 2"
            draw_game(game,b1, b2,1)
            end_game_prompt("Player 2")
            game.destroy()
            return True
        draw_game(game, b1, b2, 1)
        
def turn_prompt():
    '''Create a prompt for players inbetween turns.'''
    
    turn = Tkinter.Toplevel(bg='grey')
    turn.title("Intermission")
    turn_label = Tkinter.Message(turn, bg='grey',\
                text="Maximize this window and change players.\
                When the next player is ready, click the button.")
    turn_label.pack()
    turn_button = Tkinter.Button(turn, text="Click me when ready!", bg='grey',\
                            command= lambda: window_close(turn))
    turn_button.pack()
    turn.mainloop()
        
def play_multi(event, b1, b2):
    '''Similate a turn of a two player game and return True if there is a 
    winner.'''
    
    col = event.x / (750 / b1.size)
    row = event.y / (750 / b1.size)
    global winner
    global player
    if player == 1 and col < b1.size and row < b1.size \
       and b2.board[col][row] != 2 and b2.board[col][row]\
        != 3 and winner == "No One":
            if b2.move((col,row)):
                draw_game(game,b1, b2, 1)
                winner = ""
                ship_sunk()
                winner = "No One"
            if b2.game_over():
                winner = "Player 1"
                draw_game(game,b1, b2, 1)
                end_game_prompt("Player 1")
                game.destroy()
                return True
            draw_game(game,b1, b2, 1)
            player = 0
            turn_prompt()
            player = 2
            draw_game(game,b2, b1, 2)
    elif player == 2 and col < b1.size and row < b1.size \
       and b1.board[col][row] != 2 and b1.board[col][row]\
        != 3 and winner == "No One":
        if b1.move((col,row)):
            draw_game(game,b2, b1, 2)
            winner = ""
            ship_sunk()
            winner = "No One"
        if b1.game_over():
            winner = "Player 2"
            draw_game(game,b2, b1, 2)
            end_game_prompt("Player 1")
            game.destroy()
            return True
        draw_game(game,b2, b1, 2)
        player = 0
        turn_prompt()
        player = 1
        draw_game(game,b1, b2, 1)            

def on_finish_click():
    '''Set the variables for the board size, and the number of each of the ship
    types and quit the mainloop if the variables are acceptable. Show error
    messages if values aren't acceptable.'''

    acceptable = True
    global size
    global ships
    global two_player
    if var.get() == 0:
        two_player = False
    else:
        two_player = True
    try:
        size = int(size_entry.get())
        if size < 2 or size > 400:
            acceptable = False
            size_error_label.place(x=100, y=75)
            size_error_label.visible = True
        elif size >= 2:
            if size_error_label.visible == True:
                size_error_label.place_forget()
                size_error_label.visible = False
    except ValueError:
        size_error_label.place(x=100, y=75)
        size_error_label.visible = True
        acceptable = False
    try:
        ships[0] = int(destroyer_entry.get())
        if ships[0] < 0:
            acceptable = False
            destroyer_error_label.place(x=100, y=125)
            destroyer_error_label.visible = True
        else:
            if destroyer_error_label.visible == True:
                destroyer_error_label.place_forget()
                destroyer_error_label.visible = False
    except ValueError:
        destroyer_error_label.place(x=100, y=125)
        destroyer_error_label.visible = True
        acceptable = False
    try:
        ships[1] = int(submarine_entry.get())
        if ships[1] < 0:
            acceptable = False
            submarine_error_label.place(x=100, y=175)
            submarine_error_label.visible = True
        else:
            if submarine_error_label.visible == True:
                submarine_error_label.place_forget()
                submarine_error_label.visible = False
    except ValueError:
        submarine_error_label.place(x=100, y=175)
        submarine_error_label.visible = True
        acceptable = False
    try:
        ships[2] = int(battleship_entry.get())
        if ships[2] < 0:
            acceptable = False
            battleship_error_label.place(x=100, y=225)
            battleship_error_label.visible = True
        else:
            if battleship_error_label.visible == True:
                battleship_error_label.place_forget()
                battleship_error_label.visible = False
    except ValueError:
        battleship_error_label.place(x=100, y=225)
        battleship_error_label.visible = True
        acceptable = False
    try:
        ships[3] = int(carrier_entry.get())
        if ships[3] < 0:
            acceptable = False
            cruiser_error_label.place(x=100, y=275)
            cruiser_error_label.visible = True
        else:
            if cruiser_error_label.visible == True:
                cruiser_error_label.place_forget()
                cruiser_error_label.visible = False
    except ValueError:
        cruiser_error_label.place(x=100, y=275)
        cruiser_error_label.visible = True
        acceptable = False
    if acceptable:
        setup.destroy()    

def check_placeable(b, size, coord, direction):
    """Return True if a ship of size, size (int), will be placeable on Board, b,
    starting from coord (tuple) in direction (string)"""

    i = 0
    while i < size:
        if ((coord[0] + i) >= b.size) and direction == 'right':
            return False
        elif ((coord[1] + i) >= b.size) and direction == 'down':
            return False
        elif direction == 'right' and b.board[coord[0] + i][coord[1]] == 1:
            return False
        elif direction == 'down' and b.board[coord[0]][coord[1] + i] == 1:
            return False
        i += 1
    return True

def find_spaces(board, ship_size):
    '''Return a list of tuples (x, y) with coordinates of valid spaces on Board,
    board, for ships of ship_size (int)'''
    
    available_ships = []
    for col in range(board.size):
        for row in range(board.size):
            if check_placeable(board, ship_size, (col, row), 'right'):
                current = []
                for i in range(ship_size):
                    current.append((col + i, row))
                available_ships.append(current)
            if check_placeable(board, ship_size, (col, row), 'down'):
                current = []
                for i in range(ship_size):
                    current.append((col, row + i))
                available_ships.append(current)
    return available_ships     

def place_ship(board, ship):
    """Randomly place Ship, ship, on Board, board."""
    
    available_ships = find_spaces(player1_board, ship.size)
    try:
        random_ship = random.randint(0, len(available_ships) - 1)
        for coord in available_ships[random_ship]:
            board.board[coord[0]][coord[1]] = 1
        ship.position = available_ships[random_ship]
        board.user_pieces.append(ship)
    except ValueError:
        pass

if __name__ == '__main__':
    two_player = False
    player = 1
    size = 10
    ships = [0,0,0,0]
    setup = Tkinter.Tk()
    setup.resizable(False, False)
    setup.title("Game Setup")
    frame = Tkinter.Frame(setup, width=750, height=750, bg='grey')
    frame.pack()
    size_label = Tkinter.Label(setup, text="Enter the Board Size:", bg='grey')
    size_label.place(x=25, y=50)
    size_entry = Tkinter.Entry(setup)
    size_entry.place(x=140, y=50)
    destroyer_label = Tkinter.Label(setup, \
                text="Enter the number of Destroyers (Size = 2):", bg='grey')
    destroyer_label.place(x=25, y=100)
    destroyer_entry = Tkinter.Entry(setup)
    destroyer_entry.place(x=250, y=100)
    submarine_label = Tkinter.Label(setup, \
                text="Enter the number of Submarines (Size = 3):", bg='grey')
    submarine_label.place(x=25, y=150)
    submarine_entry = Tkinter.Entry(setup)
    submarine_entry.place(x=255, y=150)
    battleship_label = Tkinter.Label(setup, \
                text="Enter the number of Battleships (Size = 4):", bg='grey')
    battleship_label.place(x=25, y=200)
    battleship_entry = Tkinter.Entry(setup)
    battleship_entry.place(x=252, y=200)
    carrier_label = Tkinter.Label(setup, \
                    text="Enter the number of Carriers (Size = 5):", bg='grey')
    carrier_label.place(x=25, y=250)
    carrier_entry = Tkinter.Entry(setup)
    carrier_entry.place(x=235, y=250)
    size_error_label = Tkinter.Label(setup, text="Invalid Board Size",\
                                     bg='grey', fg='red')
    size_error_label.visible = False
    destroyer_error_label = Tkinter.Label(setup, text=\
                                          "Invalid Destroyer Amount", bg='grey'\
                                          , fg='red')
    destroyer_error_label.visible = False
    submarine_error_label = Tkinter.Label(setup, text=\
                                          "Invalid Submarine Amount", bg='grey'\
                                          , fg='red')
    submarine_error_label.visible = False
    battleship_error_label = Tkinter.Label(setup, text=\
                                           "Invalid Battleship Amount", \
                                           bg='grey', fg='red')
    battleship_error_label.visible = False
    cruiser_error_label = Tkinter.Label(setup, text="Invalid Carrier Amount", \
                                        bg='grey', fg='red')
    cruiser_error_label.visible = False
    var = Tkinter.BooleanVar()
    vs_player = Tkinter.Radiobutton(setup, text='Two Player', bg='grey',\
                                    variable=var, value=True)
    vs_player.place(x=75, y=335)
    vs_computer = Tkinter.Radiobutton(setup, text='Single Player', bg='grey',\
                                      variable=var, value=False)
    vs_computer.place(x=75, y=310)
    finish_button = Tkinter.Button(setup, text='Lock-in Selection!', bg='grey',\
                                   command=on_finish_click)
    finish_button.place(x=250, y=400)
    setup.mainloop()
    game = Tkinter.Tk()
    game.resizable(False, False)
    game.title('Battleship')
    player1_board = Board.Board(size)
    player2_board = Board.Board(size)
    ships.reverse()
    winner = "No One"
    print ships
    for x in range(len(ships)):
        for y in range(ships[x]):
            place_ship(player1_board, ship.Ship(5 - x, player1_board))
            place_ship(player2_board, ship.Ship(5 - x, player2_board))
    draw_game(game,player1_board, player2_board, 1)
    comp = AI.ComputerAI(player1_board)
    if two_player == False:
        game.bind("<Button 1>", lambda event: 
                  play_single(event, player1_board, player2_board, comp))
    else:
        game.bind("<Button 1>", lambda event: 
                  play_multi(event, player1_board, player2_board))
    game.mainloop()
