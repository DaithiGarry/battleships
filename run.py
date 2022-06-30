from random import randint

Guesses_Count = 5
Board_Size_Row = 8
Board_Size_Column = 8

Hidden = "-"
Ship = "X"
Guess = "0"

def read_int(prompt: str, min_value: int = 1, max_value: int = 8) -> int:
    """Read an integer between a min and max value."""

    while True:
        line = input(prompt)
        try:
            value = int(line)
            if value < min_value:
                print(f"The minimum value is {min_value}. Try again.")
            elif value > max_value:
                print(f"The maximum value is {max_value}. Try again.")
            else:
                return value
        except ValueError:
            print("That's not a number! Try again.")

class GameBoard:
    """
    define user board
    """
    def _init_(self, board):
        self.board = board

    def get_letters_to_numbers():
        """
        define the range of letters and numbers on the user board
        """
        letters_to_numbers = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8}
        return letters_to_numbers

    
    def print_board(self):
        """
        define the appearance of the userboard via printing labels for ABCD etc and create a spacer beneath -.
        """
        print("A B C D E F G H I")
        print("- - - - - - - - -")
        row_number = 1
       
        for row in self.board:
            """
            define a loop to run through the board the correct numbers
            """
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1

class Battleship:
    """ 
    The battleship class is used to define the battleship board and the functions to identify ships, hits and misses.
    """
    def _init_(self, size_x: int, size_y: int) -> None:
        #creating the board/grid function
        self.board = [[Hidden] * size_x for _ in range (size_y)]
        #Create ships function has been removed and added here
        self.x_row = random.randint(0, size_x -1)
        self.y_column = random.randint(0, size_y -1)
        self.board[self.x_row][self.y_column] = Ship

    
    
    def get_player_input(self):
        """ 
        player input functions are created to make sure the player selects 
        an existing row (x) and column (y) to insure the 
        instructions to the program are valid.
        """
        try:
            x_row = input("Enter the row of the ship: e.g. 123 ")
            while x_row not in "12345678":
                print("Cannot place ship here, please select a row")
                x_row = input("Enter the row of the ship: e.g. 123 ")

            y_column = input("Enter the column of the ship: e.g. ABC ").upper()
            while y_column not in "ABCDEFGHI":
                print("Cannot place ship here, please select a column")
                y_column = input("Enter the column of the ship: e.g. ABC ")
            return int(x_row) -1, GameBoard.get_letters_to_numbers()[y_column]
        except ValueError() and KeyError():
            print("Input is not valid")
            return self.get_player_input()
    
    def hit_ships_counter(self):
        """ 
        hit ships counter to start at 0, and will increase by 1 for each 
        X (direct hit) that is found on the board.
        """
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships

    def RunGame():
        """ 
        defining the board ranges for both the computer and the player boards. 
        Loop for player attempts and insure locations cannot be selected twice.
        """
        computer_board = GameBoard([[" "] * 8 for i in range(8)])
        player_board = GameBoard([[" "] * 8 for i in range(8)])
        Battleship.create_ships(computer_board)
        attempts = 10
        while attempts > 0:
            GameBoard.print_board(player_board)
            player_x_row, player_y_column = Battleship.get_player_input(object)
        while player_board.board[player_x_row][player_y_column] == "0"or player_board.board[player_x_row][player_y_column] == "X":
            print("Cannot complete, you have already guessed this location")
            player_x_row, player_y_column = Battleship.get_player_input(object)
        if computer_board.board[player_x_row][player_y_column] == "X":
            print("Direct hit....You sunk my battleship!")
            player_board.board[player_x_row][player_y_column] = "X"
        else:
            print("You missed!")
            player_board.board[player_x_row][player_y_column] = "0"
        if Battleship.hit_ships_counter(player_board) == 5:
            print("You have sunk all my battleships!")           
        else:
            attempts -= 1
            print(f"You have {attempts} attempts left!")
            if attempts == 0:
                print("Sorry, no attempts remaining")
                GameBoard.print_board(player_board)
                
print("Welcome to Battleships!")
if __name__ == "__main__":
    RunGame()