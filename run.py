# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

class Board:
    #define user board
    def _init_(self, board):
        self.board = board
    
    #define the range of letters and numbers on the user board
    def get_letters_to_numbers():
        letters_to_numbers = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8}
        return letters_to_numbers

    #define the appearance of the userboard via printing labels for ABCD etc and create a spacer beneath -.
    def print_board(self):
        print("A B C D E F G H I")
        print("- - - - - - - - -")
        row_number = 1
        #create a loop to loop through the board the correct numbers of times(%d|%S|) and print the row numbers(which are performed in increments of 1) for each loop which has been spaced by a |.
        for row in self.board:
            print("%d|%S|" % (row_number, "|".join(row)))
            row_number +=1

class Battleship:
    # the same function was used as was created in class Board above.
    def _init_(self, board):
        self.board = board

    def create_ships(self):
        for i in range(5):
            # run a loop to find a random place to put an X, the "while" parameter will make sure that no existing battleship has been placed in this location and loop again if it is occupied
            self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        return self.board
    
    def get_player_input(self):
        # player input functions are created to make sure the player selects an existing row (x) and column (y) to insure the instructions to the program are valid.
        try:
            x_row = input("Enter the row of the ship: e.g. 123 ")
            while x_row not in "12345678":
                print("Cannot place ship here, please select a row")
                x_row = input("Enter the row of the ship: e.g. 123 ")

            y_column = input("Enter the column of the ship: e.g. ABC ").upper()
            while y_column not in "ABCDEFGHI":
                print("Cannot place ship here, please select a column")
                y_column = input("Enter the column of the ship: e.g. ABC ")
            return int(x_row) -1, Board.get_letters_to_numbers()[y_column]
        except ValueError() and KeyError():
            print("Input is not valid")
            return self.get_player_input()
    
    def hit_ships_counter(self):
        #hit ships counter to start at 0, and will increase by 1 for each X (direct hit) that is found on the board.
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships