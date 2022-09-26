import numpy as np


class Board:
    def __init__(self, board_size):
        """Initialize the board."""
        board = []
        for i in range(board_size):
            board.append(["O"] * board_size)

        self.board_size = board_size
        self.board = board

    def every_O(self):
        """Turn every coordinate into an 'O'."""
        size = len(self.board)
        for row in range(size):
            for col in range(size):
                self.board[row][col] = "O"

    def every_X(self):
        """Turn every coordinate into an 'X'."""
        size = len(self.board)
        for row in range(size):
            for col in range(size):
                self.board[row][col] = "X"

    def check_every_coordinate(self):
        """
        Return True if every coordinate is an 'X'.
        Return False if not.
        """
        for row in self.board:
            for element in row:
                if element == "O":
                    return False

        return True

    def set_coordinate(self, row, col):
        """Set a coordinate. Displayed as an 'X' on the board."""
        if self.board[row - 1][col - 1] == "X":
            print()
            print("This coordinate has already been chosen.")
        else:
            self.board[row - 1][col - 1] = "X"

    def set_rand_coord(self):
        """Set a random coordinate. Displayed as an 'x' on the board."""
        while True:
            rand_row = int(np.floor(np.random.rand() * self.board_size)) + 1
            rand_col = int(np.floor(np.random.rand() * self.board_size)) + 1

            if self.board[rand_row - 1][rand_col - 1] == "X":
                continue
            else:
                self.board[rand_row - 1][rand_col - 1] = "X"
                break

    def show(self):
        """Print the board to the terminal."""
        print()
        for row in self.board:
            print(" ".join(e for e in row))


if __name__ == "__main__":
    # Example
    board = Board(5)

    board.set_coordinate(2, 4)
    board.set_rand_coord()

    board.show()

    board.set_rand_coord()
    board.set_rand_coord()
    board.set_rand_coord()
    board.set_rand_coord()
    board.show()

    board.every_X()
    board.show()
    print(board.check_every_coordinate())

    board.every_O()
    board.show()
    print(board.check_every_coordinate())
