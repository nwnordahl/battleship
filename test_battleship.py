from battleship import Board

board = Board(5)
board.show()


class TestBoard:
    def test_col_length(self):
        board = Board(5)
        assert len(board.board) == 5

    def test_row_length(self):
        board = Board(5)
        assert len(board.board[0]) == 5
