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
            self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
