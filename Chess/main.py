class Chessboard:
    def __init__(self):
        self.board = [['' for _ in range(8)] for _ in range(8)]

    def startgame(self):
        white_rookA = Rook('White', (0, 0))
        chessboard.place_piece(white_rookA, 0, 0)

        white_knightA = Knight('White', (0, 1))
        chessboard.place_piece(white_knightA, 0, 1)

        white_bishopB = Bishop('White', (0, 2))
        chessboard.place_piece(white_bishopB, 0, 2)

        white_queen = Queen('White', (0, 3))
        chessboard.place_piece(white_queen, 0, 3)

        white_king = King('White', (0, 4))
        chessboard.place_piece(white_king, 0, 4)

        white_bishopW = Bishop('White', (0, 5))
        chessboard.place_piece(white_bishopW, 0, 5)

        white_knightB = Knight('White', (0, 6))
        chessboard.place_piece(white_knightB, 0, 6)

        white_rookB = Rook('White', (0, 7))
        chessboard.place_piece(white_rookB, 0, 7)

        white_pawnA = Pawn('White', (1, 0))
        chessboard.place_piece(white_pawnA, 1, 0)

        white_pawnB = Pawn('White', (1, 1))
        chessboard.place_piece(white_pawnB, 1, 1)

        white_pawnC = Pawn('White', (1, 2))
        chessboard.place_piece(white_pawnC, 1, 2)

        white_pawnD = Pawn('White', (1, 3))
        chessboard.place_piece(white_pawnD, 1, 3)

        white_pawnE = Pawn('White', (1, 4))
        chessboard.place_piece(white_pawnE, 1, 4)

        white_pawnF = Pawn('White', (1, 5))
        chessboard.place_piece(white_pawnF, 1, 5)

        white_pawnG = Pawn('White', (1, 6))
        chessboard.place_piece(white_pawnG, 1, 6)

        white_pawnH = Pawn('White', (1, 7))
        chessboard.place_piece(white_pawnH, 1, 7)

        black_rookA = Rook('Black', (7, 0))
        chessboard.place_piece(black_rookA, 7, 0)

        black_knightA = Knight('Black', (7, 1))
        chessboard.place_piece(black_knightA, 7, 1)

        black_bishopW = Bishop('Black', (7, 2))
        chessboard.place_piece(black_bishopW, 7, 2)

        black_queen = Queen('Black', (7, 3))
        chessboard.place_piece(black_queen, 7, 3)

        black_king = King('Black', (7, 4))
        chessboard.place_piece(black_king, 7, 4)

        black_bishopB = Bishop('Black', (7, 5))
        chessboard.place_piece(black_bishopB, 7, 5)

        black_knightB = Knight('Black', (7, 6))
        chessboard.place_piece(black_knightB, 7, 6)

        black_rookB = Rook('Black', (7, 7))
        chessboard.place_piece(black_rookB, 7, 7)

        black_pawnA = Pawn('Black', (6, 0))
        chessboard.place_piece(black_pawnA, 6, 0)

        black_pawnB = Pawn('Black', (6, 1))
        chessboard.place_piece(black_pawnB, 6, 1)

        black_pawnC = Pawn('Black', (6, 2))
        chessboard.place_piece(black_pawnC, 6, 2)

        black_pawnD = Pawn('Black', (6, 3))
        chessboard.place_piece(black_pawnD, 6, 3)

        black_pawnE = Pawn('Black', (6, 4))
        chessboard.place_piece(black_pawnE, 6, 4)

        black_pawnF = Pawn('Black', (6, 5))
        chessboard.place_piece(black_pawnF, 6, 5)

        black_pawnG = Pawn('Black', (6, 6))
        chessboard.place_piece(black_pawnG, 6, 6)

        black_pawnH = Pawn('Black', (6, 7))
        chessboard.place_piece(black_pawnH, 6, 7)

    def print_board(self):
        for row in self.board:
            print(row)

    def place_piece(self, piece, row, col):
        self.board[row][col] = piece

    def move_piece(self, start_row, start_col, end_row, end_col):
        piece = self.board[start_row][start_col]
        if not piece:
            print("No piece found at the specified position.")
            return
        if self.is_valid_move(piece, start_row, start_col, end_row, end_col):
            self.board[end_row][end_col] = piece
            self.board[start_row][start_col] = ''
            piece.position = (end_row, end_col)
        else:
            print("Invalid move.")

    def is_valid_move(self, piece, start_row, start_col, end_row, end_col):
        if isinstance(piece, Pawn):
            # Logika dla pionka
            if piece.color == 'White':
                if start_row == 1:
                    if end_row - start_row in (1, 2) and start_col == end_col and not self.board[end_row][end_col]:
                        return True
                else:
                    if end_row - start_row == 1 and start_col == end_col and not self.board[end_row][end_col]:
                        return True
            else:
                if start_row == 6:
                    if start_row - end_row in (1, 2) and start_col == end_col and not self.board[end_row][end_col]:
                        return True
                else:
                    if start_row - end_row == 1 and start_col == end_col and not self.board[end_row][end_col]:
                        return True
        elif isinstance(piece, Knight):
            # Logika dla skoczka
            diff_row = abs(end_row - start_row)
            diff_col = abs(end_col - start_col)
            return (diff_row, diff_col) in [(1, 2), (2, 1)]
        elif isinstance(piece, Rook):
            # Logika dla wieży
            if start_row == end_row or start_col == end_col:
                return True
        elif isinstance(piece, Bishop):
            # Logika dla gońca
            diff_row = abs(end_row - start_row)
            diff_col = abs(end_col - start_col)
            return diff_row == diff_col
        elif isinstance(piece, Queen):
            # Logika dla królowej
            diff_row = abs(end_row - start_row)
            diff_col = abs(end_col - start_col)
            return (start_row == end_row or start_col == end_col) or (diff_row == diff_col)
        elif isinstance(piece, King):
            # Logika dla króla
            diff_row = abs(end_row - start_row)
            diff_col = abs(end_col - start_col)
            return diff_row <= 1 and diff_col <= 1
        # Dodaj logikę dla innych pionków
        return False


class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position


class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __str__(self):
        return 'Pawn'


class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __str__(self):
        return 'Rook'


class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __str__(self):
        return 'Knight'


class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __str__(self):
        return 'Bishop'


class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __str__(self):
        return 'Queen'


class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __str__(self):
        return 'King'




# Użycie klas
if __name__ == '__main__':
    chessboard = Chessboard()
    chessboard.startgame()
    chessboard.print_board()

    while True:
        start_row = int(input("Enter start row: "))
        start_col = int(input("Enter start column: "))
        end_row = int(input("Enter end row: "))
        end_col = int(input("Enter end column: "))
        chessboard.move_piece(start_row, start_col, end_row, end_col)
        chessboard.print_board()
        continue_game = input("Continue the game? (y/n): ")
        if continue_game.lower() != 'y':
            break
