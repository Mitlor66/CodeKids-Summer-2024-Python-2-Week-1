'''
TicTacToe project
Author: Timur Yarol
Date: 31/07/2024
'''

print("Day 3")

def intro():
    # index    0  1  2  3  4
    numbers = [7, 2, 8, 1, 6]
    print(numbers[2])    # print 8

    # index       0           1           2
    games = ["Minecraft", "Roblox", "Overcooked 2"]
    # subindex                       0123456789...
    print(games[1])    # print Roblox
    print(games[2][3]) # print r
    print(games[2][10])# print a space

    # index        0        1        2
    dial =     [[1,2,3], [4,5,6], [7,8,9]]
    # subindex   0 1 2    0 1 2    0 1 2

    print(dial[2])     # print [7,8,9]
    print(dial[0][2])  # print 3



def display_grid():
    # index        0        1        2
    dial =     [[1,2,3], [4,5,6], [7,8,9]]
    # subindex   0 1 2    0 1 2    0 1 2

    # for each element in the list dial (each element represent a row in the grid)
    for row in dial:
        print(row)
        for cell in row:
            print(cell)
    

def dictionary_revision():
    students = [{"Anna" : [1234, "Mitchell", 17]},  # index 0
                {"Sarah": [1235, "Connor",   16]},  # index 1
                {"John" : [1236, "Doe",      17]}]  # index 2

    print(students[1])              # print  {"Sarah": [1235, "Connor",   16]}
    print(students[0])              # print  {"Anna" : [1234, "Mitchell", 17]}
    print(students[0]["Anna"])      # print  [1234, "Mitchell", 17]
    print(students[0]["Anna"][1])   # print  "Mitchell"
    print(students[0]["Anna"][1][0])# print  M


def range_revision():
    # i takes all the value from 0 to 3 non included (so 0, 1 and 2)
    for i in range(3):
        print(i)


# TicTacToe

import random

class Board:
    def __init__(self):
        print("Board creation in progress")
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]

    def display(self):
        print("      0    1    2    ")
        n = 0
        for row in self.board:
            print(f"{n}   {row}")
            n = n + 1

    def row_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
        return False

    def col_win(self):
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        return False

    def dia_win(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def check_win(self):
        return self.row_win() or self.col_win() or self.dia_win()

    def full_board(self):
        for row in self.board:
            if " " in row:
                return False
        return True

class Player:
    def __init__(self, username, token):
        self.username = username
        self.token = token

    def play(self, board):
        row = int(input("Enter a row number: "))
        col = int(input("Enter a col number: "))
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Sorry, invalid row or column number")
            return False
        if board[row][col] == " ":
            board[row][col] = self.token
            return True
        else:
            print("Sorry, this spot is already taken")
            return False

class AI(Player):
    def __init__(self, username, token):
        super().__init__(username, token)

    def play(self, board):
        # Check for winning move
        if self.find_best_move(board, self.token):
            return True
        
        # Check for blocking move
        opponent_token = "O" if self.token == "X" else "X"
        if self.find_best_move(board, opponent_token):
            return True
        
        # Take a random empty spot
        empty_spots = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
        if empty_spots:
            row, col = random.choice(empty_spots)
            board[row][col] = self.token
            return True

    def find_best_move(self, board, token):
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = token
                    if self.check_win(board):
                        if token == self.token:
                            return True
                        else:
                            board[i][j] = self.token
                            return True
                    board[i][j] = " "
        return False

    def check_win(self, board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != " ":
                return True
            if board[0][i] == board[1][i] == board[2][i] != " ":
                return True
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return True
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return True
        return False

tictactoe = Board()
p1 = Player("Player 1", "X")
ai = AI("Computer", "O")
print(f"Welcome to our two players {p1.username} and {ai.username}")
print("You are the 'X' player")
tictactoe.display()
while True:
    # Player's turn
    while not p1.play(tictactoe.board):
        pass
    tictactoe.display()
    if tictactoe.check_win():
        print(f"{p1.username} won the game!!")
        break
    if tictactoe.full_board():
        print("The game is a tie!")
        break

    # AI's turn
    ai.play(tictactoe.board)
    tictactoe.display()
    if tictactoe.check_win():
        print(f"{ai.username} won the game!!")
        break
    if tictactoe.full_board():
        print("The game is a tie!")
        break































    
