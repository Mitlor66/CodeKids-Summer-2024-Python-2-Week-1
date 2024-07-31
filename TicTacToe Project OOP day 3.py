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
        if self.board[0][0] == self.board[0][1] == self.board[0][2] == "X":
            return True
        elif self.board[0][0] == self.board[0][1] == self.board[0][2] == "O":
            return True
        # Do it for row 1 and row 2
        if self.board[1][0] == self.board[1][1] == self.board[1][2] == "X":
            return True
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] == "O":
            return True
        if self.board[2][0] == self.board[2][1] == self.board[2][2] == "X":
            return True
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] == "O":
            return True

    def row_win_optimized(self):
        for i in range(0, 3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == "X":
                return True
            elif self.board[i][0] == self.board[i][1] == self.board[i][2] == "O":
                return True
    
    
class Player:
    def __init__(self, username, token):
        self.username = username
        self.token = token

    def play(self, board):
        row = input("Enter a row number: ")
        row = int(row)
        col = input("Enter a col number: ")
        col = int(col)
        # We also need to check that the row and col numbers are between 0 and 2
        # If they are, carry on with the code, otherwise, print an error message
        # and stop the code
        if row < 0 or row > 2:
            print("Sorry, invalid row number")
            return False
        elif col < 0 or col > 2:
            print("Sorry, invalid col number")
            return False
        
        # Add an if statement that will check if the board at that position is
        # equal to " ". If it is, play there
        # Else, display an error message.
        if board[row][col] == " ":
            board[row][col] = self.token
            return True
        else:
            print("Sorry, this spot is already taken")
            return False



tictactoe = Board()
p1 = Player("Mitlor", "X")
p2 = Player("John", "O")
print(f"Welcome to our two players {p1.username} and {p2.username}")

while True:
    # P1's turn
    while(p1.play(tictactoe.board) == False): pass
    tictactoe.display()
    if tictactoe.row_win() == True:
        print(f"{p1.username} won the game!!")
        break

    # P2's turn
    while(p2.play(tictactoe.board) == False): pass
    tictactoe.display()
    if tictactoe.row_win() == True:
        print(f"{p2.username} won the game!!")
        break




"""
Homework
Please complete the code by adding the check for the col_win() and
dia_win()
You will also have to add the code in the while loop at the bottom to
take these new checks into consideration.
When playing the game with all the checks, you should see that when someone
wins, it will stop the game. But what about when the board is full?
How would you handle this problem? Be creative and I will provide a solution
tomorrow.
"""





























    
